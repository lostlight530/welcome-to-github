# 系统架构深度分析报告 (System Architecture Deep Analysis)

> **"Small and Stable. Quiet and Pragmatic."**

## 1. 功能 (Features)
- **Stateful Knowledge Graph**: A centralized SQLite database (`cortex.db`) acting as the memory core, superseding legacy JSONL storage, with Synaptic Associative Search.
- **Omniscient Scanner**: Deep ingestion of internal codebase utilizing native structural extraction techniques to map system features cleanly and without external parsers.
- **Mathematical Graph Inference**: Pondering engine (`reason.py`) calculates graph density, identifies orphans, and generates actionable bounties.
- **Intent-Driven Harvester**: Radar system (`harvester.py`) that fetches external ecosystem data with Double-Clutch Anti-Shake (multi-layer physical consistency checks) to avoid redundant updates.
- **Automated Evolution Cycle**: A 5-step daily closed-loop pipeline (`nexus-life-cycle.yml`) bridging physical storage, code analysis, reasoning, and automated safe mutations.

## 2. 技术栈 (Tech Stack)
- **Backend/Core Logic**: Native language capabilities strictly stripped of external libraries, ensuring absolute determinism and extreme stability.
- **Frontend/Presentation**: Native ES Modules, HTML5, CSS3, Tailwind CSS (via CDN), Vite.
- **Automation/CI-CD**: GitHub Actions (`deploy.yml`, `nexus-life-cycle.yml`) for cron jobs, memory building, and deployments.
- **Data Storage**: SQLite (`cortex.db`) for active relationships, JSON/JSONL for append-only persistent ledgers.

## 3. 布局架构 (Layout Architecture)
- **`src/`**: Contains frontend presentation files (Tailwind, Native JS Modules).
- **`docs/brain/`**: The core operational intelligence engine containing Python scripts (`nexus.py`, `cortex.py`, `scholar.py`, `reason.py`, `harvester.py`, `evolution.py`).
- **`docs/brain/memories/` & `docs/brain/inputs/`**: Writable areas for generated daily briefs (`MISSION_ACTIVE.md`) and harvested intelligence reports.
- **`docs/archaeology/`**: Immutable records of project history, paradigm shifts, and AI-Human collaborations.

## 4. 设计 (Design)
- **Zero-Dependency Brutalism**: Strict avoidance of external libraries like `requests`, `networkx`, or `tree-sitter`.
- **Append-Only Memory**: No destructive updates. Errors are mitigated via `deprecates` or `conflicts_with` relationships.
- **Mechanical Library / Truth Court**: The system functions as a pure physics engine that validates and enforces rules upon connected agents (MCP Server).
- **Dual-Phase Intelligence**: Phase A (Watchlist) and Phase B (Ecosystem Consensus) for harvesting high-signal data.

## 5. 工作流 (Workflow)
The core workflow is automated via `nexus-life-cycle.yml`:
1. **Rebuild (`nexus.py rebuild`)**: Reconstruct the SQLite graph from immutable text ledgers.
2. **Harvest (`nexus.py harvest`)**: Fetch external updates securely.
3. **Ingest (`nexus.py ingest`)**: Deeply parse codebase and generate graph nodes.
4. **Ponder (`nexus.py ponder`)**: Run deep mathematical inference, generating `MISSION_ACTIVE.md`.
5. **Evolve (`nexus.py evolve`)**: Execute sandbox testing and genetic auto-recombination logic.

## 6. 任务的模板心得 (Task Template Insights)
- **Machine Draft, Human Decision**: The AI scripts draft plans, PRs, and targets (via `MISSION_ACTIVE.md`), but the architect (Human) makes the final explicit execution command (`nexus.py connect`).
- **Quantitative Daily Dashboard**: Using SQL and mathematical ratios (Compression Rate) instead of LLM prose for system health monitoring, ensuring purely deterministic insights.
- **Strict Error Handling**: Silent degradation on network errors in the Harvester to preserve the system's anti-fragility and rate limits.

## 7. 领先点 (Leading Points)
- **Phase IV & V Absolute Determinism**: Establishing a hard boundary where AI acts purely as a mechanical force. It calculates and dictates rather than hallucinating logic.
- **Double-Clutch Anti-Shake**: Advanced, dependency-free noise filtering (stripping timestamps/dates) to prevent false-positive updates from GitHub APIs.
- **Trust Gateway**: The MCP Server slashes trust scores for non-compliant payloads, providing real consequences for agent errors.

## 8. 优势 (Advantages)
- **Extreme Stability**: By refusing third-party packages, the system is immune to npm package rot, dependency conflicts, and supply chain attacks.
- **High Observability**: The architecture renders transparent logs, outputs clear metrics, and tracks its own logic via the graph itself (`concept_nexus_system`).
- **Low Compute Overhead**: Capable of running complex continuous integrations completely within GitHub's free tier due to the efficiency of native Python.

## 9. 借鉴 (Areas for Reference/Learning)
- **Liquid Time-Series Graph Injection**: Highly concurrent network retrieval loops designed purely with native threading components to ensure high throughput without external library bloat.
- **Polyglot Lexer**: Native, dependency-free state machine models built strictly to digest cross-language structural properties without massive third-party C-bindings.
- **Auto-Recombination Sandboxing**: A strict, secure environment that allows logic blocks to self-evaluate and propose modifications safely prior to explicit human integration.

## 10. 深度联网思考 (Deep Web-Connected Thinking)
The system currently implements a "pull" mechanism via the Harvester, probing specific whitelists. To deepen this:
- **Dynamic Watchlist Expansion**: Further integration with MCP could allow the reasoning engine to temporarily spawn LLM agents to research isolated nodes on the open web, converting "1-degree concepts" into deeply mapped territories.
- **Cross-Repo Subconscious Links**: If the system connects to the wider ecosystem, the graph could infer deep, mathematical overlaps between disparate projects based purely on their structural layout, transcending simple keyword searches.

## 11. 功能的完善 (Feature Completion)
- **Active Node Suture Verification**: The `cortex.py` automatic suturing function should undergo rigorous regression testing to ensure it doesn't create circular 'Ouroboros' loops.
- **Enhanced Agent Penalties**: The Trust Gateway could implement a "timeout" or "quarantine" zone for agents that continuously fail format checks.
- **Expanded Frontend Translations**: Ensure `translations.js` natively binds and visually represents the output of `MISSION_ACTIVE.md` on the Live Portal to broadcast current bounties publicly.
