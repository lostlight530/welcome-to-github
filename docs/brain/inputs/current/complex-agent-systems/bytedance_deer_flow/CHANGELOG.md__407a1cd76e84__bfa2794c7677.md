# bytedance/deer-flow · CHANGELOG.md

> 当前有效引用快照. 完整原文由固定 Git Blob 保存, 当前活动输入不重复内联.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) |
| 来源文件 | [CHANGELOG.md](https://github.com/bytedance/deer-flow/blob/bfa2794c7677d22d2a8097c55ffaeb2d00979c24/CHANGELOG.md) |
| 来源版本 | `bfa2794c7677d22d2a8097c55ffaeb2d00979c24` |
| 来源目录 Tree | `c5bd0cbb6f716d5385a153632276e81661a46e25` |
| 来源内容 Blob | `407a1cd76e84181395a0ed1b4e4bff8ad91a14cf` |
| 摄取时间 | `2026-11-10T03:58:24.465737+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_bytedance_deer_flow_changelog_md` |
| 快照模式 | `PINNED_EXTERNAL_REFERENCE` |
| 规范内容 SHA256 | `fd3d71ae9a19ad82e749a3b8eb53da0a13108273f7280a1c56ae1ce60fcb5e62` |
| 原文字节数 | `1037124` |
| 原文行数 | `16243` |

## 本次变化

- 新增行数 `82`.
- 删除行数 `0`.
- 完整 Diff 字节数 `7226`.
- 来源变化不等于本仓执行验证或独立研究次数.

## 阅读导航

- Changelog
- [Unreleased]
- Added
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
- ⚠ Breaking changes

## 原文完整性与取回

- [按固定源提交读取完整原文](https://github.com/bytedance/deer-flow/blob/bfa2794c7677d22d2a8097c55ffaeb2d00979c24/CHANGELOG.md).
- 原文由来源 Blob SHA 与规范内容 SHA256 共同识别.
- 被替换的完整活动快照先原样封存到只追加 Archive.
- Diff 过长时只展示有界预览, 预览不代表完整差异.

<details>
<summary>展开有界版本差异</summary>

```diff
--- previous

+++ 407a1cd76e84181395a0ed1b4e4bff8ad91a14cf

@@ -11,6 +11,25 @@

 ([2.3.0](https://github.com/bytedance/deer-flow/milestone/4)).
 
 ### Added
+- **hitl:** Optional human-in-the-loop approval for high-risk tool calls.
+  `hitl_approval.tools` (host-owned) pauses matching calls via LangGraph
+  `interrupt()`; the run enters `waiting_for_input` and the Web UI shows an
+  approval card with per-field argument summaries. Approve executes the call,
+  reject returns the reason to the model without executing. IM channels,
+  GitHub runs, and scheduled tasks follow `hitl_approval.non_interactive`
+  (`deny` by default, `allow` opt-in). Subagents and runtimes without resume
+  support always reject matching calls regardless of that setting.
+  `hitl_approval.max_actions` configures the approval-batch count limit
+  (default 32; 0 disables it). HITL is disabled by default; `config_version` 65.
+
+- **knowledge:** The WeKnora retrieval extension offers opt-in shared read-only
+  access for authenticated users, without maintaining a per-user allowlist.
+  Exact-user allowlists remain the default; shared access requires matching
+  host-verified identity and grants no management permissions. ([#7944](https://github.com/bytedance/deer-flow/pull/7944))
+
+- **community:** New SpecStream `web_search` and `web_fetch` provider. Search returns
+  ranked results with a direct answer when the sources agree on one, and fetch
+  returns a page or document as markdown. ([#7968](https://github.com/bytedance/deer-flow/pull/7968))
 
 - **subagents:** Durable batch items can wait for explicitly named prerequisites.
   An optional, once-only lead-Agent follow-up completes a previously requested
@@ -27,6 +46,39 @@

   ([#7988](https://github.com/bytedance/deer-flow/pull/7988))
 
 ### Fixed
+
+- **gateway:** Posting feedback twice for the same run now returns a 409
+  instead of a 500. `POST /api/threads/{id}/runs/{run_id}/feedback` allows one
+  feedback row per user and run; a retry, or feedback on another message of the
+  same run, hit that unique key and the Gateway failed with an unhandled
+  database error. The 409 points callers at `PUT` on the same route, which
+  updates the existing feedback. ([#8064])
+  
+- **sandbox:** AIO commands from independent subagents now run concurrently when
+  they carry per-call environment variables, including Lark CLI commands.
+  Commands within one subagent remain ordered and client cleanup drains them.
+
+- **uploads:** Re-uploading a file whose name collides with a compound archive
+  suffix no longer inserts the dedupe counter inside the suffix. A second
+  `report.tar.gz` is now named `report_1.tar.gz` (matching `report_1.tar` and
+  `report_1.txt`), instead of `report.tar_1.gz`, so the extension stays intact
+  for file-type detection. ([#8042](https://github.com/bytedance/deer-flow/pull/8042))
+
+- **gateway:** Deleting a thread no longer reports success while its
+  conversation stays readable. When the checkpoint store failed during
+  `DELETE /api/threads/{id}`, the route logged it at DEBUG, removed the
+  thread's metadata row and returned success; any signed-in user could then
+  read the leftover title and messages through `GET /threads/{id}`, `/state`,
+  `/history` and `/goal`, and the owner could not retry. The delete now
+  returns a 500 and keeps the thread, so the owner can delete it again.
+  ([#7992])
+
+- **gateway:** Creating a thread with a caller-supplied `thread_id` that
+  already belongs to another user now returns a non-disclosing 404
+  (`Thread not found`) instead of a 500. The duplicate-key recovery path reads
+  the surviving row back bypassing the owner scope so the cross-owner case
+  mirrors `ThreadOwnershipConflictError`; a duplicate key with no surviving row
+  is still surfaced as a 500. ([#8057])
 
 - **middleware:** With PII redaction enabled, a long run of text without
   spaces (such as a pasted hex dump) no longer stalls the Gateway. The email
@@ -34,6 +86,11 @@

   every user message on every model call, so one 100 KB paste blocked every
   thread for about 6 s per model call. The scan is now linear, and it redacts
   exactly the same addresses as before. ([#8006])
+
+- **agents:** Token budgets count separate accepted model calls even when a
+  provider reuses message IDs, so repeated IDs no longer bypass the configured
+  cap. Hard stops preserve already-completed structured-output tool results.
+  ([#8050](https://github.com/bytedance/deer-flow/pull/8050))
   
 - **subagents:** Managed subagent creation now rejects Windows reserved device
   names (`CON`, `PRN`, `AUX`, `NUL`, `COM1-9`, `LPT1-9`) at the shared
@@ -41,6 +98,16 @@

   Gateway `/api/subagents` boundary before attempting filesystem writes,
   preventing `OSError` failures on Windows hosts while keeping existing
   read and delete operations permissive.
+
+- **scheduler:** A stored `schedule_spec` that is JSON null, a list or a string
+  no longer aborts the scheduler poll. `stored_next_run_at` caught the value
+  errors from a dropped zone or a newer cron parser, but a non-object spec
+  fails on `.get`; the launch-failure handler recomputed it again, so the
+  `AttributeError` escaped `run_once`'s claimed-task loop. Such a task is now
+  paused with the reason, like the other unusable schedules. The poll loop also
+  isolates one task's dispatch failure from the rest of its claimed batch, so a
+  future per-record raise costs one tick instead of every other claimed task.
+  ([#7998])
 
 - **scheduler:** One scheduled task whose saved schedule can no longer be
   computed no longer stops every other task. When a stored timezone or cron
@@ -64,6 +131,15 @@

   Firecrawl SDK send `FIRECRAWL_API_KEY` to the fastCRW endpoint, and a blank
   `TAVILY_API_KEY`, `EXA_API_KEY` or `FIRECRAWL_API_KEY` now counts as missing
   instead of reaching the SDK as is. ([#7981])
+  
+- **community:** Browserless is the last search/fetch provider that read its
+  token raw. A `BROWSERLESS_TOKEN` or configured `token` from a file kept its
+  trailing newline and became the auth query parameter, so every `web_fetch`
+  and `web_capture` request failed authentication while the key was correct.
+  Both now go through `provider_credentials.resolve_api_key`, and only an
+  omitted `token` key falls back to the environment: an explicit `""` or
+  `null` keeps opting a self-hosted capture endpoint out of authentication.
+  ([#8043])
   
 - **docker:** Images built from a checkout no longer contain its local
   configuration. `.dockerignore` did not exclude `config.yaml`,
@@ -16157,5 +16233,11 @@

 [#7953]: https://github.com/bytedance/deer-flow/issues/7953
 [#7958]: https://github.com/bytedance/deer-flow/pull/7958
 [#7981]: https://github.com/bytedance/deer-flow/pull/7981
+[#7992]: https://github.com/bytedance/deer-flow/pull/7992
 [#7993]: https://github.com/bytedance/deer-flow/pull/7993
+[#7998]: https://github.com/bytedance/deer-flow/issues/7998
 [#8006]: https://github.com/bytedance/deer-flow/pull/8006
+[#8043]: https://github.com/bytedance/deer-flow/pull/8043
+[#8057]: https://github.com/bytedance/deer-flow/pull/8057
+[#8064]: https://github.com/bytedance/deer-flow/pull/8064
+
```

</details>
