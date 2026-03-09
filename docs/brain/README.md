# 🧠 NEXUS CORTEX: Cognitive Synthesis Protocol (认知合成协议)

> **"The digital brain of the lostlight-portal ecosystem."**
> *(Lostlight-portal 生态系统的数字大脑。)*

This directory houses a **Stateful, Append-Only Knowledge Graph** designed to evolve autonomously through recursive learning, multi-dimensional foraging, and Architect supervision. Now upgraded to **Phase III: Singularity**, it features Omniscience (Deep AST Codebase Ingestion) and Cognition (Graph Inference & Deep Pondering).
> 本目录包含一个**状态化、仅追加写入的知识图谱**，旨在通过递归学习、多维感知和架构师监督实现自主进化。现已升级至 **Phase III: Singularity (奇点)**，具备全知（深度代码库 AST 扫描与结构解析）与认知（图谱推理与深度思考）能力。

---

## Ⅰ. Architecture (系统架构)

The system mimics a biological brain with core integrated layers:
> 系统模仿生物大脑，分为以下核心层：

1. 🗄️ **Memory (Storage / 记忆层)**
   - **SQLite Database (`cortex.db`)**: Centralized storage utilizing biological "Memory Half-Life" (Synaptic Potentiation/Depression). Supersedes legacy Append-Only JSONL.
     *(采用生物学“记忆半衰期”和突触可塑性的中心化数据库，替代了过时的追加式 JSONL 存储。)*
   - **Memories**:
     - `memories/MISSION_ACTIVE.md`: The Architect's Daily Brief and cognitive focus. *(架构师每日简报与当前认知焦点)*

2. ⚙️ **Cortex (Engine / 皮层引擎)**
   - `cortex.py`: The core engine driving FTS5 full-text search and **Synaptic Associative Search (Graph-Augmented Retrieval)**. Acts as the "Hippocampus" for retrieval, inferencing, and dynamic weight modulation.
     *(核心引擎，驱动 FTS5 全文搜索与图谱增强的**突触联想搜索**。充当“海马体”。)*

3. 👁️ **Scholar (Omniscience / 全知之眼)**
   - `scholar.py`: Deeply parses the repository using AST (for Python) and structure parsers (for Markdown), writing local project understanding directly into the graph.
     *(深度扫描仓库，使用 AST 解析 Python 代码，提取 Markdown 结构，将对自身项目的理解直接写入知识图谱。)*

4. 🧠 **Reason (Cognition / 额叶皮层)**
   - `reason.py`: The deep thinking engine that analyzes the graph for isolated nodes (orphans), infinite loops, and hidden transitive bridges (`A -> B -> C`).
     *(深度思考引擎，分析图谱中的孤立节点、无限循环以及隐性桥接关联。)*

5. 🔌 **Nexus (Central Command / 中央神经系统)**
   - `nexus.py` & `nexus_mcp.py`: The unified Command Line Interface (CLI) and Model Context Protocol Server integrating memory operations, harvesting, ingestion, and pondering.
     *(统一命令行接口与 MCP 服务端，整合记忆操作、采集、解析与思考命令。)*

---

## Ⅱ. Usage Guide (使用指南 - Nexus CLI)

All operations are performed via `nexus.py`.
> 所有操作均通过 `nexus.py` 执行。

### 1. Evolve & Ponder (进化与思考)
```bash
# Ingest internal codebase mapping via AST (全知：摄入内部代码结构)
python docs/brain/nexus.py ingest

# Deep ponder the graph for anomalies & hidden bridges (认知：深度思考与推理)
python docs/brain/nexus.py ponder

# Run Daily Evolution Cycle (运行每日外部采集与进化循环)
python docs/brain/nexus.py evolve
```

### 2. Observe (Read / 观察)
```bash
# Check Brain Health & Entropy (检查大脑健康与熵值)
python docs/brain/nexus.py status

# Search Concepts via Synaptic Associative Search (图增强检索 / 联想匹配)
python docs/brain/nexus.py search "android"
```

### 3. Clean & Restore (清理与恢复)
```bash
# Clear Temporary Cache Targets (清除临时缓存，保护状态文件)
python docs/brain/nexus.py clean

# Rebuild database from JSONL ledger (从文本账本重建内存库)
python docs/brain/nexus.py rebuild
```

---

## Ⅲ. Schema & Rules (图谱规则)

See [SCHEMA.md](./SCHEMA.md) for the "Gene Code" of this system.
> 详见 [SCHEMA.md](./SCHEMA.md) 了解本系统的“底层基因”。

- 🚫 **Rule #1**: Never delete. Only append or deprecate. *(永不删除，只追加或标记废弃。)*
- 🔗 **Rule #2**: All relations must point to existing entities. *(所有关系必须指向已存在的实体。)*

---

## Ⅳ. Automation (CI/CD 自动化)

The brain is wired directly into GitHub Actions with a **Unified Lifecycle**:
> 大脑通过**统一生命周期**接入 GitHub Actions 自动化：

- 🧬 **`nexus-life-cycle.yml`**: A nightly heartbeat that rebuilds memory, ingests internal state (Omniscience), ponders deep logic (Cognition), and evolves strategy. *(每晚运行的心跳：重建记忆、摄入内部状态、深度推理并完成进化。)*
