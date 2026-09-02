"""Offline checks for metadata, calendar boundaries and monthly maintenance."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(relative, name):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class MaintenanceContracts(unittest.TestCase):
    def setUp(self):
        self.cortex = load("horizon-cortex/check.py", "cortex")
        self.research = load("parallax/tools/check.py", "research")

    def test_empty_field_does_not_borrow_next_line(self):
        self.assertEqual("", self.cortex.fields("Record Provenance:\nTask ID: X\n")["Record Provenance"])
        self.assertEqual([""], self.research.metadata("- Record Provenance:\n- 实际执行日期: 2026-09-02\n", "Record Provenance"))

    def test_month_cannot_close_early(self):
        errors = self.cortex.validate_month_calendar(Path("month.md"), "2026-08",
            "Month Closure Status: CLOSED\nExecution Time Asia/Shanghai: 2026-08-31T23:59:59+08:00\n")
        self.assertTrue(any("calendar" in e for e in errors), errors)

    def test_closed_calendar_can_have_blocked_task(self):
        self.assertEqual([], self.cortex.validate_month_calendar(Path("month.md"), "2026-08",
            "Month Closure Status: CLOSED\nTask Status: BLOCKED\nExecution Time Asia/Shanghai: 2026-09-01T00:00:00+08:00\n"))

    def test_open_snapshot_preserves_gap(self):
        self.assertEqual([], self.cortex.validate_month_calendar(Path("month.md"), "2026-09",
            "Month Closure Status: OPEN\nMissing Inputs Preserved: Month not ended\n"))

    def test_missing_new_month_timestamp_fails(self):
        self.assertTrue(self.cortex.validate_month_calendar(Path("month.md"), "2026-09",
            "Month Closure Status: CLOSED\n"))

    def test_legacy_unknown_execution_not_invented(self):
        self.assertEqual([], self.cortex.validate_month_calendar(Path("month.md"), "2026-08",
            "Month Closure Status: CLOSED\n"))

    def test_invalid_timestamp_fails(self):
        self.assertTrue(self.cortex.validate_month_calendar(Path("month.md"), "2026-09",
            "Month Closure Status: CLOSED\nExecution Time Asia/Shanghai: invalid\n"))

    def valid_maintenance(self):
        return ("Monthly Maintenance Status: COMPLETED\n"
                "Maintenance Coverage: inventory.md\nMaintenance Change Log: changes.md\n"
                "Maintenance Validation: validation output in changes.md\n"
                "Maintenance Unresolved: NONE\n")

    def check_both(self, text):
        return [m.validate_monthly_maintenance("month.md", text) for m in (self.cortex, self.research)]

    def test_summary_without_log_not_complete(self):
        for errors in self.check_both(self.valid_maintenance().replace("Maintenance Change Log: changes.md\n", "")):
            self.assertTrue(any("Maintenance Change Log" in e for e in errors), errors)

    def test_complete_cannot_hide_unresolved_work(self):
        for errors in self.check_both(self.valid_maintenance().replace("Maintenance Unresolved: NONE", "Maintenance Unresolved: source unavailable")):
            self.assertTrue(errors)

    def test_partial_keeps_unresolved_work(self):
        text = self.valid_maintenance().replace("COMPLETED", "PARTIAL").replace("Maintenance Unresolved: NONE", "Maintenance Unresolved: source unavailable")
        self.assertEqual([[], []], self.check_both(text))

    def test_duplicate_status_rejected(self):
        for errors in self.check_both(self.valid_maintenance() + "Monthly Maintenance Status: COMPLETED\n"):
            self.assertTrue(errors)

    def test_complete_with_explicit_evidence_accepted(self):
        self.assertEqual([[], []], self.check_both(self.valid_maintenance()))

    def test_legacy_without_new_contract_compatible(self):
        self.assertEqual([[], []], self.check_both("# Historical record\n"))


if __name__ == "__main__":
    unittest.main()
