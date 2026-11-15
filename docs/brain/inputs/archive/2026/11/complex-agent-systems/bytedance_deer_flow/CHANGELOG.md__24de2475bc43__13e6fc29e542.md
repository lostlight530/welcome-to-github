# bytedance/deer-flow · CHANGELOG.md

> 当前有效引用快照. 完整原文由固定 Git Blob 保存, 当前活动输入不重复内联.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) |
| 来源文件 | [CHANGELOG.md](https://github.com/bytedance/deer-flow/blob/13e6fc29e54201ce650b5f48743f88444b4d46f5/CHANGELOG.md) |
| 来源版本 | `13e6fc29e54201ce650b5f48743f88444b4d46f5` |
| 来源目录 Tree | `cdc73cc1bc7cc4b03ba4c38416654fe3890223c4` |
| 来源内容 Blob | `24de2475bc43b0b8a1311cddfa3b86c4872f8c39` |
| 摄取时间 | `2026-11-12T02:43:52.700456+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_bytedance_deer_flow_changelog_md` |
| 快照模式 | `PINNED_EXTERNAL_REFERENCE` |
| 规范内容 SHA256 | `3c1a985fa26158f7f4546c9ec340d38f3478250c614ece1e26608c058b91c748` |
| 原文字节数 | `1042408` |
| 原文行数 | `16329` |

## 本次变化

- 新增行数 `48`.
- 删除行数 `10`.
- 完整 Diff 字节数 `5287`.
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

- [按固定源提交读取完整原文](https://github.com/bytedance/deer-flow/blob/13e6fc29e54201ce650b5f48743f88444b4d46f5/CHANGELOG.md).
- 原文由来源 Blob SHA 与规范内容 SHA256 共同识别.
- 被替换的完整活动快照先原样封存到只追加 Archive.
- Diff 过长时只展示有界预览, 预览不代表完整差异.

<details>
<summary>展开有界版本差异</summary>

```diff
--- previous

+++ 24de2475bc43b0b8a1311cddfa3b86c4872f8c39

@@ -11,16 +11,29 @@

 ([2.3.0](https://github.com/bytedance/deer-flow/milestone/4)).
 
 ### Added
-- **hitl:** Optional human-in-the-loop approval for high-risk tool calls.
-  `hitl_approval.tools` (host-owned) pauses matching calls via LangGraph
-  `interrupt()`; the run enters `waiting_for_input` and the Web UI shows an
-  approval card with per-field argument summaries. Approve executes the call,
-  reject returns the reason to the model without executing. IM channels,
-  GitHub runs, and scheduled tasks follow `hitl_approval.non_interactive`
-  (`deny` by default, `allow` opt-in). Subagents and runtimes without resume
-  support always reject matching calls regardless of that setting.
-  `hitl_approval.max_actions` configures the approval-batch count limit
-  (default 32; 0 disables it). HITL is disabled by default; `config_version` 65.
+- **summarization:** The built-in compaction prompt guides the summarizer to
+  preserve active user requirements, literal approval phrases, action conditions,
+  and explicit revisions. Explicit `summarization.summary_prompt` configurations
+  continue to take precedence. ([#8114](https://github.com/bytedance/deer-flow/pull/8114))
+
+- **sandbox:** Short ranged `read_file` calls on uploaded and workspace files
+  display source line numbers when the result contains 1–40 lines and the
+  labeled view fits the output budget. ([#8109](https://github.com/bytedance/deer-flow/pull/8109))
+
+- **projects:** Owner-scoped project memory with automatic-extraction, delete and
+  move-to-instructions controls. Project facts share DeerMem's extraction call
+  while remaining isolated from user facts. New shelf documents receive
+  best-effort summaries by default. ([#8117])
+
+- **hitl:** Optional Ask, Auto and Full tool-permission modes, independent of
+  reasoning mode. Auto uses a separate tool-free review call with an existing
+  model profile; uncertain or high-risk operations require a human. Cards show
+  complete arguments and support approve, reject, edit and exact-operation chat
+  grants with revocation. Root approvals survive restart through checkpoints;
+  interactive subagents wait through an owner-scoped channel with cancellation
+  and expiry. Mandatory deployment rules and account permissions apply in every
+  mode. Personal/platform MCP connections, policy and arguments bind approvals.
+  Disabled by default; see the configuration guide. `config_version` 66.
 
 - **knowledge:** The WeKnora retrieval extension offers opt-in shared read-only
   access for authenticated users, without maintaining a per-user allowlist.
@@ -46,6 +59,20 @@

   ([#7988](https://github.com/bytedance/deer-flow/pull/7988))
 
 ### Fixed
+
+- **channels:** A WeCom group command that follows the bot mention now runs as a
+  command. WeCom keeps the mention inside the message text (`@RobotA /new`), and
+  the classifier required a bare leading `/`, so `/new` and `/status` sent in a
+  group became chat turns. Leading mentions are skipped for the command lookup
+  only; ordinary chat keeps them and `/connect` is unchanged. Mirrors the Feishu
+  and DingTalk handling. ([#8118])
+  
+- **frontend:** **Share** in a sidebar chat's menu now copies a link to the
+  deployment you are using. On `localhost` and `127.0.0.1`, the default
+  `make dev` and Docker addresses, it copied a link to the hosted demo
+  (`deer-flow-v2.vercel.app`) instead. That link never opened the
+  conversation, and opening it sent the thread id to an outside host.
+  ([#8126])
 
 - **runtime:** In multi-worker mode (`run_ownership.heartbeat_enabled`), a
   worker that had lost its run to a peer could put the row back. Its assembly
@@ -89,6 +116,9 @@

   database error. The 409 points callers at `PUT` on the same route, which
   updates the existing feedback. ([#8064])
   
+- **frontend:** Reopening a conversation restores successfully handed-off shared
+  artifacts in the Artifacts sidebar. ([#8080](https://github.com/bytedance/deer-flow/pull/8080))
+
 - **sandbox:** AIO commands from independent subagents now run concurrently when
   they carry per-call environment variables, including Lark CLI commands.
   Commands within one subagent remain ordered and client cleanup drains them.
@@ -227,6 +257,10 @@

   group binding, which covers every group of the bot, starts a new one in
   each group. ([#7794])
   
+- **memory:** Importing a backup without a `facts` array now returns HTTP 422
+  and preserves saved memory. An explicit empty array still clears the selected
+  fact bucket. ([#8131])
+
 - **memory:** An agent-scoped memory write whose `agent_name` is a Windows
   reserved device name (`NUL`, `CON`, `COM1`, ...) is now rejected with a `422`
   on the two routes that create that scope, `POST /memory/facts` and
@@ -16289,3 +16323,7 @@

 [#8069]: https://github.com/bytedance/deer-flow/issues/8069
 [#8071]: https://github.com/bytedance/deer-flow/issues/8071
 [#8072]: https://github.com/bytedance/deer-flow/pull/8072
+[#8117]: https://github.com/bytedance/deer-flow/pull/8117
+[#8118]: https://github.com/bytedance/deer-flow/pull/8118
+[#8126]: https://github.com/bytedance/deer-flow/pull/8126
+[#8131]: https://github.com/bytedance/deer-flow/pull/8131
```

</details>
