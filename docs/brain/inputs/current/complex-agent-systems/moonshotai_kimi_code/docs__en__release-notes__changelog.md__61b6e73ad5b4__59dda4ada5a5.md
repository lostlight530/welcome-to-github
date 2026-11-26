# MoonshotAI/kimi-code · docs/en/release-notes/changelog.md

> 当前有效引用快照. 完整原文由固定 Git Blob 保存, 当前活动输入不重复内联.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) |
| 来源文件 | [docs/en/release-notes/changelog.md](https://github.com/MoonshotAI/kimi-code/blob/59dda4ada5a5f0b621d156e580fa9b9032b611bf/docs/en/release-notes/changelog.md) |
| 来源版本 | `59dda4ada5a5f0b621d156e580fa9b9032b611bf` |
| 来源目录 Tree | `c892c54fc0974906d994ea291f332c942460a98a` |
| 来源内容 Blob | `61b6e73ad5b484762407814b550d6d83ebd044d2` |
| 摄取时间 | `2026-11-26T03:58:40.504594+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_moonshotai_kimi_code_docs_en_release_notes_changelog_md` |
| 快照模式 | `PINNED_EXTERNAL_REFERENCE` |
| 规范内容 SHA256 | `6eae0f7e8df6dbf4e3742a183edb161f5a01f1eb454071cf1186e885cb132f6c` |
| 原文字节数 | `128940` |
| 原文行数 | `2057` |

## 本次变化

- 新增行数 `12`.
- 删除行数 `0`.
- 完整 Diff 字节数 `656`.
- 来源变化不等于本仓执行验证或独立研究次数.

## 阅读导航

- Changelog
- 2.8.0 (2026-11-25)
- Polish
- Bug Fixes
- 2.7.3 (2026-11-24)
- Bug Fixes
- 2.7.2 (2026-11-20)
- Bug Fixes
- 2.7.1 (2026-11-20)
- Bug Fixes
- 2.7.0 (2026-11-19)
- Features
- Bug Fixes
- 2.6.3 (2026-11-17)
- Bug Fixes
- 2.6.2 (2026-11-14)
- Features
- Polish
- Bug Fixes
- 2.6.1 (2026-11-13)
- Bug Fixes
- 2.6.0 (2026-11-12)
- Features
- Polish

## 原文完整性与取回

- [按固定源提交读取完整原文](https://github.com/MoonshotAI/kimi-code/blob/59dda4ada5a5f0b621d156e580fa9b9032b611bf/docs/en/release-notes/changelog.md).
- 原文由来源 Blob SHA 与规范内容 SHA256 共同识别.
- 被替换的完整活动快照先原样封存到只追加 Archive.
- Diff 过长时只展示有界预览, 预览不代表完整差异.

<details>
<summary>展开有界版本差异</summary>

```diff
--- previous

+++ 61b6e73ad5b484762407814b550d6d83ebd044d2

@@ -5,6 +5,18 @@

 # Changelog
 
 This page documents the changes in each Kimi Code CLI release.
+
+## 2.8.0 (2026-11-25)
+
+### Polish
+
+- Improve prompt prediction; enable it in `/experiments`.
+- In the TUI, consecutive queued turns skip intermediate completion alerts; background tasks still notify.
+
+### Bug Fixes
+
+- Fix sessions that could not be restored after their model became unavailable.
+- Fix several known issues and make refinements. See [GitHub](https://github.com/MoonshotAI/kimi-code/blob/main/apps/kimi-code/CHANGELOG.md) for technical entries.
 
 ## 2.7.3 (2026-11-24)
```

</details>
