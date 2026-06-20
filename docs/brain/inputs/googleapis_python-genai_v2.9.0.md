# ℹ️ Intel Report: googleapis/python-genai
## 🎯 监控目标 (Target)
> googleapis/python-genai

## 🚀 新版本发布 (New Release)
> Version: v2.9.0
> Date: 2026-06-20T09:25:34.495299

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready ⚠️ Breaking-Change

## 🛡️ 信任评分 (Trust Score)
> Score: 100/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

## [2.9.0](https://github.com/googleapis/python-genai/compare/v2.9.0-rc1...v2.9.0) (2026-06-19)

### Major updates

* **The interactions implementation has been completely replaced**. The public api surface is unchanged.  ([d830f16](https://github.com/googleapis/python-genai/commit/d830f165d223ac5f42ab3fa74d2c3d868b0054d8))

### Features

* Add audioOffset to VoiceActivity ([fb785e4](https://github.com/googleapis/python-genai/commit/fb785e402a3aa958b45bf6300f0be972b2f92bf9))
* Add gemini-3-flash-preview (gemini-3.1, gemini-3.5, gemini-4 are already mapped) to the local tokenizer map. ([749f8a1](https://github.com/googleapis/python-genai/commit/749f8a1b1b5ef06b4b0fc604bc5482f003ef0e1a)), closes [#1972](https://github.com/googleapis/python-genai/issues/1972)
* Add interimInputTranscription to LiveServerContent ([fb785e4](https://github.com/googleapis/python-genai/commit/fb785e402a3aa958b45bf6300f0be972b2f92bf9))
* Add LanguageAuto, LanguageHints, and adaptationPhrases to AudioTranscriptionConfig ([fb785e4](https://github.com/googleapis/python-genai/commit/fb785e402a3aa958b45bf6300f0be972b2f92bf9))
* Broaden publisher model path check to support all publishers ([5d282e6](https://github.com/googleapis/python-genai/commit/5d282e662de39d7fb68d258e6ca20446dba16576))
* Add ServiceTier to UsageMetadata ([45b4963](https://github.com/googleapis/python-genai/commit/45b4963f4cdc8dc01cffe85260c629e50595fbf9))
* Expose Computer Use API fields ([420b5a7](https://github.com/googleapis/python-genai/commit/420b5a774852501f04c716f74b6c58f466bb71df))
* Gemma 4 local tokenizer support ([ca97c58](https://github.com/googleapis/python-genai/commit/ca97c5805666f6386d0148848132c07ce81e2c72))
* **interaction-api:** Add presence_penalty, frequency_penalty, and cached_content to models.proto ([05f16fe](https://github.com/googleapis/python-genai/commit/05f16fea01d4c8bdc4d6ac9c2b7bbed11ada3aee))
* **interaction-api:** Rename usage to total_usage in StreamMetadata. ([7c331c6](https://github.com/googleapis/python-genai/commit/7c331c6c40825cbbbd7cfc354357c171bdf395f5))

### Bug Fixes

* Add fallback for `aiohttp.readline` without `max_line_length` for backward compatibility because we still want to keep aiohttp as optional dependency ([e99ab99](https://github.com/googleapis/python-genai/commit/e99ab99d63625b2f383a08f5fb91812c096f1c2b)), closes [#2487](https://github.com/googleapis/python-genai/issues/2487)
* Fix header ([f8f9749](https://github.com/googleapis/python-genai/commit/f8f97496965795469888b93f3c70d6ea08296a83))
* Keep live music API keys out of websocket urls ([#2564](https://github.com/googleapis/python-genai/issues/2564)) ([c754ebf](https://github.com/googleapis/python-genai/commit/c754ebf3973fde9894b24c2425cee67eb2d03b64))
* Make `transformers` an optional dependency for local tokenizers, also add other dependencies to local-tokenizer-extras. ([528926b](https://github.com/googleapis/python-genai/commit/528926b5a94fb6590846e739e643895016d2c0d0))
* Use .model_copy() instead of deprecated .copy() ([216369f](https://github.com/googleapis/python-genai/commit/216369f519712285db0902f0b248be3c4faf664c))
