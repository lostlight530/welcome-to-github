# 🧠 NEXUS CORTEX: 认知合成协议 (Cognitive Synthesis Protocol)

> **"The digital brain of the lostlight-portal ecosystem and spec-X architecture."**

此目录托管了一个**有状态的、仅追加知识图谱 (Stateful, Append-Only Knowledge Graph)**，旨在通过递归学习、多维信息采集和架构师的监督来实现自主进化。目前系统运行于 **Phase VII: Heartbeat Awakening (心跳觉醒)** 阶段。它作为一个“真理法庭 (Truth Court)”，具备全知之眼 (Deep AST Codebase Ingestion)、认知推演 (Graph Inference & Deep Pondering)、衔尾蛇免疫 (Ouroboros Protection) 以及严格的 MCP 信任网关 (Trust Gateway)。

---

## Ⅰ. 系统架构 (Architecture)

The system mimics a biological brain with core integrated layers (系统模仿生物大脑，具有核心整合层):

1. 🗄️ **记忆层 (Memory / Storage)**
   - A centralized, ephemeral 4D Temporal Graph that safely maps all active and deprecated knowledge states. (一个集中的、短期的 4D 时序图谱，安全地映射所有活跃与废弃的知识状态。)
   - An immutable, append-only physical ledger that chronologically records system health, structural metrics, and current architectural focus areas. (一个不可篡改的、仅追加的物理账本，按时间顺序记录系统健康、结构指标和当前架构的焦点领域。)

2. ⚙️ **皮层引擎 (Cortex / Engine)**
   - The core engine responsible for orchestrating knowledge retrieval, full-text associative mapping, and computing system-wide quantitative health metrics. (核心引擎，负责编排知识检索、全文本联想映射以及计算系统级的量化健康指标。)

3. 👁️ **全知之眼 (Scholar / Omniscience)**
   - The structural scanner that comprehensively maps the internal codebase geometry, converting source files into queryable graph configurations without Ouroboros Loops. (结构扫描器，全面映射内部代码库几何结构，将源文件转化为可查询的图谱配置，且严格免疫拓扑死循环。)

4. 🧠 **额叶皮层 (Reason / Cognition)**
   - The deductive component that calculates knowledge density, identifies isolated conceptual orphans, and surfaces actionable targets for system evolution. (演绎组件，计算知识密度、识别孤立的概念节点，并为系统进化提供可操作的具体目标。)

5. 🔌 **中央神经系统 (Nexus / Central Command)**
   - The unified command interface and security layer. It acts as a strict gateway that validates, tracks, and penalizes external entity interactions to protect the integrity of the graph. (统一的指挥接口与安全层。它作为严格的信任网关，验证、追踪并惩罚外部实体的违规交互，以保护图谱的绝对完整性。)

---

## Ⅱ. 使用指南 (Usage Guide - Nexus CLI)

All operations are performed via `nexus.py`.

### 1. 进化与思考 (Evolve & Ponder)
```bash
# Ingest internal codebase mapping via AST
python docs/brain/nexus.py ingest

# Deep ponder the graph for anomalies & hidden bridges
python docs/brain/nexus.py ponder

# Run Daily Evolution Cycle (Includes Sandbox Verification)
python docs/brain/nexus.py evolve
```

### 2. 观察 (Observe / Read)
```bash
# Check Brain Health & Entropy
python docs/brain/nexus.py status

# Search Concepts via Synaptic Associative Search
python docs/brain/nexus.py search "android"
```

### 3. 清理与恢复 (Clean & Restore)
```bash
# Clear Temporary Cache Targets (Protects .harvester_state.json)
python docs/brain/nexus.py clean

# Rebuild database from JSONL ledger
python docs/brain/nexus.py rebuild
```

---

## Ⅲ. 图谱规则 (Schema & Rules)

See [SCHEMA.md](./SCHEMA.md) for the "Gene Code" of this system.

- 🚫 **Rule #1**: Never delete. Only append or deprecate via 4D temporal tracking.
- 🔗 **Rule #2**: All relations must point to existing entities.

---

## Ⅳ. CI/CD 自动化 (Automation)

The brain is wired directly into GitHub Actions with a **Unified Lifecycle**:

- 🧬 **`nexus-life-cycle.yml`**: A scheduled, fully automated pipeline that continuously validates the knowledge base, scans for structural changes, runs deductive metrics, and safely proposes mutations.
  - **The System Pulse**: An absolute temporal mechanism ensuring the system remains continuously active, verifiable, and free from automated hibernation or Git starvation.
