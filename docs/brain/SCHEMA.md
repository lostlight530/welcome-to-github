# Knowledge Base Schema Definition (知识库架构定义)

## Ⅰ. Architecture Decision Record (ADR / 架构决策记录)

- **Title**: Phase IV Absolute Determinism & 4D Temporal Graph (第四阶段：绝对确定性与 4D 时序图谱)
- **Status**: Active (活跃)
- **Decision (决策)**: Phase IV upgrades the system into a "Mechanical Library / Truth Court". It implements Zero Internal LLM, Zero-Dependency Brutalism, and a 4D Temporal Knowledge Graph. The legacy fragmented `JSONL` system remains the absolute immutable text ledger ("Text is Law"), while `cortex.db` acts as an ephemeral, indexed cache utilizing `valid_at` and `invalid_at` for zero-deletion temporal tracking.
  > **中文**: Phase IV 升级将系统转变为“机械图书馆/真理法庭”。它实施了零内部大模型、零依赖极简主义以及 4D 时序知识图谱。传统的碎片化 `JSONL` 系统依然是绝对不可变的文本账本（“文本即法律”），而 `cortex.db` 作为临时索引缓存，利用 `valid_at` 和 `invalid_at` 实现零删除的时序追踪。

---

## Ⅱ. Data Structures (数据结构)

### 1. Temporal Entities (时序实体层)
Stored in the `entities` table within `cortex.db`. Each entity uses a composite primary key `(id, valid_at)` and follows this Phase IV temporal schema:
> 存储于 `cortex.db` 的 `entities` 表中。每个实体使用复合主键 `(id, valid_at)` 并遵循第四阶段时序模式：

```json
{
  "id": "unique-slug-id",            // Composite PK Part 1: 唯一标识符
  "type": "tech|concept|project|code_file|config_property|...", // Type: 类型分类
  "name": "Human Readable Name",     // Name: 可读名称
  "desc": "Short description.",      // Description: 简短描述
  "weight": 1.0,                     // Synaptic Weight: 神经权重
  "last_activated": 1700000000.0,    // Last Activated: 上次激活时间 (Unix float)
  "valid_at": "ISO-8601-String",     // Composite PK Part 2 (Start of lifespan): 生命期起点
  "invalid_at": "ISO-8601-String"    // Soft-Delete Anchor (End of lifespan): 软删除端点 (NULL if active)
}
```

### 2. Temporal Relations (时序关系层)
Stored in the `relations` table within `cortex.db`. Each row defines a directed edge with a temporal anchor `valid_at`:
> 存储于 `cortex.db` 的 `relations` 表中。每一行定义一条带有时间锚点的有向边：

```json
{
  "source": "source-entity-id",      // Source Node: 源实体 ID
  "relation": "predicate-string",    // Predicate: 谓词
  "target": "destination-entity-id", // Target Node: 目标实体 ID
  "weight": 1.0,                     // Edge Strength: 连接强度
  "valid_at": "ISO-8601-String",     // Start of relationship lifespan: 关系建立时间
  "invalid_at": "ISO-8601-String"    // Soft-Delete Anchor: 关系断裂或被覆盖时间 (NULL if active)
}
```

### 3. Cognitive Immune & Structure System (认知免疫与结构关系类型)
Special relation types designed to maintain knowledge integrity and model logic:
> 用于维护知识图谱完整性和建模代码逻辑的特殊关系类型：

- 💥 `conflicts_with`: Indicates a semantic or technical conflict (e.g., library incompatibility). *(存在语义或技术冲突。)*
- ⚰️ `deprecates`: Indicates that the source entity supersedes or obsoletes the destination entity. *(源实体取代或废弃了目标实体。)*
- 🛡️ `unaffected_by`: Explicitly states that the source entity is immune or unrelated to a vulnerability/issue in the destination entity. *(源实体免疫或不受目标实体漏洞影响。)*
- 🧱 `defines`: Maps a file entity to a structure entity like a class, function, or markdown section. *(指示某个文件定义了类、函数等结构)*
- 🧬 `inherits_from`: Used for class hierarchy tracking to empower transitive inference. *(用于类的继承层级追踪以支持传递推断)*

### 4. Inputs (原始输入层)
- 📁 `inputs/*.md` and `inputs/archive/*/*.md`
  Raw text or search results from the Harvester with Architect Filters applied. These files are **immutable** events.
  > 来自带有架构师滤镜雷达的原始文本或搜索结果。这些文件是**不可变**的事件快照。