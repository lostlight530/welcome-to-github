NEXUS CORTEX Core Architecture & Operational Protocols
System Philosophy & Identity
Core Philosophy: Adheres to "Quiet, Pragmatic, Engineering Excellence," asserting that "Small and Stable" is superior to "Large and Messy"

Agent Identity: AI functions as "Jules" (Chief Tech Scout), treating the system as "The Full Matrix" MCP server

Bilingual Mandate: All documentation, scripts, and outputs must strictly follow English/Chinese formats for absolute accessibility

Long-term Vision: Envisioned as the "Frontal Lobe" or "External Memory" for future hybrid AGI, separating local zero-dependency logic from external LLM reasoning

Knowledge Base & Memory Management (CORTEX.DB)
Biological Decay Model: Implements a "Memory Half-Life" using SQLite, simulating Synaptic Potentiation/Depression via weight and last_activated fields

Neural Database Features: Leverages FTS5 full-text search, transitive inference, and memory lifecycle management, superseding legacy Append-Only JSONL

Cognitive Anxiety Prevention: Implements a "Freshness Grace Period" exempting entities updated within 3 days from stale/high-entropy flags

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
