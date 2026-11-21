"""NEXUS local cache cleanup keeps sealed evidence outside the deletion boundary."""
import sys
import tempfile
import unittest
from pathlib import Path

BRAIN = Path(__file__).resolve().parents[1] / "docs" / "brain"
sys.path.insert(0, str(BRAIN))
from nexus import cleanup_brain_sqlite_index


class BrainCleanupContracts(unittest.TestCase):
    def test_only_closed_sqlite_index_and_sidecars_are_removed(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            brain = root / "docs" / "brain"
            brain.mkdir(parents=True)
            targets = [brain / ("cortex.db" + suffix)
                       for suffix in ("", "-journal", "-wal", "-shm")]
            for path in targets:
                path.write_bytes(b"rebuildable")
            protected = [
                brain / "inputs" / "archive" / "historic.md",
                brain / "inputs" / ".harvester_state.json",
                brain / "knowledge" / "entities" / "concept.jsonl",
                brain / "memories" / "20261121-quantitative-dashboard.md",
                root / "horizon-cortex" / "trace.md",
                root / "parallax" / "records" / "trace.md",
            ]
            for path in protected:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b"original evidence")

            self.assertEqual(
                cleanup_brain_sqlite_index(brain / "cortex.db"),
                [path.name for path in targets],
            )
            self.assertFalse(any(path.exists() for path in targets))
            self.assertEqual(cleanup_brain_sqlite_index(brain / "cortex.db"), [])
            for path in protected:
                self.assertEqual(path.read_bytes(), b"original evidence")

    def test_symlink_preflight_aborts_without_partial_cleanup(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            db = root / "cortex.db"
            db.write_bytes(b"stable")
            protected = root / "evidence.md"
            protected.write_bytes(b"do not touch")
            (root / "cortex.db-wal").symlink_to(protected)
            with self.assertRaisesRegex(ValueError, "unsafe NEXUS cache target"):
                cleanup_brain_sqlite_index(db)
            self.assertEqual(db.read_bytes(), b"stable")
            self.assertEqual(protected.read_bytes(), b"do not touch")

    def test_rejects_unrelated_db(self):
        with tempfile.TemporaryDirectory() as temp:
            other = Path(temp) / "research.db"
            other.write_bytes(b"owned")
            with self.assertRaisesRegex(ValueError, "non-NEXUS"):
                cleanup_brain_sqlite_index(other)
            self.assertEqual(other.read_bytes(), b"owned")


if __name__ == "__main__":
    unittest.main()
