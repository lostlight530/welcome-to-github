# 核心架构与运行协议 (Core Architecture & Operational Protocols)
## 系统哲学与身份定位 (System Philosophy & Identity)

**Core Philosophy:** Adheres to "Quiet, Pragmatic, Engineering Excellence," asserting that "Small and Stable" is superior to "Large and Messy". The system operates under the **Phase VI: Absolute Determinism** parameters within the `spec-X` architecture. It is a "Mechanical Library / Truth Court" — a pure deterministic physical engine that dictates logic to external LLMs.

---

## Ⅰ. 工程化闭环 (Architecture & Workflow)

The system operates on a strict, 5-step pure-physics lifecycle (`nexus-life-cycle.yml`):

1. 🏗️ **物理挂载 (Rebuild)**: `nexus.py rebuild` reconstructs the ephemeral `cortex.db` directly from the immutable `.jsonl` ledger.
2. 📡 **双重防抖感知 (Harvest)**: `harvester.py` fetches data using HTTP ETag + SHA-256 Hash + Pure Text Diff, short-circuiting if mathematically identical.
3. 👁️ **全知降维吞噬 (Ingest)**: `scholar.py` dissects code using standard library AST and Polyglot Regex parsers, generating deterministic config nodes.
4. 🤔 **纯数学图论推演 (Ponder)**: `reason.py` calculates graph metrics, isolates orphans, and generates `MISSION_ACTIVE.md` using `string.Template` mapped dynamically from data dictionaries.
5. 🛡️ **沙盒免疫合入 (Evolve)**: `evolution.py` executes `test_mcp.py` via `subprocess`. If the lie detector fails, the entire pipeline halts immediately.

All Agents (including Jules) must prioritize: **Zero-Dependency Brutalism, Append-Only Memory, and Machine Draft, Human Decision**.

---

## Ⅱ. 核心法则 (Core Philosophy)

1. **零依赖极简 (Zero-Dependency Brutalism)**: Prefer Python stdlib (`urllib`, `sqlite3`, `ast`, pure math). Reject bloated frameworks.
2. **不可篡改 (Append-Only Memory)**: History is immutable. Mistakes are fixed via `deprecates` or `conflicts_with` tension edges, utilizing `valid_at` and `invalid_at` 4D temporal tracking.
3. **算力主权 (Machine Draft, Human Decision)**: Agents propose updates (via PR or quantitative dashboards), but humans execute the final integration.

---

## Ⅲ. 允许写入的目录 (Whitelisted Directories)

- 📁 `docs/brain/inputs/`: Raw intelligence briefs from Harvester (Radar).
- 📁 `docs/brain/memories/`:
  - 📄 `MISSION_ACTIVE.md`: The single source of current cognitive focus, driven by the quantitative dashboard.
  - 📄 `*-scholar-synthesis.md`: Auto-generated daily learning reports.
  - 📁 `archive/`: History of past missions.
- 📁 `docs/archaeology/`: Permanent records of human-AI collaboration (e.g., `MEMORIAL.md`).

*(Note: Legacy fragmented `knowledge/` JSONL directories remain as the unmutable source, but interaction flows strictly via `cortex.db`.)*

---

## Ⅳ. 情报与感知 (Intelligence & Senses)

- 👁️ **全知之眼 (Omniscience)**: `scholar.py` deep scans internal project files using standard library parsers (AST, polyglot regex) to extract dependencies, functions, classes, and markdown structures.
- 🤔 **深度思考 (Cognition)**: `reason.py` infers logical connections using pure math (PageRank/Markov Chains), detecting orphaned concepts and epistemic depth.
- 📡 **事实基准 (Facts)**: External signals sourced from whitelisted official repositories (Google, Anthropic, Huawei, Microsoft) via `harvester.py`.

---

## Ⅴ. 系统最佳实践 (System Best Practices)

1. 🗑️ **垃圾回收 (Garbage Collection)**: Orphan nodes must be connected via `suture_orphans`. Protect `.harvester_state.json` at all times.
2. 💎 **知识结晶 (Crystallization)**: Utilize MCP tools to formalize intelligence briefs into persistent graph structures.
3. ⚖️ **信任网关 (Trust Gateway Penalty)**: The system slashes agent trust (-10 points) for missing MCP schemas and physically blocks execution if trust reaches zero.
4. ⚡ **相信直觉 (Trust Intuition)**: Actively address structural anomalies highlighted in the quantitative dashboard.

---

## Ⅵ. 交互接口 (Interface)

- 💻 **命令行接口 (CLI)**: `docs/brain/nexus.py` is the unified Central Nervous System that handles Evolve, Harvest, Ingest, and Ponder.
- 🔌 **模型上下文协议 (MCP)**: `docs/brain/nexus_mcp.py` and `mcp_demo.py` expose the graph and Trust Gateway to external LLMs/IDEs.

> **"Small and Stable. Quiet and Pragmatic."**