NEXUS CORTEX Core Architecture & Operational Protocols
System Philosophy & Identity
Core Philosophy: Adheres to "Quiet, Pragmatic, Engineering Excellence," asserting that "Small and Stable" is superior to "Large and Messy"

Agent Identity: AI functions as "Jules" (Chief Tech Scout), treating the system as "The Full Matrix" MCP server

Bilingual Mandate: All documentation, scripts, and outputs must strictly follow English/Chinese formats for absolute accessibility

Long-term Vision: Envisioned as the "Frontal Lobe" or "External Memory" for future hybrid AGI, separating local zero-dependency logic from external LLM reasoning

Knowledge Base & Memory Management (CORTEX.DB)
Biological Decay Model: Implements a "Memory Half-Life" using SQLite, simulating Synaptic Potentiation/Depression via weight and last_activated fields

Neural Database Features: Leverages FTS5 full-text search, transitive inference, and memory lifecycle management, superseding legacy Append-Only JSONL

## Intelligence & Senses (情报与感知)
- **Facts**: Must be sourced from official documentation, release notes, or repositories (via `harvester.py`).
- **Signal-to-Noise**: Harvester strictly checks ETags/states to avoid fetching duplicate or stagnant data (Zero Inbox Policy).
- **Epiphany Engine**: The system actively combats entropy by pairing disconnected entities and prompting the Architect to find hidden synergies (Cross-Pollination).
- **Synaptic Associative Search (图增强检索)**: The `cortex.py` engine merges FTS5 literal text matching with 1-Hop graph associative retrieval (for nodes with `weight > 1.2`). This provides the system with "Brainstorming" and "Deduction" capabilities.

## System Best Practices (系统最佳实践)
1. **Garbage Collection (垃圾回收)**: "Orphan Nodes Must Die." Entities with 0 relations after 3 evolution cycles and a weight `< 0.5` must be physically pruned to prevent database bloat.
2. **Crystallization (知识结晶)**: Fragmented raw intel (`inputs/`) must be routinely manually or semi-automatically crystallized into permanent `Entity` nodes via `nexus.py add entity`. Do not leave them as temporary events.
3. **Stay Hungry (保持饥饿)**: Expand sensory inputs (e.g., RSS parsers for Hacker News) using strictly Zero-Dependency Python standard libraries (`xml.etree.ElementTree`).
4. **Trust Intuition (相信直觉)**: Actively execute `nexus.py connect` when the system proposes "Subconscious Intuitions" in `MISSION_ACTIVE.md` to reinforce reasoning confidence.

Operational Commands:

nexus.py connect <source> <relation> <target>: Manually injects knowledge graph and rewards intuition

nexus.py touch <entity>: Manually triggers memory activation, increasing weight and updating timestamps

nexus.py visualize: Renders knowledge topology via Mermaid.js

Automated Evolution (OODA Loop)
Execution Flow: harvester.py (Sensory) -> nexus.py evolve (Inference & Decay) -> nexus.py archive (Housekeeping) -> nexus.py clean (Cleanup)

Stateful Radar: harvester.py monitors whitelists including Anthropic (MCP), Google (Edge AI), and Huawei (MindSpore), alerting on high-velocity updates

Epiphany Engine: evolution.py identifies disconnected entities to generate "Subconscious Intuitions" via transitive inference, prompting human analysis in MISSION_ACTIVE.md

Cleanup Rules: nexus.py clean must strictly exclude .harvester_state.json to preserve radar state; numerical prefixes are forbidden in memories/

Engineering Standards & MCP Specifications
Zero-Dependency Brutalism: Forbids outbound API calls; relies entirely on Python stdlib (e.g., sqlite3, urllib) for robust features

MCP Server: docs/brain/nexus_mcp.py acts as the production server, directing logs to stderr and exposing tools like search_knowledge and add_memory

Deployment Logic: The lostlight-portal frontend relies on native ES Modules and Tailwind CDN, managed via src/scripts/translations.js

Risk Mitigation: Evolution follows a "Machine Draft, Human Decision" model; direct pushes to the main branch are forbidden in favor of Pull Requests
