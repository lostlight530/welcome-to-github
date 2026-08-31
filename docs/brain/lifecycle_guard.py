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

HUMAN_OUTCOMES = {
    "VALIDATED_ONLY": "只读验证通过，没有尝试写入",
    "APPLIED": "候选变化通过全部门禁，已写入 main",
    "NO_MEANINGFUL_DELTA": "生命周期已完成，没有产生值得提交的有效变化",
    NO_APPLY: "运行期间 main 已变化，为避免覆盖而拒绝写入",
    "REJECTED_INVALID_EVIDENCE": "候选内容未通过确定性证据门禁，没有写入",
    "FAILED_RUNTIME": "运行环境或程序失败，未形成有效生命周期结论",
}


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


def _human_outcome(
    manifest: dict[str, object] | None, job_status: str, validation_failed: bool
) -> str:
    if job_status != "success":
        return "REJECTED_INVALID_EVIDENCE" if validation_failed else "FAILED_RUNTIME"
    if manifest is None:
        return "VALIDATED_ONLY"
    return str(manifest.get("outcome") or "FAILED_RUNTIME")


def _metric_change(before: dict[str, object], after: dict[str, object], key: str) -> str:
    return f"{before.get(key, '未知')} → {after.get(key, '未知')}"


def _short_sha(value: object) -> str:
    text = str(value or "UNKNOWN")
    return text[:12] if len(text) >= 12 else text


def render_lifecycle_receipt(
    *,
    manifest: dict[str, object] | None,
    repository_kind: str,
    before_metrics: dict[str, object],
    event_name: str,
    actor: str,
    triggering_actor: str,
    final_sha: str,
    job_status: str,
    validation_failed: bool,
    base_sha: str | None = None,
    run_id: str = "未记录",
    run_attempt: str = "1",
    gate_results: dict[str, str] | None = None,
) -> str:
    """Render a concise human result followed by an expandable evidence panorama."""
    if repository_kind not in {"welcome", "zero"}:
        raise ValueError("unsupported repository kind")
    outcome = _human_outcome(manifest, job_status, validation_failed)
    explanation = HUMAN_OUTCOMES.get(outcome, "未识别的生命周期结果")
    title = "Welcome" if repository_kind == "welcome" else "Zero"
    event_labels = {
        "schedule": "定时周期",
        "workflow_dispatch": "人工触发应用",
        "pull_request": "拉取请求验证",
        "push": "推送验证",
    }
    data = manifest or {}
    after_metrics = dict(data.get("metrics_snapshot") or before_metrics)
    deltas = dict(data.get("deltas") or {})
    candidates = list(data.get("candidate_paths") or [])
    effective_base = str(data.get("base_sha") or base_sha or "UNKNOWN")
    logical_time = str(data.get("logical_cycle_time") or "本次事件时间")
    observed_time = str(data.get("observed_time") or "未记录")
    applied_time = str(data.get("applied_time") or "未写入")
    source_names = sorted(
        Path(path).name
        for path in candidates
        if "/inputs/current/" in f"/{path}"
    )
    visible_sources = source_names[:20]
    source_summary = "、".join(f"`{name}`" for name in visible_sources) or "无新增当前来源快照"
    if len(source_names) > len(visible_sources):
        source_summary += f", 其余 `{len(source_names) - len(visible_sources)}` 个见 Manifest"
    if repository_kind == "welcome":
        key_change = (
            f"来源快照 `{_metric_change(before_metrics, after_metrics, 'current_source_snapshots')}`, "
            f"实体 `{_metric_change(before_metrics, after_metrics, 'active_entity_records')}`, "
            f"关系 `{_metric_change(before_metrics, after_metrics, 'active_relation_records')}`"
        )
    else:
        key_change = (
            f"来源快照 `{_metric_change(before_metrics, after_metrics, 'current_source_snapshots')}`, "
            f"实体 `{_metric_change(before_metrics, after_metrics, 'active_entity_records')}`, "
            f"关系 `{_metric_change(before_metrics, after_metrics, 'active_relation_records')}`, "
            f"哈希记录 `{_metric_change(before_metrics, after_metrics, 'active_hash_records')}`"
        )
    semantic_note = ""
    if repository_kind == "zero" and deltas.get("hash_chain_derived", 0):
        semantic_note = (
            f"\n- 语义边界: `{deltas.get('hash_chain_derived', 0)}` 个路径仅为哈希链确定性派生, "
            "不代表新增外部事实"
        )
    actor_text = actor if actor == triggering_actor else f"{actor}, 重跑触发者 {triggering_actor}"
    visible_paths = candidates[:100]
    path_rows = "\n".join(f"- `{path}`" for path in visible_paths) or "- 无候选路径"
    if len(candidates) > len(visible_paths):
        path_rows += f"\n- 其余 `{len(candidates) - len(visible_paths)}` 个候选路径见 Manifest"
    gate_order = (
        "运行时契约",
        "活动账本",
        "哈希链与图谱",
        "最终验证",
        "写入边界",
        "只读边界",
        "世界线检查",
        "应用步骤",
    )
    gates = gate_results or {}
    ordered_gates = [name for name in gate_order if name in gates]
    ordered_gates.extend(sorted(name for name in gates if name not in gate_order))
    gate_rows = "\n".join(f"| {name} | `{gates[name]}` |" for name in ordered_gates)
    if not gate_rows:
        gate_rows = "| 未记录 | `unknown` |"
    return f"""# {title} 周期运行收据

## 一眼看懂

- 结果: `{outcome}`, {explanation}
- 关键变化: {key_change}
- 候选构成: 来源 `{deltas.get('source_content', 0)}`, 知识 `{deltas.get('knowledge', 0)}`, 投影 `{deltas.get('projection', 0)}`{semantic_note}

<details>
<summary>展开完整周期证据</summary>

## 完整周期证据

| 项目 | 记录 |
| --- | --- |
| 触发方式 | {event_labels.get(event_name, event_name)} |
| 逻辑周期 | `{logical_time}` |
| 实际观察时间 | `{observed_time}` |
| 来源时间 | `{data.get('source_time', '只读验证无来源时间')}` |
| 应用时间 | `{applied_time}` |
| 执行身份 | `{actor_text}` |
| GitHub Run | `{run_id}`, 第 `{run_attempt}` 次尝试 |
| 基础 SHA | `{_short_sha(effective_base)}` |
| 最终 SHA | `{_short_sha(final_sha)}` |
| 幂等键 | `{data.get('idempotency_key', '只读验证无应用键')}` |
| 自动证据上限 | `{data.get('automatic_evidence_ceiling', '只读验证不升级证据')}` |

### 来源摘要

{source_summary}

### 候选路径

{path_rows}

### 门禁状态

| 门禁 | 状态 |
| --- | --- |
{gate_rows}

### 门禁解释

- `VALIDATED_ONLY` 只证明代码、账本和边界检查通过, 不代表执行过生命周期写入
- 负向测试中的预期拒绝是测试证据, 不代表本轮发生真实事故
- 只有 `APPLIED` 表示候选变化通过世界线和写入边界后进入 main

</details>
"""


def _write_json(destination: Path, value: object) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


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
    _write_json(destination, manifest)
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
    _write_json(destination, manifest)
    return 0


def _command_snapshot(args: argparse.Namespace) -> int:
    _write_json(Path(args.output), snapshot_metrics())
    return 0


def _command_receipt(args: argparse.Namespace) -> int:
    manifest_path = Path(args.manifest) if args.manifest else None
    before_path = Path(args.before) if args.before else None
    manifest = (
        json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest_path and manifest_path.exists()
        else None
    )
    before = (
        json.loads(before_path.read_text(encoding="utf-8"))
        if before_path and before_path.exists()
        else snapshot_metrics()
    )
    receipt = render_lifecycle_receipt(
        manifest=manifest,
        repository_kind=args.repository_kind,
        before_metrics=before,
        event_name=args.event_name,
        actor=args.actor,
        triggering_actor=args.triggering_actor,
        base_sha=args.base_sha,
        final_sha=args.final_sha,
        job_status=args.job_status,
        validation_failed=args.validation_failed,
        run_id=args.run_id,
        run_attempt=args.run_attempt,
        gate_results=dict(item.split("=", 1) for item in args.gate),
    )
    with Path(args.output).open("a", encoding="utf-8") as handle:
        handle.write(receipt)
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
    snapshot = commands.add_parser("snapshot")
    snapshot.add_argument("--output", required=True)
    snapshot.set_defaults(handler=_command_snapshot)
    receipt = commands.add_parser("receipt")
    receipt.add_argument("--manifest")
    receipt.add_argument("--before")
    receipt.add_argument("--repository-kind", choices=("welcome", "zero"), required=True)
    receipt.add_argument("--event-name", required=True)
    receipt.add_argument("--actor", required=True)
    receipt.add_argument("--triggering-actor", required=True)
    receipt.add_argument("--base-sha")
    receipt.add_argument("--final-sha", required=True)
    receipt.add_argument("--job-status", required=True)
    receipt.add_argument("--validation-failed", action="store_true")
    receipt.add_argument("--run-id", default="未记录")
    receipt.add_argument("--run-attempt", default="1")
    receipt.add_argument("--gate", action="append", default=[])
    receipt.add_argument("--output", required=True)
    receipt.set_defaults(handler=_command_receipt)
    args = parser.parse_args(argv)
    return args.handler(args)


if __name__ == "__main__":
    raise SystemExit(main())
