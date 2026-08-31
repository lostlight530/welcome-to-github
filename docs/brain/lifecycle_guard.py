"""Deterministic lifecycle decisions for GitHub Actions.

This module does not harvest, mutate ledgers, call a model, or access the network.
It turns explicit evidence into a stable manifest and a fail-closed apply decision.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import subprocess
from pathlib import Path


SCHEMA_VERSION = 1
NO_APPLY = "CONFLICTED_WORLD_LINE_NO_APPLY"


def _utc(value: str) -> dt.datetime:
    parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timestamp must include a timezone")
    return parsed.astimezone(dt.timezone.utc)


def _iso(value: dt.datetime) -> str:
    return value.astimezone(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def logical_cycle_time(event_name: str, observed_time: str, schedule: str = "0 22 * * *") -> str:
    """Return the nominal cycle slot instead of the delayed runner start time."""
    observed = _utc(observed_time)
    if event_name != "schedule":
        return _iso(observed)
    fields = schedule.split()
    if len(fields) != 5 or not fields[0].isdigit() or not fields[1].isdigit():
        raise ValueError("only fixed daily minute and hour schedules are supported")
    minute, hour = int(fields[0]), int(fields[1])
    if not 0 <= minute <= 59 or not 0 <= hour <= 23:
        raise ValueError("invalid schedule slot")
    slot = observed.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if slot > observed:
        slot -= dt.timedelta(days=1)
    return _iso(slot)


def _canonical(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def build_manifest(
    *,
    repository: str,
    mode: str,
    base_sha: str,
    logical_time: str,
    source_time: str,
    candidate_paths: list[str],
    deltas: dict[str, int],
    metrics_snapshot: dict[str, object],
    observed_time: str | None = None,
    applied_time: str | None = None,
    outcome: str | None = None,
) -> dict[str, object]:
    if mode not in {"validate", "dry-run", "apply"}:
        raise ValueError("unsupported lifecycle mode")
    candidates = sorted(set(candidate_paths))
    stable = {
        "schema_version": SCHEMA_VERSION,
        "repository": repository,
        "mode": mode,
        "base_sha": base_sha,
        "logical_cycle_time": logical_time,
        "source_time": source_time,
        "candidate_paths": candidates,
        "deltas": {key: int(deltas[key]) for key in sorted(deltas)},
        "metrics_snapshot": {key: metrics_snapshot[key] for key in sorted(metrics_snapshot)},
        "automatic_evidence_ceiling": "E2",
    }
    identity = hashlib.sha256(_canonical(stable)).hexdigest()
    manifest = {
        **stable,
        "idempotency_key": identity,
        "observed_time": observed_time or logical_time,
        "applied_time": applied_time,
        "outcome": outcome or ("CANDIDATE_READY" if candidates else "NO_MEANINGFUL_DELTA"),
    }
    return manifest


def world_line_outcome(base_sha: str, remote_sha: str) -> str:
    if not base_sha or not remote_sha:
        raise ValueError("world-line SHAs must be non-empty")
    return "WORLD_LINE_STABLE" if base_sha == remote_sha else NO_APPLY


def changed_paths() -> list[str]:
    tracked = subprocess.check_output(("git", "diff", "--name-only"), text=True).splitlines()
    untracked = subprocess.check_output(
        ("git", "ls-files", "--others", "--exclude-standard"), text=True
    ).splitlines()
    return sorted({path for path in tracked + untracked if path})


def classify_delta(paths: list[str]) -> dict[str, int]:
    return {
        "source_content": sum(path.startswith("docs/brain/inputs/current/") for path in paths),
        "knowledge": sum(path.startswith("docs/brain/knowledge/") for path in paths),
        "projection": sum(path.startswith("docs/brain/memories/") for path in paths),
    }


def snapshot_metrics(root: Path = Path(".")) -> dict[str, int]:
    knowledge = root / "docs" / "brain" / "knowledge"
    active = [path for path in knowledge.rglob("*.jsonl") if "archive" not in path.parts]
    entity_records = 0
    relation_records = 0
    for path in active:
        count = sum(bool(line.strip()) for line in path.read_text(encoding="utf-8").splitlines())
        if "relations" in path.parts:
            relation_records += count
        else:
            entity_records += count
    current = root / "docs" / "brain" / "inputs" / "current"
    return {
        "active_entity_records": entity_records,
        "active_relation_records": relation_records,
        "current_source_snapshots": sum(1 for path in current.rglob("*.md")) if current.exists() else 0,
    }


def _command_manifest(args: argparse.Namespace) -> int:
    now = _iso(dt.datetime.now(dt.timezone.utc))
    paths = changed_paths()
    manifest = build_manifest(
        repository=args.repository,
        mode=args.mode,
        base_sha=args.base_sha,
        logical_time=logical_cycle_time(args.event_name, args.observed_time or now),
        source_time=args.source_time or "UNKNOWN",
        observed_time=args.observed_time or now,
        candidate_paths=paths,
        deltas=classify_delta(paths),
        metrics_snapshot=snapshot_metrics(),
    )
    destination = Path(args.output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, sort_keys=True))
    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with Path(output).open("a", encoding="utf-8") as handle:
            handle.write(f"candidate_count={len(paths)}\n")
    return 0


def _command_finalize(args: argparse.Namespace) -> int:
    destination = Path(args.manifest)
    manifest = json.loads(destination.read_text(encoding="utf-8"))
    manifest["outcome"] = args.outcome
    manifest["applied_time"] = (
        _iso(dt.datetime.now(dt.timezone.utc)) if args.outcome == "APPLIED" else None
    )
    destination.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


def _command_world_line(args: argparse.Namespace) -> int:
    outcome = world_line_outcome(args.base_sha, args.remote_sha)
    print(outcome)
    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with Path(output).open("a", encoding="utf-8") as handle:
            handle.write(f"outcome={outcome}\n")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", required=True)
    manifest = commands.add_parser("manifest")
    manifest.add_argument("--repository", required=True)
    manifest.add_argument("--mode", choices=("validate", "dry-run", "apply"), required=True)
    manifest.add_argument("--base-sha", required=True)
    manifest.add_argument("--event-name", required=True)
    manifest.add_argument("--observed-time")
    manifest.add_argument("--source-time")
    manifest.add_argument("--output", required=True)
    manifest.set_defaults(handler=_command_manifest)
    world_line = commands.add_parser("world-line")
    world_line.add_argument("--base-sha", required=True)
    world_line.add_argument("--remote-sha", required=True)
    world_line.set_defaults(handler=_command_world_line)
    finalize = commands.add_parser("finalize")
    finalize.add_argument("--manifest", required=True)
    finalize.add_argument(
        "--outcome",
        choices=("APPLIED", "NO_MEANINGFUL_DELTA", NO_APPLY),
        required=True,
    )
    finalize.set_defaults(handler=_command_finalize)
    args = parser.parse_args(argv)
    return args.handler(args)


if __name__ == "__main__":
    raise SystemExit(main())
