# ℹ️ Intel Report: googleapis/python-genai
## 🎯 监控目标 (Target)
> googleapis/python-genai

## 🚀 新版本发布 (New Release)
> Version: v1.67.0
> Date: 2026-03-15T11:37:15.089233

## 🛡️ 信任评分 (Trust Score)
> Score: 80/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

## [1.67.0](https://github.com/googleapis/python-genai/compare/v1.66.0...v1.67.0) (2026-03-12)

> [!CAUTION]
> **Known Issue:**
> This release contains a bug where the `typing-extensions` lower bound is set too low, which causes the SDK to break in some environments.
>
> **Recommended Actions:**
> * **Fall back to 1.66.0:** If you do not immediately need the new features in 1.67.0, we recommend sticking with the previous stable version:
>     `pip install google-genai==1.66.0`
> * **Manual Fix:** If you must use 1.67.0, you can resolve the issue by manually upgrading `typing-extensions`:
>     `pip install "typing-extensions>=4.14.0"`

### Features

* Add inference_generation_config to EvaluationConfig for Tuning ([1fdb4b8](https://github.com/googleapis/python-genai/commit/1fdb4b87aaec6e58b415168ea5893c0e901819a9))
* Add live history_config with initial_history_in_client_content ([a80babd](https://github.com/googleapis/python-genai/commit/a80babd22d195d82881cdda0a2c0d5cdefd9573d))
* Add support for referencing registered metrics by resource name in evaluation run API ([41b348e](https://github.com/googleapis/python-genai/commit/41b348ed7a5b3a817861e56ccd01251dc65859d3))
* Enable language code for audio transcription config in Live API for Vertex AI ([c04be0d](https://github.com/googleapis/python-genai/commit/c04be0db2b65506ba0ad3e1b0922ec871df1580b))


### Bug Fixes

* Forward http_options in async_request_streamed to enable retry support ([8b3be87](https://github.com/googleapis/python-genai/commit/8b3be8744065ad1fa96484fcc2910842a7414a32))
* Forward http_options in async_request_streamed to enable retry support ([#2097](https://github.com/googleapis/python-genai/issues/2097)) ([8b10efb](https://github.com/googleapis/python-genai/commit/8b10efb0349bcf64599405a48325f4415aa7eaad))
