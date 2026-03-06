# NEXUS CORTEX: Operational Directives (操作指令)

## Ⅰ. Architecture & Workflow (工程化闭环)

The system operates on an **"Autonomous Radar → OODA Loop → Human Decision → Append-Only Memory"** lifecycle.
> 本仓库采用**“雷达索敌 → OODA 循环 → 人类裁决 → 追加记忆”**的工程化闭环。

All Agents (including Jules) must prioritize: **Auditability, Restraint, Zero-Dependency, and Human-in-the-loop**.
> 任何 Agent 必须优先保证：**可审计、克制、零依赖、人在环**。

---

## Ⅱ. Core Philosophy (核心法则)

1. **Zero-Dependency Brutalism (零依赖极简)**: Prefer Python stdlib (`urllib`, `sqlite3`, `ast`). Reject bloated frameworks.
2. **Append-Only Memory (不可篡改)**: History is immutable. Mistakes are fixed via `deprecates` or `conflicts_with` tension edges, not deletions.
3. **Machine Draft, Human Decision (算力主权)**: Agents propose updates (via PR or `MISSION_ACTIVE.md`), but humans execute the final `nexus.py connect` commands.

---

## Ⅲ. Whitelisted Directories (允许写入的目录)

- 📁 `docs/brain/inputs/`: Raw intelligence briefs from Harvester (Radar).
- 📁 `docs/brain/memories/`:
  - 📄 `MISSION_ACTIVE.md`: The single source of current cognitive focus.
  - 📄 `*-scholar-synthesis.md`: Auto-generated daily learning reports.
  - 📁 `archive/`: History of past missions.
- 📁 `docs/archaeology/`: Permanent records of human-AI collaboration (e.g., `MEMORIAL.md`).

*(Note: The legacy `docs/daily-briefs/` and fragmented `knowledge/` JSONL directories are deprecated. All data flows into `cortex.db`.)*

---

## Ⅳ. Intelligence & Senses (情报与感知)

- 📡 **Facts (事实基准)**: Must be sourced from official documentation, release notes, or repositories (via `harvester.py`).
- 🛡️ **Signal-to-Noise (信噪比控制)**: Harvester strictly checks ETags/states to avoid fetching duplicate or stagnant data (Zero Inbox Policy).
- 💡 **Epiphany Engine (顿悟引擎)**: The system actively combats entropy by pairing disconnected entities and prompting the Architect to find hidden synergies (Cross-Pollination).
- 🧠 **Synaptic Associative Search (图增强检索)**: The `cortex.py` engine merges FTS5 literal text matching with 1-Hop graph associative retrieval (for nodes with `weight > 1.2`). This provides the system with "Brainstorming" and "Deduction" capabilities.

---

## Ⅴ. System Best Practices (系统最佳实践)

1. 🗑️ **Garbage Collection (垃圾回收)**: "Orphan Nodes Must Die." Entities with 0 relations after 3 evolution cycles and a weight `< 0.5` must be physically pruned to prevent database bloat.
2. 💎 **Crystallization (知识结晶)**: Fragmented raw intel (`inputs/`) must be routinely manually or semi-automatically crystallized into permanent `Entity` nodes via `nexus.py add entity`. Do not leave them as temporary events.
3. 🦅 **Stay Hungry (保持饥饿)**: Expand sensory inputs (e.g., RSS parsers for Hacker News) using strictly Zero-Dependency Python standard libraries (`xml.etree.ElementTree`).
4. ⚡ **Trust Intuition (相信直觉)**: Actively execute `nexus.py connect` when the system proposes "Subconscious Intuitions" in `MISSION_ACTIVE.md` to reinforce reasoning confidence.

---

## Ⅵ. Interface (交互接口)

- 💻 **CLI**: `docs/brain/nexus.py` is the Central Nervous System.
- 🔌 **MCP**: `docs/brain/nexus_mcp.py` exposes the graph to external LLMs/IDEs via standard Model Context Protocol.

> **"Small and Stable. Quiet and Pragmatic."**
