# ℹ️ Intel Report: huggingface/transformers
## 🎯 监控目标 (Target)
> huggingface/transformers

## 🚀 新版本发布 (New Release)
> Version: v5.9.0
> Date: 2026-06-03T02:25:13.389427

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
* Block image_start/end_token_id in generation test sampling (#45914) by @Rocketknight1 in [#45914]


## Bugfixes and improvements

* Remove mask visualization tool from `masking_utils.py` (#46066) by @Cyrilvallez in [#46066]
* fix: owned_by field in GET /v1/models returns list instead of string (#46006) by @nileshpatil6 in [#46006]
* [CB] Remove OpenTelemetry (#45984) by @remi-or in [#45984]
* docs(readme): use canonical `huggingface.co` domain in prose links (#46042) by @kiwigitops in [#46042]
* Fix remaining RAG doc examples that crash on current transformers (#46044) by @Sriniketh24 in [#46044]
* Init the actual tensor, not a copy (#46030) by @Rocketknight1 in [#46030]
* docs: sync legacy ACL anthology URLs and update metrics across i18n READMEs (#46027) by @irfaan101 in [#46027]
* [MultimodalLM] add language_model to the get/set_input_embeddings logic (#46029) by @eustlb in [#46029]
* [`HRM Text`] Add integration tests (#46033) by @vasqu in [#46033]
* hy_v3: add XPU expectations (#45858) by @kaixuanliu in [#45858]
* exaone4_5: add XPU expectations (#45890) by @kaixuanliu in [#45890]
* hyperclovax: add XPU Expectations for CI test (#45926) by @kaixuanliu in [#45926]
* chore(ci): remove dead env vars from circleci-failure-summary-comment.yml (#45972) by @XciD in [#45972]
* [CB] [Major] Add tensor paralellism (#45821) by @remi-or in [#45821]
* docs: update models architecture count and sync ACL anthology URLs (#46001) by @irfaan101 in [#46001]
* bugfix(ci): avoid E2BIG in pr_slow_ci_suggestion  (#45983) by @tarekziade in [#45983]
* RFDetr - use correct Roboflow org for release (#45946) by @sbucaille in [#45946]
* docs: Fix formatting issues in weightconverter.md (#45988) by @ArjunSrivastava1 in [#45988]
* Fix colqwen2 test (#45981) by @IlyasMoutawwakil in [#45981]
* Fix M-RoPE device mismatch in Qwen3VL family under FSDP2 CPU offload (#45861) by @jamesbraza in [#45861]
* [docs] chat template prefill (#45947) by @stevhliu in [#45947]
* [docs] decode fast path (#45899) by @stevhliu in [#45899]
* fix: restore `_attn_implementation `and fix request offset in `generate_batch()` (#45943) by @sergiopaniego in [#45943]
* Expose `per_layer_inputs` for every Gemma4 variants (#45927) by @Cyrilvallez in [#45927]
* chore: update benchmark_v2.yml (#45966) by @hf-security-analysis[bot] in [#45966]
* fix(ci): set persist-credentials: false on actions/checkout and close remaining template injection findings (#45964) by @XciD in [#45964]
* chore(ci): set default workflow permissions to contents: read (#45961) by @XciD in [#45961]
* fix(ci): remove template injection on pull_request_target workflows (#45956) by @XciD in [#45956]
* chore(ci): pin all GitHub Actions and reusable workflows by SHA (#45955) by @XciD in [#45955]
* [docs] ALMModelTest (#45900) by @stevhliu in [#45900]
* Enhance apply_chat_template to support custom field prefilling (reasoning_content, thinking, etc.) (#45896) by @Mamiglia in [#45896]
* BUGFIX: Support hubert models that don't have conv_pos_batch_norm configured (#45921) by @igordertigor in [#45921]
* Revert 45777 (#45942) by @Rocketknight1 in [#45942]
* pass the otel secrets (#45933) by @tarekziade in [#45933]
* Add initial torch_tpu backend support (#45918) by @tengomucho in [#45918]
* [CB] Hide activation footprint by using the CUDA graph pool (#45911) by @remi-or in [#45911]
* Require input_ids for repetition penalty (#45389) by @ruben-aghayan in [#45389]
* Fix undefined 'input' variable (#45895) by @fullyz in [#45895]
* Fix post processing RF-DETR (#46041) by @yonigozlan (direct commit on v5.9.0)
* [loading] Free up tensors faster inside ConversionOps (#46110) by @Cyrilvallez (direct commit on v5.9.0)
* Add new cohere2_moe model (#46115) by @Cyrilvallez (direct commit on v5.9.0)
* Fix cohere2 tp_plan for release by @Cyrilvallez (direct commit on v5.9.0)
* Release v5.9.0 by @Cyrilvallez (direct commit on v5.9.0)

## Significant community contributions

The following contributors have made significant changes to the library over the last release:

* @lmaksym
    * Parakeet tdt (#44171)
* @eustlb
    * user friendly error when loading audio from video (#45221)
    * [MultimodalLM] add language_model to the get/set_input_embeddings logic (#46029)
* @remi-or
    * [CB] Remove OpenTelemetry (#45984)
    * [CB] [Major] Add tensor paralellism (#45821)
    * [CB] Hide activation footprint by using the CUDA graph pool (#45911)
* @abcd1927
    * Add hrm text (#46025)
