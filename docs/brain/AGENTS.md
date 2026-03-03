# NEXUS CORTEX: Operational Directives (操作指令)

## Architecture & Workflow (工程化闭环)
The system operates on an "Autonomous Radar → OODA Loop → Human Decision → Append-Only Memory" lifecycle.
本仓库采用“雷达索敌 → OODA 循环 → 人类裁决 → 追加记忆”的工程化闭环。

All Agents (including Jules) must prioritize: **Auditability, Restraint, Zero-Dependency, and Human-in-the-loop**.
任何 Agent 必须优先保证：可审计、克制、零依赖、人在环。

## Core Philosophy (核心法则)
1. **Zero-Dependency Brutalism (零依赖极简)**: Prefer Python stdlib (`urllib`, `sqlite3`). Reject bloated frameworks.
2. **Append-Only Memory (不可篡改)**: History is immutable (ADR-0001). Mistakes are fixed via `deprecates` or `conflicts_with` tension edges, not deletions.
3. **Machine Draft, Human Decision (算力主权)**: Agents propose updates (via PR or `MISSION_ACTIVE.md`), but humans execute the final `nexus.py connect` commands.

## Whitelisted Directories (允许写入的目录)
- `docs/brain/inputs/`: Raw intelligence briefs from Harvester (Radar).
- `docs/brain/knowledge/`: Append-only JSONL files for the Knowledge Graph.
- `docs/brain/memories/`:
  - `MISSION_ACTIVE.md`: The single source of current cognitive focus.
  - `*-scholar-synthesis.md`: Auto-generated daily learning reports.
  - `archive/LAST_STABLE_STATE.md`: The unified historical log.
- `docs/archaeology/`: Permanent records of human-AI collaboration (e.g., `MEMORIAL.md`).

*(Note: The legacy `docs/daily-briefs/` is deprecated. Intelligence flows through `inputs/` into `memories/`.)*

## Intelligence & Senses (情报与感知)
- **Facts**: Must be sourced from official documentation, release notes, or repositories (via `harvester.py`).
- **Signal-to-Noise**: Harvester strictly checks ETags/states to avoid fetching duplicate or stagnant data (Zero Inbox Policy).
- **Epiphany Engine**: The system actively combats entropy by pairing disconnected entities and prompting the Architect to find hidden synergies (Cross-Pollination).

## Interface (交互接口)
- **CLI**: `docs/brain/nexus.py` is the Central Nervous System.
- **MCP**: `docs/brain/nexus_mcp.py` exposes the graph to external LLMs/IDEs via standard Model Context Protocol.

> "Small and Stable. Quiet and Pragmatic."
