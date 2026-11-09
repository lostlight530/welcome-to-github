# bytedance/deer-flow · README.md

> 当前有效引用快照. 完整原文由固定 Git Blob 保存, 当前活动输入不重复内联.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) |
| 来源文件 | [README.md](https://github.com/bytedance/deer-flow/blob/7d805cd1b8daf317370636388cf8828327065bf9/README.md) |
| 来源版本 | `7d805cd1b8daf317370636388cf8828327065bf9` |
| 来源目录 Tree | `cd8a122c3535f94658127e34a85a9bc76b9e0263` |
| 来源内容 Blob | `0d230173c0cddff4ef1318a3268781a95f057353` |
| 摄取时间 | `2026-11-08T01:08:16.062813+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_bytedance_deer_flow_readme_md` |
| 快照模式 | `PINNED_EXTERNAL_REFERENCE` |
| 规范内容 SHA256 | `03b1d9fee7293121d167af9b2622e82a45c88a95a6de00d6813f7a3106c9269e` |
| 原文字节数 | `384975` |
| 原文行数 | `4331` |

## 本次变化

- 新增行数 `42`.
- 删除行数 `4`.
- 完整 Diff 字节数 `12524`.
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

- [按固定源提交读取完整原文](https://github.com/bytedance/deer-flow/blob/7d805cd1b8daf317370636388cf8828327065bf9/README.md).
- 原文由来源 Blob SHA 与规范内容 SHA256 共同识别.
- 被替换的完整活动快照先原样封存到只追加 Archive.
- Diff 过长时只展示有界预览, 预览不代表完整差异.

<details>
<summary>展开有界版本差异</summary>

```diff
--- previous

+++ 0d230173c0cddff4ef1318a3268781a95f057353

@@ -254,7 +254,7 @@

 
    Brave web search preserves valid entries in mixed result lists. Malformed response containers or lists containing no usable entries return a structured format error; missing, null, or empty results keep the existing "No results found" response. Format errors also log the malformed container's path and type, or the absence of usable result objects, without including search queries, credentials, or payload values.
 
-   Several providers, including You.com, GroundRoute, Webz and InfoQuest, initialize HTTPX clients in a worker thread so synchronous TLS trust loading does not block the agent event loop; requests and session cleanup remain asynchronous.
+   Several providers, including You.com, GroundRoute, Webz, InfoQuest and Jsonify, initialize HTTPX clients in a worker thread so synchronous TLS trust loading does not block the agent event loop; requests and session cleanup remain asynchronous.
 
    GroundRoute web search and fetch contain malformed HTTP-success payloads the same way: a non-object payload, a `results` container that is not a list, or a non-empty list with no object entries returns the provider's format error, while non-object entries in an otherwise valid list are skipped in order. Missing, null, or empty results keep the existing "No results found" response.
 
@@ -710,6 +710,19 @@

 exits non-zero and prints the container status plus recent Gateway logs. The
 production image starts from its already-built environment and never resolves
 or installs Python dependencies at container startup.
+
+Images built from a checkout never contain its local configuration:
+`.dockerignore` keeps `config.yaml`, `config.yaml.bak`, `extensions_config.json`
+and `mcp_config.json` (at the root or in the legacy `backend/` location), `.env`
+and `.env*.local` files, local HTTPS keys (`frontend/*.pem`), and the credential
+files the extension manager refuses inside `backend/extensions/sources/` out of
+the build context. Compose mounts the config and passes the environment at
+runtime, so pushing or sharing an image does not publish those credentials.
+A locally built frontend image therefore no longer picks up `NEXT_PUBLIC_*`
+values from `frontend/.env.local`: `next build` inlines them into the client
+bundle, Compose's environment reaches only `next start`, and `frontend/Dockerfile`
+takes no build arguments for them. The Docker stack serves the frontend and
+Gateway from one nginx origin and needs none of them.
 
 If `make up` reports an unwritable runtime home or an unreadable persisted secret
 after `make docker-start`, run the printed `sudo chown -R <uid>:<gid> '<home>'`
@@ -1106,8 +1119,14 @@

 that no port is available instead of attempting an out-of-range bind.
 In open network mode, a missing Docker/Apple Container CLI or a permission-denied
 CLI startup returns the reserved port while reporting the original error, so
-repeated attempts do not exhaust the port range. Restricted network mode
-retains its existing cleanup rules because a proxy may already hold the port.
+repeated attempts do not exhaust the port range. Restricted network creation
+returns its reservation when no proxy could have been created or after confirming
+that the proxy has been removed, including when later network cleanup fails.
+An uncertain proxy keeps its reservation in the existing local cleanup ledger.
+Later creation attempts do not automatically reclaim it. The reservation remains
+until the existing ownership-fenced absent teardown completes or the backend
+process restarts. This bookkeeping does not provide durable recovery across
+backend instances.
 
 AIO teardown failures retain a generation-bound cleanup record. Partial shutdown
 reports failure and can be retried; retries verify the runtime identity and absence
@@ -1498,7 +1517,7 @@

 2. Add permissions: `im:message`, `im:message.p2p_msg:readonly`, `im:resource`.
 3. Under **Events**, subscribe to `im.message.receive_v1` and select **Long Connection** mode.
 4. Copy the App ID and App Secret. Set `FEISHU_APP_ID` and `FEISHU_APP_SECRET` in `.env` and enable the channel in `config.yaml`.
-5. The bot supports inbound text, image, and file messages. Inbound attachment downloads are limited to 20 MB per attachment.
+5. The bot supports inbound text, image, and file messages. Inbound attachment downloads are limited to 20 MB per attachment. A reply longer than one card (about 8,000 CJK characters) continues in further cards, up to 10 per answer.
 6. _(Optional)_ Interactive clarification cards: set `card_interaction_enabled: true` under `channels.feishu` to let the agent's option-based clarifications render as clickable button cards, preserving any background context before the question. Then, in the developer console, open **Callback Configuration** (回调配置 — a separate tab from **Event Subscriptions**), subscribe to `card.action.trigger` in **Long Connection** mode, and publish a new app version. A click resolves the clarification exactly like typing the choice; only the user who triggered the clarification can operate its card. Button answers are saved in the conversation history, and subsequent clarifications continue in the same thread.
 
 If the SDK repeatedly logs `CERTIFICATE_VERIFY_FAILED`, see [Feishu / Lark TLS troubleshooting](backend/docs/IM_CHANNEL_CONNECTIONS.md#feishu--lark-tls-troubleshooting) to check the Gateway's CA trust configuration.
@@ -1823,6 +1842,9 @@

 URLs remain absent; sources without a URL are readable as local evidence.
 Inline citations remain readable after Markdown sanitization, and supplied page
 numbers use the selected interface language.
+Shared knowledge results skip entries that exceed the remaining output budget
+and retain later fitting entries in provider order. Retained citations stay
+paired with their visible evidence.
 Copying a source reference produces a Markdown link that escapes brackets in the
 visible title and wraps a URL containing parentheses in angle brackets, so the
 copied reference stays a valid link. New providers use the shared
@@ -1876,6 +1898,11 @@

 Skills are what make DeerFlow do *almost anything*.
 
 A standard Agent Skill is a structured capability module — a Markdown file that defines a workflow, best practices, and references to supporting resources. DeerFlow ships with built-in skills for research, report generation, slide creation, web pages, image and video generation, and more. But the real power is extensibility: add your own skills, replace the built-in ones, or combine them into compound workflows.
+
+For MiniMax, the [video-generation skill](skills/public/video-generation/SKILL.md)
+accepts `MINIMAX_VIDEO_RESOLUTION` and `MINIMAX_VIDEO_DURATION` (integer seconds).
+Unset overrides use the provider defaults. Invalid duration strings fail before
+the script submits a request.
 
 The video-generation skill derives reference-image MIME metadata from `.png`,
 `.jpg`, `.jpeg`, `.webp`, and `.gif` filename extensions (case-insensitive). A
@@ -2714,6 +2741,10 @@

 In planning mode, if the original `write_todos` call is no longer visible,
 DeerFlow adds a reminder using the latest task statuses before the next model
 call. Skipped or failed compaction leaves the existing messages unchanged.
+When loop detection, the run token budget, or a provider safety/output-length
+limit stops a run, unfinished todos are retained for a later user run; todo
+completion reminders do not restart model calls or tool execution after that stop.
+Safety-stopped partial text is preserved; it does not trigger a Todo retry.
 
 Optional `pii_redaction.enabled` redacts detected identifiers in user messages,
 remote tool results, compaction input, reinjected summaries, configured
@@ -2944,6 +2975,11 @@

 for authorization, cancellation, recovery and result semantics.
 
 Ordinary `task` delegation and explicit durable `batch_task` execution share the startup-scoped `subagent_runtime` process capacity. Batch mode keeps large independent item sets in SQL with separate total, live, and running limits, restart recovery, bounded results, and a thread-scoped Web UI panel. The panel pages through bounded previews on demand and opens a selected item’s stored report and captured evidence for review. Citations open the matching saved excerpt without contacting the provider, and an open result refreshes until the item finishes and when the item list observes a later retry. Closed result dialogs do not fetch full details. Bulk stored results remain available through the owner-scoped JSONL export, while internal execution and authorization context never enters owner-facing responses. If the batch worker is later stopped or disabled, threads with persisted batches retain read-only item inspection and JSONL export; execution controls remain disabled until the worker is running again. See `config.example.yaml` and [the implementation contract](docs/plans/2026-08-24-subagent-batch-capacity-implementation.md) for limits and recovery semantics.
+
+Queued requests finish removing their queue entry and returning any transferred
+slot before cancellation propagates. The cleanup waits for the capacity lock
+without its own deadline. Cancellation during timeout cleanup takes precedence
+over the queue timeout.
 
 While durable batch tools are available, a later owner turn can explicitly inspect selected results with `read_batch_result(batch_id, position=0, offset=0, max_chars=4000)`. The reader is restricted to the current user and thread, including in explicitly bound SDK graphs. It returns one window of a JSON document containing the stored report, execution/error state and separate acceptance criteria/verdict, without starting or waiting for work. Concatenate `content` windows before parsing: pass `next_offset` and the returned `revision` as `expected_revision` until `next_offset` is null. A changed item returns `restart_required`; discard prior windows and start at zero. Use `next_position` for a selected next item within `batch_status.total_items`. The maximum window is 8,192 characters; metadata shares the window budget, and JSON response framing adds overhead. `result_truncated` means storage already capped the report; continuation cannot recover discarded content. A succeeded item is not an accepted task, and unchecked criteria remain UNVERIFIED. No automatic result ingestion, waiting loop or UI change is added.
 
@@ -3230,6 +3266,8 @@

 recording the others. A concurrent scratch-file removal therefore does not
 discard the whole snapshot or suppress detection of other produced outputs.
 This remains a best-effort scan, not an atomic filesystem snapshot.
+
+`present_shared_artifact` publishes another conversation's persisted output using `origin_thread_id + path + sha256`. Same-user, runtime-home-confined reads and writes reject path traversal, symlinks and changed content; an existing destination with different content is retained, while identical concurrent handoffs succeed. Successful handoffs count as run delivery and archive receipts. The current POSIX implementation does not acquire a source sandbox or cross user boundaries.
 
 Files presented through `present_files` remain part of the thread's artifact state, and the Web UI restores the artifact panel and selected document after a page refresh. Long artifact lists scroll within the panel on desktop and in the mobile drawer, keeping every file reachable. When a completed response successfully presents between 2 and 50 files, its final file card also offers one ZIP download. Archive membership comes from the terminal delivery receipt rather than browser-supplied paths, and the ZIP contains the current file versions, which may have changed since the response. The currently selected formal artifact is refreshed once when the run finishes so edits become visible without a manual reload. Existing UTF-8 text artifacts under `/mnt/user-data/outputs` can also be edited and explicitly saved from the panel on Unix and Windows while the thread is idle; saves use content revisions to prevent overwriting agent changes. A delayed background read cannot replace a successfully saved revision in the editor; cancelled preview and full-file reads also abort their HTTP requests. Source previews also recognize extensionless `Dockerfile` and `Makefile` artifacts by their file names. Unknown file types, including names such as `constructor` and `__proto__`, retain the download fallback.
```

</details>
