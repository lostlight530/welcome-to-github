# 知识库架构定义 (Knowledge Base Schema Definition)

## Ⅰ. 架构决策记录 (Architecture Decision Record - ADR)

- **Title**: Phase VII Architecture & 4D Temporal Mechanics
- **Status**: Active
- **Decision**: The system functions strictly as a "Truth Court". It relies heavily on zero-deletion temporal tracking. All actions are logged immutably, ensuring that knowledge states transition through time rather than being destructively overwritten.

---

## Ⅱ. 逻辑结构 (Logical Structures)

### 1. 量化账本机制 (Quantitative Ledger Mechanism)
The system maintains a continuous, append-only chronological ledger.
- **Function**: It continuously registers a unique physical temporal pulse during active cycles, ensuring an unbroken chain of systemic health monitoring and architectural records without requiring destructive file rewrites.

### 2. 时序实体模型 (Temporal Entities Model)
Every node within the system's memory represents a unique, isolated concept bounded by time.
- **Function**: Entities (such as technical concepts, projects, or configurations) are tracked securely. Old concepts are never deleted; they simply "expire," providing a flawless historical snapshot of the system's previous understanding.

### 3. 时序关系模型 (Temporal Relations Model)
Nodes are connected via directed conceptual edges.
- **Function**: Like entities, connections between ideas are temporally anchored, allowing the system to verify the validity of logical dependencies at any specific point in the project's history.

### 4. 认知免疫类型 (Cognitive Immune Types)
Specific, constrained relationship definitions intended to protect logical integrity:
- `conflicts_with`: Flags architectural or logic incompatibilities.
- `deprecates`: Safely transitions focus from obsolete structures to newer implementations.
- `unaffected_by`: Creates definitive isolation firewalls against perceived systemic risks.
- `defines`: Hard-links physical system files to abstract logic entities.
- `inherits_from`: Enables strict hierarchical mapping across the knowledge matrix.

### 5. 原始情报流 (Input Streams)
Raw external intelligence and system observations are persisted as immutable, read-only events, ensuring an incorruptible baseline of evidence for the deductive engines.