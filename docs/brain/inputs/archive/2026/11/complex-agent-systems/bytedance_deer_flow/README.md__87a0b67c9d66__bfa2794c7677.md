# bytedance/deer-flow · README.md

> 当前有效引用快照. 完整原文由固定 Git Blob 保存, 当前活动输入不重复内联.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) |
| 来源文件 | [README.md](https://github.com/bytedance/deer-flow/blob/bfa2794c7677d22d2a8097c55ffaeb2d00979c24/README.md) |
| 来源版本 | `bfa2794c7677d22d2a8097c55ffaeb2d00979c24` |
| 来源目录 Tree | `c5bd0cbb6f716d5385a153632276e81661a46e25` |
| 来源内容 Blob | `87a0b67c9d66be4628fda7f88914dce5f7ec3da8` |
| 摄取时间 | `2026-11-10T03:58:25.356225+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_bytedance_deer_flow_readme_md` |
| 快照模式 | `PINNED_EXTERNAL_REFERENCE` |
| 规范内容 SHA256 | `ba1b03d6db5ad9e3e47226892f6f4052df08135ca9a6d075bd8109509e6131f7` |
| 原文字节数 | `391901` |
| 原文行数 | `4407` |

## 本次变化

- 新增行数 `57`.
- 删除行数 `6`.
- 完整 Diff 字节数 `14311`.
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

- [按固定源提交读取完整原文](https://github.com/bytedance/deer-flow/blob/bfa2794c7677d22d2a8097c55ffaeb2d00979c24/README.md).
- 原文由来源 Blob SHA 与规范内容 SHA256 共同识别.
- 被替换的完整活动快照先原样封存到只追加 Archive.
- Diff 过长时只展示有界预览, 预览不代表完整差异.

<details>
<summary>展开有界版本差异</summary>

```diff
--- previous

+++ 87a0b67c9d66be4628fda7f88914dce5f7ec3da8

@@ -941,6 +941,8 @@

    make dev
    ```
 
+   Local nginx writes temporary files under the checkout's `temp/` directory.
+
 5. **Access**: http://localhost:2026
 
 6. **(Optional) Load sample memory data for local review**: open `Settings > Memory`, click **Import memory**, and select `backend/docs/memory-settings-sample.json`. The browser imports into the signed-in user's memory.
@@ -1774,6 +1776,20 @@

 actions remain visible beside the compact sidebar on narrow screens.
 
 ### Skills & Tools
+
+**Human approval for high-risk tools**: Set `hitl_approval.enabled: true` and
+list tools such as `write_file`, `str_replace`, or `bash` in `config.yaml` to
+pause matching calls before execution. The Web UI shows an approval card for
+each action; approval attempts execution under the existing guardrails and
+sandbox authorization, while rejection returns the reason to the agent without
+running the tool. Non-interactive runs follow `hitl_approval.non_interactive`;
+subagents and runtimes without resume support always fail closed.
+
+Pending approvals do not expire and block new runs on the same thread until
+resolved. Long argument values may be truncated in the display, but approval
+executes the original complete arguments. The feature is disabled by default.
+See [HITL Tool Approval](backend/docs/CONFIGURATION.md#hitl-tool-approval) for
+configuration and safety semantics.
 
 Agents can call the read-only `inspect_run_status` tool to inspect visible run
 token usage, message and tool-call counts, an approximate context-window fill,
@@ -1873,8 +1889,9 @@

 for extension registration and configuration. The installable
 [WeKnora read-only extension](examples/deerflow-extension-weknora/README.md)
 targets WeKnora v0.8.3 and adds knowledge-base/document selection and shared
-retrieval citations. Configure explicit user-to-workspace credential bindings;
-resource authorization remains with WeKnora. The extension directory includes
+retrieval citations. Configure explicit user-to-workspace credential bindings,
+or opt into shared read-only access for authenticated users without maintaining
+a user-ID list. Resource authorization remains with WeKnora. The extension directory includes
 its installation guide.
 
 The optional [knowledge platform extension](examples/deerflow-extension-knowledge-platform/README.md)
@@ -2151,7 +2168,8 @@

 SkillScan warns about remote downloads piped into common shells, including `env` launchers, sudo, interpreter paths, and shell line continuations. It distinguishes environment dumps from `env` commands, including assignments and GNU split-string escapes. Shell parsing and split expansion are bounded; reaching a limit preserves critical findings already detected. Pipes to non-shell tools such as `jq` and `tee` do not trigger this warning.
 
 SkillScan treats HTTP/HTTPS scheme spellings and HTTP hostnames case-insensitively and recognizes bracketed IPv6
-loopback (`[::1]`) URLs as local. External IPv6 endpoints still trigger network findings,
+loopback (`[::1]`) hosts as local. Raw brackets in the URL's userinfo make it count as outbound for
+exfiltration checks. External IPv6 endpoints still trigger network findings,
 and cloud-metadata hostname detection is case-insensitive.
 
 SkillScan recognizes unquoted integer model-usage counters such as `total_tokens` and `input_tokens` in skill examples as measurements. Benchmark token statistics and signed deltas are also recognized; credential fields and other string values remain subject to secret detection.
@@ -2635,6 +2653,8 @@

 
 Unsent Web UI composer drafts survive page reloads and switching between conversations within the same browser tab. Drafts are isolated by user, agent, and conversation, include the selected skill and explicit conversation references, and are cleared once a send is accepted. Project documents already attached to the thread also survive reloads; browser-local uploads and quoted message excerpts are not persisted.
 
+The composer's paperclip button opens the local file chooser directly; the `@` button opens the reference picker for skills, project files, conversations, and plugins.
+
 If an attachment upload reports `success: false`, the Web UI stops the send even when the HTTP response is 200. The upload error is shown and the composer keeps its draft and attachments for correction or retry. Files already accepted by a partially successful upload remain on the server; this does not roll them back.
 
 Document conversion reads the live PDF-converter setting and parses documents in a background worker, keeping configuration-file checks off the Gateway event loop.
@@ -2779,6 +2799,7 @@

 The chat header also shows a context-window gauge when the selected model has a positive `context_window` configured. It estimates the latest materialized checkpoint's message tokens and keeps the previous same-thread percentage visible while data refetches, independently of the cumulative token-usage setting.
 
 When `token_budget.enabled` and `token_usage.enabled` are both enabled, each lead-agent run budget includes completed subagent usage, including the final batch. Hidden goal continuations share the budget; a new user run starts fresh.
+The token budget counts separate accepted model calls even when their response message IDs repeat, without double-counting repeated observations or later subagent-usage increments.
 
 ### Sub-Agents
 
@@ -2907,6 +2928,11 @@

 independently shaped summaries from other runners still contribute evidence.
 Pytest sibling summaries retain warning counts and the optional human-readable
 duration suffix printed for runs lasting at least a minute, such as `(0:01:05)`.
+
+`tests_passed` evidence pairs each command with its own result, even when a
+provider reuses a tool-call id in a later response. Each run stays a separate
+entry in execution order, so a later failing run is decisive and an earlier
+run's output is never credited to another command.
 
 For Maven and Gradle test acceptance, a `BUILD SUCCESS` / `BUILD SUCCESSFUL`
 banner alone remains `UNVERIFIED`: builds can succeed without running tests.
@@ -3040,6 +3066,23 @@

 For example, independent read-only research can run concurrently when the wall-clock savings outweigh duplicated discovery and synthesis cost, while a repository refactor with shared files and sequential test feedback remains with the lead agent. When `max_concurrent_subagents` is `1`, parallel and multi-batch routing guidance is disabled; delegation remains available only for material specialist or context-isolation benefit.
 
 ### Sandbox & File System
+
+AIO runs commands from independent subagents concurrently, including Lark CLI
+and skill commands with per-call environment variables. Commands within one
+subagent stay ordered, and each environment-bearing call uses a fresh session.
+Environment-bearing calls share a per-sandbox Bash admission limit, configured
+by `sandbox.environment.AIO_BASH_MAX_SESSIONS` (positive integer, default `50`).
+Excess calls wait without creating a session and can be cancelled while waiting;
+the slot is retained through session cleanup. This pool is separate from
+`MAX_SHELL_SESSIONS`. Docker reuse checks the persisted container environment;
+K8s reuse checks the provisioner's Pod-reported Bash capacity. Upgrade the
+provisioner with the Gateway: missing capacity metadata blocks admission.
+Cancellation remains routed to the running command while scope release or
+sandbox close waits for it to finish and clean up.
+Scope release waits for in-flight execution and cleanup without a separate drain
+deadline. Allow for the remaining command timeout (600 seconds by default), plus
+session/transport/recovery/cleanup time when setting operator-facing release
+budgets; the HTTP cleanup timeout does not bound the preceding lock wait.
 
 With local host bash enabled, the path guard permits division in simple shell
 arithmetic and recognized single-quoted Python, Node.js and Perl programs.
@@ -3327,8 +3370,9 @@

 
 If the sample cuts a CRLF line ending in half, the preview keeps the earlier complete rows and omits the incomplete final record, including when its last field is quoted.
 
-Text artifacts are streamed with HTTP byte-range support. The Web UI initially
-loads at most 1 MiB, shows the preview size when a file is larger, and waits for
+Text artifacts are streamed with HTTP byte-range support. A resumed download
+validates its ETag against the file version that supplies its response bytes.
+The Web UI initially loads at most 1 MiB, shows the preview size for larger files, and waits for
 an explicit **Load full file** action before fetching the remainder or mounting
 the full code editor. Editing becomes available once the complete file has loaded;
 unsaved-change detection uses the full content, including when reverting edits
@@ -3650,6 +3694,8 @@

 
 File-backed memory now separates global user context from agent facts. Each user has one `memory.json` containing only the project-independent `user` and `history` summaries; every fact is a canonical Markdown file below `agents/{agent_name}/facts/`. Existing lead-agent middleware, API, Settings, import/export, and embedded-client calls that omit `agent_name` resolve inside DeerMem to the reserved `__default__` bucket. That bucket is outside the valid custom-agent name grammar, so a real custom agent named `lead-agent` has a separate fact repository and deleting a custom agent cannot delete a memory-only directory without `config.yaml`. Public agent identifiers are case-insensitive and canonicalized to lowercase. Runtime/API readers still receive a compatibility `facts` array for the selected/default agent, so the frontend does not read agent facts from `memory.json`; structured Markdown `source` metadata is projected to the historical string field at the MemoryManager boundary. An unscoped Clear All first migrates facts from unread legacy per-agent JSON without adopting its soon-to-be-cleared summaries, then removes shared summaries and facts from every agent bucket while preserving agent configuration files, so a later read cannot resurrect skipped legacy facts; an explicitly agent-scoped clear removes only that agent's facts. On first normal read, old facts embedded in the user JSON are migrated automatically to `__default__`; facts written to the earlier implicit `lead-agent` bucket are also moved when that directory is not a real custom agent. Migration and normal writes notify the configured retrieval adapter only after durable storage locks are released. DeerMem uses a scope-aware SQLite FTS5/BM25 adapter by default, stores only rebuildable derived index data under `.retrieval/` (or under `memory.backend_config.retrieval_index_path` when set; a relative value resolves against `storage_path`), and rebuilds it in the background during Gateway startup or lazily on the first scoped search. A corrupt derived index is recreated automatically. When several Gateway instances share one `storage_path`, point `retrieval_index_path` at instance-local disk: SQLite's WAL mode is unsupported on network filesystems, each instance re-syncs a user's index on its next search after a peer writes, and a declared multi-instance deployment (`deployment.multi_instance: true` / `DEER_FLOW_MULTI_INSTANCE=1`) that leaves the index under the memory root logs a warning at startup. The Helm chart mounts a Pod-local `emptyDir` for it. Set `memory.backend_config.retrieval_adapter` to an empty string to disable it and use the local substring fallback. Chinese tokenization is optional; install the backend `memory-zh` extra (`uv sync --extra memory-zh`) for jieba-assisted sub-phrase search. Journaled writes, a shared user lock, and optimistic user-memory revisions prevent silent lost updates.
 
+FTS5 search selects the highest combined BM25, time-decay, and confidence scores across all matching facts before applying the requested result count. Requesting fewer results preserves the same ranking.
+
 Set `memory.backend_config.retrieval_relevance_enabled: true` to opt into deterministic relevance/confidence ranking and query-aware injection. This **bypasses `retrieval_adapter` for search**, including the default FTS5/BM25 and custom adapters; indexing remains configured. `retrieval_relevance_weight` controls the blend and `retrieval_diversity_weight` enables near-duplicate penalties (default 0). Scoring uses at most the first 4096 characters and 128 tokens per query/fact. Search diversifies only up to `top_k`; injection diversifies guaranteed and regular facts independently until their token budgets are reached. Leave the feature disabled to retain the existing retrieval and injection behavior.
 
 Lexical relevance measures IDF-weighted coverage of distinct query terms, so
@@ -3729,7 +3775,12 @@

 
 `DeerFlowClient.stream()` includes `summary_text` in each `values` event. This is the current compacted context summary, or `None` when absent. Consumers can record changes without reading checkpoint internals; repeated snapshots may carry the same summary, and an initial snapshot may already contain one from an earlier turn.
 
-DeerFlow can be used as an embedded Python library without running the full HTTP services. The `DeerFlowClient` provides direct in-process access to all agent and Gateway capabilities, returning the same response schemas as the HTTP Gateway API. The HTTP Gateway also exposes `DELETE /api/threads/{thread_id}` to remove DeerFlow-managed local thread data after the LangGraph thread itself has been deleted:
+DeerFlow can be used as an embedded Python library without running the full HTTP services. The `DeerFlowClient` provides direct in-process access to all agent and Gateway capabilities, returning the same response schemas as the HTTP Gateway API.
+
+The HTTP Gateway exposes `DELETE /api/threads/{thread_id}` to remove a thread's
+files, checkpoints, and metadata. If checkpoint deletion fails, the Gateway
+returns 500 and retains the owner record for retry.
+[Thread cleanup API](backend/docs/API.md#thread-cleanup)
 
 An embedded `DeerFlowClient(config_path="custom/config.yaml")` keeps the process
 config singleton on that file, even after a working-directory change. Later edits
```

</details>
