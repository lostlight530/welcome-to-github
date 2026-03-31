# NEXUS CORTEX Core Architecture & Operational Protocols
## System Philosophy & Identity (系统哲学与身份定位)

**Core Philosophy (核心法则):** Adheres to "Quiet, Pragmatic, Engineering Excellence," asserting that "Small and Stable" is superior to "Large and Messy". The system operates under the **Phase IV: Absolute Determinism (绝对物理契约)** parameters. It is a "Mechanical Library / Truth Court" — a pure deterministic physical engine that dictates logic to external LLMs, not the other way around.
> 遵循“安静、务实、工程卓越”，坚信“小而稳”胜过“大而乱”。系统运行在 **Phase IV: 绝对确定性** 模式下。它是一座“机械图书馆/真理法庭”——一个纯粹的物理引擎闭环，它向外部大模型发号施令，绝不依赖内部玄学。

---

## Ⅰ. Architecture & Workflow (工程化闭环: The Deterministic Pipeline)

The system operates on a strict, 5-step pure-physics lifecycle (`nexus-life-cycle.yml`):
> 系统依靠 5 个纯物理脚本，实现从“吸收”到“进化”的绝对闭环：

1. 🏗️ **Rebuild (物理挂载)**: `nexus.py rebuild` reconstructs the ephemeral `cortex.db` directly from the immutable `.jsonl` ledger.
2. 📡 **Harvest (双重防抖感知)**: `harvester.py` fetches data using HTTP ETag + SHA-256 Hash + Pure Text Diff, short-circuiting if mathematically identical.
3. 👁️ **Ingest (X光降维吞噬)**: `scholar.py` dissects code using standard library AST and Stack-Based parsers, generating deterministic config nodes.
4. 🤔 **Ponder (纯数学图论推演)**: `reason.py` calculates graph density, isolates orphans, and generates `MISSION_ACTIVE.md` using `string.Template`.
5. 🛡️ **Evolve (沙盒免疫合入)**: `evolution.py` executes `test_mcp.py` via `subprocess`. If the lie detector fails, the entire pipeline halts immediately.

All Agents (including Jules) must prioritize: **Zero-Dependency Brutalism, Append-Only Memory, and Machine Draft, Human Decision**.
> 任何 Agent 必须优先保证：**零依赖极简主义、仅追加记忆、机器起草/人类裁决**。

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

- 👁️ **Omniscience (全知之眼)**: `scholar.py` deep scans internal project files using standard library parsers (AST, re) to extract functions, classes, and markdown structures into graph entities. *(使用 AST 扫描内部代码库，了解自身项目架构。)*
- 🤔 **Cognition (深度思考)**: `reason.py` infers logical connections, detecting orphaned concepts, circular logic, and implicit bridging via transitive dependencies. *(图论深度推理系统，寻找隐性依赖和孤立节点。)*
- 📡 **Facts (事实基准)**: External signals sourced from official documentation via `harvester.py`, leveraging Architect Filters. *(外部事实通过雷达进行严格过滤和抓取。)*

---

## Ⅴ. System Best Practices (系统最佳实践)

1. 🗑️ **Garbage Collection (垃圾回收)**: "Orphan Nodes Must Die." Handled automatically or identified during the Ponder cycle. Protect `.harvester_state.json` at all times. *(清理孤儿节点，防止内存膨胀，保护采集状态。)*
2. 💎 **Crystallization (知识结晶)**: Utilize `nexus.py add` to formalize intelligence briefs into persistent graph structures. *(将情报通过 CLI 结晶为持续的知识图谱。)*
3. 🦅 **Stay Hungry (保持饥饿)**: Focus heavily on multi-actor Agent systems and Edge AI (e.g., MCP) integrating through unified life-cycle actions (`nexus-life-cycle.yml`). *(保持对 Edge AI 生态的敏感与探索。)*
4. ⚡ **Trust Intuition (相信直觉)**: Actively execute `nexus.py connect` when the Ponder engine uncovers subconscious inferences in the knowledge base. *(相信图谱推理出的连接暗示。)*

---

## Ⅵ. Interface (交互接口)

- 💻 **CLI**: `docs/brain/nexus.py` is the unified Central Nervous System that handles Evolve, Harvest, Ingest, and Ponder. *(处理各种功能的统一命令行接口)*
- 🔌 **MCP**: `docs/brain/nexus_mcp.py` exposes the graph to external LLMs/IDEs. *(为外部 LLM 和工具暴露的图谱接口)*

> **"Small and Stable. Quiet and Pragmatic."**