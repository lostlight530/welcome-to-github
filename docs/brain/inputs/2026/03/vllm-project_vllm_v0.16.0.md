# ℹ️ Intel: vllm-project/vllm v0.16.0
> Source: GitHub Releases
> Date: 2026-02-25T19:58:49Z

## 📝 Summary
v0.16.0

## 🔍 Changelog (Extract)
# vLLM v0.16.0
Please note that this release was branch cut on Feb 8, so any features added to vLLM after that date is not included.

## Highlights

This release features 440 commits from 203 contributors (7 new)!

* **Async scheduling + Pipeline Parallelism** is now fully supported, delivering **30.8% E2E throughput improvement** and **31.8% TPOT improvement** (#32618).
* **Realtime API**: A new WebSocket-based Realtime API enables streaming audio interactions (#33187), building on the Voxtral realtime infrastructure.
* **RLHF workflow improvements**: Native NCCL-based weight syncing API (#31943), layerwise weight reloading for QeRL (#32133), and engine pause/resume with request preservation (#32351).
* **Unified Parallel Drafting** for speculative decoding (#32887), plus spec decode now works with structured outputs (#33374) and penalty application in Model Runner V2 (#33251).
* **Major XPU platform overhaul**: Deprecated IPEX in favor of vllm-xpu-kernels (#33379), adding MoE (#33659), MXFP4 MoE (#33679), WNA16 (#33973), scaled_mm (#34117), and FP8 MoE (#34202) support.

### Model Support
* New architectures: GLM-OCR with MTP (#33005), Qwen3-ASR (#33312), DeepSeek-OCR-2 (#33165), Intern-S1-Pro (#33636), MiniCPM-o 4.5 (#33431), openPangu7B-VL (#32449), NemotronHPuzzle heterogeneous (#32549), MusicFlamingo (#32696), FunAudioChat (#2), ColBERT late interaction (#33686), voyage-4-nano (#33720), GLM-5 (#34124).
* Speculative decoding: EAGLE3 for Hunyuan/HunyuanVL (#33035), AFMoE (#33111), Mistral3 (#33939).
* LoRA expansion: Gemma3 vision components (#32764), Nemotron-H MTP models (#32265), Qwen3 output embedding (#29816). Optimized fused MoE-LoRA kernel indexing (#32770, #32774), unpermute-aware fused MoE LoRA path (#32655), reduced kernel overhead for fewer active LoRAs with multiple CUDA graphs (#32005).
* Features: Qwen3-Omni transcription (#29828), Mistral Large 3 with FlashInfer MoE (#33174), LFM2 SigLIP2 intermediate encoder layers (#33370), Qwe... (truncated)

## 🤖 Cognitive Analysis Required
- [ ] Is this a major version update? (False)
- [ ] Does it conflict with existing 'tech_stack' nodes?
- [ ] Action: Run `nexus.py add` or `nexus.py connect` to integrate.
