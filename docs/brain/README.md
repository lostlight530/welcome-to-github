# 🧠 NEXUS CORTEX: Cognitive Synthesis Protocol (认知合成协议)

> **"The digital brain of the lostlight-portal ecosystem."**
> *(Lostlight-portal 生态系统的数字大脑。)*

This directory houses a **Decentralized, Append-Only Knowledge Graph** designed to evolve autonomously through recursive learning and targeted foraging.
> 本目录包含一个**去中心化、仅追加写入的知识图谱**，旨在通过递归学习和定向搜索实现自主进化。

---

## Ⅰ. Architecture (系统架构)

The system mimics a biological brain with four core layers:
> 系统模仿生物大脑，分为四个核心层：

1. 🗄️ **Memory (Storage / 记忆层)**
   - **SQLite Database (`cortex.db`)**: Centralized storage utilizing biological "Memory Half-Life" (Synaptic Potentiation/Depression). Supersedes legacy ADR-0001 Append-Only JSONL.
     *(采用生物学“记忆半衰期”和突触可塑性的中心化数据库，替代了过时的追加式 JSONL 存储。)*
   - **Memories**:
     - `memories/MISSION_ACTIVE.md`: The current cognitive focus. *(当前的认知焦点)*
     - `memories/archive/`: History of past missions. *(历史任务归档)*

2. ⚙️ **Cortex (Engine / 皮层引擎)**
   - `cortex.py`: The core engine driving FTS5 full-text search and **Synaptic Associative Search (Graph-Augmented Retrieval)**. Acts as the "Hippocampus" for retrieval, inferencing, and dynamic weight modulation.
     *(核心引擎，驱动 FTS5 全文搜索与图谱增强的**突触联想搜索**。充当“海马体”，负责检索、推理和动态权重调节。)*

3. 🔌 **Nexus (Interface / 神经中枢)**
   - `nexus.py` & `nexus_mcp.py`: The unified Command Line Interface (CLI) and Model Context Protocol Server for all brain operations. Acts as the "Central Nervous System".
     *(所有大脑操作的统一命令行接口与 MCP 服务端。充当“中央神经系统”。)*

4. 🧬 **Evolution (Orchestration / 进化编排)**
   - `evolution.py`: The executive function that runs the **OODA Loop**:
     *(执行 **OODA 循环** 的执行功能：)*
     1. **Observe (观察)**: Analyze graph entropy (missing links, stale nodes).
     2. **Orient (调整)**: Check active mission status.
     3. **Decide (决策)**: Generate new `MISSION_ACTIVE.md` or archive old ones.
     4. **Act (行动)**: Agents read the mission and execute via Nexus.

---

## Ⅱ. Usage Guide (使用指南 - Nexus CLI)

All operations are performed via `nexus.py`.
> 所有操作均通过 `nexus.py` 执行。

### 1. Observe (Read / 观察)
```bash
# Check Brain Health & Entropy (检查大脑健康与熵值)
python docs/brain/nexus.py status

# Search Concepts via Synaptic Associative Search (图增强检索 / 联想匹配)
python docs/brain/nexus.py search "android"

# Visualize Topology via Mermaid.js (生成可视化拓扑图)
python docs/brain/nexus.py visualize
```

### 2. Evolve (Write / 进化)
```bash
# Run Daily Evolution Cycle (运行每日进化循环)
python docs/brain/nexus.py evolve
# -> Updates docs/brain/memories/MISSION_ACTIVE.md
```

### 3. Ingest (Action / 摄入)
```bash
# Add New Concept (添加新概念)
python docs/brain/nexus.py add entity --id "rag" --type "concept" --name "RAG" --desc "Retrieval Augmented Generation"

# Connect Concepts (建立图谱连接)
python docs/brain/nexus.py connect "rag" "improves" "llm" --desc "arXiv:2301.00000"
```

### 4. Clean (Maintenance / 清理)
```bash
# Clear Temporary Cache Targets (清除临时缓存)
python docs/brain/nexus.py clean
```

---

## Ⅲ. Schema & Rules (图谱规则)

See [SCHEMA.md](./SCHEMA.md) for the "Gene Code" of this system.
> 详见 [SCHEMA.md](./SCHEMA.md) 了解本系统的“底层基因”。

- 🚫 **Rule #1**: Never delete. Only append or deprecate. *(永不删除，只追加或标记废弃。)*
- 🔗 **Rule #2**: All relations must point to existing entities. *(所有关系必须指向已存在的实体。)*
- 📜 **Rule #3**: Evolution must be documented in Missions and ADRs. *(架构进化必须记录在任务日志和 ADR 中。)*

---

## Ⅳ. Automation (CI/CD 自动化)

The brain is wired directly into GitHub Actions:
> 大脑已直接接入 GitHub Actions 生态：

- 🛡️ **`brain-integrity.yml`**: Validates every commit using `nexus status` and MCP health checks. *(每次提交验证大脑完整性与 MCP 存活状态。)*
- ⏰ **`brain-evolution.yml`**: Runs daily to trigger `harvester`, `nexus clean`, and `nexus evolve`. *(每日定时触发雷达采集、清理与进化循环。)*
