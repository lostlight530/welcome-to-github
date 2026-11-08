# bytedance/deer-flow · CHANGELOG.md

> 当前有效引用快照. 完整原文由固定 Git Blob 保存, 当前活动输入不重复内联.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) |
| 来源文件 | [CHANGELOG.md](https://github.com/bytedance/deer-flow/blob/2a16b26960cb953cd3283702d018bd7dce6b80b7/CHANGELOG.md) |
| 来源版本 | `2a16b26960cb953cd3283702d018bd7dce6b80b7` |
| 来源目录 Tree | `e095fed0e99021fea9aa911c1413b6fe3109fcc4` |
| 来源内容 Blob | `d3d0fb0c74f828484c9576c70991248b304c512d` |
| 摄取时间 | `2026-11-06T16:28:09.656480+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_bytedance_deer_flow_changelog_md` |
| 快照模式 | `PINNED_EXTERNAL_REFERENCE` |
| 规范内容 SHA256 | `ba6a45c1ec9740128e5173566e1d3b17ea4a508779ad941ed1963b296666d4c2` |
| 原文字节数 | `1025490` |
| 原文行数 | `16058` |

## 本次变化

- 新增行数 `23`.
- 删除行数 `2`.
- 完整 Diff 字节数 `2423`.
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

- [按固定源提交读取完整原文](https://github.com/bytedance/deer-flow/blob/2a16b26960cb953cd3283702d018bd7dce6b80b7/CHANGELOG.md).
- 原文由来源 Blob SHA 与规范内容 SHA256 共同识别.
- 被替换的完整活动快照先原样封存到只追加 Archive.
- Diff 过长时只展示有界预览, 预览不代表完整差异.

<details>
<summary>展开有界版本差异</summary>

```diff
--- previous

+++ d3d0fb0c74f828484c9576c70991248b304c512d

@@ -24,11 +24,30 @@

 
 ### Fixed
 
+- **channels:** WeCom group messages now have their own conversation. Every
+  message used the sender's userid as both chat and topic ID, so a member's
+  private chat and every group they wrote in shared one DeerFlow thread
+  wherever no group binding kept them apart: in auth-disabled mode, with
+  `require_bound_identity: false`, and under legacy group bindings. A group
+  reply could then draw on the member's private chat or another group, and a
+  reply sent without its frame went to the private chat. Groups are now keyed
+  by `chatid` with one thread per member, and private chats keep their
+  threads. A group bound with its own `/connect` keeps its thread; a legacy
+  group binding, which covers every group of the bot, starts a new one in
+  each group. ([#7794])
+  
 - **sandbox:** Fresh lazy AIO runs with an explicit authorized skill view no
   longer create or acquire a sandbox before the first sandbox-backed tool
   call. Existing sandbox bindings and providers that require skill uploads
   retain their eager synchronization behavior. ([#7782])
-  
+
+- **parsing:** Follow-up suggestions and the `/goal` evaluator keep a literal
+  `<think>` tag that appears inside a JSON string value, such as an answer
+  quoting the tag, while reasoning around the JSON is still removed. An
+  unclosed literal tag inside a string no longer truncates the document and
+  fails parsing, and reasoning outside the payload still strips and truncates
+  as before. ([#7907])
+
 - **gateway:** A caller-supplied thread ID that is a Windows reserved device
   name (`NUL`, `CON`, `COM1`, ...) is now rejected at the shared
   `validate_thread_id()` boundary. Such IDs previously passed validation but
@@ -16031,7 +16050,9 @@

 [#7762]: https://github.com/bytedance/deer-flow/pull/7762
 [#7772]: https://github.com/bytedance/deer-flow/pull/7772
 [#7781]: https://github.com/bytedance/deer-flow/pull/7781
+[#7782]: https://github.com/bytedance/deer-flow/pull/7782
 [#7792]: https://github.com/bytedance/deer-flow/pull/7792
+[#7794]: https://github.com/bytedance/deer-flow/pull/7794
 [#7831]: https://github.com/bytedance/deer-flow/pull/7831
-[#7782]: https://github.com/bytedance/deer-flow/pull/7782
 [#7892]: https://github.com/bytedance/deer-flow/pull/7892
+[#7907]: https://github.com/bytedance/deer-flow/pull/7907
```

</details>
