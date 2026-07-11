import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "docs" / "brain"))
from document_hygiene import maintain_jsonl, render_snapshot, validate_owned_punctuation
from harvester import Harvester


class ReadabilityContracts(unittest.TestCase):
    def test_snapshot_is_human_readable_and_traceable(self):
        provenance = {"source_repo": "owner/repo", "source_path": "README.md", "source_sha": "abc123", "retrieved_at": "2026-07-11T00:00:00Z", "confidence": 1.0, "entity_id": "doc_readme"}
        output = render_snapshot(provenance, "# Title\nBody。", "+new", "agent-runtime")
        self.assertIn("## 一眼看懂", output)
        self.assertIn("<summary>展开完整外部原文</summary>", output)
        validate_owned_punctuation(output)

    def test_jsonl_maintenance_recurses_and_deduplicates(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "nested" / "items.jsonl"
            path.parent.mkdir()
            item = {"id": "a", "valid_at": "2026-07-11T00:00:00Z"}
            path.write_text(json.dumps(item) + "\n" + json.dumps(item) + "\n", encoding="utf-8")
            result = maintain_jsonl(Path(tmp), rewrite=True)
            self.assertEqual(result["duplicates"], 1)
            self.assertEqual(len(path.read_text(encoding="utf-8").splitlines()), 1)

    def test_truncated_tree_is_a_hard_failure(self):
        harvester = Harvester.__new__(Harvester)
        harvester.state = {"repositories": {}}
        harvester.inputs = Path("inputs")
        harvester._api = lambda url: {"default_branch": "main"} if "/repos/" in url and "/git/trees/" not in url else {"truncated": True}
        with self.assertRaisesRegex(ValueError, "truncated"):
            harvester._source({"repo": "owner/repo", "documents": [], "ignore_patterns": [], "layer": "test", "primary_owner": "welcome"})


if __name__ == "__main__":
    unittest.main()
