import base64
import json
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path, PureWindowsPath
from unittest.mock import Mock, call, patch

sys.path.insert(0, str(Path(__file__).parents[1] / "docs" / "brain"))
from cortex import Cortex
from harvester import Harvester
from evolution import Evolver
from reason import ReasoningEngine
from scholar import Scholar
import nexus as nexus_module


class HarvesterContracts(unittest.TestCase):
    def test_state_rejects_non_mapping_repository_records(self):
        with self.assertRaisesRegex(ValueError, "repositories"):
            Harvester._validated_state({"repositories": "invalid"})

    def test_previous_diff_baseline_comes_from_recorded_git_blob(self):
        harvester = Harvester.__new__(Harvester)
        harvester._api = Mock(
            return_value={
                "encoding": "base64",
                "content": base64.b64encode(b"previous body").decode("ascii"),
            }
        )

        self.assertEqual(
            harvester._blob_text("owner/repo", "old-sha"),
            "previous body",
        )
        harvester._api.assert_called_once_with(
            "https://api.github.com/repos/owner/repo/git/blobs/old-sha"
        )

    def test_removed_source_is_archived_and_removed_from_state(self):
        with tempfile.TemporaryDirectory() as tmp:
            harvester = Harvester.__new__(Harvester)
            harvester.inputs = Path(tmp)
            current = harvester.inputs / "current" / "test" / "owner_repo"
            current.mkdir(parents=True)
            snapshot = current / "README.md__old.md"
            snapshot.write_text("sealed snapshot", encoding="utf-8")
            harvester.state = {
                "repositories": {
                    "owner/repo": {
                        "documents": {
                            "README.md": {
                                "sha": "old",
                                "output": snapshot.relative_to(harvester.inputs).as_posix(),
                            }
                        }
                    }
                }
            }
            harvester._api = Mock(
                side_effect=[
                    {"default_branch": "main"},
                    {"tree": [], "truncated": False},
                ]
            )
            harvester.dry = False

            changed = harvester._source(
                {
                    "repo": "owner/repo",
                    "documents": ["README.md"],
                    "ignore_patterns": [],
                    "layer": "test",
                    "primary_owner": "welcome",
                }
            )

            self.assertEqual(changed, [])
            self.assertFalse(snapshot.exists())
            self.assertEqual(
                list((harvester.inputs / "archive").rglob(snapshot.name))[0].read_text(
                    encoding="utf-8"
                ),
                "sealed snapshot",
            )
            self.assertNotIn(
                "README.md",
                harvester.state["repositories"]["owner/repo"]["documents"],
            )

    def test_archive_collision_never_overwrites_different_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            harvester = Harvester.__new__(Harvester)
            harvester.inputs = Path(tmp)
            current = harvester.inputs / "current" / "test" / "owner_repo"
            current.mkdir(parents=True)
            stale = current / "README.md__same.md"
            stale.write_text("current", encoding="utf-8")
            archive = (
                harvester.inputs
                / "archive"
                / "2026"
                / "07"
                / "test"
                / "owner_repo"
                / stale.name
            )
            archive.parent.mkdir(parents=True)
            archive.write_text("sealed", encoding="utf-8")

            with patch("harvester.dt.datetime") as clock:
                clock.now.return_value.strftime.return_value = "2026/07"
                with self.assertRaisesRegex(FileExistsError, "archive collision"):
                    harvester._archive_stale(
                        current / "README.md__new.md",
                        "README.md",
                        "test",
                        "owner_repo",
                    )

            self.assertEqual(stale.read_text(encoding="utf-8"), "current")
            self.assertEqual(archive.read_text(encoding="utf-8"), "sealed")

    def test_profiles_have_unique_welcome_owner(self):
        h = Harvester(Path(__file__).parents[1] / "docs" / "brain")
        self.assertTrue(h.validate_profiles())

    def test_external_links_are_not_selected(self):
        self.assertFalse(Harvester._selected("docs/link-from-readme.md", ["README.md"], []))

    def test_noise_normalization(self):
        self.assertEqual(Harvester._normalized("![badge](https://shields.io/x)\nArchitecture"), "Architecture")

    def test_api_retries_transient_network_failures_with_backoff(self):
        harvester = Harvester.__new__(Harvester)
        harvester.token = ""

        with patch("harvester.urllib.request.urlopen", side_effect=urllib.error.URLError("offline")) as urlopen:
            with patch("harvester.time.sleep") as sleep:
                with self.assertRaises(urllib.error.URLError):
                    harvester._api("https://example.invalid")

        self.assertEqual(urlopen.call_count, 3)
        self.assertEqual(sleep.call_args_list, [call(1), call(2)])

    def test_structural_array_index_is_not_treated_as_a_version(self):
        scholar = Scholar.__new__(Scholar)
        entity_id = "file_source_profiles_prop_sources_7_documents_0"

        self.assertEqual(scholar._strip_version(entity_id), entity_id)
        self.assertEqual(scholar._strip_version("component_v1.2.3"), "component")


    def test_evolver_propagates_cycle_failure(self):
        evolver = Evolver.__new__(Evolver)

        with patch.object(
            evolver,
            "_genetic_auto_recombination",
            side_effect=RuntimeError("cycle failed"),
        ):
            with self.assertRaisesRegex(RuntimeError, "cycle failed"):
                evolver.run_daily_cycle()

    def test_evolver_propagates_render_failure(self):
        evolver = Evolver.__new__(Evolver)
        evolver.brain_path = Path(".")

        with patch("evolution.ReasoningEngine", side_effect=RuntimeError("render failed")):
            with self.assertRaisesRegex(RuntimeError, "render failed"):
                evolver._trigger_render({}, [])

    def test_reason_reads_current_harvester_state_schema(self):
        with tempfile.TemporaryDirectory() as tmp:
            state_path = Path(tmp) / ".harvester_state.json"
            state_path.write_text(
                json.dumps({
                    "schema_version": 3,
                    "baseline": "2026-07-11T13:40:00+08:00",
                    "repositories": {
                        "owner/repo": {
                            "last_tag": "v1",
                            "last_checked_at": "2026-07-22T00:00:00Z",
                        }
                    },
                }),
                encoding="utf-8",
            )

            self.assertEqual(
                ReasoningEngine._read_harvester_releases(state_path),
                ["- **owner/repo** @ `v1` (Last Updated: 2026-07-22T00:00:00Z)"],
            )

    def test_evolver_propagates_mutator_failure(self):
        evolver = Evolver.__new__(Evolver)
        evolver.brain_path = Path(__file__).parent / "missing-brain"

        with self.assertRaises(FileNotFoundError):
            evolver._genetic_auto_recombination()
    def test_evolver_keeps_input_contract_out_of_monthly_archive(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            inputs = Path(tmp) / "inputs"
            inputs.mkdir()
            contract = inputs / "ARCHIVE_AND_HARVESTER.md"
            contract.write_text("contract", encoding="utf-8")
            incoming = inputs / "incoming.md"
            incoming.write_text("input", encoding="utf-8")
            evolver = Evolver.__new__(Evolver)
            evolver.inputs_path = inputs

            evolver._archive_inputs()

            self.assertTrue(contract.exists())
            self.assertFalse(incoming.exists())
            self.assertEqual(len(list((inputs / "archive").rglob("incoming.md"))), 1)

    def test_orphan_suturing_creates_its_target_entity(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cortex = Cortex(root / "cortex.db")
            try:
                cortex.add_entity("orphan", "concept", "Orphan", "Isolated")

                cortex.suture_orphans()

                target = cortex.conn.execute(
                    "SELECT 1 FROM entities WHERE id = ? AND invalid_at IS NULL",
                    ("concept_nexus_system",),
                ).fetchone()
                dangling = cortex.conn.execute(
                    """
                    SELECT COUNT(*) FROM relations r
                    LEFT JOIN entities src ON src.id = r.source AND src.invalid_at IS NULL
                    LEFT JOIN entities dst ON dst.id = r.target AND dst.invalid_at IS NULL
                    WHERE r.invalid_at IS NULL AND (src.id IS NULL OR dst.id IS NULL)
                    """
                ).fetchone()[0]
                self_loop = cortex.conn.execute(
                    """
                    SELECT COUNT(*) FROM relations
                    WHERE source = ? AND target = ? AND invalid_at IS NULL
                    """,
                    ("concept_nexus_system", "concept_nexus_system"),
                ).fetchone()[0]
                self.assertIsNotNone(target)
                self.assertEqual(dangling, 0)
                self.assertEqual(self_loop, 0)
            finally:
                cortex.conn.close()

    def test_orphan_suturing_propagates_write_failure(self):
        cortex = Cortex.__new__(Cortex)
        cortex.get_orphans = lambda limit=10: [{"id": "orphan"}]
        cortex.conn = Mock()
        cortex.conn.execute.return_value.fetchone.return_value = (1,)

        with patch.object(cortex, "connect_entities", side_effect=RuntimeError("write failed")):
            with self.assertRaisesRegex(RuntimeError, "write failed"):
                cortex.suture_orphans()

    def test_scholar_file_ids_are_platform_independent(self):
        scholar = Scholar.__new__(Scholar)
        self.assertEqual(
            scholar._file_id(PureWindowsPath("docs/brain/reason.py")),
            "file_docs_brain_reason_py",
        )

    def test_scholar_excludes_parallel_systems_and_unsupported_files(self):
        self.assertFalse(
            Scholar._is_supported_path(Path("horizon-cortex/owned.py"))
        )
        self.assertFalse(Scholar._is_supported_path(Path("parallax/owned.py")))
        self.assertFalse(Scholar._is_supported_path(Path("index.html")))
        self.assertTrue(Scholar._is_supported_path(Path("docs/brain/reason.py")))

    def test_scholar_links_only_local_inheritance_targets(self):
        class RecordingCortex:
            def __init__(self):
                self.entities = []
                self.relations = []

            def add_entity(
                self,
                entity_id,
                type_slug,
                name,
                desc,
                save_to_disk=True,
            ):
                self.entities.append(entity_id)

            def connect_entities(
                self,
                source,
                relation,
                target,
                desc="",
                save_to_disk=True,
            ):
                self.relations.append((source, relation, target))

        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "inheritance.py"
            source.write_text(
                "class Base:\n    pass\n\n"
                "class Child(Base):\n    pass\n\n"
                "class External(http.server.BaseHTTPRequestHandler):\n    pass\n",
                encoding="utf-8",
            )
            scholar = Scholar.__new__(Scholar)
            scholar.cortex = RecordingCortex()
            scholar._analyze_python_ast(source, "file_inheritance_py")

            self.assertIn(
                (
                    "file_inheritance_py__class_Child",
                    "inherits_from",
                    "file_inheritance_py__class_Base",
                ),
                scholar.cortex.relations,
            )
            self.assertFalse(
                any(target.startswith("class_") for _, _, target in scholar.cortex.relations)
            )
    def test_nexus_resolves_relative_module_paths(self):
        brain_root = nexus_module._brain_root("docs/brain/nexus.py")

        self.assertTrue(brain_root.is_absolute())
        self.assertEqual(brain_root, (Path.cwd() / "docs" / "brain").resolve())

    def test_rebuild_does_not_open_database_before_replacing_it(self):
        cortex = Mock()
        cortex.conn = Mock()
        with patch.object(sys, "argv", ["nexus.py", "rebuild"]):
            with patch.object(nexus_module, "Cortex", return_value=cortex) as factory:
                with patch.object(nexus_module.os, "remove"):
                    nexus_module.main()

        self.assertEqual(factory.call_count, 2)
        self.assertEqual(cortex.conn.close.call_count, 2)


if __name__ == "__main__":
    unittest.main()
