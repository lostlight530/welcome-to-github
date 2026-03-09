# Knowledge Base Schema Definition (知识库架构定义)

## Ⅰ. Architecture Decision Record (ADR / 架构决策记录)

- **Title**: Biological Neural Engine, SQLite Cortex & Singularity Pondering (生物神经网络、SQLite 皮层与奇点推理)
- **Status**: Active (活跃)
- **Decision (决策)**: Phase III: Singularity extends the central SQLite cortex with self-codebase ingestion (Omniscience/AST) and deeper graph inferences (Cognition/Ponder). The legacy fragmented `JSONL` system is the immutable text ledger, while `cortex.db` manages the dynamic and inferable cognitive state.
  > **中文**: Phase III 奇点升级为中心化 SQLite 皮层扩展了自我代码库摄入（全知/AST 解析）和深度图论推理（认知/思考）能力。传统的碎片化 `JSONL` 作为不可变文本账本，而 `cortex.db` 负责管理动态与可推理的认知状态。

---

## Ⅱ. Data Structures (数据结构)

### 1. Entities (实体层)
Stored in the `entities` table within `cortex.db`. Each entity follows this schema:
> 存储于 `cortex.db` 的 `entities` 表中。每个实体遵循以下模式：

```json
{
  "id": "unique-slug-id",            // Primary Key: 唯一标识符
  "type": "tech|concept|project|code_file|code_class|code_function", // Type: 类型分类（包括代码解析出的类、函数等）
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
  "relation": "predicate-string",    // Predicate: 谓词 (e.g., uses, authored, deprecates, defines, inherits_from)
  "target": "destination-entity-id", // Target Node: 目标实体 ID
  "weight": 1.0,                     // Edge Strength: 权重（置信度或连接强度）
  "annotation": "Source of truth",   // Context: 注释或上下文来源（如 URL/Doc）
  "created_at": "Unix-Time"          // Created At: 创建时间
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