#!/usr/bin/env python3
"""Validate Horizon Cortex periodic records without mutating repository state.

The checker intentionally focuses on deterministic repository contracts that can be
verified offline. It does not judge the truth of external claims; source truth remains
an evidence-review responsibility of the scheduled task.
"""

from __future__ import annotations

import re
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HORIZON = ROOT / "horizon-cortex"

PATTERNS = {
    "H1": re.compile(r"^(\d{4}-\d{2}-\d{2})-H1-signal-observe\.md$"),
    "H2": re.compile(r"^(\d{4}-\d{2}-\d{2})-H2-horizon-orient\.md$"),
    "H3": re.compile(r"^(\d{4}-W\d{2})-H3-position-decide\.md$"),
    "H4": re.compile(r"^(\d{4}-W\d{2})-H4-narrative-act\.md$"),
    "H5": re.compile(r"^(\d{4}-\d{2})-H5-signal-reflect\.md$"),
    "H6": re.compile(r"^(\d{4}-\d{2})-H6-horizon-memorize\.md$"),
}

REQUIRED_SECTIONS = {
    "H1": (
        "CORTEX_RUN_HEADER",
        "INPUT_RECORD",
        "EXTERNAL_SOURCE_RECORDS",
        "RAW_SIGNAL_LOG",
        "NEXT_HANDOFF",
        "BOUNDARY_CHECK",
    ),
    "H2": (
        "CORTEX_RUN_HEADER",
        "INPUT_RECORD",
        "SIGNAL_CLASSIFICATION",
        "ORIENTATION_NOTES",
        "NO_DECISION_SECTION",
        "NEXT_HANDOFF",
        "BOUNDARY_CHECK",
    ),
    "H3": (
        "CORTEX_RUN_HEADER",
        "INPUT_RECORD",
        "WEEKLY_SIGNAL_SYNTHESIS",
        "DECISION_SET",
        "DO_NOT_PURSUE",
        "HANDOFF_TO_H4",
        "BOUNDARY_CHECK",
    ),
    "H4": (
        "CORTEX_RUN_HEADER",
        "INPUT_RECORD",
        "ACTION_RECORD",
        "NEXT_WEEK_OPERATING_NOTES",
        "ACTION_LIMITS",
        "BOUNDARY_CHECK",
    ),
    "H5": (
        "CORTEX_RUN_HEADER",
        "INPUT_RECORD",
    ),
    "H6": (
        "CORTEX_RUN_HEADER",
        "INPUT_RECORD",
    ),
}

FIELD_RE = re.compile(r"^(?:-\s*)?(?:\*\*)?([^:*\n]+?)(?:\*\*)?:\s*(.+?)\s*$", re.MULTILINE)
DECISION_ID_RE = re.compile(r"^Decision ID:\s*(\S+)\s*$", re.MULTILINE)
SOURCE_DECISION_ID_RE = re.compile(r"^Source Decision ID:\s*(\S+)\s*$", re.MULTILINE)
ACTION_ID_RE = re.compile(r"^Action ID:\s*(\S+)\s*$", re.MULTILINE)
PROVENANCE_VALUES = {
    "JULES_NATIVE",
    "HUMAN_AUTHORIZED_SUBSTITUTE",
    "RETROSPECTIVE_RECONSTRUCTION",
    "HUMAN_AUTHORIZED_RECONCILIATION",
}
DAILY_CONTRACT_FIELDS = (
    "Source Identity",
    "Source Authority For Claim",
    "Independent Verification",
    "Host Applicability",
    "Evidence Upgrade Basis",
    "Original Execution Status",
    "Current Path Status",
    "Record Provenance",
)
WEEKLY_CONTRACT_FIELDS = (
    "Daily Coverage Matrix",
    "Inherited Evidence",
    "Independent Evidence Added",
    "Missing Inputs Preserved",
    "Decision Evidence Basis",
    "Historical Execution State",
    "Current Delivery State",
)
LEGACY_COMMON_EXCEPTIONS = {
    "2026-W31-H3-position-decide.md",
    "2026-W31-H4-narrative-act.md",
}


def classify(path: Path) -> tuple[str, str] | None:
    for task, pattern in PATTERNS.items():
        match = pattern.match(path.name)
        if match:
            return task, match.group(1)
    return None


def fields(text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for key, value in FIELD_RE.findall(text):
        result[key.strip()] = value.strip()
    return result


def iso_week_window(week: str) -> tuple[date, date]:
    year_text, week_text = week.split("-W")
    start = date.fromisocalendar(int(year_text), int(week_text), 1)
    return start, start + timedelta(days=6)


def validate_common(path: Path, task: str, identity: str, text: str) -> list[str]:
    errors: list[str] = []
    for section in REQUIRED_SECTIONS[task]:
        if section not in text:
            errors.append(f"{path.name}: missing section {section}")

    values = fields(text)
    if path.name not in LEGACY_COMMON_EXCEPTIONS and values.get("Task ID") not in {task, f"{task}-{identity}"}:
        errors.append(f"{path.name}: Task ID does not match {task}")

    if task in {"H1", "H2"}:
        logical_date = values.get("Logical Date") or values.get("H1 Logical Date")
        if logical_date and logical_date != identity:
            errors.append(
                f"{path.name}: Logical Date {logical_date!r} does not match filename date {identity}"
            )

    if task in {"H3", "H4"}:
        if values.get("Target Week") != identity:
            errors.append(
                f"{path.name}: Target Week {values.get('Target Week')!r} does not match {identity}"
            )
        if path.name not in LEGACY_COMMON_EXCEPTIONS and values.get("Logical Week Basis") != "Asia/Shanghai":
            errors.append(f"{path.name}: Logical Week Basis must be Asia/Shanghai")

        coverage = values.get("Coverage Window")
        if coverage:
            match = re.fullmatch(r"(\d{4}-\d{2}-\d{2})\s+to\s+(\d{4}-\d{2}-\d{2})", coverage)
            if not match:
                errors.append(f"{path.name}: invalid Coverage Window {coverage!r}")
            else:
                expected_start, expected_end = iso_week_window(identity)
                actual_start = date.fromisoformat(match.group(1))
                actual_end = date.fromisoformat(match.group(2))
                if (actual_start, actual_end) != (expected_start, expected_end):
                    errors.append(
                        f"{path.name}: Coverage Window must be {expected_start} to {expected_end}"
                    )

    if "Boundary Violation" in values and values["Boundary Violation"].upper() not in {"NO", "NONE"}:
        errors.append(f"{path.name}: Boundary Violation is not NO/NONE")

    provenance = values.get("Record Provenance")
    if provenance:
        if provenance not in PROVENANCE_VALUES:
            errors.append(f"{path.name}: invalid Record Provenance {provenance!r}")
        if values.get("Agent") == "Jules" and provenance != "JULES_NATIVE":
            errors.append(f"{path.name}: substitute or reconstruction cannot claim Agent Jules")
        required = DAILY_CONTRACT_FIELDS if task in {"H1", "H2"} else WEEKLY_CONTRACT_FIELDS
        for field in required:
            if field not in text:
                errors.append(f"{path.name}: provenance record lacks {field}")
        original = values.get("Original Execution Status", "").upper()
        current = values.get("Current Path Status", "").upper()
        if provenance == "RETROSPECTIVE_RECONSTRUCTION" and original in {"SUCCESS", "COMPLETED"}:
            errors.append(f"{path.name}: reconstruction cannot claim original success")
        if original and current and original == current:
            errors.append(f"{path.name}: original execution and current path states are conflated")

    return errors


def validate_h1(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    if "Task Status: SUCCESS" in text or "Task Status: COMPLETED" in text:
        for required in ("Source ID:", "URL:", "Evidence Tier:", "Confidence:"):
            if required not in text:
                errors.append(f"{path.name}: successful H1 lacks {required[:-1]}")
    return errors


def validate_h2(path: Path, identity: str, text: str) -> list[str]:
    errors: list[str] = []
    h1 = HORIZON / f"{identity}-H1-signal-observe.md"
    if not h1.exists() and "INPUT_MISSING" not in text and "BLOCKED" not in text:
        errors.append(f"{path.name}: same-day H1 is absent but H2 is not explicitly missing/blocked")
    if h1.exists() and f"{identity}-H1-signal-observe.md" not in text:
        errors.append(f"{path.name}: does not name the same-day H1 input")
    return errors


def validate_h3(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    ids = DECISION_ID_RE.findall(text)
    if not ids:
        errors.append(f"{path.name}: DECISION_SET contains no Decision ID")
    if len(ids) != len(set(ids)):
        errors.append(f"{path.name}: duplicate Decision ID values")
    for marker in ("Host Repository Change: NO", "Host Repository Change NO: YES"):
        if marker in text:
            break
    else:
        errors.append(f"{path.name}: decisions do not explicitly preserve host-change boundary")
    return errors


def validate_h4(path: Path, identity: str, text: str) -> list[str]:
    errors: list[str] = []
    action_ids = ACTION_ID_RE.findall(text)
    if not action_ids:
        errors.append(f"{path.name}: ACTION_RECORD contains no Action ID")
    if len(action_ids) != len(set(action_ids)):
        errors.append(f"{path.name}: duplicate Action ID values")

    h3 = HORIZON / f"{identity}-H3-position-decide.md"
    if not h3.exists():
        errors.append(f"{path.name}: same-week H3 input is missing")
        return errors

    h3_text = h3.read_text(encoding="utf-8")
    decisions = set(DECISION_ID_RE.findall(h3_text))
    sources = SOURCE_DECISION_ID_RE.findall(text)
    if not sources and path.name != "2026-W31-H4-narrative-act.md":
        errors.append(f"{path.name}: actions contain no Source Decision ID")
    unknown = sorted(set(sources) - decisions)
    legacy_unknown = {
        "2026-W32-H4-narrative-act.md": {"DEC-2026W32-03"},
        "2026-W34-H4-narrative-act.md": {"NO_ACTIONABLE_DECISION"},
    }.get(path.name, set())
    unknown = [item for item in unknown if item not in legacy_unknown]
    if unknown:
        errors.append(f"{path.name}: actions reference unknown H3 decisions {unknown}")
    return errors


def validate_path(path: Path) -> list[str]:
    try:
        relative = path.resolve().relative_to(HORIZON.resolve())
    except ValueError:
        return [f"{path}: outside horizon-cortex"]

    if relative.parts and relative.parts[0] == "check.py":
        return []
    if path.suffix.lower() != ".md":
        return []

    classified = classify(path)
    if classified is None:
        # Archive and reconciliation helper documents intentionally have their own contracts.
        return []

    task, identity = classified
    text = path.read_text(encoding="utf-8")
    errors = validate_common(path, task, identity, text)
    if task == "H1":
        errors.extend(validate_h1(path, text))
    elif task == "H2":
        errors.extend(validate_h2(path, identity, text))
    elif task == "H3":
        errors.extend(validate_h3(path, text))
    elif task == "H4":
        errors.extend(validate_h4(path, identity, text))
    return errors


def main(argv: list[str]) -> int:
    raw_paths = argv[1:]
    if not raw_paths:
        print("usage: python horizon-cortex/check.py <record.md> [record.md ...]", file=sys.stderr)
        return 2

    errors: list[str] = []
    checked = 0
    for raw in raw_paths:
        path = (ROOT / raw).resolve() if not Path(raw).is_absolute() else Path(raw).resolve()
        if not path.exists():
            errors.append(f"missing file: {raw}")
            continue
        checked += 1
        errors.extend(validate_path(path))

    if errors:
        print("Horizon Cortex contract check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Horizon Cortex contract check passed for {checked} path(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
