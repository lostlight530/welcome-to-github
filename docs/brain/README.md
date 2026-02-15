# NEXUS CORTEX: Cognitive Synthesis Protocol

> "The digital brain of the lostlight-portal ecosystem."

This directory houses a **Decentralized, Append-Only Knowledge Graph** designed to evolve autonomously through recursive learning and targeted foraging.

## Architecture

The system mimics a biological brain with three core layers:

1.  **Memory (Storage)**:
    -   **Fragmented JSONL**: Knowledge is stored in atomic `.jsonl` files to prevent merge conflicts.
    -   **Entities**: Located in `knowledge/entities/{category}.jsonl`.
    -   **Relations**: Located in `knowledge/relations/{YYYY-MM}.jsonl`.
    -   **Memories**:
        -   `memories/MISSION_ACTIVE.md`: The current cognitive focus.
        -   `memories/archive/`: History of past missions.

2.  **Cortex (Engine)**:
    -   `cortex.py`: The read-only engine that loads the graph, validates integrity, and performs entropy analysis.
    -   acts as the "Hippocampus" for retrieval and associative search.

3.  **Nexus (Interface)**:
    -   `nexus.py`: The unified Command Line Interface (CLI) for all brain operations.
    -   acts as the "Central Nervous System".

4.  **Evolution (Orchestration)**:
    -   `evolution.py`: The executive function that runs the **OODA Loop**:
        1.  **Observe**: Analyze graph entropy (missing links, stale nodes).
        2.  **Orient**: Check active mission status.
        3.  **Decide**: Generate new `MISSION_ACTIVE.md` or archive old ones.
        4.  **Act**: Agents read the mission and execute via Nexus.

## Usage Guide (Nexus CLI)

All operations are performed via `nexus.py`.

### 1. Observe (Read)
```bash
# Check Brain Health & Entropy
python docs/brain/nexus.py status

# Search Concepts (Fuzzy Match)
python docs/brain/nexus.py search "android"

# Visualize Topology (Mermaid.js)
python docs/brain/nexus.py visualize
```

### 2. Evolve (Write)
```bash
# Run Daily Evolution Cycle
python docs/brain/nexus.py evolve
# -> Updates docs/brain/memories/MISSION_ACTIVE.md
```

### 3. Ingest (Action)
```bash
# Add New Concept
python docs/brain/nexus.py add concepts --id "rag" --type "pattern" --name "RAG" --desc "Retrieval Augmented Generation" --tags "ai,search"

# Connect Concepts
python docs/brain/nexus.py connect "rag" "improves" "llm" --context "arXiv:2301.00000"
```

## Schema & Rules

See [SCHEMA.md](./SCHEMA.md) for the "Gene Code" of this system.
-   **Rule #1**: Never delete. Only append.
-   **Rule #2**: All relations must point to existing entities.
-   **Rule #3**: Evolution must be documented in Missions and ADRs.

## Automation

The brain is wired into GitHub Actions:
-   `brain-integrity.yml`: Validates every commit using `nexus status`.
-   `brain-evolution.yml`: Runs daily to trigger `nexus evolve`.
