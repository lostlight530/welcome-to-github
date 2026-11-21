"""Read-only regression tests for existing NEXUS archive/source custody.

All checks use local, checked-out files and original Git objects. No network,
harvest, archive mutation, main push, or generated ledger modification.
"""
import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
SYSTEM = ROOT / "docs/brain"
sys.path.insert(0, str(ROOT / "docs/brain"))
from harvester import Harvester


class NexusArchiveCustodyTests(unittest.TestCase):
    def test_current_snapshots_match_registered_source_state(self):
        inputs = SYSTEM / "inputs"
        profiles = json.loads((SYSTEM / "source_profiles.json").read_text(encoding="utf-8"))
        state = json.loads((inputs / ".harvester_state.json").read_text(encoding="utf-8"))
        approved = {profile["repo"] for profile in profiles["sources"]}
        self.assertEqual(len(approved), len(profiles["sources"]))
        self.assertTrue(set(state["repositories"]).issubset(approved))

        expected = set()
        for repo, repo_state in state["repositories"].items():
            for source, document in repo_state["documents"].items():
                output = PurePosixPath(document["output"])
                self.assertEqual(output.parts[0], "current", (repo, source, output))
                self.assertNotIn("..", output.parts)
                target = inputs.joinpath(*output.parts)
                self.assertTrue(target.is_file(), (repo, source, target))
                self.assertNotIn(target, expected)
                expected.add(target)

        observed = set((inputs / "current").rglob("*.md"))
        self.assertEqual(expected, observed)
        # Harvester validates each selected source's persisted provenance,
        # bounded content hash, source identity, and on-disk current snapshot.
        harvester = Harvester(SYSTEM)
        self.assertEqual(harvester.validate_active_snapshots()["documents"], len(expected))

    def test_sealed_precanonical_archive_matches_original_manifest_bytes(self):
        archive = SYSTEM / "knowledge" / "archive" / "pre-canonical-2026-07-13"
        manifest = json.loads((archive / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["schema"], "nexus-ledger-archive")
        declared = set()
        for entry in manifest["files"]:
            rel = PurePosixPath(entry["path"])
            self.assertEqual(rel.suffix, ".jsonl")
            self.assertFalse(rel.is_absolute())
            self.assertNotIn("..", rel.parts)
            target = archive.joinpath(*rel.parts)
            self.assertTrue(target.is_file(), target)
            self.assertNotIn(target, declared)
            declared.add(target)

            # EOL conversion may change worktree bytes; Git blob identity is
            # authoritative for the historical archive manifest.
            object_name = target.relative_to(ROOT).as_posix()
            raw = subprocess.check_output(
                ["git", "show", f"HEAD:{object_name}"], cwd=ROOT
            )
            self.assertEqual(len(raw), entry["size"], object_name)
            self.assertEqual(hashlib.sha256(raw).hexdigest(), entry["sha256"], object_name)
            self.assertEqual(
                sum(bool(line.strip()) for line in raw.splitlines()),
                entry["records"],
                object_name,
            )

        observed = set(archive.rglob("*.jsonl"))
        self.assertEqual(declared, observed)


if __name__ == "__main__":
    unittest.main()
