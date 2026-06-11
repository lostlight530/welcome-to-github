# ℹ️ Intel Report: huggingface/transformers
## 🎯 监控目标 (Target)
> huggingface/transformers

## 🚀 新版本发布 (New Release)
> Version: v5.11.0
> Date: 2026-06-11T03:31:17.389718

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 100/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

# Release v5.11.0


## New Model additions

### DiffusionGemma

<img width="1240" height="700" alt="image" src="https://github.com/user-attachments/assets/5081e449-6374-4076-bd96-d295c8334ca4" />

DiffusionGemma is engineered to reduce the sequential bottlenecks of standard causal language models by employing an encoder-decoder architecture specifically optimized for inference speed. During inference, DiffusionGemma leverages multi-canvas sampling, where rather than generating one token at a time, the model iteratively denoises a full block of tokens using a diffusion sampler. This block-autoregressive approach facilitates text generation at higher speeds compared to traditional sequential generation methods.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/diffusion_gemma)
* GPU go brr (#46540) by @gante in [#46540](https://github.com/huggingface/transformers/pull/46540)



### DeepSeek-V3.2

<img width="1135" height="671" alt="image" src="https://github.com/user-attachments/assets/24c9694d-eeae-402c-9a98-f7a3971dd9d0" />

DeepSeek-V3.2-Exp is an experimental model from DeepSeek-AI that introduces DeepSeek Sparse Attention (DSA), a trainable, fine-grained sparse attention mechanism designed to improve training and inference efficiency in long-context scenarios. Built on top of DeepSeek-V3.1-Terminus with a 685B-parameter Mixture-of-Experts backbone, it reduces the quadratic cost of attention over long sequences by attending only to a selected subset of past tokens while maintaining virtually identical benchmark performance. The work was extended in DeepSeek-V3.2 which pairs DSA with scalable reinforcement learning and achieves gold-medal level results on competition math and competitive programming benchmarks.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/deepseek_v32) | [Paper](https://huggingface.co/papers/2512.02556)
* Add deepseek 3.2 exp (#41251) by @ArthurZucker in [#41251](https://github.com/huggingface/transformers/pull/41251)


## Kernels

The `KernelConfig` API was extended to support n-to-1 module fusion and parameter transformation, simplifying how custom kernels are integrated with Transformers modules. Additional fixes include resolving a dtype mismatch in the Mamba2 CUDA kernel path for NemotronH/Zamba2, adding fine-grained fp8/fp4 Triton kernel support, and correcting the FalconMamba fast-path warning to recommend `pip install kernels` instead of `mamba-ssm`.


* Extended & simplified n-to-1 kernel fusion via KernelConfig (#46339) by @michaelbenayoun in [#46339]
* Triton finegrained fp8/fp4 (#46407) by @IlyasMoutawwakil in [#46407]
* Fix dtype mismatch in NemotronH/Zamba2 Mamba2 CUDA-kernel path (`out_proj`) (#46487) by @yuekaizhang in [#46487]
* fix(falcon_mamba): recommend `pip install kernels` in fast-path warning (#46343) by @Anai-Guo in [#46343]


## Parallelization

Fixed model parallel beam search bugs in the Qwen2-VL, Qwen2.5-VL, and Qwen3-VL MoE model families, and added documentation for tensor parallelism support with continuous batching.


* [docs] tp for continuous batching (#46019) by @stevhliu in [#46019]
* revisit history parallel beam search tests to avoid unnecessary fix (#46495) by @kaixuanliu in [#46495]
* fix qwen series VL model's model parallel bug (#46316) by @kaixuanliu in [#46316]


## Bugfixes and improvements

* Fix the offsets in processing (#46525) by @zucchini-nlp in [#46525]
* Fix buggy action sha pin (#46534) by @ydshieh in [#46534]
* Fix trailing comma bug in DataCollatorForLanguageModeling example (#46527) by @JemmaUZH in [#46527]
* Fix missing Gemma4Processor._compute_audio_num_tokens (#46416) by @csantosbh in [#46416]
* Fix InternVL models (#46524) by @hmellor in [#46524]
* fix(afmoe): reduce tokens in test_compile_static_cache to avoid flaky bfloat16 drift (#46521) by @ydshieh in [#46521]
* [CB] Add a "max_requests_per_batch" parameter (#46434) by @remi-or in [#46434]
* revamp cv docs and fix rf-detr (#46219) by @merveenoyan in [#46219]
* Update hub metadata (#46379) by @zucchini-nlp in [#46379]
* extend DeepseekV4FlashIntegrationTest to non-cuda device (#46517) by @sywangyi in [#46517]
* [docs] deepgemm (#46361) by @stevhliu in [#46361]
* [fix] regression introduced by #45534 (#46456) by @eustlb in [#46456]
* Use torchvision's native LANCZOS interpolation instead of PIL fallback (#46496) by @NicolasHug in [#46496]
* Add debugging info in `pr-ci-caller.yml` (#46505) by @ydshieh in [#46505]
* Fix tests: 'Cohere2MoeModel' object has no attribute 'hf_device_map' (#46337) by @kaixuanliu in [#46337]
* Bump the actions group across 1 directory with 19 updates (#46414) by @dependabot[bot] in [#46414]
* Log some information in `.github/workflows/pr-ci-post-dashboard-link.yml` (#46499) by @ydshieh in [#46499]
* feat(quantizers): support non-weight param names in TorchAo safetensors loading (#46325) by @agesf in [#46325]
* docs: fix typo in make_list_of_images docstring (#46469) by @ramkumar27072006 in [#46469]
* add XPU expectation for deepseek_ocr2 model tests (#46492) by @kaixuanliu in [#46492]
* Fix sapiens2 tests: add XPU device expectations (#46488) by @kaixuanliu in [#46488]
* Add vLLM smoke test to CI (#46383) by @hmellor in [#46383]
* extend deepseek v4 test to xpu (#46366) by @sywangyi in [#46366]
* Added cosmos3 model (#46146) by @MaciejBalaNV in [#46146]
* fbgemm_fp8:Keep the current device aligned with the input tensor (#46403) by @kaixuanliu in [#46403]
* [Modular] Add `no_inherit_decorators` and fixup wrong RoPE related inheritances  (#46440) by @Bissmella in [#46440]
* skip deepgemm test except cuda (#46090) by @jiqing-feng in [#46090]
* Fix/video classification pipeline video processor (#46256) by @J3r3myPerera in [#46256]
* ci: less flaky test_assisted_decoding_matches_greedy_search_1_same (#46445) by @ydshieh in [#46445]
* Fix flip_back graph break (#46344) by @guarin in [#46344]
* Add the other processors to auto-mappings (#46046) by @zucchini-nlp in [#46046]
* fix: compatibility with torch<=2.7 (#46393) by @andylin-hao in [#46393]
* fix: remove dynamic per-actor Slack ID lookup in ssh-runner workflow (#46327) by @ydshieh in [#46327]
* [docs] Romanian translation of `pipeline_tutorial.md`, `pipeline_gradio.md`, `pipeline_webserver.md` and `add_new_pipeline.md`. (#46388) by @filipinescu in [#46388]
* [docs] gemma4 typos (#46351) by @stevhliu in [#46351]
* [docs] padding-free training (#46333) by @stevhliu in [#46333]
* fix[vLLM x v5]: Default untied embeddings in AudioFlamingo3 and VibeVoice (#46400) by @harshaljanjani in [#46400]
* Fix deepspeed docker (#46108) by @SunMarc in [#46108]
* Fix conversion for clip models (#46406) by @zucchini-nlp in [#46406]
* ci: mention code quality failure in CI dashboard comment (#46415) by @ydshieh in [#46415]
* Fix noisy logging from image_processing module aliases issue - 46298 (#46350) by @skshmjn in [#46350]
* Raise tqdm minimum to 4.60 to match tqdm.contrib.logging import (#46397) by @n0gu-furiosa in [#46397]
* fix(gemma4_unified): conversion script and config bugs (#46398) by @douglas-reid in [#46398]
* [docs] remove sparsity from compressed-tensors (#46387) by @stevhliu in [#46387]
* [CB] Fix crashes when fork is not possible (#46251) by @remi-or in [#46251]
* Improve CI dashboard comment: rename and deduplicate (#46412) by @ydshieh in [#46412]
* Fix missing f-string prefixes in error messages (#46354) by @joaopedroassad in [#46354]
* Add workflow to post CI Grafana dashboard link to PR (#46410) by @ydshieh in [#46410]
* [docs] Romanian translation of `fast_tokenizers.md`, `custom_tokenizers.md`, `tokenizer_summary.md`, `image_processors.md` and `video_processors.md`. (#46356) by @filipinescu in [#46356]
* Clean up new models after release (#46092) by @zucchini-nlp in [#46092]

## Significant community contributions

The following contributors have made significant changes to the library over the last release:

* @ArthurZucker
    * Add deepseek 3.2 exp (#41251)
* @gante
    * GPU go brr (#46540)
* @merveenoyan
    * revamp cv docs and fix rf-detr (#46219)
* @sgerrard
    * Quantization for small models (#46449)
* @MaciejBalaNV
    * Added cosmos3 model (#46146)
* @J3r3myPerera
    * Fix/video classification pipeline video processor (#46256)
* @filipinescu
    * [docs] Romanian translation of `pipeline_tutorial.md`, `pipeline_gradio.md`, `pipeline_webserver.md` and `add_new_pipeline.md`. (#46388)
    * [docs] Romanian translation of `fast_tokenizers.md`, `custom_tokenizers.md`, `tokenizer_summary.md`, `image_processors.md` and `video_processors.md`. (#46356)
