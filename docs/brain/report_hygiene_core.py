"""Render the latest machine reports as concise human-readable Markdown."""
import argparse
import re
from pathlib import Path


def atomic_write(path, text):
    from document_hygiene import atomic_write as write
    write(Path(path), text.rstrip() + "\n")


def values(text):
    result = {}
    for line in text.splitlines():
        if ":" in line and not line.startswith("#"):
            key, value = line.split(":", 1)
            if re.fullmatch(r"[A-Z0-9_ ]+", key.strip()):
                result[key.strip()] = value.strip()
    return result


def assert_period(text):
    if "。" in text:
        raise ValueError("generated report contains a Chinese full stop")


def render_welcome(memories):
    dashboards = sorted(memories.glob("*-quantitative-dashboard.md"))
    if not dashboards:
        return []
    dashboard = dashboards[-1]
    raw = dashboard.read_text(encoding="utf-8")
    stats = re.search(r"Entities=\[(\d+)\] Relations=\[(\d+)\] Compression Rate=\[([^]]+)\]", raw)
    trust = re.search(r"Trust Score: \[([^]]+)\]", raw)
    orphans = re.search(r"Orphan Alert: \[([^]]+)\]", raw)
    hubs = []
    for line in raw.splitlines():
        match = re.match(r"\[(\d+)\+(.+?)\+([0-9.]+)\+", line)
        if match:
            hubs.append((match.group(1), match.group(2), match.group(3)))
    entity, relation, compression = stats.groups() if stats else ("未知", "未知", "未知")
    rows = "\n".join(f"| {rank} | {name} | {score} |" for rank, name, score in hubs)
    output = f"""# 每日认知仪表盘

## 今日结论

- 系统状态 `ONLINE`.
- 实体 `{entity}`.
- 关系 `{relation}`.
- 压缩率 `{compression}`.
- 信任评分 `{trust.group(1) if trust else '未知'}`.

## 记忆健康

- 孤立节点 `{orphans.group(1) if orphans else '未知'}`.
- JSONL 是事实账本，SQLite 是可重建索引.

## 核心认知节点

| 排名 | 节点 | PageRank |
| --- | --- | --- |
{rows}

<details>
<summary>展开机器原始数据</summary>

```text
{raw.rstrip()}
```

</details>
"""
    assert_period(output)
    atomic_write(dashboard, output)
    mission = memories / "MISSION_ACTIVE.md"
    if mission.exists():
        source = mission.read_text(encoding="utf-8")
        tasks = [line for line in source.splitlines() if line.startswith("- [ ]")]
        mission_output = "# 当前任务\n\n## 建议动作\n\n" + ("\n".join(tasks) if tasks else "- 当前没有待执行动作.") + "\n\n## 约束\n\n- 结论必须可验证.\n- 自动生成内容只使用英文句号.\n- Jules 自主维护目录不由本流程改写.\n"
        assert_period(mission_output)
        atomic_write(mission, mission_output)
    return [dashboard, mission]


def render_zero(memories):
    reports = sorted(memories.glob("*-cognitive-report.md"))
    if not reports:
        return []
    report = reports[-1]
    raw = report.read_text(encoding="utf-8")
    data = values(raw)
    output = f"""# 每日认知报告

## 今日结论

- 系统状态 `{data.get('STATUS', 'UNKNOWN')}`.
- 节点 `{data.get('NODES', '未知')}`.
- 关系 `{data.get('EDGES', '未知')}`.
- 拓扑 `{data.get('TOPOLOGY', '未知')}`.

## 物理遥测

| 指标 | 值 |
| --- | --- |
| 存储 MB | `{data.get('STORAGE_MB', '未知')}` |
| Journal 行数 | `{data.get('JOURNAL_ROWS', '未知')}` |
| 图密度 | `{data.get('GRAPH_DENSITY', '未知')}` |

## 风险与动作

- 结构桥 `{data.get('STRUCTURAL_BRIDGES', '未知')}`.
- 推荐任务 `{data.get('TASK_SUGGESTION', '未知')}`.
- 演进策略 `{data.get('STRATEGY', '未知')}`.

<details>
<summary>展开机器原始数据</summary>

```text
{raw.rstrip()}
```

</details>
"""
    assert_period(output)
    atomic_write(report, output)
    mission = memories / "MISSION_ACTIVE.md"
    if mission.exists():
        source = mission.read_text(encoding="utf-8")
        mission_data = values(source)
        mission_output = f"""# 当前任务

## 系统状态

- 状态 `{mission_data.get('STATUS', 'UNKNOWN')}`.
- 节点 `{mission_data.get('NODES', '未知')}`.
- 关系 `{mission_data.get('EDGES', '未知')}`.

## 建议动作

- 聚焦 `{mission_data.get('FOCUS', 'SYSTEM_OPTIMIZATION')}`.
- 建议时间 `{mission_data.get('BLOCK_HOURS', '2')}` 小时.

## 约束

- 结论必须可验证.
- 自动生成内容只使用英文句号.
- Jules 自主维护目录不由本流程改写.
"""
        assert_period(mission_output)
        atomic_write(mission, mission_output)
    return [report, mission]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("welcome", "zero"))
    parser.add_argument("memories", type=Path)
    args = parser.parse_args()
    files = render_welcome(args.memories) if args.mode == "welcome" else render_zero(args.memories)
    print(f"formatted={len(files)}")


if __name__ == "__main__":
    main()
