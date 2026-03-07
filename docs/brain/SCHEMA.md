# Knowledge Base Schema Definition (知识库架构定义)

## Ⅰ. Architecture Decision Record (ADR / 架构决策记录)

- **ID**: `ADR-0002`
- **Title**: Biological Neural Engine & SQLite Cortex (生物神经网络与 SQLite 皮层引擎)
- **Status**: Active (活跃)
- **Decision (决策)**: Replaced fragmented `JSONL` with a centralized SQLite database (`cortex.db`) featuring FTS5 full-text search and Synaptic Plasticity (dynamic weight adjustments).
  > **中文**: 将碎片化 `JSONL` 替换为支持 `FTS5` 全文搜索与突触可塑性（动态权重调整）的 SQLite 中心化数据库。
- **Deprecates (废弃)**: `ADR-0001`

---

## Ⅱ. Data Structures (数据结构)

### 1. Entities (实体层)
Stored in the `entities` table within `cortex.db`. Each entity follows this schema:
> 存储于 `cortex.db` 的 `entities` 表中。每个实体遵循以下模式：

```json
{
  "id": "unique-slug-id",            // Primary Key: 唯一标识符
  "type": "tech|concept|project",    // Type: 类型分类（技术、概念、项目等）
  "name": "Human Readable Name",     // Name: 可读名称
  "desc": "Short description.",      // Description: 简短描述
  "weight": 1.0,                     // Synaptic Weight: 神经权重 (>1.0 强化, <1.0 衰减)
  "last_activated": "Unix-Time",     // Last Activated: 上次激活时间
  "created_at": "Unix-Time",         // Created At: 创建时间
  "updated_at": "Unix-Time"          // Updated At: 更新时间
}
```

### 2. Relations (关系层)
Stored in the `relations` table within `cortex.db`. Each row defines a directed edge:
> 存储于 `cortex.db` 的 `relations` 表中。每一行定义一条有向边：

```json
{
  "source": "source-entity-id",      // Source Node: 源实体 ID
  "relation": "predicate-string",    // Predicate: 谓词 (e.g., uses, authored, deprecates)
  "target": "destination-entity-id", // Target Node: 目标实体 ID
  "weight": 1.0,                     // Edge Strength: 权重（置信度或连接强度）
  "annotation": "Source of truth",   // Context: 注释或上下文来源（如 URL/Doc）
  "created_at": "Unix-Time"          // Created At: 创建时间
}
```

### 3. Cognitive Immune System (认知免疫关系类型)
Special relation types designed to maintain knowledge integrity:
> 用于维护知识图谱完整性的特殊关系类型：

- 💥 `conflicts_with`: Indicates a semantic or technical conflict (e.g., library incompatibility). (存在语义或技术冲突。)
- ⚰️ `deprecates`: Indicates that the source entity supersedes or obsoletes the destination entity. (源实体取代或废弃了目标实体。)
- 🛡️ `unaffected_by`: Explicitly states that the source entity is immune or unrelated to a vulnerability/issue in the destination entity. (源实体免疫或不受目标实体漏洞影响。)

### 4. Inputs (原始输入层)
- 📁 `inputs/*.md` and `inputs/archive/YYYY/MM/*.md`
  Raw text or search results from the Harvester with Architect Filters applied. These files are **immutable** events.
  > 来自带有架构师滤镜雷达的原始文本或搜索结果。这些文件是**不可变**的事件快照。
