# ℹ️ Intel Report: huggingface/transformers
## 🎯 监控目标 (Target)
> huggingface/transformers

## 🚀 新版本发布 (New Release)
> Version: v5.9.0
> Date: 2026-05-29T03:28:06.912345

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready ⚠️ Breaking-Change 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 100/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

# Release v5.9.0


## New Model additions

### Cohere2Moe

Command A+ is a Mixture-of-Experts (MoE) language model from Cohere that features a hybrid attention pattern combining sliding window and full attention layers. The model incorporates both shared and routed experts and supports a very large context window for processing extensive text sequences.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/cohere2_moe)
* Add new cohere2_moe model (#46115) by @Cyrilvallez in [#46115](https://github.com/huggingface/transformers/pull/46115)

### Parakeet tdt (#44171)

* Parakeet tdt (#44171) by @lmaksym

### HRM-Text

HRM-Text is an improved autoregressive language-modeling variant of the Hierarchical Reasoning Model (HRM) that uses a hierarchical recurrent forward pass with two transformer stacks - one for slow, abstract planning (H) and one for fast, detailed computation (L) - reused inside a nested recurrence. It features PrefixLM attention where instruction tokens attend bidirectionally while response tokens attend causally, per-head sigmoid output gates, and parameterless RMSNorm. The model is designed as a base language model without instruction tuning or chat templates.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/hrm_text) | [Paper](https://huggingface.co/papers/2506.21734)
* Add hrm text (#46025) by @abcd1927 in [#46025](https://github.com/huggingface/transformers/pull/46025)



## Breaking changes

The `text_embeds` input for SAM3, EdgeTAM, and SAM3-Lite-Text models now expects full text embeddings instead of just pooler outputs, aligning with other models in the library — users must update their inputs accordingly.
* 🚨Fix memory leaks caused by lru decorators in vision models (#45922) by @yonigozlan



## Audio

Audio support was expanded with the addition of AudioFlamingoNext model checkpoints and improved compilability of audio/vision encoders via standalone pure functions. Additional improvements include better error messaging when loading audio from video files and new documentation for audio/video processors.


* user friendly error when loading audio from video (#45221) by @eustlb in [#45221]
* [docs] adding audio/video processors (#45795) by @stevhliu in [#45795]
* Support Audio Flamingo Next checkpoints (#44830) by @lashahub in [#44830]
* Extract dynamic vision/audio tensors into standalone pure functions (#45396) by @IlyasMoutawwakil in [#45396]


## Generation

Fixed generation issues including `inputs_embeds` and `per_layer_inputs` handling for Gemma4, an `AttributeError` in RAG's `generate()` caused by missing config fields, and flaky VLM generation tests by blocking special image tokens during sampling.


* Fix Gemma4 generation from inputs_embeds and per_layer_inputs (#46049) by @Cyrilvallez in [#46049]
* Fix AttributeError in RAG generate() for missing config fields (#46035) by @Sriniketh24 in [#46035]
