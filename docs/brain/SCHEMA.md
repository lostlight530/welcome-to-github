# Knowledge Base Schema Definition

## Architecture Decision Record (ADR)
- **ID**: ADR-0001
- **Title**: Decentralized Append-Only Knowledge Graph
- **Date**: 2026-02-14
- **Status**: Active
- **Decision**: Use fragmented JSONL files instead of a monolithic JSON.

## Data Structures

### 1. Entities (`knowledge/entities/**/*.jsonl`)
Each line must be a valid JSON object:
```json
{
  "id": "unique-slug-id",
  "type": "tech|concept|person|project",
  "name": "Human Readable Name",
  "desc": "Short description.",
  "tags": ["tag1", "tag2"],
  "updated_at": "ISO-8601-Date"
}
```

### 2. Relations (`knowledge/relations/YYYY-MM.jsonl`)
Each line defines a directed edge:
```json
{
  "src": "source-entity-id",
  "rel": "predicate (e.g. supports, uses, authored)",
  "dst": "destination-entity-id",
  "weight": 1.0,  // Optional: confidence or strength
  "context": "Source of truth (e.g. URL or doc)",
  "created_at": "ISO-8601-Date"
}
```

### 3. Inputs (`inputs/YYYY/MM/*.md`)
Raw text or search results. These are immutable.
