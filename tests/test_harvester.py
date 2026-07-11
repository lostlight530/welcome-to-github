import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "docs" / "brain"))
from harvester import Harvester


class HarvesterContracts(unittest.TestCase):
    def test_profiles_have_unique_welcome_owner(self):
        h = Harvester(Path(__file__).parents[1] / "docs" / "brain")
        self.assertTrue(h.validate_profiles())

    def test_external_links_are_not_selected(self):
        self.assertFalse(Harvester._selected("docs/link-from-readme.md", ["README.md"], []))

    def test_noise_normalization(self):
        self.assertEqual(Harvester._normalized("![badge](https://shields.io/x)\nArchitecture"), "Architecture")


if __name__ == "__main__":
    unittest.main()
