# bytedance/deer-flow · README.md

> 当前有效引用快照. 完整原文由固定 Git Blob 保存, 当前活动输入不重复内联.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) |
| 来源文件 | [README.md](https://github.com/bytedance/deer-flow/blob/2a16b26960cb953cd3283702d018bd7dce6b80b7/README.md) |
| 来源版本 | `2a16b26960cb953cd3283702d018bd7dce6b80b7` |
| 来源目录 Tree | `e095fed0e99021fea9aa911c1413b6fe3109fcc4` |
| 来源内容 Blob | `0793a01056d0b1d96c78ccd6a28dfce466183d80` |
| 摄取时间 | `2026-11-06T16:28:10.660568+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_bytedance_deer_flow_readme_md` |
| 快照模式 | `PINNED_EXTERNAL_REFERENCE` |
| 规范内容 SHA256 | `a994f8f3c9c42b11c5f5d5add9bc52aefe10a948a232996656e231cc0c712044` |
| 原文字节数 | `382008` |
| 原文行数 | `4293` |

## 本次变化

- 新增行数 `19`.
- 删除行数 `5`.
- 完整 Diff 字节数 `11261`.
- 来源变化不等于本仓执行验证或独立研究次数.

## 阅读导航

- 🦌 DeerFlow - 2.0
- Official Website
- Sister Projects
- Coding Plan from ByteDance Volcengine
- InfoQuest
- Table of Contents
- One-Line Agent Setup
- Quick Start
- Configuration
- Running the Application
- Deployment Sizing
- Option 1: Docker (Recommended)
- Upgrading an existing checkout
- Option 2: Local Development
- Startup Modes
- LangGraph Studio (Optional)
- Docker Production Deployment
- One-step (build + start)
- Two-step (build once, start later)
- Stop
- Advanced
- Sandbox Mode
- MCP Server
- IM Channels

## 原文完整性与取回

- [按固定源提交读取完整原文](https://github.com/bytedance/deer-flow/blob/2a16b26960cb953cd3283702d018bd7dce6b80b7/README.md).
- 原文由来源 Blob SHA 与规范内容 SHA256 共同识别.
- 被替换的完整活动快照先原样封存到只追加 Archive.
- Diff 过长时只展示有界预览, 预览不代表完整差异.

<details>
<summary>展开有界版本差异</summary>

```diff
--- previous

+++ 0793a01056d0b1d96c78ccd6a28dfce466183d80

@@ -254,7 +254,7 @@

 
    Brave web search preserves valid entries in mixed result lists. Malformed response containers or lists containing no usable entries return a structured format error; missing, null, or empty results keep the existing "No results found" response. Format errors also log the malformed container's path and type, or the absence of usable result objects, without including search queries, credentials, or payload values.
 
-   You.com, GroundRoute and Webz initialize HTTPX clients in a worker thread so synchronous TLS trust loading does not block the agent event loop; requests and session cleanup remain asynchronous.
+   Several providers, including You.com, GroundRoute, Webz and InfoQuest, initialize HTTPX clients in a worker thread so synchronous TLS trust loading does not block the agent event loop; requests and session cleanup remain asynchronous.
 
    GroundRoute web search and fetch contain malformed HTTP-success payloads the same way: a non-object payload, a `results` container that is not a list, or a non-empty list with no object entries returns the provider's format error, while non-object entries in an otherwise valid list are skipped in order. Missing, null, or empty results keep the existing "No results found" response.
 
@@ -1955,7 +1955,7 @@

 or replace them with `NULL` in SQL; the CLI reports an error and preserves any
 existing output rather than writing invalid JSON.
 
-The **data-analysis** skill preserves each CSV file or Excel sheet when names collide across inputs. [Prepare its Python environment](skills/public/data-analysis/SKILL.md#environment-setup) explicitly with DuckDB and openpyxl; missing packages report setup instructions instead of installing themselves during analysis. Use the SQL names printed by `inspect` (such as `report`, `report_1`) for queries and summaries. Its cache follows ordered input basenames and contents, so renaming or reordering inputs rebuilds their table map instead of silently selecting a different source. Quoted original names also resolve without rewriting query text; apostrophes in upload paths and double quotes in column names are preserved through loading, inspection, queries, and summaries. CSV, JSON, and Markdown exports accept bare filenames such as `report.csv` in the current working directory as well as nested relative and absolute paths.
+The **data-analysis** skill preserves each CSV file or Excel sheet when names collide across inputs. [Prepare its Python environment](skills/public/data-analysis/SKILL.md#environment-setup) explicitly with DuckDB and openpyxl; missing packages report setup instructions instead of installing themselves during analysis. Use the SQL names printed by `inspect` (such as `report`, `report_1`) for queries and summaries. Its cache follows ordered input basenames and contents, so renaming or reordering inputs rebuilds their table map instead of silently selecting a different source. Cache publication uses complete immutable generations: import writers close before their database and table map become visible together, so overlapping processes can read the same snapshot. Interrupted private builds are removed and damaged entries rebuild; legacy flat caches rebuild once. Complete generations remain available to active readers, so stop analyses before manually clearing `.data-analysis-cache/`. Automatic cache garbage collection is not provided. Quoted original names also resolve without rewriting query text; apostrophes in upload paths and double quotes in column names are preserved through loading, inspection, queries, and summaries. CSV, JSON, and Markdown exports accept bare filenames such as `report.csv` in the current working directory as well as nested relative and absolute paths.
 
 After an answer loads skills, its toolbar includes **Skills used**. Hover over or click the icon to see the skills and their sources; hovering a skill name underlines it. Select a skill to inspect its `SKILL.md` in the resizable side panel (a drawer on mobile). The view uses snapshots captured during successful configured read-tool loads or explicit slash activation, so later edits or removal of a skill do not rewrite its history. Repeated loads appear once per run, in first-load order. Range reads and bounded snapshots are labeled as partial; older conversations without captured evidence do not show this menu. Copy returns the captured Markdown, including YAML frontmatter. Package-relative links and images remain readable references rather than navigating away from the conversation. Skill loads performed through other tools, such as shell commands, are not inferred from answer text.
 
@@ -2597,9 +2597,10 @@

 The Web UI composer can polish draft input before sending. The rewrite runs as a short Gateway LLM request using the `input_polish` model configuration, keeps slash skill prefixes such as `/data-analysis`, and only replaces the local draft after the user clicks the polish button; it does not create a thread run or persist a message.
 
 Input polishing, follow-up suggestions, background project-file summaries, the
-LLM skill scanner, thread title generation, and the `/goal` evaluator construct
-their model providers off the Gateway event loop, so local credential reads do
-not stall unrelated requests.
+LLM skill scanner, thread title generation, the `/goal` evaluator, and manual
+context compaction (`/compact`) construct their model providers off the
+Gateway event loop, so local credential reads do not stall unrelated
+requests.
 
 When the agent asks for clarification, the Web UI shows the structured response card but keeps the normal composer available. Users can complete the card or send a free-form chat message to bypass it; that message closes the latest pending clarification and becomes the agent's next input. Accompanying answer text stays outside the execution steps panel, and answering the request keeps previously completed text in the conversation while the agent continues.
 
@@ -2677,6 +2678,9 @@

 chunks before replacing it. `summarization.trim_tokens_to_summarize` bounds raw
 input per step; generated summaries use at most half to leave room for source.
 Oversized summaries retain marked head/tail text; raw history is never clipped.
+Native document titles, context and direct plain-text bodies are included in the
+summary input. Binary documents and remote media are not decoded or fetched;
+nested document blocks are not traversed.
 A pass is limited to 64 chunks and leaves history unchanged on failure or limit
 exhaustion. A limit breach starts a five-minute per-process cooldown for the
 same thread/history window and policy, including rebuilt middleware. A larger
@@ -2721,6 +2725,9 @@

 value-derived placeholders. No token-to-raw mapping is persisted. Raw thread
 text and local fallback titles remain available for display; memory redaction
 copies messages without changing the caller's history or tool execution.
+For SDK agents without a checkpointer, deeply nested JSON tool arguments do not
+prevent memory admission, with PII redaction either enabled or disabled.
+Structured JSON content blocks still use recursive redaction and remain depth-limited.
 The hidden `/goal` continuation is redacted before it is stored.
 
 The Web UI preserves persisted message order when merging history with live updates. Streaming steps around a persisted result inside the loaded history stay together, including steps that arrive after the result. Steps captured during compaction also remain visible before their persisted result when history has not refreshed and the UI has not rendered them yet.
@@ -3608,6 +3615,13 @@

 An individual Custom Agent can opt out of memory without changing the global setting. Add `memory_enabled: false` to that agent's `users/{user_id}/agents/{name}/config.yaml`. The agent still receives the current-date reminder, but DeerFlow does not inject recalled memory, queue passive or summarization-driven memory updates (including manual `/compact`), expose memory tools, or add memory-tool instructions for that agent. If an existing agent is switched off, its previously injected memory block is removed from checkpoint state before the next model call while its date reminder and conversation remain. Omitting the field (or setting it to `true`) preserves the existing global `memory` behavior.
 
 Single-fact repository operations are genuinely incremental: an upsert/delete reads, journals, writes, and re-indexes only the addressed fact files, and returns an explicit incomplete delta rather than a cache-dependent fake full document. Summary change sets merge the supplied `user`/`history` child keys over the persisted sections so a partial update cannot erase omitted siblings; full imports normalize both sections to the complete compatibility schema before applying replacement values. Imports reject malformed fact lists or blank/non-text content with HTTP 400 before changing stored memory; recoverable legacy metadata still receives defaults. An explicit empty fact list remains an intentional clear. Manager/API compatibility methods materialize a fresh full document only when their public response contract requires one. Fact-level point operations use separate expected user-memory and fact revisions and may explicitly rebase when every addressed fact precondition still holds. Snapshot-derived operations such as scoped clear, capped create, consolidation, and trimming never replay stale delete/trim sets: a manifest conflict reloads the complete document and recomputes the operation, with a bounded retry. Fact paths use the first two hexadecimal characters of `SHA-256(fact_id)` so generated `fact_*` IDs distribute across shards. The cache token combines the shared JSON's nanosecond mtime, size, and persisted revision; this prevents coarse-mtime same-size writes from returning stale data without scanning fact files. Direct out-of-band Markdown edits require an explicit reload. Storage-specific conflicts and corruption are translated at the MemoryManager boundary; the Gateway returns conflict as HTTP 409 and a stable, non-sensitive corruption error as HTTP 500. Full-document `save()` remains a compatibility API and computes a diff before writing; malformed or missing `facts` can no longer silently erase an agent's Markdown files. Legacy migration preserves non-empty `user`/`history` before deleting an agent `memory.json`; conflicting summaries keep the legacy file and fail loudly instead of choosing a winner.
+
+DeerMem backup imports restore saved fact contents even after those facts have
+been edited, using the current stored revisions to protect the restore. Older
+backups may omit fact revisions. Backup revisions are validated before the
+importer substitutes current revisions. Rejected imports preserve stored memory.
+A concurrent write during import still returns HTTP 409 so the caller can reload
+and retry.
 
 Legacy facts in `memory.json` migrate automatically into the reserved `__default__` Markdown bucket on the user's first normal memory read. Operators who prefer to audit or complete the migration before serving traffic can run the optional idempotent CLI from `backend/`:
```

</details>
