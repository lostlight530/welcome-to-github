# Knowledge Base Schema Definition (知识库架构定义)

## Architecture Decision Record (ADR / 架构决策记录)
- **ID**: ADR-0002
- **Title**: Biological Neural Engine & SQLite Cortex (生物神经网络与 SQLite 皮层引擎)
- **Date**: 2026-03-06
- **Status**: Active (活跃)
- **Decision (决策)**: Replaced fragmented `JSONL` with a centralized SQLite database (`cortex.db`) featuring FTS5 full-text search and Synaptic Plasticity (dynamic weight adjustments). (将碎片化 JSONL 替换为支持 FTS5 全文搜索与突触可塑性/动态权重调整的 SQLite 中心化数据库。)
- **Deprecates**: ADR-0001

## Data Structures (数据结构)

### 1. Entities (Stored in `entities` table within `cortex.db`)
Each entity follows this schema:
每个实体遵循以下模式：

```json
{
  "id": "unique-slug-id", // 唯一标识符 (Primary Key)
  "type": "tech|concept|person|project", // 类型：技术、概念、人物、项目
  "name": "Human Readable Name", // 可读名称
  "desc": "Short description.", // 简短描述
  "weight": 1.0, // 神经权重 (Synaptic Potentiation/Depression, >1.0 强化, <1.0 衰减)
  "last_activated": "ISO-8601-Date", // 上次激活时间
  "created_at": "ISO-8601-Date", // 创建时间
  "updated_at": "ISO-8601-Date" // 更新时间
}
```

### 2. Relations (Stored in `relations` table within `cortex.db`)
Each row defines a directed edge:
每一行定义一条有向边：

```json
{
  "source": "source-entity-id", // 源实体 ID
  "relation": "predicate (e.g. supports, uses, authored, conflicts_with, deprecates, unaffected_by)", // 谓词
  "target": "destination-entity-id", // 目标实体 ID
  "weight": 1.0,  // Optional: confidence or strength (权重：置信度或强度)
  "annotation": "Source of truth (e.g. URL or doc)", // 注释或上下文
  "created_at": "ISO-8601-Date" // 创建时间
}
```

**New Relation Types (Cognitive Immune System):**
- `conflicts_with`: Indicates a semantic or technical conflict (e.g., library incompatibility).
- `deprecates`: Indicates that the source entity supersedes or obsoletes the destination entity.
- `unaffected_by`: Explicitly states that the source entity is immune or unrelated to a vulnerability/issue in the destination entity.

### 3. Inputs (`inputs/YYYY/MM/*.md`)
Raw text or search results. These are immutable.
原始文本或搜索结果。这些是不可变的。
