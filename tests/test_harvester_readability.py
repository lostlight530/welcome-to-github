import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "docs" / "brain"))
from document_hygiene import (
    canonicalize_ledger,
    maintain_jsonl,
    project_current_snapshots,
    render_snapshot,
    validate_owned_punctuation,
)
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

    def test_current_snapshot_projection_is_stable_and_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            inputs = root / "inputs"
            current = inputs / "current" / "agent-runtime" / "owner_repo"
            current.mkdir(parents=True)
            snapshot = current / "README.md__abc123.md"
            snapshot.write_text(
                "# owner/repo ? README.md\n\n"
                "| ???? | [owner/repo](https://github.com/owner/repo) |\n"
                "| ???? | [README.md](https://github.com/owner/repo/blob/abc123/README.md) |\n"
                "| ???? | `abc123` |\n"
                "| ??? | `agent-runtime` |\n",
                encoding="utf-8",
            )
            knowledge = root / "knowledge"

            first = project_current_snapshots(inputs, knowledge)
            before = {path.name: path.read_bytes() for path in knowledge.rglob("*.jsonl")}
            second = project_current_snapshots(inputs, knowledge)
            after = {path.name: path.read_bytes() for path in knowledge.rglob("*.jsonl")}

            self.assertEqual(first, {"documents": 1, "repositories": 1, "relations": 1})
            self.assertEqual(second, first)
            self.assertEqual(after, before)
            document = json.loads((knowledge / "entities" / "external_document.jsonl").read_text(encoding="utf-8"))
            self.assertEqual(document["id"], "external_doc_owner_repo_readme_md")

    def test_canonicalization_removes_semantic_duplicates_and_dangling_relations(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            entities = root / "entities"
            relations = root / "relations"
            entities.mkdir()
            relations.mkdir()
            (entities / "concept.jsonl").write_text(
                json.dumps({"id": "a", "type": "concept", "name": "A", "desc": "x", "valid_at": "1"}) + "\n"
                + json.dumps({"id": "a", "type": "concept", "name": "A", "desc": "x", "valid_at": "2"}) + "\n"
                + json.dumps({"id": "b", "type": "concept", "name": "B", "desc": "y"}) + "\n",
                encoding="utf-8",
            )
            (relations / "items.jsonl").write_text(
                json.dumps({"src": "a", "relation": "links", "dst": "b"}) + "\n"
                + json.dumps({"src": "a", "relation": "links", "dst": "b"}) + "\n"
                + json.dumps({"src": "a", "relation": "links", "dst": "missing"}) + "\n",
                encoding="utf-8",
            )

            result = canonicalize_ledger(root)

            self.assertEqual(result["duplicate_entities"], 1)
            self.assertEqual(result["duplicate_relations"], 1)
            self.assertEqual(result["dangling_relations"], 1)
            self.assertEqual(result["entities"], 2)
            self.assertEqual(result["relations"], 1)

    def test_truncated_tree_is_a_hard_failure(self):
        harvester = Harvester.__new__(Harvester)
        harvester.state = {"repositories": {}}
        harvester.inputs = Path("inputs")
        harvester._api = lambda url: {"default_branch": "main"} if "/repos/" in url and "/git/trees/" not in url else {"truncated": True}
        with self.assertRaisesRegex(ValueError, "truncated"):
            harvester._source({"repo": "owner/repo", "documents": [], "ignore_patterns": [], "layer": "test", "primary_owner": "welcome"})


if __name__ == "__main__":
    unittest.main()
