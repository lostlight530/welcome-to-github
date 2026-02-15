# NEXUS CORTEX: Cognitive Synthesis Protocol (认知合成协议)

> "The digital brain of the lostlight-portal ecosystem."
> "Lostlight-portal 生态系统的数字大脑。"

This directory houses a **Decentralized, Append-Only Knowledge Graph** designed to evolve autonomously through recursive learning and targeted foraging.
本目录包含一个**去中心化、仅追加写入的知识图谱**，旨在通过递归学习和定向搜索实现自主进化。

## Architecture (架构)

The system mimics a biological brain with three core layers:
系统模仿生物大脑，分为三个核心层：

1.  **Memory (Storage / 记忆层)**:
    -   **Fragmented JSONL**: Knowledge is stored in atomic `.jsonl` files to prevent merge conflicts.
        (知识存储在原子的 `.jsonl` 文件中，以防止合并冲突。)
    -   **Entities**: Located in `knowledge/entities/{category}.jsonl`.
    -   **Relations**: Located in `knowledge/relations/{YYYY-MM}.jsonl`.
    -   **Memories**:
        -   `memories/MISSION_ACTIVE.md`: The current cognitive focus. (当前的认知焦点)
        -   `memories/archive/`: History of past missions. (历史任务归档)

2.  **Cortex (Engine / 皮层引擎)**:
    -   `cortex.py`: The read-only engine that loads the graph, validates integrity, and performs entropy analysis.
        (只读引擎，负责加载图谱、验证完整性并执行熵值分析。)
    -   acts as the "Hippocampus" for retrieval and associative search.
        (充当“海马体”，负责检索和联想搜索。)

3.  **Nexus (Interface / 神经中枢)**:
    -   `nexus.py`: The unified Command Line Interface (CLI) for all brain operations.
        (所有大脑操作的统一命令行接口。)
    -   acts as the "Central Nervous System". (充当“中央神经系统”。)

4.  **Evolution (Orchestration / 进化编排)**:
    -   `evolution.py`: The executive function that runs the **OODA Loop**:
        (执行 **OODA 循环** 的执行功能：)
        1.  **Observe (观察)**: Analyze graph entropy (missing links, stale nodes).
        2.  **Orient (调整)**: Check active mission status.
        3.  **Decide (决策)**: Generate new `MISSION_ACTIVE.md` or archive old ones.
        4.  **Act (行动)**: Agents read the mission and execute via Nexus.

## Usage Guide (Nexus CLI)

All operations are performed via `nexus.py`.
所有操作均通过 `nexus.py` 执行。

### 1. Observe (Read / 观察)
```bash
# Check Brain Health & Entropy (检查大脑健康与熵值)
python docs/brain/nexus.py status

# Search Concepts (Fuzzy Match / 模糊搜索)
python docs/brain/nexus.py search "android"

# Visualize Topology (Mermaid.js / 生成拓扑图)
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
python docs/brain/nexus.py add concepts --id "rag" --type "pattern" --name "RAG" --desc "Retrieval Augmented Generation" --tags "ai,search"

# Connect Concepts (建立连接)
python docs/brain/nexus.py connect "rag" "improves" "llm" --context "arXiv:2301.00000"
```

### 4. Clean (Maintenance / 清理)
```bash
# Clear Cache (清除缓存)
python docs/brain/nexus.py clean
```

## Schema & Rules (规则)

See [SCHEMA.md](./SCHEMA.md) for the "Gene Code" of this system.
详见 [SCHEMA.md](./SCHEMA.md)。

-   **Rule #1**: Never delete. Only append. (永不删除，只追加。)
-   **Rule #2**: All relations must point to existing entities. (所有关系必须指向存在的实体。)
-   **Rule #3**: Evolution must be documented in Missions and ADRs. (进化必须记录在任务和 ADR 中。)

## Automation (自动化)

The brain is wired into GitHub Actions:
大脑已接入 GitHub Actions：

-   `brain-integrity.yml`: Validates every commit using `nexus status`. (每次提交验证大脑完整性。)
-   `brain-evolution.yml`: Runs daily to trigger `nexus clean` & `nexus evolve`. (每日运行清理与进化。)
