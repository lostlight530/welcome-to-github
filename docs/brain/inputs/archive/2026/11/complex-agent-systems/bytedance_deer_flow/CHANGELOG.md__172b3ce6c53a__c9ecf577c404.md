# bytedance/deer-flow · CHANGELOG.md

> 当前有效引用快照. 完整原文由固定 Git Blob 保存, 当前活动输入不重复内联.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) |
| 来源文件 | [CHANGELOG.md](https://github.com/bytedance/deer-flow/blob/c9ecf577c4040f98b177f4248b7e1bfb92e2d6a7/CHANGELOG.md) |
| 来源版本 | `c9ecf577c4040f98b177f4248b7e1bfb92e2d6a7` |
| 来源目录 Tree | `749d23cad5a5c5e482ef36b89db91201a6329b14` |
| 来源内容 Blob | `172b3ce6c53a41cee88cf4d1415d1f7c8d01eed9` |
| 摄取时间 | `2026-11-19T02:57:08.290095+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_bytedance_deer_flow_changelog_md` |
| 快照模式 | `PINNED_EXTERNAL_REFERENCE` |
| 规范内容 SHA256 | `c1f80fe2fac24a98581dd4c9fb9560869ae73b41f0a986e47f5c5bdda9adf9e7` |
| 原文字节数 | `1050093` |
| 原文行数 | `16455` |

## 本次变化

- 新增行数 `10`.
- 删除行数 `0`.
- 完整 Diff 字节数 `1109`.
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

- [按固定源提交读取完整原文](https://github.com/bytedance/deer-flow/blob/c9ecf577c4040f98b177f4248b7e1bfb92e2d6a7/CHANGELOG.md).
- 原文由来源 Blob SHA 与规范内容 SHA256 共同识别.
- 被替换的完整活动快照先原样封存到只追加 Archive.
- Diff 过长时只展示有界预览, 预览不代表完整差异.

<details>
<summary>展开有界版本差异</summary>

```diff
--- previous

+++ 172b3ce6c53a41cee88cf4d1415d1f7c8d01eed9

@@ -67,6 +67,15 @@

   of skipping. ([#8139])
 
 ### Fixed
+
+- **scheduler:** Scheduled-task IM notices no longer forward a credential that
+  carries no secret-like key. A URL's user info
+  (`postgres://admin:hunter2@host`) and an `Authorization` or `Cookie` header
+  value (`Authorization: Bearer ...`) used to reach the platform verbatim; both
+  now read `[redacted]`, and the scheme with the rest of the sentence stays
+  readable. A URL without credentials is unchanged. A `Cookie` header or a
+  `Digest` credential is replaced through the end of the line, so text that
+  follows it on the same line is removed as well. ([#8250])
 
 - **frontend:** Cron presets in the task form now require minute 0-59, hour
   0-23 and day of month 1-31, so an out-of-range expression such as
@@ -16443,3 +16452,4 @@

 [#8139]: https://github.com/bytedance/deer-flow/pull/8139
 [#8151]: https://github.com/bytedance/deer-flow/pull/8151
 [#8174]: https://github.com/bytedance/deer-flow/pull/8174
+[#8250]: https://github.com/bytedance/deer-flow/pull/8250
```

</details>
