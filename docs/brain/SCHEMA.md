# 知识库架构定义 (Knowledge Base Schema Definition)

## Ⅰ. 架构决策记录 (Architecture Decision Record - ADR)

- **Title (标题)**: Phase VII Architecture & 4D Temporal Mechanics (第七阶段架构与 4D 时序机制)
- **Status (状态)**: Active (生效中)
- **Decision (决策)**: The system functions strictly as a "Truth Court". It relies heavily on zero-deletion temporal tracking. All actions are logged immutably, ensuring that knowledge states transition through time rather than being destructively overwritten. (系统严格作为“真理法庭”运行。它高度依赖零删除的时序追踪。所有操作均被不可篡改地记录，确保知识状态在时间维度上平滑过渡，而非被破坏性覆盖。)

---

## Ⅱ. 逻辑结构 (Logical Structures)

### 1. 量化账本机制 (Quantitative Ledger Mechanism)
The system maintains a continuous, append-only chronological ledger. (系统维护一个连续的、仅追加的时间轴账本。)
- **Function (功能)**: It continuously registers a unique physical temporal pulse during active cycles, ensuring an unbroken chain of systemic health monitoring and architectural records without requiring destructive file rewrites. (它在活跃周期内持续注册独特的物理时间脉冲，确保系统健康监控和架构记录链条的连续性，无需进行破坏性的文件重写。)

### 2. 时序实体模型 (Temporal Entities Model)
Every node within the system's memory represents a unique, isolated concept bounded by time. (系统记忆中的每个节点代表一个受时间限制的独特、孤立的概念。)
- **Function (功能)**: Entities (such as technical concepts, projects, or configurations) are tracked securely. Old concepts are never deleted; they simply "expire," providing a flawless historical snapshot of the system's previous understanding. (实体（如技术概念、项目或配置）被安全地追踪。旧概念永远不会被删除；它们只会“过期”，从而提供了系统之前认知状态的完美历史快照。)

### 3. 时序关系模型 (Temporal Relations Model)
Nodes are connected via directed conceptual edges. (节点通过有向概念边缘连接。)
- **Function (功能)**: Like entities, connections between ideas are temporally anchored, allowing the system to verify the validity of logical dependencies at any specific point in the project's history. (与实体一样，思想之间的联系也有时间锚点，允许系统验证项目历史中任何特定时间点的逻辑依赖的有效性。)

### 4. 认知免疫类型 (Cognitive Immune Types)
Specific, constrained relationship definitions intended to protect logical integrity (特定的、受限的关系定义，旨在保护逻辑完整性):
- `conflicts_with`: Flags architectural or logic incompatibilities. (标记架构或逻辑不兼容。)
- `deprecates`: Safely transitions focus from obsolete structures to newer implementations. (安全地将焦点从废弃的结构转移到新的实现。)
- `unaffected_by`: Creates definitive isolation firewalls against perceived systemic risks. (创建明确的隔离防火墙，抵御感知的系统风险。)
- `defines`: Hard-links physical system files to abstract logic entities. (将物理系统文件硬链接到抽象逻辑实体。)
- `inherits_from`: Enables strict hierarchical mapping across the knowledge matrix. (在知识矩阵中实现严格的层级映射。)

### 5. 原始情报流 (Input Streams)
Raw external intelligence and system observations are persisted as immutable, read-only events, ensuring an incorruptible baseline of evidence for the deductive engines. (原始外部情报和系统观察被持久化为不可篡改的只读事件，确保为演绎引擎提供不可破坏的证据基线。)