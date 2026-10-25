"""Focused regression tests for derived Audit reference recognition.

Run: python -m unittest discover -s parallax/tools -p 'test_audit_record_refs.py'
These tests do not replace the full-tree parallax/tools/check.py command.
"""

from __future__ import annotations

import unittest

from check import AUDIT_RECORD_REF_PATTERN, NOTE_SUPPORT_PATTERN


class AuditRecordIdentityTests(unittest.TestCase):
    def test_frontier_daily_ids_are_valid_audit_references(self) -> None:
        ids = [
            "PX-20261019-STRUCTURED-VERSION-BOUNDARY",
            "PX-20261020-SAMPLING-LIFECYCLE",
            "PX-20261021-CHECK-SURFACE-IDENTITY",
            "PX-20261022-PR-REVIEW-ATTESTATION",
            "PX-20261023-PR-BASE-DRIFT",
            "PX-20261024-BLOB-CONTINUITY",
            "PX-20261025-ARTIFACT-RETENTION",
        ]
        for identifier in ids:
            with self.subTest(identifier=identifier):
                self.assertEqual(
                    AUDIT_RECORD_REF_PATTERN.findall(identifier), [identifier]
                )
                self.assertEqual(NOTE_SUPPORT_PATTERN.findall(identifier), [])

    def test_legacy_case_and_special_ids_remain_supported(self) -> None:
        for identifier in ("PX-20260914-P04", "PX-S-20260918-P04"):
            with self.subTest(identifier=identifier):
                self.assertEqual(
                    AUDIT_RECORD_REF_PATTERN.findall(identifier), [identifier]
                )
                self.assertEqual(NOTE_SUPPORT_PATTERN.findall(identifier), [identifier])

    def test_audit_references_still_reject_unresolved_record_ids(self) -> None:
        known = {"PX-20261025-ARTIFACT-RETENTION"}
        text = (
            "[PX-20261025-ARTIFACT-RETENTION](../records/2026-10/2026-10-25.md) "
            "PX-20261026-UNKNOWN"
        )
        found = set(AUDIT_RECORD_REF_PATTERN.findall(text))
        self.assertEqual(found, known | {"PX-20261026-UNKNOWN"})
        self.assertEqual(found - known, {"PX-20261026-UNKNOWN"})

    def test_nearby_non_record_labels_are_not_citations(self) -> None:
        for value in ("PA-2026-W43", "FRONTIER-ARTIFACT-RETENTION", "PX-20261025"):
            with self.subTest(value=value):
                self.assertEqual(AUDIT_RECORD_REF_PATTERN.findall(value), [])


if __name__ == "__main__":
    unittest.main()
