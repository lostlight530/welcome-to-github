import sys
import unittest
from pathlib import Path


BRAIN_DIR = Path(__file__).resolve().parents[1] / "docs" / "brain"
sys.path.insert(0, str(BRAIN_DIR))

import report_hygiene


class ReportHygieneFullOutputTests(unittest.TestCase):
    def test_daily_dashboard_does_not_backfill_unobserved_dates(self):
        import datetime
        import tempfile
        from types import SimpleNamespace
        from unittest.mock import patch
        import reason

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            memories = root / "memories"
            memories.mkdir()
            today = datetime.datetime.now().date()
            previous = today - datetime.timedelta(days=2)
            missing = today - datetime.timedelta(days=1)
            historical_path = memories / f"{previous:%Y%m%d}-quantitative-dashboard.md"
            historical_path.write_text("sealed historical record\\n", encoding="utf-8")
            fake = SimpleNamespace(
                cortex=SimpleNamespace(get_stats=lambda: {"density": 0.0}),
                _query=lambda _sql: [],
                _generate_pagerank_top_hubs=lambda _limit: "",
                _generate_pagerank_bounty=lambda: None,
            )
            with patch.object(reason, "__file__", str(root / "reason.py")):
                reason.ReasoningEngine._render_daily_archives(
                    fake,
                    {"active_entities": 2, "active_relations": 1},
                    [],
                )
            self.assertFalse((memories / f"{missing:%Y%m%d}-quantitative-dashboard.md").exists())
            self.assertEqual(historical_path.read_text(encoding="utf-8"), "sealed historical record\\n")
            self.assertTrue((memories / f"{today:%Y%m%d}-quantitative-dashboard.md").exists())
            self.assertTrue((memories / "QUANTITATIVE_LEDGER.md").exists())

    def test_rejects_chinese_full_stop_inside_details(self):
        rendered = "# Generated report.\n<details>\nraw trace\u3002\n</details>\n"

        with self.assertRaisesRegex(ValueError, "Chinese full stop"):
            report_hygiene.validate_owned_report(rendered)


if __name__ == "__main__":
    unittest.main()
