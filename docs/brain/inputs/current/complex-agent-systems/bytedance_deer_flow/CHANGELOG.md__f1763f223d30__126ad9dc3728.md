# bytedance/deer-flow · CHANGELOG.md

> 当前有效引用快照. 完整原文由固定 Git Blob 保存, 当前活动输入不重复内联.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) |
| 来源文件 | [CHANGELOG.md](https://github.com/bytedance/deer-flow/blob/126ad9dc3728863314f3ebb4988e0a80f0a89057/CHANGELOG.md) |
| 来源版本 | `126ad9dc3728863314f3ebb4988e0a80f0a89057` |
| 来源目录 Tree | `050752bd0701622f892a374a4f9a9ae290133fc4` |
| 来源内容 Blob | `f1763f223d30cad2175812529600e6aa8b5d8016` |
| 摄取时间 | `2026-11-25T04:47:56.895522+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_bytedance_deer_flow_changelog_md` |
| 快照模式 | `PINNED_EXTERNAL_REFERENCE` |
| 规范内容 SHA256 | `879c2397de514f539ee153c5b2befb2b3c0bbdeb6d973bd055aa301c3bd7d086` |
| 原文字节数 | `1051554` |
| 原文行数 | `16474` |

## 本次变化

- 新增行数 `4`.
- 删除行数 `0`.
- 完整 Diff 字节数 `628`.
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

- [按固定源提交读取完整原文](https://github.com/bytedance/deer-flow/blob/126ad9dc3728863314f3ebb4988e0a80f0a89057/CHANGELOG.md).
- 原文由来源 Blob SHA 与规范内容 SHA256 共同识别.
- 被替换的完整活动快照先原样封存到只追加 Archive.
- Diff 过长时只展示有界预览, 预览不代表完整差异.

<details>
<summary>展开有界版本差异</summary>

```diff
--- previous

+++ f1763f223d30cad2175812529600e6aa8b5d8016

@@ -11,6 +11,10 @@

 ([2.3.0](https://github.com/bytedance/deer-flow/milestone/4)).
 
 ### Added
+- **crawl4ai:** `web_fetch` accepts an optional `max_chars` output cap (default
+  4096). A page cut at the cap ends with a note giving the kept and total
+  length. ([#8553](https://github.com/bytedance/deer-flow/pull/8553))
+
 - **summarization:** The built-in compaction prompt guides the summarizer to
   preserve active user requirements, literal approval phrases, action conditions,
   and explicit revisions. Explicit `summarization.summary_prompt` configurations
```

</details>
