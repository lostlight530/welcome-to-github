# ℹ️ Intel Report: googleapis/python-genai
## 🎯 监控目标 (Target)
> googleapis/python-genai

## 🚀 新版本发布 (New Release)
> Version: v2.9.0-rc0
> Date: 2026-06-16T10:15:06.953851

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: ⚠️ Breaking-Change

## 🛡️ 信任评分 (Trust Score)
> Score: 90/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

## [2.9.0-rc0](https://github.com/googleapis/python-genai/compare/v2.8.0...v2.9.0-rc0) (2026-06-16)

### Major updates

* The interactions implementation has been completely replaced. The public api surface should be unchanged.  ([d830f16](https://github.com/googleapis/python-genai/commit/d830f165d223ac5f42ab3fa74d2c3d868b0054d8))

### Features

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


### Documentation

* Announce Automatic Function Calling (AFC) upcoming breaking change warning ([4697258](https://github.com/googleapis/python-genai/commit/4697258417902a5d0074a2247db34bfdf40e5468))
* Clarify Live API START/END_SENSITIVITY_HIGH/LOW defaults are different in Gemini Live and Gemini Enterprise Agent Platform Live API ([a0ec6ab](https://github.com/googleapis/python-genai/commit/a0ec6abc8f54f9cfc110e9b1dd3271971961f193)), closes [#2555](https://github.com/googleapis/python-genai/issues/2555)
* Regenerate docs for 2.8.0 ([93e7ab1](https://github.com/googleapis/python-genai/commit/93e7ab1e8851dd68e59368d49bc2e3695dfd5148))
