# ℹ️ Intel Report: huggingface/transformers
## 🎯 监控目标 (Target)
> huggingface/transformers

## 🚀 新版本发布 (New Release)
> Version: v5.10.1
> Date: 2026-06-03T23:45:01.929739

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready ⚠️ Breaking-Change 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 100/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

# Release v5.10.1
v5.10.0 was yanked as we publish on a corrupted branch. Sorry everyone, this happens when we rush a release!!! 

## New Model additions

### Gemma4 unified+ Gemma4 MTP
<img width="2000" height="400" alt="image" src="https://github.com/user-attachments/assets/5e3ee940-f78d-4343-ac7a-889930800aa6" />

Gemma 4 12B Unified is an **encoder-free** multimodal model with pretrained and instruction-tuned variants. Unlike [standard Gemma 4](./gemma4), which uses dedicated encoder towers, Gemma 4 12B Unified projects raw inputs directly into the language model's embedding space through lightweight linear pipelines. This results in a simpler architecture while maintaining strong multimodal performance.

Key differences from standard Gemma 4:
- **No Vision Tower**: Raw pixel patches are projected directly into LM space via a `Dense + LayerNorm` pipeline with factorized 2D positional embeddings, replacing the vision encoder.
- **No Audio Tower**: Raw 16 kHz waveform samples are chunked into fixed-length frames and projected through a simple `RMSNorm → Linear` pipeline, replacing the mel spectrogram + Conformer encoder.
- **Shared Multimodal Pipeline**: Both vision and audio use the same `Gemma4UnifiedMultimodalEmbedder` (RMSNorm → Linear) for the final projection to text hidden space.

You can find the original Gemma 4 12B Unified checkpoints under the [Gemma 4](https://huggingface.co/collections/google/gemma-4) release.

* who needs encoders? (#46385) by @douglas-reid @sgerrard @vasqu @molbap

### Sapiens2

Sapiens2 is a family of high-resolution vision transformers pretrained on ~1 billion curated human images, designed for human-centric computer vision tasks including pose estimation, body-part segmentation, surface normal estimation, and pointmap estimation. The models scale from 0.4B to 5B parameters and train at native 1K resolution, with hierarchical 4K variants for extended spatial reasoning. Sapiens2 achieves substantial improvements over its predecessor with +4 mAP in pose estimation, +24.3 mIoU in body-part segmentation, and 45.6% error reduction in normal estimation.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/sapiens2) | [Paper](https://huggingface.co/papers/2604.21681)
* Add Sapiens2 Model (#45919) by @guarin in [#45919](https://github.com/huggingface/transformers/pull/45919)

### DeepSeek-OCR-2

DeepSeek-OCR-2 is an OCR-specialized vision-language model built on a distinctive architecture that combines a SAM ViT-B vision encoder with a Qwen2 hybrid attention encoder, connected through an MLP projector to a DeepSeek-V2 Mixture-of-Experts (MoE) language model. The model features a hybrid attention mechanism that applies bidirectional attention over image tokens and causal attention over query tokens, enabling efficient and accurate document understanding. It supports both plain OCR tasks and grounding capabilities with coordinate-aware output for document conversion to markdown format.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/deepseek_ocr2)
* Add Deepseek-OCR-2 model (#45075) by @thisisiron in [#45075](https://github.com/huggingface/transformers/pull/45075)

### Mellum

Mellum is a code-focused Mixture-of-Experts language model developed by JetBrains. It is derived from the Qwen3-MoE architecture with per-layer-type RoPE and interleaved sliding window attention. The model has 12B total parameters with 2.5B active parameters per token, using 64 routed experts with 8 activated per token across 28 layers.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/mellum)
* feat: Add support for JetBrains' `Mellum` v2 code generation model (#46112) by @shadeMe in [#46112](https://github.com/huggingface/transformers/pull/46112)



## Breaking changes

The Gemma4 vision pooler now casts inputs to float32 before scaling to prevent float16 overflow (inf saturation) with large checkpoints, which may cause minor numerical differences in outputs for users running Gemma-4 vision models in float16.
* 🚨 Fix float16 overflow in Gemma4 vision pooler (#46277) by @Bluear7878

Audio Language Models (ALMs) now have a dedicated base model class without a language modeling head, aligning them with the design of Vision Language Models (VLMs); users relying on the previous model class structure should update their code to use the new base model class where appropriate.
* 🚨 [ALM] Add base model without head (#45534) by @eustlb



## Parallelization

This release includes numerous bug fixes for model parallelism across multiple models (Gemma4, AltCLIP, ChineseClip, Blip-2, Whisper, Ovis2, Moshi) and parallel execution strategies, including fixes for tensor parallelism (TP), expert parallelism (EP), beam search under model parallel settings, and loss over-counting under TP/EP configurations. The continuous batching manager was also reworked for clearer control flow and improved TP race condition handling, and FSDP initialization via `from_pretrained` was introduced.


* Fix dsv4 dequant + tp/ep (#46378) by @IlyasMoutawwakil in [#46378]
* [CB] [Major] Rework manager to have clearer control flow + handle TP (#46070) by @remi-or in [#46070]
* fix series of bugs for model parallel beam search (#46280) by @kaixuanliu in [#46280]
* Fix model parallel issue for altclip model and ChineseClip model (#45487) by @kaixuanliu in [#45487]
* Model parallel fix (#46230) by @kaixuanliu in [#46230]
* [`Revert`] FSDP+Dtensor refactor related changes (#46246) by @vasqu in [#46246]
* Fix model parallel bugs for Gemma4 (#45817) by @kaixuanliu in [#45817]
* init FSDP through from_pretrained (#46102) by @3outeille in [#46102]
* fix model parallel device mismatch issue in `create_bidirectional_mask` (#46221) by @kaixuanliu in [#46221]
* Trainer.compute_loss: fix loss over-counting under TP and EP-as-TP (#45994) by @AmineDiro in [#45994]
* Fix caching allocator warmup byte estimation for EP model loading (#46149) by @sywangyi in [#46149]


## Cache

Fixed a regression in encoder-decoder cache initialization where the decoder config was incorrectly applied to the cross-attention cache, and resolved a `RuntimeError` caused by buffer size limits when warming up the cache on MPS devices. Additional test infrastructure improvements were made to support read-only cache environments used in CI.


* fix: cache warmup `RuntimeError` on mps (#46239) by @McPatate in [#46239]
* Make more tests work with read-only cache (#46299) by @ydshieh in [#46299]
* Update a test to avoid writing to the default xet cache (#46250) by @ydshieh in [#46250]
* Fix a regression in encoder-decoder generation cache initialization (#46111) by @kaixuanliu in [#46111]


## Quantization

Added support for DeepGEMM BF16, mixed FP8/FP4, and MegaMoE quantization via a grouped linear refactor, while fixing two bugs: an FP8 MoE reverse substring issue affecting DSv4 initialization, and a BitsAndBytes 4-bit/8-bit quantization bug that silently dropped chunked tensors from one-to-many weight converters.


* DeepGEMM BF16 + mixed FP8/FP4 + MegaMoE + refactor (#45634) by @IlyasMoutawwakil in [#45634]
* Fix fp8 moe reverse substring (#46265) by @ArthurZucker in [#46265]
* Fix bnb 4bit/8bit quantization drop chunked tensors bug (#46210) by @kaixuanliu in [#46210]


## Bugfixes and improvements

* Fix wrong changes produced by style/repo. check bot (#46371) by @ydshieh in [#46371]
* Fix path traversal when saving Bark voice preset embeddings (#46237) by @LinZiyuu in [#46237]
* Pass library_name/version to Hub calls via a shared HfApi (#46318) by @Wauplin in [#46318]
* docs: update ACL Anthology URL in CITATION.cff (#46352) by @irfaan101 in [#46352]
* [docs] contributing (#45465) by @stevhliu in [#45465]
* [docs] Romanian translation of `contributing.md`, `modular_transformers.md`, `multimodal_processing.md`, `add_vision_processing_components.md`, `add_audio_processing_components.md`, `modeling_rules.md`, `model_output_tracing.md`, `auto_docstring.md`, `testing.md`, `pr_checks.md` and `add_new_model.md` . (#46345) by @filipinescu in [#46345]
* [docs] xpu continuous batching (#46334) by @stevhliu in [#46334]
* Fix incorrect attribute mapping relationships in GLM MoE DSA Config (#46338) by @Dovis01 in [#46338]
* Fix grammar typos in Whisper documentation (#46336) by @calliec-1223 in [#46336]
* [docs] update num_items_in_batch for causal LMs (#46335) by @stevhliu in [#46335]
* Update compressed tensors minimum version (#46342) by @SunMarc in [#46342]
* Fix _is_package_available reporting available without a version (#46125) by @blipbyte in [#46125]
* remove sec (#46346) by @ydshieh in [#46346]
* fix: include transitive relative imports when loading from local directory (#46022) by @trducng in [#46022]
* perf(feature_extraction_sequence): skip re-splitting already-batched numpy arrays in pad() (#46329) by @Anai-Guo in [#46329]
* [Zamba] Support attn_implementation dispatch (#46317) by @YangKai0616 in [#46317]
* Fix TestAppRoutes test failures caused by deprecated asyncio.get_event_loop() on Python 3.10+ (#46340) by @ydshieh in [#46340]
* [Qwen3VL] Fix video token placeholder: use self.video_token instead of hardcoded "<|placeholder|>" (#46296) by @kpal002 in [#46296]
* chore(linter): fixes for rule 16 (#46023) by @tarekziade in [#46023]
* [docs] Romanian translation of  `weightconverter.md`,  `models.md`,  `custom_models.md`,  `monkey_patching.md`,  `fusion_mapping.md`, `how_to_hack_models.md`, `model_sharing.md` and `serialization.md`. (#46309) by @filipinescu in [#46309]
* Normalize CUDA OOM errors when comparing commit failures in check_bad_commit (#46322) by @ydshieh in [#46322]
* Fix unhandled exception noise from background safetensors conversion thread (#45752) by @dhruv7477 in [#45752]
* Add Expectations for pipeline token classification tests (#46151) by @kaixuanliu in [#46151]
* [docs] fix auto-add release dates (#46283) by @zucchini-nlp in [#46283]
* Separate pip command syntax for notebook and CLI tabs in Quickstart (#46243) by @pvelayudhan in [#46243]
* Romanian translation of README.md, index.md, installation.md, _config.py and quicktour.md. (#46166) by @filipinescu in [#46166]
* Fall back to flat kwarg when modality dict is passed without it (#46195) by @Ace3Z in [#46195]
* Fix load_adapter OOM caused by full-model warmup sizing (#46145) by @Yooniel in [#46145]
* Replace assert with raise ImportError for optuna/ray dependency checks (#46263) by @SebTardif in [#46263]
* chore(linter): respect TRF017 modeling rule (#46260) by @tarekziade in [#46260]
* Delete dead code in qwen-vl series (#45827) by @zucchini-nlp in [#45827]
* qa: fix ty caching and align CI with local run (#46278) by @tarekziade in [#46278]
* Guard DeviceMesh import in continuous batching (#46205) by @danyalahmed1995 in [#46205]
* Processor compatibility with vLLM  (#46258) by @zucchini-nlp in [#46258]
* Fix PR CI workflow cancellation condition (#46276) by @ydshieh in [#46276]
* [fix] toctree (#46106) by @stevhliu in [#46106]
* add more generic support for distributed trainer tests (#46109) by @kaixuanliu in [#46109]
* add XPU Expectations for florence2 and lfm2_vl model test (#46275) by @kaixuanliu in [#46275]
* Fix `StaticCache` building an empty layer list when `num_kv_shared_layers == 0` (#46235) by @tengomucho in [#46235]
* Fix inverted assertion in remove_handler (#46227) by @SebTardif in [#46227]
* [ShieldGemma2] Support attn_implementation dispatch (#46069) by @YangKai0616 in [#46069]
* [Gemma4] Replace one-hot matmul with F.embedding in position embeddings (#46176) by @Sriniketh24 in [#46176]
* fix: kosmos2.5: properly expand embeddings table (#45835) by @nunq in [#45835]
* find pytest launch error in torch 2.13.0.dev20260526 (#46252) by @sywangyi in [#46252]
* [Test][Kosmos2.5] Add XPU expectations for integration tests (#46135) by @YangKai0616 in [#46135]
* Support FA2 flash_attn_with_kvcache for XPU continuous batching (#46028) by @YangKai0616 in [#46028]
* [`Configs`] Fix layer type validation to include its mlp counterpart (#46220) by @vasqu in [#46220]
* Fix `num_items_in_batch` over-counting for causal LM losses (#46204) by @qgallouedec in [#46204]
* RF-DETR doc fixes (#46244) by @merveenoyan in [#46244]
* Use `main` instead of commit SHA for now (#46241) by @ydshieh in [#46241]
* Enable push event (to main) for PR CI workflow (#46240) by @ydshieh in [#46240]
* fix(hrm_text): Add XPU Expectations for tests (#46214) by @kaixuanliu in [#46214]
* [deepseek_v4] keep hc_head / sinks / position_bias in fp32 (#46198) by @ArthurZucker in [#46198]
* Fix FSDP2 and distributed checkpointing imports for older PyTorch versions (#46141) by @ryota-komatsu in [#46141]
* Fix Gemma4 Array Mask Indexing (#46203) by @petecao in [#46203]
* utils: handle flash_attn missing from importlib packages_distributions without crashing (#45524) by @SAY-5 in [#45524]
* [AMD CI] revert AMD mi325 hf-workflows ref from SHA back to @main (#46213) by @Abdennacer-Badaoui in [#46213]
* [GLM-4.6V] Update with GLM-GA Processor (#46184) by @zRzRzRzRzRzRzR in [#46184]
* update xpu expectation for falcon mamba (#46086) by @sywangyi in [#46086]
* chore: enable Dependabot weekly GitHub Actions bumps (#46157) by @hf-dependantbot-rollout[bot] in [#46157]
* Fix Gemma4 use_bidirectional_attention="all" mask behavior (#46079) by @oliverholworthy in [#46079]
* Fix loading with only 1 device or distributed config (#46197) by @Cyrilvallez in [#46197]
* Fix TypeError on list-typed ignore_keys_at_rope_validation in RoPE config (#46142) by @Charly21r in [#46142]
* Support XPU autocast dtype fallback for FlashAttention (#46199) by @YangKai0616 in [#46199]
* Fix path traversal when saving named chat templates (#46191) by @LinZiyuu in [#46191]
* Fix is_last off-by-one in MaskGenerationPipeline for partial batches (#46136) by @J3r3myPerera in [#46136]
* Fix wrong variable in check_model_type isinstance check (#46080) by @SebTardif in [#46080]
* Enable passing kwargs through RoFormer models (#46171) by @ir2718 in [#46171]
* Update cohere2_moe tp_plan (#46189) by @Cyrilvallez in [#46189]
* Update release tool (#46193) by @Cyrilvallez in [#46193]
* [loading] Fix base_model_prefix issues in conversions (#46067) by @Cyrilvallez in [#46067]
* Bump dev version (#46188) by @Cyrilvallez in [#46188]
* Update self-comment-ci (#46137) by @guarin in [#46137]

## Significant community contributions

The following contributors have made significant changes to the library over the last release:

* @filipinescu
    * [docs] Romanian translation of `contributing.md`, `modular_transformers.md`, `multimodal_processing.md`, `add_vision_processing_components.md`, `add_audio_processing_components.md`, `modeling_rules.md`, `model_output_tracing.md`, `auto_docstring.md`, `testing.md`, `pr_checks.md` and `add_new_model.md` . (#46345)
    * [docs] Romanian translation of  `weightconverter.md`,  `models.md`,  `custom_models.md`,  `monkey_patching.md`,  `fusion_mapping.md`, `how_to_hack_models.md`, `model_sharing.md` and `serialization.md`. (#46309)
    * Romanian translation of README.md, index.md, installation.md, _config.py and quicktour.md. (#46166)
* @remi-or
    * [CB] [Major] Rework manager to have clearer control flow + handle TP (#46070)
* @thisisiron
    * Add Deepseek-OCR-2 model (#45075)
* @kaixuanliu
    * Add Expectations for pipeline token classification tests (#46151)
    * fix series of bugs for model parallel beam search (#46280)
    * add more generic support for distributed trainer tests (#46109)
    * add XPU Expectations for florence2 and lfm2_vl model test (#46275)
    * Fix model parallel issue for altclip model and ChineseClip model (#45487)
    * Model parallel fix (#46230)
    * fix(hrm_text): Add XPU Expectations for tests (#46214)
    * Fix model parallel bugs for Gemma4 (#45817)
    * Fix bnb 4bit/8bit quantization drop chunked tensors bug (#46210)
    * fix model parallel device mismatch issue in `create_bidirectional_mask` (#46221)
    * Fix a regression in encoder-decoder generation cache initialization (#46111)
* @shadeMe
    * feat: Add support for JetBrains' `Mellum` v2 code generation model (#46112)
* @vasqu
    * [`Revert`] FSDP+Dtensor refactor related changes (#46246)
    * [`Configs`] Fix layer type validation to include its mlp counterpart (#46220)
* @zRzRzRzRzRzRzR
    * [GLM-4.6V] Update with GLM-GA Processor (#46184)
* @eustlb
    * 🚨 [ALM] Add base model without head (#45534)

