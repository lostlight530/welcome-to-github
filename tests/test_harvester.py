import json
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import call, patch

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

    def test_api_retries_transient_network_failures_with_backoff(self):
        harvester = Harvester.__new__(Harvester)
        harvester.token = ""

        with patch("harvester.urllib.request.urlopen", side_effect=urllib.error.URLError("offline")) as urlopen:
            with patch("harvester.time.sleep") as sleep:
                with self.assertRaises(urllib.error.URLError):
                    harvester._api("https://example.invalid")

        self.assertEqual(urlopen.call_count, 3)
        self.assertEqual(sleep.call_args_list, [call(1), call(2)])

    def test_structural_array_index_is_not_treated_as_a_version(self):
        scholar = Scholar.__new__(Scholar)
        entity_id = "file_source_profiles_prop_sources_7_documents_0"

        self.assertEqual(scholar._strip_version(entity_id), entity_id)
        self.assertEqual(scholar._strip_version("component_v1.2.3"), "component")


    def test_evolver_propagates_cycle_failure(self):
        evolver = Evolver.__new__(Evolver)

        with patch.object(
            evolver,
            "_genetic_auto_recombination",
            side_effect=RuntimeError("cycle failed"),
        ):
            with self.assertRaisesRegex(RuntimeError, "cycle failed"):
                evolver.run_daily_cycle()

    def test_evolver_propagates_render_failure(self):
        evolver = Evolver.__new__(Evolver)
        evolver.brain_path = Path(".")

        with patch("evolution.ReasoningEngine", side_effect=RuntimeError("render failed")):
            with self.assertRaisesRegex(RuntimeError, "render failed"):
                evolver._trigger_render({}, [])

    def test_evolver_propagates_mutator_failure(self):
        evolver = Evolver.__new__(Evolver)
        evolver.brain_path = Path(__file__).parent / "missing-brain"

        with self.assertRaises(FileNotFoundError):
            evolver._genetic_auto_recombination()
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
