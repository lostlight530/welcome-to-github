# ℹ️ Intel Report: vllm-project/vllm
## 🎯 监控目标 (Target)
> vllm-project/vllm

## 🚀 新版本发布 (New Release)
> Version: v0.18.0
> Date: 2026-03-26T07:10:54.004732

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready ⚠️ Breaking-Change

## 🛡️ 信任评分 (Trust Score)
> Score: 100/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

# vLLM v0.18.0

## Known issues
- Degraded accuracy when serving Qwen3.5 with FP8 KV cache on B200 (#37618)
- If you previously ran into `CUBLAS_STATUS_INVALID_VALUE` and had to use a workaround in `v0.17.0`, you can reinstall `torch 2.10.0`. PyTorch published an updated wheel that addresses this bug.

## Highlights

This release features 445 commits from 213 contributors (61 new)!

* **gRPC Serving Support**: vLLM now supports gRPC serving via the new `--grpc` flag (#36169), enabling high-performance RPC-based serving alongside the existing HTTP/REST interface.
* **GPU-less Render Serving**: New `vllm launch render` command (#36166, #34551) enables GPU-less preprocessing and rendering, allowing separation of multimodal preprocessing from GPU inference.
* **NGram GPU Speculative Decoding**: NGram speculative decoding now runs on GPU and is compatible with the async scheduler (#29184), significantly reducing spec decode overhead.
* **KV Cache Offloading Improvements**: Smart CPU offloading that stores only frequently-reused blocks (#35342), plus FlexKV as a new offloading backend (#34328) and support for multiple KV groups in offloading spec (#36610).
* **Elastic Expert Parallelism Milestone 2**: NIXL-EP integration (#35627) enables dynamic GPU scaling for MoE experts, with new `--enable-ep-weight-filter` CLI option (#37351) for faster EP model loading.
* **FlashInfer 0.6.6**: Updated FlashInfer dependency (#36768) with numerous performance and correctness improvements.
* **Responses API Streaming Tool Calls**: The OpenAI Responses API now supports tool/function calling with streaming (#29947).
* **Online Beam Search for ASR**: Beam search support for encoder/decoder models both offline (#36153) and online transcriptions (#36160).
* **Ray No Longer a Default Dependency**: Ray has been removed as a default dependency (#36170) — install it explicitly if needed.

### Model Support
* **New architectures**: Sarvam MoE (#33942), OLMo Hybrid (#32550), HyperCLOVAX-SEED-Think-32B VLM (#31471), HyperCLOVAX-SEED-Think-14B (#37107), Kimi-Audio-7B-Instruct (#36127), ColPali late-interaction retrieval (#36818), ERNIE pooling models (#36385).
* **Speculative decoding**: Eagle3 for Qwen3.5 (#36658), Eagle3 for Kimi K2.5 MLA (#36361), Eagle for Mistral Large 3 with dense layers (#36163).
* **LoRA**: Whisper LoRA (#29856), FP8 LoRA dense kernel (#35242).
* **Multimodal**: Online use_audio_in_video (#36319), audio extraction from MP4 for Nemotron Nano VL (#35539), audio transcription for MP4/M4A/WebM (#35109), expose media_io_kwargs at runtime (#34778), fast media preprocessing for Nano Nemotron VL (#35657).
* **Compatibility**: Gemma/Gemma2 inputs_embeds (#36787), SigLIP/CLIP Transformers v5 (#37200), fused expert weights in Transformers backend (#36997).
* **Performance**: Qwen3 Next fused GDN kernel (#35777), LFM2 tuned H100 MoE configs (#36699).
* **Fixes**: DeepSeek-V3.2 tokenizer space stripping (#37004), Qwen3.5 tool calling (#36774
