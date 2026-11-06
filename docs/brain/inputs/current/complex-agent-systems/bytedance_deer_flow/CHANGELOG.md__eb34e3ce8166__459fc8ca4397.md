# bytedance/deer-flow · CHANGELOG.md

> 当前有效引用快照. 原始证据位于固定上游 Git Blob, 不在当前活动输入中重复内联.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) |
| 来源文件 | [CHANGELOG.md](https://github.com/bytedance/deer-flow/blob/459fc8ca4397bf75637cdbe6ffbb91e871f5107a/CHANGELOG.md) |
| 来源版本 | `459fc8ca4397bf75637cdbe6ffbb91e871f5107a` |
| 来源目录 Tree | `b89c4f139b43eb45fb4f9f0b0835c8a7c86f9c72` |
| 来源内容 Blob | `eb34e3ce81664aa8cd91187b486d7302016dc9eb` |
| 摄取时间 | `2026-11-05T02:00:38.194663+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_bytedance_deer_flow_changelog_md` |
| 快照模式 | `PINNED_EXTERNAL_REFERENCE` |
| 规范内容 SHA256 | `2a3fba8eac03065683a38439a4942260958ff98e53c4fc5495bca2fbdd6b3517` |
| 原文字节数 | `1022883` |
| 原文行数 | `16014` |

## 本次变化

- 新增行数 `4`.
- 删除行数 `0`.
- 完整 Diff 字节数 `1012`.
- 边界: 这只是来源文件变化, 不是本仓执行验证或独立研究次数.

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

- [按源提交读取完整上游原文](https://github.com/bytedance/deer-flow/blob/459fc8ca4397bf75637cdbe6ffbb91e871f5107a/CHANGELOG.md).
- 原文以来源 Blob SHA 与规范内容 SHA256 识别. 本地活动快照只保留可恢复的固定引用.
- 早期原文快照由历史 Git 提交及只追加 Archive 保留, 不因引用模式删除.
- Diff 过长时仅展示有界预览, 不把预览当作完整版本差异.
- [修正前完整活动快照](https://github.com/lostlight530/welcome-to-github/blob/af7337d378613007289e5e13514e124ca259dca5/docs/brain/inputs/current/complex-agent-systems/bytedance_deer_flow/CHANGELOG.md__eb34e3ce8166__459fc8ca4397.md).

<details>
<summary>展开有界版本差异</summary>

```diff
--- previous

+++ eb34e3ce81664aa8cd91187b486d7302016dc9eb

@@ -70,6 +70,9 @@

   path but walked the unresolved tree, so no document matched and every
   original older than 24 hours was removed as an orphan, at Gateway startup
   and from `GET /api/trash/documents`. ([#7732])
+
+- **chat:** Cancelling a queued input after dispatch starts no longer
+  prevents subsequent queued inputs from executing. ([#7746])
 
 - **dev:** `scripts/dev_multi_instance.sh logs all` now prints the nginx logs
   as well as both Gateway logs; it printed only the Gateway logs, the same as
@@ -16005,6 +16008,7 @@

 [#7727]: https://github.com/bytedance/deer-flow/pull/7727
 [#7729]: https://github.com/bytedance/deer-flow/pull/7729
 [#7732]: https://github.com/bytedance/deer-flow/pull/7732
+[#7746]: https://github.com/bytedance/deer-flow/pull/7746
 [#7762]: https://github.com/bytedance/deer-flow/pull/7762
 [#7772]: https://github.com/bytedance/deer-flow/pull/7772
 [#7781]: https://github.com/bytedance/deer-flow/pull/7781
```

</details>
