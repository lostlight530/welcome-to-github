# bytedance/deer-flow · CHANGELOG.md

> 当前有效引用快照. 完整原文由固定 Git Blob 保存, 当前活动输入不重复内联.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) |
| 来源文件 | [CHANGELOG.md](https://github.com/bytedance/deer-flow/blob/b4eb44f06fdf32a1178f13780b1932b0edc66af6/CHANGELOG.md) |
| 来源版本 | `b4eb44f06fdf32a1178f13780b1932b0edc66af6` |
| 来源目录 Tree | `18eb466d9517efc255cda410c3d815c02361c615` |
| 来源内容 Blob | `351e82141a198861d2df8fc953c2e295984a1e64` |
| 摄取时间 | `2026-11-23T02:20:03.763066+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_bytedance_deer_flow_changelog_md` |
| 快照模式 | `PINNED_EXTERNAL_REFERENCE` |
| 规范内容 SHA256 | `d71c466a0f35118e17d956ef982df825a1fc5aa72207416d1239cb9f90320296` |
| 原文字节数 | `1051329` |
| 原文行数 | `16470` |

## 本次变化

- 新增行数 `22`.
- 删除行数 `7`.
- 完整 Diff 字节数 `3962`.
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

- [按固定源提交读取完整原文](https://github.com/bytedance/deer-flow/blob/b4eb44f06fdf32a1178f13780b1932b0edc66af6/CHANGELOG.md).
- 原文由来源 Blob SHA 与规范内容 SHA256 共同识别.
- 被替换的完整活动快照先原样封存到只追加 Archive.
- Diff 过长时只展示有界预览, 预览不代表完整差异.

<details>
<summary>展开有界版本差异</summary>

```diff
--- previous

+++ 351e82141a198861d2df8fc953c2e295984a1e64

@@ -67,6 +67,21 @@

   of skipping. ([#8139])
 
 ### Fixed
+
+- **agents:** A todo list revised after the last `write_todos` call (for
+  example an approved plan edited on resume) is shown to the model again
+  instead of being silently skipped, and a stale injected reminder is
+  refreshed in place, or removed when the visible call already shows the
+  current list. Injected reminders are stamped with middleware
+  provenance, and caller-edited todo text is neutralized before rendering so
+  it cannot forge framework tags. Reminders persisted before provenance
+  stamps existed are migrated or superseded instead of being left next to
+  a fresh one, an explicitly cleared list keeps a stamped clear-state
+  notice only while a superseded non-empty write is still visible, and a
+  hidden caller message that only wraps text in
+  reminder tags is never treated as a pre-stamp reminder,
+  and todo items render as data after the framework block rather than
+  inside it. ([#8168](https://github.com/bytedance/deer-flow/issues/8168))
 
 - **scheduler:** Scheduled-task IM notices no longer forward a credential that
   carries no secret-like key. A URL's user info
@@ -14594,8 +14609,8 @@

 [#3810]: https://github.com/bytedance/deer-flow/pull/3810
 [#3812]: https://github.com/bytedance/deer-flow/pull/3812
 [#3821]: https://github.com/bytedance/deer-flow/pull/3821
-[#3823]: https://github.com/bytedance/deer-flow/pull/3823
-[#3824]: https://github.com/bytedance/deer-flow/pull/3824
+[#3823]: https://github.com/bytedance/deer-flow/commit/a0d9744d5af14c520efdb45a2988691d59ef246e
+[#3824]: https://github.com/bytedance/deer-flow/commit/904cee4a7248dcd3e57de9b56677bb1386e0fcbb
 [#3826]: https://github.com/bytedance/deer-flow/pull/3826
 [#3828]: https://github.com/bytedance/deer-flow/pull/3828
 [#3833]: https://github.com/bytedance/deer-flow/pull/3833
@@ -15018,11 +15033,11 @@

 [#4817]: https://github.com/bytedance/deer-flow/pull/4817
 [#4820]: https://github.com/bytedance/deer-flow/pull/4820
 [#4822]: https://github.com/bytedance/deer-flow/pull/4822
-[#4823]: https://github.com/bytedance/deer-flow/pull/4823
-[#4825]: https://github.com/bytedance/deer-flow/pull/4825
+[#4823]: https://github.com/bytedance/deer-flow/commit/3a967d4f9abee1272c1b3f142310120367c38fb3
+[#4825]: https://github.com/bytedance/deer-flow/commit/9668b35b1a66e22358b2447e3de256d9138ad5ad
 [#4826]: https://github.com/bytedance/deer-flow/pull/4826
 [#4827]: https://github.com/bytedance/deer-flow/pull/4827
-[#4830]: https://github.com/bytedance/deer-flow/pull/4830
+[#4830]: https://github.com/bytedance/deer-flow/commit/adf6c422c2aa2aa023d6534369999981594f12e3
 [#4833]: https://github.com/bytedance/deer-flow/pull/4833
 [#4834]: https://github.com/bytedance/deer-flow/pull/4834
 [#4836]: https://github.com/bytedance/deer-flow/pull/4836
@@ -15057,7 +15072,7 @@

 [#4918]: https://github.com/bytedance/deer-flow/pull/4918
 [#4919]: https://github.com/bytedance/deer-flow/pull/4919
 [#4921]: https://github.com/bytedance/deer-flow/pull/4921
-[#4928]: https://github.com/bytedance/deer-flow/pull/4928
+[#4928]: https://github.com/bytedance/deer-flow/commit/f1f4af99bbf1cffb83a80744bf6e4a44ee8f24be
 [#4929]: https://github.com/bytedance/deer-flow/pull/4929
 [#4933]: https://github.com/bytedance/deer-flow/pull/4933
 [#4936]: https://github.com/bytedance/deer-flow/pull/4936
@@ -15107,7 +15122,7 @@

 [#5039]: https://github.com/bytedance/deer-flow/pull/5039
 [#5041]: https://github.com/bytedance/deer-flow/pull/5041
 [#5045]: https://github.com/bytedance/deer-flow/pull/5045
-[#5047]: https://github.com/bytedance/deer-flow/pull/5047
+[#5047]: https://github.com/bytedance/deer-flow/commit/c6f6a01f56b04b6c99d73df82ed6053beb8c1a10
 [#5049]: https://github.com/bytedance/deer-flow/pull/5049
 [#5050]: https://github.com/bytedance/deer-flow/pull/5050
 [#5051]: https://github.com/bytedance/deer-flow/pull/5051
```

</details>
