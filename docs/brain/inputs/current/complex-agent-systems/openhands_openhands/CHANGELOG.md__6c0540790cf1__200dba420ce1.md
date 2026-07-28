# OpenHands/OpenHands · CHANGELOG.md

> 当前有效快照. 中文说明只使用英文句号. 外部原文保持来源原貌.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) |
| 来源文件 | [CHANGELOG.md](https://github.com/OpenHands/OpenHands/blob/200dba420ce127a76fc758d39f011af36fe17508/CHANGELOG.md) |
| 来源版本 | `200dba420ce127a76fc758d39f011af36fe17508` |
| 来源目录 Tree | `167cbf21536568aa81d5a77f5501cde416ce1785` |
| 来源内容 Blob | `6c0540790cf1f459b31d556b4f70f224a2e81383` |
| 摄取时间 | `2026-07-28T07:52:12.674046+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_openhands_openhands_changelog_md` |

## 本次变化

- 新增行数 `29`.
- 删除行数 `0`.
- 内容哈希变化时才生成新快照.

## 阅读导航

- Changelog
- [Unreleased]
- [1.0.0-alpha.2] - 2025-05-11
- Added

<details>
<summary>展开完整外部原文</summary>

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0-alpha.2] - 2025-05-11

### Added

- Initial npm package release of `@openhands/agent-canvas`
- CLI entry point (`npx @openhands/agent-canvas`) to run full stack locally
- Library build mode with component barrel exports
- Subpath exports for modular imports:
  - `@openhands/agent-canvas/browser`
  - `@openhands/agent-canvas/conversation`
  - `@openhands/agent-canvas/files`
  - `@openhands/agent-canvas/settings`
  - `@openhands/agent-canvas/sidebar`
  - `@openhands/agent-canvas/terminal`
  - `@openhands/agent-canvas/i18n`
- TypeScript type declarations
- GitHub Actions workflow for automated npm publishing (OIDC trusted publishing)

[Unreleased]: https://github.com/OpenHands/agent-canvas/compare/v1.0.0-alpha.2...HEAD
[1.0.0-alpha.2]: https://github.com/OpenHands/agent-canvas/releases/tag/v1.0.0-alpha.2

</details>

<details>
<summary>展开完整版本差异</summary>

```diff
--- previous

+++ 6c0540790cf1f459b31d556b4f70f224a2e81383

@@ -0,0 +1,29 @@

+# Changelog
+
+All notable changes to this project will be documented in this file.
+
+The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
+and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
+
+## [Unreleased]
+
+## [1.0.0-alpha.2] - 2025-05-11
+
+### Added
+
+- Initial npm package release of `@openhands/agent-canvas`
+- CLI entry point (`npx @openhands/agent-canvas`) to run full stack locally
+- Library build mode with component barrel exports
+- Subpath exports for modular imports:
+  - `@openhands/agent-canvas/browser`
+  - `@openhands/agent-canvas/conversation`
+  - `@openhands/agent-canvas/files`
+  - `@openhands/agent-canvas/settings`
+  - `@openhands/agent-canvas/sidebar`
+  - `@openhands/agent-canvas/terminal`
+  - `@openhands/agent-canvas/i18n`
+- TypeScript type declarations
+- GitHub Actions workflow for automated npm publishing (OIDC trusted publishing)
+
+[Unreleased]: https://github.com/OpenHands/agent-canvas/compare/v1.0.0-alpha.2...HEAD
+[1.0.0-alpha.2]: https://github.com/OpenHands/agent-canvas/releases/tag/v1.0.0-alpha.2
```

</details>
