# bytedance/deer-flow · CHANGELOG.md

> 当前有效引用快照. 完整原文由固定 Git Blob 保存, 当前活动输入不重复内联.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) |
| 来源文件 | [CHANGELOG.md](https://github.com/bytedance/deer-flow/blob/3b05ab7dc3a7dc6df00601ab348b6ed691ff273b/CHANGELOG.md) |
| 来源版本 | `3b05ab7dc3a7dc6df00601ab348b6ed691ff273b` |
| 来源目录 Tree | `a02807088d53022c1905de7b01173463a6373ee5` |
| 来源内容 Blob | `f61c5cd609182dd661e0a0a1ede86635d83f845a` |
| 摄取时间 | `2026-11-09T01:28:45.485536+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_bytedance_deer_flow_changelog_md` |
| 快照模式 | `PINNED_EXTERNAL_REFERENCE` |
| 规范内容 SHA256 | `ac0d5250c115e8f5c9fb28d48e9160d2430e6039b71d9d8b38d989e6be3b7169` |
| 原文字节数 | `1031989` |
| 原文行数 | `16161` |

## 本次变化

- 新增行数 `42`.
- 删除行数 `0`.
- 完整 Diff 字节数 `3848`.
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

- [按固定源提交读取完整原文](https://github.com/bytedance/deer-flow/blob/3b05ab7dc3a7dc6df00601ab348b6ed691ff273b/CHANGELOG.md).
- 原文由来源 Blob SHA 与规范内容 SHA256 共同识别.
- 被替换的完整活动快照先原样封存到只追加 Archive.
- Diff 过长时只展示有界预览, 预览不代表完整差异.

<details>
<summary>展开有界版本差异</summary>

```diff
--- previous

+++ f61c5cd609182dd661e0a0a1ede86635d83f845a

@@ -22,8 +22,35 @@

   native subagents pause and resume. Unconfirmed messages can be retried
   after a Gateway restart. ([#7729])
 
+- **models:** Administrators can select StepFun in **Settings → Models** and
+  connect an ordinary StepFun API account with an API key and model ID.
+  ([#7988](https://github.com/bytedance/deer-flow/pull/7988))
+
 ### Fixed
 
+- **middleware:** With PII redaction enabled, a long run of text without
+  spaces (such as a pasted hex dump) no longer stalls the Gateway. The email
+  detector was quadratic in the length of such a run, and redaction re-scans
+  every user message on every model call, so one 100 KB paste blocked every
+  thread for about 6 s per model call. The scan is now linear, and it redacts
+  exactly the same addresses as before. ([#8006])
+  
+- **subagents:** Managed subagent creation now rejects Windows reserved device
+  names (`CON`, `PRN`, `AUX`, `NUL`, `COM1-9`, `LPT1-9`) at the shared
+  `normalize_managed_subagent_name(..., for_creation=True)` validator and
+  Gateway `/api/subagents` boundary before attempting filesystem writes,
+  preventing `OSError` failures on Windows hosts while keeping existing
+  read and delete operations permissive.
+
+- **scheduler:** One scheduled task whose saved schedule can no longer be
+  computed no longer stops every other task. When a stored timezone or cron
+  expression stopped working (a zone missing from the time zone database
+  after an upgrade, a cron expression a newer croniter rejects), recomputing
+  its next run raised inside the scheduler poll; once its launch lease
+  expired, every later poll failed before admitting any due task. That task
+  is now paused with the reason as its last error, and resuming it reports
+  the problem until the schedule is fixed. ([#7993])
+  
 - **community:** A search or fetch API key that ends in a newline no longer
   leaks into the conversation. GroundRoute (`GROUNDROUTE_API_KEY`), InfoQuest,
   Tavily, Exa, Jina, Firecrawl, fastCRW and Crawl4AI put the key into an HTTP
@@ -78,6 +105,18 @@

   threads. A group bound with its own `/connect` keeps its thread; a legacy
   group binding, which covers every group of the bot, starts a new one in
   each group. ([#7794])
+  
+- **memory:** An agent-scoped memory write whose `agent_name` is a Windows
+  reserved device name (`NUL`, `CON`, `COM1`, ...) is now rejected with a `422`
+  on the two routes that create that scope, `POST /memory/facts` and
+  `POST /memory/import`. DeerMem resolves the scope to
+  `{storage}/users/{uid}/agents/{name}/facts` and creates it on the first write;
+  the character-class check admitted such names, so the write raised
+  `FileNotFoundError` and the endpoint answered an opaque `500`. The check reuses
+  `windows_incompatible_segment()` and applies on every platform. Read and delete
+  routes stay permissive, so a scope with a reserved-name identifier that an
+  older release stored on a Linux host can still be exported and cleared.
+  ([#7941])
 
 - **skills:** A custom skill name that is a Windows reserved device name
   (`nul`, `con`, `com1`, ...) is now rejected when the skill is created —
@@ -16113,7 +16152,10 @@

 [#7831]: https://github.com/bytedance/deer-flow/pull/7831
 [#7892]: https://github.com/bytedance/deer-flow/pull/7892
 [#7907]: https://github.com/bytedance/deer-flow/pull/7907
+[#7941]: https://github.com/bytedance/deer-flow/pull/7941
 [#7945]: https://github.com/bytedance/deer-flow/issues/7945
 [#7953]: https://github.com/bytedance/deer-flow/issues/7953
 [#7958]: https://github.com/bytedance/deer-flow/pull/7958
 [#7981]: https://github.com/bytedance/deer-flow/pull/7981
+[#7993]: https://github.com/bytedance/deer-flow/pull/7993
+[#8006]: https://github.com/bytedance/deer-flow/pull/8006
```

</details>
