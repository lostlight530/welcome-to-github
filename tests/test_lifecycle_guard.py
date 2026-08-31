import json
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parents[1] / "docs" / "brain"))

from lifecycle_guard import (
    build_manifest,
    logical_cycle_time,
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


if __name__ == "__main__":
    unittest.main()
