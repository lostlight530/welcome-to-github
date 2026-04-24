# 知识库架构定义 (Knowledge Base Schema Definition)

## Ⅰ. 架构决策记录 (Architecture Decision Record - ADR)

- **Title**: Phase VI Absolute Determinism & 4D Temporal Graph
- **Status**: Active
- **Decision**: Phase VI upgrades the system into a "Mechanical Library / Truth Court". It implements Zero Internal LLM, Zero-Dependency Brutalism, and a 4D Temporal Knowledge Graph. The legacy fragmented `JSONL` system remains the absolute immutable text ledger ("Text is Law"), while `cortex.db` acts as an ephemeral, indexed cache utilizing `valid_at` and `invalid_at` for zero-deletion temporal tracking.

---

## Ⅱ. 数据结构 (Data Structures)

### 1. 时序实体层 (Temporal Entities)
Stored in the `entities` table within `cortex.db`. Each entity uses a composite primary key `(id, valid_at)` and follows the temporal schema:

```json
{
  "id": "unique-slug-id",            // Composite PK Part 1
  "type": "tech|concept|project|code_file|config_property|...",
  "name": "Human Readable Name",     // Name
  "desc": "Short description.",      // Description
  "weight": 1.0,                     // Synaptic Weight
  "last_activated": 1700000000.0,    // Last Activated (Unix float)
  "valid_at": "ISO-8601-String",     // Composite PK Part 2 (Start of lifespan)
  "invalid_at": "ISO-8601-String"    // Soft-Delete Anchor (NULL if active)
}
```

### 2. 时序关系层 (Temporal Relations)
Stored in the `relations` table within `cortex.db`. Each row defines a directed edge with a temporal anchor `valid_at`:

```json
{
  "source": "source-entity-id",      // Source Node
  "relation": "predicate-string",    // Predicate
  "target": "destination-entity-id", // Target Node
  "weight": 1.0,                     // Edge Strength
  "valid_at": "ISO-8601-String",     // Start of relationship lifespan
  "invalid_at": "ISO-8601-String"    // Soft-Delete Anchor (NULL if active)
}
```

### 3. 认知免疫与结构系统 (Cognitive Immune & Structure System)
Special relation types designed to maintain knowledge integrity and model logic:

- 💥 `conflicts_with`: Indicates a semantic or technical conflict (e.g., library incompatibility).
- ⚰️ `deprecates`: Indicates that the source entity supersedes or obsoletes the destination entity.
- 🛡️ `unaffected_by`: Explicitly states that the source entity is immune or unrelated to a vulnerability/issue in the destination entity.
- 🧱 `defines`: Maps a file entity to a structure entity like a class, function, or markdown section.
- 🧬 `inherits_from`: Used for class hierarchy tracking to empower transitive inference.

### 4. 原始输入层 (Inputs)
- 📁 `inputs/*.md` and `inputs/archive/*/*.md`
  Raw text or search results from the Harvester with Architect Filters applied. These files are **immutable** events.