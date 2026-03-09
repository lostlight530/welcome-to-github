# NEXUS CORTEX Core Architecture & Operational Protocols
## System Philosophy & Identity (系统哲学与身份定位)

**Core Philosophy (核心法则):** Adheres to "Quiet, Pragmatic, Engineering Excellence," asserting that "Small and Stable" is superior to "Large and Messy".
> 遵循“安静、务实、工程卓越”，坚信“小而稳”胜过“大而乱”。

---

## Ⅰ. Architecture & Workflow (工程化闭环)

The system operates on an **"Autonomous Radar → OODA Loop → Human Decision → Append-Only Memory"** lifecycle.
> 本仓库采用**“雷达索敌 → OODA 循环 → 人类裁决 → 追加记忆”**的工程化闭环。

All Agents (including Jules) must prioritize: **Auditability, Restraint, Zero-Dependency, and Human-in-the-loop**.
> 任何 Agent 必须优先保证：**可审计、克制、零依赖、人在环**。

---

## Ⅱ. Core Philosophy (核心法则)

1. **Zero-Dependency Brutalism (零依赖极简)**: Prefer Python stdlib (`urllib`, `sqlite3`, `ast`). Reject bloated frameworks. *(首选 Python 标准库，拒绝臃肿框架。)*
2. **Append-Only Memory (不可篡改)**: History is immutable. Mistakes are fixed via `deprecates` or `conflicts_with` tension edges, not deletions. *(历史不可修改。错误通过创建取代或冲突边来修正，而不是删除。)*
3. **Machine Draft, Human Decision (算力主权)**: Agents propose updates (via PR or `MISSION_ACTIVE.md`), but humans execute the final `nexus.py connect` commands. *(AI 提出草案，人类执行最终的连接决策。)*

---

## Ⅲ. Whitelisted Directories (允许写入的目录)

- 📁 `docs/brain/inputs/`: Raw intelligence briefs from Harvester (Radar). *(来自雷达的原始情报)*
- 📁 `docs/brain/memories/`:
  - 📄 `MISSION_ACTIVE.md`: The single source of current cognitive focus, featuring the Architect's Daily Brief. *(当前认知焦点的唯一真相来源)*
  - 📄 `*-scholar-synthesis.md`: Auto-generated daily learning reports. *(自动生成的日常学习报告)*
  - 📁 `archive/`: History of past missions. *(历史任务归档)*
- 📁 `docs/archaeology/`: Permanent records of human-AI collaboration (e.g., `MEMORIAL.md`). *(人类与 AI 协作的永久记录)*

*(Note: Legacy fragmented `knowledge/` JSONL directories remain as the unmutable source, but interaction flows strictly via `cortex.db`.)*

---

## Ⅳ. Intelligence & Senses (情报与感知)

- 📡 **Facts (事实基准)**: Must be sourced from official documentation, release notes, or repositories (via `harvester.py`), utilizing multi-dimensional **Architect Filters** (Edge-Ready, Breaking-Change, Agent-Protocol). *(必须通过雷达从官方源获取事实)*
- 🛡️ **Signal-to-Noise (信噪比控制)**: Harvester strictly checks ETags/states to avoid fetching duplicate or stagnant data (Zero Inbox Policy). *(严格检查 ETag，拒绝重复噪音)*
- 💡 **Epiphany Engine (顿悟引擎)**: The system actively combats entropy by pairing disconnected entities and prompting the Architect to find hidden synergies via transitive inference (`A -> B -> C`). *(主动配对未连接实体，促使顿悟)*
- 🧠 **Synaptic Associative Search (图增强检索)**: The `cortex.py` engine merges FTS5 literal text matching with 1-Hop graph associative retrieval. This provides the system with stateful memory and deduction capabilities. *(通过 FTS5 和单跳图谱增强检索提供状态化记忆)*

---

## Ⅴ. System Best Practices (系统最佳实践)

1. 🗑️ **Garbage Collection (垃圾回收)**: "Orphan Nodes Must Die." Entities with 0 relations after multiple evolution cycles and low weights must be physically pruned to prevent database bloat. Protect `.harvester_state.json` at all times. *(清理孤儿节点以防止数据库膨胀)*
2. 💎 **Crystallization (知识结晶)**: Fragmented raw intel (`inputs/`) must be routinely manually or semi-automatically crystallized into permanent `Entity` nodes via `nexus.py add entity`. *(日常将碎片情报结晶化为永久实体)*
3. 🦅 **Stay Hungry (保持饥饿)**: Expand sensory inputs using strictly Zero-Dependency Python standard libraries. Focus heavily on stateful, multi-actor Agent systems and Edge AI integration paradigms (e.g., MCP). *(使用零依赖库扩展感知，聚焦端侧 AI)*
4. ⚡ **Trust Intuition (相信直觉)**: Actively execute `nexus.py connect` when the system proposes "Subconscious Intuitions" in `MISSION_ACTIVE.md` to reinforce reasoning confidence. *(积极执行系统推演出的潜意识连接)*

---

## Ⅵ. Interface (交互接口)

- 💻 **CLI**: `docs/brain/nexus.py` is the Central Nervous System. *(中央神经系统命令接口)*
- 🔌 **MCP**: `docs/brain/nexus_mcp.py` exposes the stateful graph to external LLMs/IDEs via the Model Context Protocol. *(通过模型上下文协议暴露图谱)*

> **"Small and Stable. Quiet and Pragmatic."**