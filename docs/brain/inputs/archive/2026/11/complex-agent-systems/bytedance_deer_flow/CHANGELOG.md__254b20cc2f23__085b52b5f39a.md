# bytedance/deer-flow · CHANGELOG.md

> 当前有效引用快照. 完整原文由固定 Git Blob 保存, 当前活动输入不重复内联.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) |
| 来源文件 | [CHANGELOG.md](https://github.com/bytedance/deer-flow/blob/085b52b5f39a2dc6ca23f207584763bc17d3950b/CHANGELOG.md) |
| 来源版本 | `085b52b5f39a2dc6ca23f207584763bc17d3950b` |
| 来源目录 Tree | `cbe5a15f848d5b83711e2076917c1ae1076ca6d4` |
| 来源内容 Blob | `254b20cc2f237125a0045ffdc41e779a9fb9d64e` |
| 摄取时间 | `2026-11-15T01:31:33.527280+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_bytedance_deer_flow_changelog_md` |
| 快照模式 | `PINNED_EXTERNAL_REFERENCE` |
| 规范内容 SHA256 | `645bf67bf55420d13659944238dad0b70731efc534578b572b8e2434a3470f9e` |
| 原文字节数 | `1049462` |
| 原文行数 | `16445` |

## 本次变化

- 新增行数 `116`.
- 删除行数 `0`.
- 完整 Diff 字节数 `11191`.
- 来源变化不等于本仓执行验证或独立研究次数.

## 阅读导航

- Changelog
- [Unreleased]
- Added
- Changed
- Fixed
- [2.2.0] — 2026-10-29
- Added
- Scheduler
- Agents & runtime
- Memory
- Knowledge & retrieval
- Skills
- Models & integrations
- Channels
- Auth & guardrails
- Extensions & plugins
- Persistence
- Frontend
- Changed
- Fixed
- Security
- Documentation
- Internal
- [2.1.0] — 2026-09-24

## 原文完整性与取回

- [按固定源提交读取完整原文](https://github.com/bytedance/deer-flow/blob/085b52b5f39a2dc6ca23f207584763bc17d3950b/CHANGELOG.md).
- 原文由来源 Blob SHA 与规范内容 SHA256 共同识别.
- 被替换的完整活动快照先原样封存到只追加 Archive.
- Diff 过长时只展示有界预览, 预览不代表完整差异.

<details>
<summary>展开有界版本差异</summary>

```diff
--- previous

+++ 254b20cc2f237125a0045ffdc41e779a9fb9d64e

@@ -58,7 +58,56 @@

   connect an ordinary StepFun API account with an API key and model ID.
   ([#7988](https://github.com/bytedance/deer-flow/pull/7988))
 
+### Changed
+
+- **checkpoint:** DeltaChannel deployments now require `langgraph-checkpoint`
+  4.3.0, SQLite saver 3.1.2, and Postgres saver 3.1.3, excluding versions that
+  could reorder parallel writes during replay or lose paged ancestor history.
+  The ordering and Postgres pagination contracts now fail on regression instead
+  of skipping. ([#8139])
+
 ### Fixed
+
+- **frontend:** Cron presets in the task form now require minute 0-59, hour
+  0-23 and day of month 1-31, so an out-of-range expression such as
+  `0 24 * * *` stays a custom schedule and keeps its original text. Previously,
+  it was parsed as a preset and could be clamped to a different time when
+  serialized for submission. Creating or duplicating a task with an invalid
+  expression, or updating its schedule configuration while the expression is
+  invalid, returns the Gateway's `422`; edits to other fields do not revalidate
+  an unchanged schedule. ([#8020])
+
+- **gateway:** Creating a thread with checkpoint-owned keys such as `step`,
+  `parents` or `counters_since_delta_snapshot` in its metadata no longer
+  leaves the thread broken. Those keys used to land on the thread's first
+  checkpoint, so a bad `parents` made the thread's history fail with 500 for
+  good, and a bad `step` or delta counter made every later turn fail. A
+  `deerflow_agent_name` key was also copied into the next state update as if
+  the server had set it. The first checkpoint now takes none of these keys
+  from the request. ([#8019])
+  
+- **mcp:** Two enabled MCP servers could bind the same tool name (server `a`
+  exposing `b_x` and server `a_b` exposing `x` both bind `a_b_x`). Both
+  declarations reached the model and the provider silently kept only one.
+  Duplicate bound names are now dropped with a warning naming the surviving
+  server, in enabled-server declaration order. Note the surviving server is
+  stable only while its discovery keeps succeeding: if the winner's discovery
+  fails transiently, the later duplicate becomes served again, so the
+  implementation behind a bound name can alternate across cache generations
+  with server health.
+  ([#8135](https://github.com/bytedance/deer-flow/pull/8135))
+  
+- **channels:** WeCom no longer drops images between 2 MB and 10 MB. The
+  adapter capped image uploads at 2 MB — the voice limit in the same protocol —
+  so a larger chart was skipped before upload and the turn arrived without it.
+  The cap now matches the platform's 10 MB for images; the 20 MB file limit is
+  unchanged. ([#8174])
+
+- **threads:** Deleting a conversation on Windows no longer fails with
+  `Failed to delete local thread data.` when the workspace holds a file whose
+  path exceeds `MAX_PATH`. The thread directory is now resolved through the
+  Windows extended-length namespace before removal.
+  ([#8144](https://github.com/bytedance/deer-flow/pull/8144))
 
 - **channels:** A WeCom group command that follows the bot mention now runs as a
   command. WeCom keeps the mention inside the message text (`@RobotA /new`), and
@@ -67,6 +116,14 @@

   only; ordinary chat keeps them and `/connect` is unchanged. Mirrors the Feishu
   and DingTalk handling. ([#8118])
   
+- **subagents:** Apply tool allowlists and denylists to middleware-declared
+  tools even when global authorization is disabled, including the default
+  denial of `task`. Restricted subagents reject non-Sequence declarations
+  explicitly, and invalid declarations report middleware-specific configuration
+  guidance. Final graph assembly checks both explicit and middleware tools;
+  framework-generated discovery helpers retain their filtered catalogs.
+  ([#8136](https://github.com/bytedance/deer-flow/pull/8136))
+
 - **frontend:** **Share** in a sidebar chat's menu now copies a link to the
   deployment you are using. On `localhost` and `127.0.0.1`, the default
   `make dev` and Docker addresses, it copied a link to the hosted demo
@@ -84,6 +141,12 @@

   active run (`RunStore.merge_owned_metadata()`); otherwise the worker stops
   the run before executing it. Custom `RunStore` implementations used with
   heartbeats must implement that method. ([#8046])
+
+- **subagents:** Concurrent creates for the same managed-subagent name in shared
+  file storage now preserve the winning definition and return HTTP 409 to the
+  losing request instead of reporting two successes and overwriting one definition.
+  Gateway startup also probes hard-link support and warns if the storage volume
+  cannot support managed subagent creation. ([#8132](https://github.com/bytedance/deer-flow/pull/8132))
 
 - **agents:** A high-risk tool call without a usable id no longer wedges the
   thread when `hitl_approval` is enabled. A provider that omits a tool-call id
@@ -149,6 +212,11 @@

   mirrors `ThreadOwnershipConflictError`; a duplicate key with no surviving row
   is still surfaced as a 500. ([#8057])
 
+- **models:** Cancelling a Codex-backed run now closes its upstream HTTP/SSE
+  connection, including while waiting for response headers, and retry waits
+  are cancellable. Local resources are released; the remote service may still
+  continue generation. ([#8053](https://github.com/bytedance/deer-flow/pull/8053))
+
 - **middleware:** With PII redaction enabled, a long run of text without
   spaces (such as a pasted hex dump) no longer stalls the Gateway. The email
   detector was quadratic in the length of such a run, and redaction re-scans
@@ -178,6 +246,14 @@

   future per-record raise costs one tick instead of every other claimed task.
   ([#7998])
 
+- **scheduler:** Exceptions escaping the queue-timeout sweep or the
+  queued-occurrence drain are now contained to that occurrence. The
+  scheduler logs the failed row and continues with the remaining queue
+  and the tasks claimed in the same poll. Expired rows are excluded before
+  owner ranking and the batch limit, and a launch claim enforces the same
+  cutoff, so a row left queued by a failed sweep neither starts nor crowds
+  healthy work out of the queue while timeout recovery retries it. ([#7998])
+
 - **scheduler:** One scheduled task whose saved schedule can no longer be
   computed no longer stops every other task. When a stored timezone or cron
   expression stopped working (a zone missing from the time zone database
@@ -187,6 +263,16 @@

   is now paused with the reason as its last error, and resuming it reports
   the problem until the schedule is fixed. ([#7993])
   
+- **models:** A Claude model using a Claude Code OAuth token no longer fails
+  every request once the request carries `betas`. The OAuth betas
+  (`oauth-2025-04-20`, …) were only the client's default `anthropic-beta`
+  header, and the SDK sends a request's `betas` as that header instead, so a
+  configured `betas` list (even `[]`), per-call `betas`, or a server tool for
+  which langchain-anthropic adds a beta left them out and Anthropic rejected
+  the token. The OAuth betas now lead any request `betas` and any
+  `anthropic-beta` in `extra_headers`.
+  ([#8061](https://github.com/bytedance/deer-flow/pull/8061))
+
 - **community:** A search or fetch API key that ends in a newline no longer
   leaks into the conversation. GroundRoute (`GROUNDROUTE_API_KEY`), InfoQuest,
   Tavily, Exa, Jina, Firecrawl, fastCRW and Crawl4AI put the key into an HTTP
@@ -257,6 +343,9 @@

   group binding, which covers every group of the bot, starts a new one in
   each group. ([#7794])
   
+- **memory:** DeerMem rejects backups with duplicate fact IDs before replacing
+  saved memory, regardless of entry order. ([#8151])
+
 - **memory:** Importing a backup without a `facts` array now returns HTTP 422
   and preserves saved memory. An explicit empty array still clears the selected
   fact bucket. ([#8131])
@@ -332,6 +421,13 @@

   there. Retrying in a completed, failed, running or paused batch is
   unchanged. ([#7792])
 
+- **gateway:** A run that names a missing or invalid custom agent now says so.
+  Messaging a chat whose custom agent was deleted, or passing a malformed
+  `agent_name`, returned the 422 detail "knowledge_scope assistant configuration
+  could not be resolved" even when no knowledge scope was involved. The 422 now
+  reports `Agent '<name>' not found`, an invalid `agent_name`, or an agent
+  config that could not be loaded. ([#8087])
+
 - **agents:** `PUT /api/agents/{name}` with `"description": null` now resets the
   description to empty. It used to store the null, which the agent config
   rejects, so the agent then failed every load: the update, GET and repair
@@ -382,6 +478,19 @@

   `config.yaml`, then `extensions_config.json` — so a config edit landing just
   before a thread view stalled the Gateway event loop that runs, streams and
   every other thread share. The response is unchanged. ([#7727])
+
+- **community:** The shared SSRF guard now returns its documented `Error: ...`
+  rejection for malformed URLs instead of raising `ValueError`.
+  `validate_public_http_url` and `validate_delegated_backend_url` called
+  `urlparse()` unguarded, so an authority it rejects, such as the unmatched
+  IPv6 bracket in `http://[::1/api`, escaped to the caller. That surfaced as an
+  unhandled 500 from the personal MCP router and as generic exception text in
+  the crawl4ai and fastCRW `web_fetch` tools. Both validators now reject any
+  malformed authority before the scheme check and the private-address escape
+  hatches, including a raw bracket in userinfo, which RFC 3986 forbids and
+  Python versions disagree on. This is a fail-closed contract fix plus
+  version-drift hardening: no host reachable through a well-formed URL becomes
+  blocked. ([#8079])
 
 ## [2.2.0] — 2026-10-29
 
@@ -16316,6 +16425,8 @@

 [#7993]: https://github.com/bytedance/deer-flow/pull/7993
 [#7998]: https://github.com/bytedance/deer-flow/issues/7998
 [#8006]: https://github.com/bytedance/deer-flow/pull/8006
+[#8019]: https://github.com/bytedance/deer-flow/pull/8019
+[#8020]: https://github.com/bytedance/deer-flow/pull/8020
 [#8043]: https://github.com/bytedance/deer-flow/pull/8043
 [#8046]: https://github.com/bytedance/deer-flow/pull/8046
 [#8057]: https://github.com/bytedance/deer-flow/pull/8057
@@ -16323,7 +16434,12 @@

 [#8069]: https://github.com/bytedance/deer-flow/issues/8069
 [#8071]: https://github.com/bytedance/deer-flow/issues/8071
 [#8072]: https://github.com/bytedance/deer-flow/pull/8072
+[#8079]: https://github.com/bytedance/deer-flow/pull/8079
+[#8087]: https://github.com/bytedance/deer-flow/pull/8087
 [#8117]: https://github.com/bytedance/deer-flow/pull/8117
 [#8118]: https://github.com/bytedance/deer-flow/pull/8118
 [#8126]: https://github.com/bytedance/deer-flow/pull/8126
 [#8131]: https://github.com/bytedance/deer-flow/pull/8131
+[#8139]: https://github.com/bytedance/deer-flow/pull/8139
+[#8151]: https://github.com/bytedance/deer-flow/pull/8151
+[#8174]: https://github.com/bytedance/deer-flow/pull/8174
```

</details>
