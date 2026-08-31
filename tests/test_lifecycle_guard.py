import json
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parents[1] / "docs" / "brain"))

from lifecycle_guard import (
    build_manifest,
    logical_cycle_time,
    render_lifecycle_receipt,
    world_line_outcome,
)


class LifecycleGuardTests(unittest.TestCase):
    def test_scheduled_cycle_uses_nominal_slot_not_delayed_start(self):
        self.assertEqual(
            logical_cycle_time("schedule", "2026-08-31T00:17:00Z", "0 22 * * *"),
            "2026-08-30T22:00:00Z",
        )

    def test_manifest_is_deterministic_for_the_same_inputs(self):
        kwargs = {
            "repository": "lostlight530/welcome-to-github",
            "mode": "apply",
            "base_sha": "a" * 40,
            "logical_time": "2026-08-30T22:00:00Z",
            "source_time": "2026-08-30T21:59:00Z",
            "candidate_paths": ["docs/brain/knowledge/entities.jsonl"],
            "deltas": {"source_content": 1, "knowledge": 2, "projection": 1},
            "metrics_snapshot": {"trust_score": 0.4, "entities": 12},
        }
        first = build_manifest(**kwargs)
        second = build_manifest(**kwargs)
        self.assertEqual(first, second)
        self.assertEqual(
            json.dumps(first, sort_keys=True, separators=(",", ":")),
            json.dumps(second, sort_keys=True, separators=(",", ":")),
        )

    def test_world_line_change_is_a_green_no_apply_outcome(self):
        self.assertEqual(
            world_line_outcome("a" * 40, "b" * 40),
            "CONFLICTED_WORLD_LINE_NO_APPLY",
        )

    def test_receipt_combines_human_essentials_with_expandable_panorama(self):
        manifest = build_manifest(
            repository="lostlight530/welcome-to-github",
            mode="apply",
            base_sha="a" * 40,
            logical_time="2026-08-30T22:00:00Z",
            source_time="UNKNOWN",
            observed_time="2026-08-30T22:03:00Z",
            applied_time="2026-08-30T22:04:00Z",
            outcome="APPLIED",
            candidate_paths=[
                "docs/brain/inputs/current/github-actions.md",
                "docs/brain/knowledge/entities.jsonl",
                "docs/brain/memories/MISSION_ACTIVE.md",
            ],
            deltas={"source_content": 1, "knowledge": 1, "projection": 1},
            metrics_snapshot={
                "active_entity_records": 18,
                "active_relation_records": 11,
                "current_source_snapshots": 4,
            },
        )
        receipt = render_lifecycle_receipt(
            manifest=manifest,
            repository_kind="welcome",
            before_metrics={
                "active_entity_records": 12,
                "active_relation_records": 9,
                "current_source_snapshots": 3,
            },
            event_name="workflow_dispatch",
            actor="lostlight530",
            triggering_actor="lostlight530",
            final_sha="b" * 40,
            job_status="success",
            validation_failed=False,
            run_id="12345",
            run_attempt="2",
            gate_results={"运行时契约": "success", "写入边界": "success"},
        )
        self.assertIn("# Welcome 周期运行收据", receipt)
        self.assertIn("## 一眼看懂", receipt)
        self.assertIn("已写入 main", receipt)
        self.assertIn("实体 `12 → 18`", receipt)
        self.assertIn("关系 `9 → 11`", receipt)
        self.assertIn("<details>", receipt)
        self.assertIn("完整周期证据", receipt)
        self.assertIn("github-actions.md", receipt)
        self.assertIn("`12345`, 第 `2` 次尝试", receipt)
        self.assertIn("| 运行时契约 | `success` |", receipt)
        self.assertNotIn("\u3002", receipt)

    def test_receipt_explains_validation_without_claiming_an_apply(self):
        receipt = render_lifecycle_receipt(
            manifest=None,
            repository_kind="welcome",
            before_metrics={
                "active_entity_records": 12,
                "active_relation_records": 9,
                "current_source_snapshots": 3,
            },
            event_name="pull_request",
            actor="contributor",
            triggering_actor="contributor",
            base_sha="a" * 40,
            final_sha="a" * 40,
            job_status="success",
            validation_failed=False,
            gate_results={"只读边界": "success"},
        )
        self.assertIn("`VALIDATED_ONLY`", receipt)
        self.assertIn("只读验证", receipt)
        self.assertIn("没有尝试写入", receipt)


if __name__ == "__main__":
    unittest.main()
