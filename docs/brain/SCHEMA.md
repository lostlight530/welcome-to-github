# Knowledge Base Schema Definition (知识库架构定义)

## Architecture Decision Record (ADR / 架构决策记录)
- **ID**: ADR-0001
- **Title**: Decentralized Append-Only Knowledge Graph (去中心化追加式知识图谱)
- **Date**: 2026-02-14
- **Status**: Active (活跃)
- **Decision (决策)**: Use fragmented JSONL files instead of a monolithic JSON. (使用碎片化 JSONL 文件，而非单体 JSON。)

## Data Structures (数据结构)

### 1. Entities (`knowledge/entities/**/*.jsonl`)
Each line must be a valid JSON object:
每一行必须是一个有效的 JSON 对象：

```json
{
  "id": "unique-slug-id", // 唯一标识符
  "type": "tech|concept|person|project", // 类型：技术、概念、人物、项目
  "name": "Human Readable Name", // 可读名称
  "desc": "Short description.", // 简短描述
  "tags": ["tag1", "tag2"], // 标签
  "updated_at": "ISO-8601-Date" // 更新时间
}
```

### 2. Relations (`knowledge/relations/YYYY-MM.jsonl`)
Each line defines a directed edge:
每一行定义一条有向边：

```json
{
  "src": "source-entity-id", // 源实体 ID
  "rel": "predicate (e.g. supports, uses, authored)", // 谓词（例如：支持、使用、创作）
  "dst": "destination-entity-id", // 目标实体 ID
  "weight": 1.0,  // Optional: confidence or strength (权重：置信度或强度)
  "context": "Source of truth (e.g. URL or doc)", // 上下文（来源 URL 或文档）
  "created_at": "ISO-8601-Date" // 创建时间
}
```

### 3. Inputs (`inputs/YYYY/MM/*.md`)
Raw text or search results. These are immutable.
原始文本或搜索结果。这些是不可变的。
