# ℹ️ Intel Report: googleapis/python-genai
## 🎯 监控目标 (Target)
> googleapis/python-genai

## 🚀 新版本发布 (New Release)
> Version: v1.68.0
> Date: 2026-03-18T05:43:30.285506

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: ⚠️ Breaking-Change

## 🛡️ 信任评分 (Trust Score)
> Score: 90/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

## [1.68.0](https://github.com/googleapis/python-genai/compare/v1.67.0...v1.68.0) (2026-03-17)

### Breaking changes

* [Interactions] Breaking change to Interactions API to refactor TextContent annotations to use specific citation types ([6c3379f](https://github.com/googleapis/python-genai/commit/6c3379faa5e533d4146eee1b3c88ed80bbff46ce))
* [Interactions] Breaking change for Interactions, rename ContentDelta unions. ([1b03909](https://github.com/googleapis/python-genai/commit/1b03909ac8367205a2f0dd46847a0f6d36fb62fd))
* [Interactions] Breaking change to Interactions API to rename rendered_content to search_suggestions ([0e21c4e](https://github.com/googleapis/python-genai/commit/0e21c4ef3234fe195793711b8eb90354e154339f))


### Features

* [Interactions] Add and update 'signature' fields for tool call/result content types. ([d896373](https://github.com/googleapis/python-genai/commit/d89637383f2c2ca28bef22f65dfbe56cd1f878cc))
* [Interactions] Support Google Maps in Interactions ([68f247c](https://github.com/googleapis/python-genai/commit/68f247c04af99915b946f04806f3b0a0543180fa))
* Support include_server_side_tool_invocations for genai. ([546440c](https://github.com/googleapis/python-genai/commit/546440c9f56118c8d27005f2d5b935603e50454e))

### Bug Fixes

* **deps:** Correct typing-extensions constraint (1.67 Issue)[https://github.com/googleapis/python-genai/releases/tag/v1.67.0] ([9a4fd39](https://github.com/googleapis/python-genai/commit/9a4fd3983ac093fd9e197099ab970bd89a5a6a56))
* Python 3.10-3.11 breakage caused by https://github.com/googleapis/python-genai/pull/2131 ([9a4fd39](https://github.com/googleapis/python-genai/commit/9a4fd3983ac093fd9e197099ab970bd89a5a6a56))
* Treat `attempts=0` as `attempts=1` in retry options to ensure no retries ([2856c0a](https://github.com/googleapis/python-genai/commit/2856c0ac76eb51b9171a6bd1626b5f6e63bf4a31))



### Documentation

* Regenerate docs for 1.67.0 ([ff7469a](https://github.com/googleapis/python-genai/commit/ff7469a99a931b8415f214c8f711fc4e93422f09))
