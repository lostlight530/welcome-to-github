# NEXUS CORTEX: MCP Server Specification (MCP 服务器规范)

## Metadata (元数据)
- **ID**: 0006-nexus-mcp-server-spec
- **Title**: Transformation of Nexus CLI into a Standard MCP Server (Nexus CLI 向标准 MCP 服务器的转型)
- **Date**: 2026-02-14
- **Status**: Draft (草案)
- **Author**: Jules (AI Agent)
- **References**: [Model Context Protocol](https://modelcontextprotocol.io), ADR-0001

## 1. Executive Summary (执行摘要)
The goal is to elevate `docs/brain/nexus.py` from a local CLI script to a fully compliant **Model Context Protocol (MCP) Server**. This will allow external AI agents (including IDEs like Cursor/Windsurf or other LLM orchestrators) to treat this repository's knowledge base as a first-class **Context** (via Resources) and **Capability** (via Tools).

目标是将 `docs/brain/nexus.py` 从本地 CLI 脚本升级为完全兼容的 **Model Context Protocol (MCP) 服务器**。这将允许外部 AI 代理（包括 Cursor/Windsurf 等 IDE 或其他 LLM 编排器）将此存储库的知识库视为一等公民的 **上下文**（通过资源）和 **能力**（通过工具）。

## 2. Architecture (架构)

The server will be implemented using the `mcp` Python SDK (specifically `FastMCP` for simplicity and performance). It will wrap the existing `Cortex` (Read), `KnowledgeFactory` (Write), and `Evolver` (Maintenance) classes.

服务器将使用 `mcp` Python SDK（特别是 `FastMCP` 以简化实现并提高性能）实现。它将封装现有的 `Cortex`（读取）、`KnowledgeFactory`（写入）和 `Evolver`（维护）类。

```mermaid
graph TD
    Client[MCP Client (IDE/Agent)] <-->|Stdio/SSE| NexusMCP[Nexus MCP Server]

    subgraph Nexus Logic
        NexusMCP --> Cortex[Cortex (Read)]
        NexusMCP --> Factory[Factory (Write)]
        NexusMCP --> Evolver[Evolver (Maintain)]
    end

    subgraph Storage
        Cortex -->|Reads| JSONL[*.jsonl Files]
        Factory -->|Appends| JSONL
        Evolver -->|Analyzes| JSONL
    end
```

## 3. Resources (资源定义)

Resources provide read-only access to the knowledge graph. They are "passive" context.
资源提供对知识图谱的只读访问。它们是“被动”上下文。

### 3.1 Entities (实体)
- **URI Pattern**: `knowledge://entities/{type}/{id}`
- **Description**: Returns the full JSON content of a specific entity.
- **Example**: `knowledge://entities/concept/mcp-protocol`
- **MIME Type**: `application/json`

### 3.2 Relations (关系)
- **URI Pattern**: `knowledge://relations/{year}/{month}`
- **Description**: Returns all relations recorded in a specific month.
- **Example**: `knowledge://relations/2026/02`
- **MIME Type**: `application/json`

### 3.3 System Stats (系统状态)
- **URI Pattern**: `knowledge://stats/entropy`
- **Description**: Returns the current entropy report (density, orphans, etc.).
- **MIME Type**: `application/json`

## 4. Tools (工具定义)

Tools provide "active" capabilities to modify the graph or perform complex queries.
工具提供修改图谱或执行复杂查询的“主动”能力。

### 4.1 Add Entity (添加实体)
- **Name**: `add_entity`
- **Description**: Registers a new concept, technology, or person into the knowledge base. strict append-only.
- **Input Schema**:
  ```json
  {
    "type": "object",
    "properties": {
      "category": { "type": "string", "enum": ["concepts", "tech_stack", "people", "projects"], "description": "The category folder" },
      "id": { "type": "string", "pattern": "^[a-z0-9-]+$", "description": "Unique slug ID (kebab-case)" },
      "type": { "type": "string", "description": "Entity type (e.g., 'concept', 'framework')" },
      "name": { "type": "string", "description": "Human readable name" },
      "desc": { "type": "string", "description": "Short description" },
      "tags": { "type": "array", "items": { "type": "string" }, "description": "Tags for classification" }
    },
    "required": ["category", "id", "type", "name", "desc"]
  }
  ```

### 4.2 Connect Entities (连接实体)
- **Name**: `connect_entities`
- **Description**: Creates a directed relationship between two existing entities.
- **Input Schema**:
  ```json
  {
    "type": "object",
    "properties": {
      "src": { "type": "string", "description": "Source Entity ID" },
      "rel": { "type": "string", "description": "Predicate (e.g., 'uses', 'depends_on')" },
      "dst": { "type": "string", "description": "Destination Entity ID" },
      "context": { "type": "string", "description": "Context or justification for this link" }
    },
    "required": ["src", "rel", "dst"]
  }
  ```

### 4.3 Search Knowledge (搜索知识)
- **Name**: `search_knowledge`
- **Description**: Fuzzy search for entities by name, description, or tags.
- **Input Schema**:
  ```json
  {
    "type": "object",
    "properties": {
      "query": { "type": "string", "description": "Search term" }
    },
    "required": ["query"]
  }
  ```

### 4.4 Get Entropy Report (获取熵值报告)
- **Name**: `get_entropy_report`
- **Description**: Trigger an immediate analysis of the knowledge graph to detect orphans, stale nodes, and density.
- **Input Schema**:
  ```json
  {
    "type": "object",
    "properties": {},
    "required": []
  }
  ```

## 5. Security & Integrity (安全与完整性)

### 5.1 Append-Only Enforcement (只追加强制)
The `add_entity` tool must strictly validate that the `id` does not already exist. If it exists, the tool MUST fail (or return a specific error), preventing overwrite. This preserves the historical integrity of the knowledge base.
`add_entity` 工具必须严格验证 `id` 是否已存在。如果存在，工具必须失败（或返回特定错误），防止覆盖。这保护了知识库的历史完整性。

### 5.2 Input Sanitization (输入清洗)
All file paths are constructed internally based on `category` and `id`. User input (IDs) will be sanitized to allow only alphanumeric characters and hyphens, preventing directory traversal attacks.
所有文件路径均基于 `category` 和 `id` 在内部构建。用户输入（ID）将被清洗，仅允许字母数字字符和连字符，防止目录遍历攻击。

## 6. Implementation Plan (实施计划)

1.  **Dependencies**: Add `mcp` to `requirements.txt` (or install in env).
2.  **Refactor**: Modify `nexus.py` to import `FastMCP` and define the server.
3.  **Legacy Support**: Maintain the `argparse` CLI block for backward compatibility (or separate the server logic).
4.  **Testing**: Verify via `npx @modelcontextprotocol/inspector`.
