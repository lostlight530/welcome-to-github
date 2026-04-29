# ℹ️ Intel Report: googleapis/python-genai
## 🎯 监控目标 (Target)
> googleapis/python-genai

## 🚀 新版本发布 (New Release)
> Version: v1.74.0
> Date: 2026-04-29T22:56:01.356502

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready

## 🛡️ 信任评分 (Trust Score)
> Score: 90/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

## [1.74.0](https://github.com/googleapis/python-genai/compare/v1.73.1...v1.74.0) (2026-04-29)


### Features

* [Interactions] Add FileCitation.{custom_metadata,media_id,page_number} ([aed41ec](https://github.com/googleapis/python-genai/commit/aed41ecf4940f63446fc3e22744663be4d1057a6))
* Add `output_info` to `BatchJob` ([7b77ab8](https://github.com/googleapis/python-genai/commit/7b77ab850283a2c55cb711084e8de6b6da5e589c))
* Add gemini-3.1-flash-tts-preview model to options ([8bdc1c3](https://github.com/googleapis/python-genai/commit/8bdc1c353d987a5a18282fd2265950257891d308))
* Add ImageResizeMode for GenerateVideos ([317d2af](https://github.com/googleapis/python-genai/commit/317d2af040adc7639c4464971d2a5ffa5e381402))
* Add new Gemini Deep Research agent models ([16fffbd](https://github.com/googleapis/python-genai/commit/16fffbd3504e9c83c605410dc75914bf3bcaeedb))
* Add one_of support to JSONSchema for Agent Platform ([8c00c52](https://github.com/googleapis/python-genai/commit/8c00c524488250f25f497e47b495dcedb362da86))
* Add Vertex Dataset input and output options for batch jobs ([d880f92](https://github.com/googleapis/python-genai/commit/d880f92a0631868d6cf86e30aa219a18305ad1a0))
* **interaction-api:** Add grounding tool usage breakdown to Interaction Usage. ([b24fb5a](https://github.com/googleapis/python-genai/commit/b24fb5a1758499e3979cdcadfa734bfa7dd72c94))
* Introduce `enterprise` to Client constructor and `GOOGLE_GENAI_USE_ENTERPRISE` ([693fd9a](https://github.com/googleapis/python-genai/commit/693fd9af1054fde006f76ea820b0c9066577b243))
* Replace the more ambiguous rate field with sample_rate. ([88d9b4a](https://github.com/googleapis/python-genai/commit/88d9b4ad772ce75f21d44174f4679e994fcfca48))


### Bug Fixes

* Catch google-auth wrapped errors ([48ac850](https://github.com/googleapis/python-genai/commit/48ac850fa06de2288e4d736f2f7349909c2a0727))
* Removing Python 3.9 support due to EOL ([8bc2b10](https://github.com/googleapis/python-genai/commit/8bc2b1028da7b94ed0baa31f89a1bf007aaa0bf8))
* **retry:** Retry on httpx.TimeoutException with HttpRetryOptions ([#2345](https://github.com/googleapis/python-genai/issues/2345)) ([0598bab](https://github.com/googleapis/python-genai/commit/0598bab551f40d852dcd4b4575be8dacec42f83e))
* Streaming method doesn't handle multi-line SSE ([f8a2e7e](https://github.com/googleapis/python-genai/commit/f8a2e7ea8c39800aa0a6c50585de49c2c0d5f247))
* Typing in `AsyncClient.__aexit__`, `__exit__`. ([a74dc65](https://github.com/googleapis/python-genai/commit/a74dc6564e3409f9c45a1ec8456ed4386c3711c0))


### Documentation

* Add instruction for custom endpoint ([dd79904](https://github.com/googleapis/python-genai/commit/dd79904ed3a51fb53c43d4b01082556baf579759))
* Fix broken link for rate limits ([d22ea99](https://github.com/googleapis/python-genai/commit/d22ea99dd4318c3bd47bfd6cb571bf9db3316922))
* Regenerate docs for 1.73.1 ([2fb714b](https://github.com/googleapis/python-genai/commit/2fb714b3fefa3a8972da57ef0675116b67e4
