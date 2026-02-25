# 🧠 NEXUS CORTEX: Deterministic Evolution Blueprint v2.0 (确定性进化蓝图)

> **Last Updated (最后更新)**: 2026-02-16
> **Paradigm (范式)**: Dual-Dimensional Static Contemplation (双维静态沉思)
> **Philosophy**: "Small and Stable" (Quiet, Pragmatic, Engineering Excellence)

---

## I. Strategic Shift: From "Preference Guesser" to "Static Thinker" (战略重构)

### 🚫 The Rejected Model (被否决的旧范式)
Attempts to establish a "Dual-Loop Learning" mechanism via `Curator` and `Reflector`, treating user PR closure as "Negative Feedback" to dynamically adjust `harvester.py` weights (e.g., `Delta_Stars = -0.5`).

**Fatal Flaw (致命缺陷)**:
User intent is complex (e.g., closing a PR due to lack of time vs. lack of value). Reducing weights based on tactical actions contaminates the radar's objectivity, degrading the system into an echo chamber that only reinforces existing biases.

### ✅ The Deterministic Paradigm (确立的新范式)
The system abandons all implicit behavioral learning models in favor of a **"Dual-Dimensional Static Contemplation Protocol"**.
It operates as an absolutely objective scholar on the `main` branch, performing **Micro-Introspection** via Python's native `ast` module and **Macro-Cognition** via heuristic regex extraction from a global top-tier technology whitelist. The system is Read-Only, Extraction-Only, and Inference-Free. All cognitive sedimentation must be finalized via standardized PRs for explicit human decision-making.

---

## II. Micro-Introspection Engine: AST Topology Guardian (微观自省引擎)
> System requires no "touch" (dynamic execution environment); static code analysis is its sharpest scalpel.

### 1. Architectural Integrity Guard (架构守护机制)
**Mechanism**: `learner.py` scans `docs/brain/` core engine files (e.g., `evolution.py`, `cortex.py`) daily using Python's `ast` (Abstract Syntax Tree) module.

**Audit Dimensions**:
- **Dependency Flow Audit**: Strictly validates import paths (`Import` / `ImportFrom` nodes) to ensure a unidirectional data flow: **Data Layer -> Logic Layer -> Interface Layer**. Circular dependencies trigger immediate corruption warnings.
- **Complexity Entropy**: Measures depth/breadth of `ClassDef` and `FunctionDef` nodes. Monitors cyclomatic complexity to ensure no single module violates the "Small" philosophy.

### 2. Zero-Risk Execution Boundary (零风险执行边界)
By only invoking `ast.parse()` to generate in-memory tree structures, malicious code, infinite loops, or destructive system calls are physically isolated. The system gains "X-ray vision" at the source level while maintaining absolute runtime safety and purity.

---

## III. Macro-Cognition Engine: Objective Absorption via Heuristic Whitelist (宏观认知引擎)
> Abolishes dynamic recommendation algorithms. Adopts a hardcoded global top-tier technology whitelist (e.g., Kubernetes Declarative Architecture, Kafka Append-Only Design, React Fiber Scheduling).

### 1. Heuristic Feature Extraction (启发式特征提取)
**Mechanism**: Daily, the system selects a target from `whitelist_sources` using a random seed and fetches the raw Markdown or plaintext RFC document via minimal `urllib`.

**Regex Anchoring**: Uses a predefined regex matrix (capturing keywords like `Architecture`, `Design Philosophy`, `Core Concepts`, `Trade-offs` in Headers and subsequent blocks) to slice out core architectural discourse directly from the source.

### 2. Immutable Knowledge Preservation (知识原貌的物理固化)
Extracted content is appended **verbatim** (without AI semantic transformation) to `docs/brain/memories/learning-record-[DATE].md`.

**Engineering Benefit**: This "Scrapbook" approach eliminates model hallucination. It preserves original formulations from top engineers (e.g., Linus Torvalds, Dan Abramov), establishing a high-signal-to-noise ratio architectural asset library.

---

## IV. Governance & Firewall: The Absolute Human-Machine Boundary (防御与治理体系)

### 1. Human-in-the-Loop Mandate (坚守“人在环”铁律)
**Auto-Pilot Ban**: The "Auto-Merge High Score Intel" feature is permanently banned. The system has **zero authority** to directly modify `.jsonl` fragments in the knowledge graph.
Even if a candidate's Trust Score hits 1000, it can only be flagged as `High Priority` in `MISSION_ACTIVE.md` and presented in a PR. **The Merge Button is the exclusive symbol of human power.**

### 2. Static Math as Constitution (静态配置与数学铁律)
**Immutable Weights**: The scoring weights in `harvester.py` (30/10/0.3) are physical laws of the system, **forbidden** from dynamic fine-tuning by any automation script (`Reflector`).
Any adjustment to radar sensitivity must be an explicit code change by a human engineer. This hardcoding ensures absolute predictability of system behavior.

---

## V. Implementation Roadmap (实施路线图)

### Phase 1: The Static Thinker Initialization (静态思想家的降临)
- [x] Deploy `docs/brain/learner.py` with AST parsing engine and heuristic regex logic.
- [x] Hardcode the full major-tech architecture whitelist (RFCs/Design Docs) into `brain_config.json`.
- [x] Ensure total independence from third-party libraries (No `requests`, No `transformers`, No LLM API).

### Phase 2: The Contemplation Pacemaker (每日沉思起搏器)
- [x] Upgrade `.github/workflows/brain_evolution.yml` to chain `Learner` after `Harvester` and `Evolution`.
- [ ] Configure workflow to package daily AST reports and whitelist literature into a unified Pull Request tagged `[Daily Intelligence]`.

### Phase 3: Cognitive Compound Accumulation (认知资产复利)
- [ ] Passively accumulate a massive, structured "Apocalypse of Top-Tier Architecture" in `docs/brain/memories/`.
- [ ] Future: Utilize `cortex.py` to weave these Markdown memories into `entities/concepts.jsonl` via keyword association, finalizing the sublimation from "Info Fragments" to "Graph Neurons".
