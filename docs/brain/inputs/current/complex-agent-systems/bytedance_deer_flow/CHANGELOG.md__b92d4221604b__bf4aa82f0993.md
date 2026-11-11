# bytedance/deer-flow · CHANGELOG.md

> 当前有效引用快照. 完整原文由固定 Git Blob 保存, 当前活动输入不重复内联.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) |
| 来源文件 | [CHANGELOG.md](https://github.com/bytedance/deer-flow/blob/bf4aa82f09939ba364f43385ddefa7b3619099d7/CHANGELOG.md) |
| 来源版本 | `bf4aa82f09939ba364f43385ddefa7b3619099d7` |
| 来源目录 Tree | `b3539e9ede9777549d050ed7c9528d93454f7dab` |
| 来源内容 Blob | `b92d4221604b96348b93b9408cea3de87aaace0e` |
| 摄取时间 | `2026-11-11T01:44:07.025931+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_bytedance_deer_flow_changelog_md` |
| 快照模式 | `PINNED_EXTERNAL_REFERENCE` |
| 规范内容 SHA256 | `b6d77c493aaf1ad51db0a8653d00e37ab434d5392732e6eea74c2ba990670f90` |
| 原文字节数 | `1040178` |
| 原文行数 | `16291` |

## 本次变化

- 新增行数 `49`.
- 删除行数 `1`.
- 完整 Diff 字节数 `4534`.
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

- [按固定源提交读取完整原文](https://github.com/bytedance/deer-flow/blob/bf4aa82f09939ba364f43385ddefa7b3619099d7/CHANGELOG.md).
- 原文由来源 Blob SHA 与规范内容 SHA256 共同识别.
- 被替换的完整活动快照先原样封存到只追加 Archive.
- Diff 过长时只展示有界预览, 预览不代表完整差异.

<details>
<summary>展开有界版本差异</summary>

```diff
--- previous

+++ b92d4221604b96348b93b9408cea3de87aaace0e

@@ -47,6 +47,41 @@

 
 ### Fixed
 
+- **runtime:** In multi-worker mode (`run_ownership.heartbeat_enabled`), a
+  worker that had lost its run to a peer could put the row back. Its assembly
+  evidence write was an unconditional full-row upsert, so after a peer
+  reclaimed the run it reset the row to `running` and erased the takeover
+  error. The run could then finish as `success` after the peer had already
+  reported it failed, or be reclaimed a second time. The evidence is now merged
+  into the row's metadata only while the worker still holds a live lease on an
+  active run (`RunStore.merge_owned_metadata()`); otherwise the worker stops
+  the run before executing it. Custom `RunStore` implementations used with
+  heartbeats must implement that method. ([#8046])
+
+- **agents:** A high-risk tool call without a usable id no longer wedges the
+  thread when `hitl_approval` is enabled. A provider that omits a tool-call id
+  (`None`) or repeats one within a response made the middleware pause with an
+  approval payload the Gateway can never validate: every resume answered 422
+  and every new run stayed 409-blocked, all-reject included. An empty id was
+  technically resumable but is denied as well, since strict providers reject it
+  when the conversation is replayed. Such calls are now removed from the model
+  response with a visible rejection note instead of pausing, and deny paths no
+  longer build an invalid `ToolMessage` for a null id. A call whose id an
+  ordinary call also carries is stripped before it can be answered by result,
+  so the next request cannot advertise the id twice with two results.
+  A pause stored before
+  this change stays unresolvable; in-place recovery is tracked in [#8071].
+  ([#8069])
+
+- **runtime:** A HITL rejection, including the all-reject escape after approval is
+  disabled or the gated tools change during a pause, now reaches the thread's
+  message history under the resume run instead of existing only in checkpoint
+  state. ([#8073](https://github.com/bytedance/deer-flow/pull/8073))
+  
+- **summarization:** vLLM compaction counts reasoning tokens replayed to the
+  model when checking the trigger and estimating how much history to keep.
+  ([#8077](https://github.com/bytedance/deer-flow/pull/8077))
+
 - **gateway:** Posting feedback twice for the same run now returns a 409
   instead of a 500. `POST /api/threads/{id}/runs/{run_id}/feedback` allows one
   feedback row per user and run; a retry, or feedback on another message of the
@@ -57,6 +92,10 @@

 - **sandbox:** AIO commands from independent subagents now run concurrently when
   they carry per-call environment variables, including Lark CLI commands.
   Commands within one subagent remain ordered and client cleanup drains them.
+
+- **sandbox:** BoxLite VMs recovered at startup now run health checks, commands,
+  and cleanup on the provider's event loop, avoiding sync/async SDK mismatches
+  that made healthy recovered VMs fail their first command. ([#8072])
 
 - **uploads:** Re-uploading a file whose name collides with a compound archive
   suffix no longer inserts the dedupe counter inside the suffix. A second
@@ -159,6 +198,12 @@

   tool execution after a loop-detection, run token-budget, provider-safety, or
   model output-length stop. Todo state is preserved so users can continue in a
   later run. ([#7953])
+
+- **runtime:** A thread can accept new runs and mutations after a transient
+  database failure leaves a completed operation's reservation in place. The
+  next request for the thread on the same Gateway worker retries the release,
+  including in single-worker deployments with lease heartbeats disabled.
+  ([#8068](https://github.com/bytedance/deer-flow/pull/8068))
 
 - **channels:** Long Feishu/Lark answers are no longer lost. Card text was
   unbounded and ASCII-escaped, so an answer of about 4,400 CJK characters made
@@ -16238,6 +16283,9 @@

 [#7998]: https://github.com/bytedance/deer-flow/issues/7998
 [#8006]: https://github.com/bytedance/deer-flow/pull/8006
 [#8043]: https://github.com/bytedance/deer-flow/pull/8043
+[#8046]: https://github.com/bytedance/deer-flow/pull/8046
 [#8057]: https://github.com/bytedance/deer-flow/pull/8057
 [#8064]: https://github.com/bytedance/deer-flow/pull/8064
-
+[#8069]: https://github.com/bytedance/deer-flow/issues/8069
+[#8071]: https://github.com/bytedance/deer-flow/issues/8071
+[#8072]: https://github.com/bytedance/deer-flow/pull/8072
```

</details>
