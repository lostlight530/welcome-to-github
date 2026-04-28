# 🧠 NEXUS CORTEX: 认知合成协议 (Cognitive Synthesis Protocol)

> **"The digital brain of the lostlight-portal ecosystem and spec-X architecture."**

This directory houses a **Stateful, Append-Only Knowledge Graph** designed to evolve autonomously through recursive learning, multi-dimensional foraging, and Architect supervision. Now operating under **Phase VI: Absolute Determinism**, it features Omniscience (Deep AST Codebase Ingestion), Cognition (Graph Inference & Deep Pondering), and a strict Trust Gateway for MCP interactions.

---

## Ⅰ. 系统架构 (Architecture)

The system mimics a biological brain with core integrated layers:

1. 🗄️ **记忆层 (Memory / Storage)**
   - **SQLite Database (`cortex.db`)**: Centralized ephemeral storage functioning as a 4D Temporal Graph (utilizing `valid_at` and `invalid_at`). The legacy Append-Only JSONL remains the absolute immutable truth ("Text is Law").
   - **Memories**:
     - `memories/MISSION_ACTIVE.md`: The Architect's Daily Brief and cognitive focus, dynamically injected with a UTC System Pulse and brain entropy.
     - `memories/QUANTITATIVE_LEDGER.md`: An immutable, Append-Only ledger recording the daily physical state (entities, relations, compression rate) driven entirely by time and deterministic mathematics.

2. ⚙️ **皮层引擎 (Cortex / Engine)**
   - `cortex.py`: The core engine driving FTS5 full-text search, Synaptic Associative Search (Graph-Augmented Retrieval), and calculating quantitative dashboard metrics (Compression Rate, Low-Connectivity).

3. 👁️ **全知之眼 (Scholar / Omniscience)**
   - `scholar.py`: Deeply parses the repository using AST (for Python) and a Polyglot Regex State Machine (for JS/TS), writing local project understanding directly into the graph without external dependencies.

4. 🧠 **额叶皮层 (Reason / Cognition)**
   - `reason.py`: The deep thinking engine that analyzes the graph using pure Python mathematical PageRank/Markov Chain implementations to identify epistemic depth and isolated nodes.

5. 🔌 **中央神经系统 (Nexus / Central Command)**
   - `nexus.py` & `nexus_mcp.py`: The unified Command Line Interface (CLI) and Model Context Protocol Server. It features a Phase V Trust Gateway that actively slashes agent trust for malformed inputs, physically blocking depleted agents.

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

- 🧬 **`nexus-life-cycle.yml`**: A nightly heartbeat that rebuilds memory, ingests internal state (Omniscience), ponders deep logic (Cognition), and evolves strategy.
  - **The System Pulse**: The system ensures continuous Git history updates through an embedded exact UTC timestamp (`System Pulse`). This physical time variation breaks Git's idempotency lock, guaranteeing that the system outputs an explicit "I am alive" commit (`--allow-empty`) every single night, even if no nodes change. It operates under strict Zero-Dependency Brutalism constraints.
