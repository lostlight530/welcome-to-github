import sys
import unittest
from pathlib import Path


BRAIN_DIR = Path(__file__).resolve().parents[1] / "docs" / "brain"
sys.path.insert(0, str(BRAIN_DIR))

import report_hygiene


class ReportHygieneFullOutputTests(unittest.TestCase):
    def test_rejects_chinese_full_stop_inside_details(self):
        rendered = "# Generated report.\n<details>\nraw trace\u3002\n</details>\n"

        with self.assertRaisesRegex(ValueError, "Chinese full stop"):
            report_hygiene.validate_owned_report(rendered)


if __name__ == "__main__":
    unittest.main()
