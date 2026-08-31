import base64
import hashlib
import json
import os
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
                    {
                        "sha": "commit-sha",
                        "commit": {"tree": {"sha": "tree-sha"}},
                    },
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

    def test_source_snapshot_uses_pinned_commit_tree_and_blob(self):
        with tempfile.TemporaryDirectory() as tmp:
            harvester = Harvester.__new__(Harvester)
            harvester.inputs = Path(tmp)
            harvester.state = {"repositories": {}}
            harvester.dry = False
            commit_sha = "c" * 40
            tree_sha = "t" * 40
            blob_sha = "b" * 40
            def response(url):
                if url == "https://api.github.com/repos/owner/repo":
                    return {"default_branch": "main"}
                if url.endswith("/commits/main"):
                    return {
                        "sha": commit_sha,
                        "commit": {"tree": {"sha": tree_sha}},
                    }
                if "/git/trees/" in url:
                    return {
                        "tree": [
                            {"type": "blob", "path": "README.md", "sha": blob_sha}
                        ],
                        "truncated": False,
                    }
                if "/git/blobs/" in url:
                    return {
                        "encoding": "base64",
                        "content": base64.b64encode(b"# Source\n").decode("ascii"),
                    }
                raise AssertionError(f"unexpected API URL: {url}")

            harvester._api = Mock(side_effect=response)

            changed = harvester._source(
                {
                    "repo": "owner/repo",
                    "documents": ["README.md"],
                    "ignore_patterns": [],
                    "layer": "test",
                    "primary_owner": "welcome",
                }
            )

            rendered = (harvester.inputs / changed[0]).read_text(encoding="utf-8")
            document = harvester.state["repositories"]["owner/repo"]["documents"]["README.md"]
            self.assertIn(
                f"https://github.com/owner/repo/blob/{commit_sha}/README.md",
                rendered,
            )
            self.assertNotIn(f"/blob/{blob_sha}/README.md", rendered)
            self.assertEqual(document["commit_sha"], commit_sha)
            self.assertEqual(document["tree_sha"], tree_sha)
            self.assertEqual(document["blob_sha"], blob_sha)
            self.assertEqual(
                harvester._api.call_args_list[:3],
                [
                    call("https://api.github.com/repos/owner/repo"),
                    call("https://api.github.com/repos/owner/repo/commits/main"),
                    call(
                        f"https://api.github.com/repos/owner/repo/git/trees/{tree_sha}?recursive=1"
                    ),
                ],
            )

    def test_legacy_blob_state_is_migrated_once(self):
        with tempfile.TemporaryDirectory() as tmp:
            harvester = Harvester.__new__(Harvester)
            harvester.inputs = Path(tmp)
            old_snapshot = (
                harvester.inputs
                / "current"
                / "test"
                / "owner_repo"
                / "README.md__bbbbbbbbbbbb.md"
            )
            old_snapshot.parent.mkdir(parents=True)
            old_snapshot.write_text("legacy", encoding="utf-8")
            source = "# Source\n"
            digest = hashlib.sha256(
                Harvester._normalized(source).encode()
            ).hexdigest()
            blob_sha = "b" * 40
            commit_sha = "c" * 40
            tree_sha = "t" * 40
            harvester.state = {
                "repositories": {
                    "owner/repo": {
                        "documents": {
                            "README.md": {
                                "sha": blob_sha,
                                "content_hash": digest,
                                "entity_id": "existing-entity",
                                "output": old_snapshot.relative_to(
                                    harvester.inputs
                                ).as_posix(),
                            }
                        }
                    }
                }
            }
            def response(url):
                if url == "https://api.github.com/repos/owner/repo":
                    return {"default_branch": "main"}
                if url.endswith("/commits/main"):
                    return {
                        "sha": commit_sha,
                        "commit": {"tree": {"sha": tree_sha}},
                    }
                if "/git/trees/" in url:
                    return {
                        "tree": [
                            {"type": "blob", "path": "README.md", "sha": blob_sha}
                        ],
                        "truncated": False,
                    }
                if "/git/blobs/" in url:
                    return {
                        "encoding": "base64",
                        "content": base64.b64encode(source.encode()).decode("ascii"),
                    }
                raise AssertionError(f"unexpected API URL: {url}")

            harvester._api = Mock(side_effect=response)
            harvester.dry = False
            profile = {
                "repo": "owner/repo",
                "documents": ["README.md"],
                "ignore_patterns": [],
                "layer": "test",
                "primary_owner": "welcome",
            }

            first = harvester._source(profile)
            second = harvester._source(profile)

            self.assertEqual(len(first), 1)
            self.assertEqual(second, [])
            document = harvester.state["repositories"]["owner/repo"]["documents"]["README.md"]
            self.assertEqual(document["commit_sha"], commit_sha)
            self.assertEqual(document["tree_sha"], tree_sha)
            self.assertEqual(document["blob_sha"], blob_sha)
            blob_calls = [
                item
                for item in harvester._api.call_args_list
                if "/git/blobs/" in item.args[0]
            ]
            self.assertEqual(len(blob_calls), 1)

    def test_normalized_noise_does_not_mutate_persisted_provenance(self):
        with tempfile.TemporaryDirectory() as tmp:
            harvester = Harvester.__new__(Harvester)
            harvester.inputs = Path(tmp)
            old_commit = "a" * 40
            old_tree = "b" * 40
            old_blob = "c" * 40
            new_commit = "d" * 40
            new_tree = "e" * 40
            new_blob = "f" * 40
            old_snapshot = (
                harvester.inputs
                / "current"
                / "test"
                / "owner_repo"
                / f"README.md__{old_blob[:12]}__{old_commit[:12]}.md"
            )
            old_snapshot.parent.mkdir(parents=True)
            old_snapshot.write_text(
                "\n".join(
                    [
                        "# owner/repo · README.md",
                        "",
                        f"| 来源文件 | [README.md](https://github.com/owner/repo/blob/{old_commit}/README.md) |",
                        f"| 来源版本 | `{old_commit}` |",
                        f"| 来源目录 Tree | `{old_tree}` |",
                        f"| 来源内容 Blob | `{old_blob}` |",
                    ]
                ),
                encoding="utf-8",
            )
            source = "![badge](https://img.shields.io/old)\n# Stable body\n"
            digest = hashlib.sha256(
                Harvester._normalized(source).encode()
            ).hexdigest()
            harvester.state = {
                "schema_version": 5,
                "repositories": {
                    "owner/repo": {
                        "documents": {
                            "README.md": {
                                "sha": old_blob,
                                "blob_sha": old_blob,
                                "commit_sha": old_commit,
                                "tree_sha": old_tree,
                                "observed_blob_sha": old_blob,
                                "observed_commit_sha": old_commit,
                                "observed_tree_sha": old_tree,
                                "content_hash": digest,
                                "entity_id": "existing-entity",
                                "output": old_snapshot.relative_to(
                                    harvester.inputs
                                ).as_posix(),
                            }
                        }
                    }
                },
            }

            def response(url):
                if url == "https://api.github.com/repos/owner/repo":
                    return {"default_branch": "main"}
                if url.endswith("/commits/main"):
                    return {
                        "sha": new_commit,
                        "commit": {"tree": {"sha": new_tree}},
                    }
                if "/git/trees/" in url:
                    return {
                        "tree": [
                            {"type": "blob", "path": "README.md", "sha": new_blob}
                        ],
                        "truncated": False,
                    }
                if url.endswith(f"/git/blobs/{new_blob}"):
                    return {
                        "encoding": "base64",
                        "content": base64.b64encode(
                            b"![badge](https://img.shields.io/new)\n# Stable body\n"
                        ).decode("ascii"),
                    }
                raise AssertionError(f"unexpected API URL: {url}")

            harvester._api = Mock(side_effect=response)
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

            document = harvester.state["repositories"]["owner/repo"]["documents"]["README.md"]
            self.assertEqual(changed, [])
            self.assertEqual(document["commit_sha"], old_commit)
            self.assertEqual(document["tree_sha"], old_tree)
            self.assertEqual(document["blob_sha"], old_blob)
            self.assertEqual(document["observed_commit_sha"], old_commit)
            self.assertEqual(document["observed_tree_sha"], old_tree)
            self.assertEqual(document["observed_blob_sha"], old_blob)
            self.assertTrue(old_snapshot.exists())

    def test_schema_four_recovers_snapshot_provenance_from_current_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            inputs = root / "inputs"
            current = inputs / "current" / "test" / "owner_repo"
            current.mkdir(parents=True)
            snapshot_commit = "a" * 40
            snapshot_tree = "b" * 40
            snapshot_blob = "c" * 40
            observed_commit = "d" * 40
            observed_tree = "e" * 40
            observed_blob = "f" * 40
            output = current / f"README.md__{snapshot_blob[:12]}__{snapshot_commit[:12]}.md"
            output.write_text(
                "\n".join(
                    [
                        "# owner/repo · README.md",
                        "",
                        f"| 来源文件 | [README.md](https://github.com/owner/repo/blob/{snapshot_commit}/README.md) |",
                        f"| 来源版本 | `{snapshot_commit}` |",
                        f"| 来源目录 Tree | `{snapshot_tree}` |",
                        f"| 来源内容 Blob | `{snapshot_blob}` |",
                        "",
                        "<details>",
                        "<summary>source</summary>",
                        "",
                        "# Stable body",
                        "",
                        "</details>",
                        "",
                        "<details>",
                        "<summary>diff</summary>",
                        "",
                        "```diff",
                        "```",
                        "",
                        "</details>",
                    ]
                ),
                encoding="utf-8",
            )
            (root / "source_profiles.json").write_text(
                '{"owner":"welcome","sources":[{"repo":"owner/repo","primary_owner":"welcome","layer":"test","documents":["README.md"]}]}',
                encoding="utf-8",
            )
            (inputs / ".harvester_state.json").write_text(
                json.dumps(
                    {
                        "schema_version": 4,
                        "repositories": {
                            "owner/repo": {
                                "documents": {
                                    "README.md": {
                                        "sha": observed_blob,
                                        "blob_sha": observed_blob,
                                        "commit_sha": observed_commit,
                                        "tree_sha": observed_tree,
                                        "content_hash": hashlib.sha256(
                                            Harvester._normalized("# Old body").encode()
                                        ).hexdigest(),
                                        "entity_id": "existing-entity",
                                        "output": output.relative_to(inputs).as_posix(),
                                    }
                                }
                            }
                        },
                    }
                ),
                encoding="utf-8",
            )

            harvester = Harvester(root)
            document = harvester.state["repositories"]["owner/repo"]["documents"]["README.md"]

            self.assertEqual(harvester.state["schema_version"], 5)
            self.assertEqual(document["commit_sha"], snapshot_commit)
            self.assertEqual(document["tree_sha"], snapshot_tree)
            self.assertEqual(document["blob_sha"], snapshot_blob)
            self.assertEqual(document["observed_commit_sha"], observed_commit)
            self.assertEqual(document["observed_tree_sha"], observed_tree)
            self.assertEqual(document["observed_blob_sha"], observed_blob)

    def test_unchanged_blob_does_not_mutate_persisted_document_state(self):
        harvester = Harvester.__new__(Harvester)
        blob_sha = "c" * 40
        old_commit = "a" * 40
        old_tree = "b" * 40
        new_commit = "d" * 40
        new_tree = "e" * 40
        harvester.state = {
            "schema_version": 5,
            "repositories": {
                "owner/repo": {
                    "documents": {
                        "README.md": {
                            "sha": blob_sha,
                            "blob_sha": blob_sha,
                            "commit_sha": old_commit,
                            "tree_sha": old_tree,
                            "observed_blob_sha": blob_sha,
                            "observed_commit_sha": old_commit,
                            "observed_tree_sha": old_tree,
                            "content_hash": "digest",
                            "entity_id": "existing-entity",
                            "output": "current/test/owner_repo/README.md",
                        }
                    }
                }
            },
        }
        harvester.dry = False
        harvester._api = Mock(
            side_effect=[
                {"default_branch": "main"},
                {"sha": new_commit, "commit": {"tree": {"sha": new_tree}}},
                {
                    "tree": [
                        {"type": "blob", "path": "README.md", "sha": blob_sha}
                    ],
                    "truncated": False,
                },
            ]
        )

        changed = harvester._source(
            {
                "repo": "owner/repo",
                "documents": ["README.md"],
                "ignore_patterns": [],
                "layer": "test",
                "primary_owner": "welcome",
            }
        )

        document = harvester.state["repositories"]["owner/repo"]["documents"]["README.md"]
        self.assertEqual(changed, [])
        self.assertEqual(document["commit_sha"], old_commit)
        self.assertEqual(document["tree_sha"], old_tree)
        self.assertEqual(document["blob_sha"], blob_sha)
        self.assertEqual(document["observed_commit_sha"], old_commit)
        self.assertEqual(document["observed_tree_sha"], old_tree)
        self.assertEqual(document["observed_blob_sha"], blob_sha)

    def test_schema_five_rejects_state_output_provenance_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            inputs = root / "inputs"
            current = inputs / "current" / "test" / "owner_repo"
            current.mkdir(parents=True)
            snapshot_commit = "a" * 40
            snapshot_tree = "b" * 40
            snapshot_blob = "c" * 40
            output = current / f"README.md__{snapshot_blob[:12]}__{snapshot_commit[:12]}.md"
            output.write_text(
                "\n".join(
                    [
                        "# owner/repo · README.md",
                        "",
                        f"| 来源文件 | [README.md](https://github.com/owner/repo/blob/{snapshot_commit}/README.md) |",
                        f"| 来源版本 | `{snapshot_commit}` |",
                        f"| 来源目录 Tree | `{snapshot_tree}` |",
                        f"| 来源内容 Blob | `{snapshot_blob}` |",
                        "",
                        "<details>",
                        "<summary>source</summary>",
                        "",
                        "# Stable body",
                        "",
                        "</details>",
                        "",
                        "<details>",
                        "<summary>diff</summary>",
                        "",
                        "```diff",
                        "```",
                        "",
                        "</details>",
                    ]
                ),
                encoding="utf-8",
            )
            (root / "source_profiles.json").write_text(
                '{"owner":"welcome","sources":[{"repo":"owner/repo","primary_owner":"welcome","layer":"test","documents":["README.md"]}]}',
                encoding="utf-8",
            )
            (inputs / ".harvester_state.json").write_text(
                json.dumps(
                    {
                        "schema_version": 5,
                        "repositories": {
                            "owner/repo": {
                                "documents": {
                                    "README.md": {
                                        "sha": "f" * 40,
                                        "blob_sha": "f" * 40,
                                        "commit_sha": "d" * 40,
                                        "tree_sha": "e" * 40,
                                        "observed_blob_sha": "f" * 40,
                                        "observed_commit_sha": "d" * 40,
                                        "observed_tree_sha": "e" * 40,
                                        "content_hash": "digest",
                                        "entity_id": "existing-entity",
                                        "output": output.relative_to(inputs).as_posix(),
                                    }
                                }
                            }
                        },
                    }
                ),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "snapshot provenance"):
                Harvester(root)

    def test_schema_five_rejects_noncanonical_current_output_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            inputs = root / "inputs"
            current = inputs / "current" / "test" / "owner_repo"
            current.mkdir(parents=True)
            commit_sha, tree_sha, blob_sha = "a" * 40, "b" * 40, "c" * 40
            output = current / f"README.md__{blob_sha[:12]}__{commit_sha[:12]}.md"
            output.write_text(
                "\n".join(
                    [
                        "# owner/repo · README.md",
                        "",
                        f"| 来源文件 | [README.md](https://github.com/owner/repo/blob/{commit_sha}/README.md) |",
                        f"| 来源版本 | `{commit_sha}` |",
                        f"| 来源目录 Tree | `{tree_sha}` |",
                        f"| 来源内容 Blob | `{blob_sha}` |",
                    ]
                ),
                encoding="utf-8",
            )
            (root / "source_profiles.json").write_text(
                '{"owner":"welcome","sources":[{"repo":"owner/repo","primary_owner":"welcome","layer":"test","documents":["README.md"]}]}',
                encoding="utf-8",
            )
            noncanonical = (
                "current/test/../test/owner_repo/"
                f"README.md__{blob_sha[:12]}__{commit_sha[:12]}.md"
            )
            (inputs / ".harvester_state.json").write_text(
                json.dumps(
                    {
                        "schema_version": 5,
                        "repositories": {
                            "owner/repo": {
                                "documents": {
                                    "README.md": {
                                        "sha": blob_sha,
                                        "blob_sha": blob_sha,
                                        "commit_sha": commit_sha,
                                        "tree_sha": tree_sha,
                                        "observed_blob_sha": blob_sha,
                                        "observed_commit_sha": commit_sha,
                                        "observed_tree_sha": tree_sha,
                                        "content_hash": "digest",
                                        "entity_id": "existing-entity",
                                        "output": noncanonical,
                                    }
                                }
                            }
                        },
                    }
                ),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "canonical current path"):
                Harvester(root)

    def test_legacy_sha_only_state_defers_to_controlled_source_migration(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            inputs = root / "inputs"
            current = inputs / "current" / "test" / "owner_repo"
            current.mkdir(parents=True)
            output = current / "README.md__legacy.md"
            output.write_text("legacy snapshot", encoding="utf-8")
            (root / "source_profiles.json").write_text(
                '{"owner":"welcome","sources":[{"repo":"owner/repo","primary_owner":"welcome","layer":"test","documents":["README.md"]}]}',
                encoding="utf-8",
            )
            (inputs / ".harvester_state.json").write_text(
                json.dumps(
                    {
                        "schema_version": 3,
                        "repositories": {
                            "owner/repo": {
                                "documents": {
                                    "README.md": {
                                        "sha": "c" * 40,
                                        "content_hash": "digest",
                                        "entity_id": "existing-entity",
                                        "output": output.relative_to(inputs).as_posix(),
                                    }
                                }
                            }
                        },
                    }
                ),
                encoding="utf-8",
            )

            harvester = Harvester(root)

            self.assertEqual(harvester.state["schema_version"], 5)
            document = harvester.state["repositories"]["owner/repo"]["documents"]["README.md"]
            self.assertEqual(document["sha"], "c" * 40)
            self.assertNotIn("commit_sha", document)
            self.assertNotIn("observed_blob_sha", document)

    def test_missing_state_requires_explicit_bootstrap(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "inputs").mkdir()
            (root / "source_profiles.json").write_text(
                '{"owner":"welcome","sources":[]}',
                encoding="utf-8",
            )

            with self.assertRaisesRegex(FileNotFoundError, "state"):
                Harvester(root)

            with patch.dict(os.environ, {"HARVESTER_BOOTSTRAP": "1"}):
                harvester = Harvester(root)

            self.assertEqual(harvester.state["schema_version"], 5)
            self.assertEqual(harvester.state["repositories"], {})

    def test_corrupt_state_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "inputs").mkdir()
            (root / "source_profiles.json").write_text(
                '{"owner":"welcome","sources":[]}',
                encoding="utf-8",
            )
            (root / "inputs" / ".harvester_state.json").write_text(
                "{",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "invalid JSON"):
                Harvester(root)

    def test_evolver_archive_collision_preserves_both_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            inputs = Path(tmp) / "inputs"
            inputs.mkdir()
            incoming = inputs / "incoming.md"
            incoming.write_text("new", encoding="utf-8")
            now = __import__("datetime").datetime.now()
            archived = (
                inputs
                / "archive"
                / str(now.year)
                / f"{now.month:02d}"
                / incoming.name
            )
            archived.parent.mkdir(parents=True)
            archived.write_text("sealed", encoding="utf-8")
            evolver = Evolver.__new__(Evolver)
            evolver.inputs_path = inputs

            with self.assertRaisesRegex(FileExistsError, "archive collision"):
                evolver._archive_inputs()

            self.assertEqual(incoming.read_text(encoding="utf-8"), "new")
            self.assertEqual(archived.read_text(encoding="utf-8"), "sealed")

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
