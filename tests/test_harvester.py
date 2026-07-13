import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "docs" / "brain"))
from harvester import Harvester
from evolution import Evolver
from scholar import Scholar


class HarvesterContracts(unittest.TestCase):
    def test_profiles_have_unique_welcome_owner(self):
        h = Harvester(Path(__file__).parents[1] / "docs" / "brain")
        self.assertTrue(h.validate_profiles())

    def test_external_links_are_not_selected(self):
        self.assertFalse(Harvester._selected("docs/link-from-readme.md", ["README.md"], []))

    def test_noise_normalization(self):
        self.assertEqual(Harvester._normalized("![badge](https://shields.io/x)\nArchitecture"), "Architecture")
    def test_structural_array_index_is_not_treated_as_a_version(self):
        scholar = Scholar.__new__(Scholar)
        entity_id = "file_source_profiles_prop_sources_7_documents_0"

        self.assertEqual(scholar._strip_version(entity_id), entity_id)
        self.assertEqual(scholar._strip_version("component_v1.2.3"), "component")

    def test_evolver_keeps_input_contract_out_of_monthly_archive(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            inputs = Path(tmp) / "inputs"
            inputs.mkdir()
            contract = inputs / "ARCHIVE_AND_HARVESTER.md"
            contract.write_text("contract", encoding="utf-8")
            incoming = inputs / "incoming.md"
            incoming.write_text("input", encoding="utf-8")
            evolver = Evolver.__new__(Evolver)
            evolver.inputs_path = inputs

            evolver._archive_inputs()

            self.assertTrue(contract.exists())
            self.assertFalse(incoming.exists())
            self.assertEqual(len(list((inputs / "archive").rglob("incoming.md"))), 1)

if __name__ == "__main__":
    unittest.main()
