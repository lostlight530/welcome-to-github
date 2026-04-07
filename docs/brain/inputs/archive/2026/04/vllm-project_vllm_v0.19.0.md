# ℹ️ Intel Report: vllm-project/vllm
## 🎯 监控目标 (Target)
> vllm-project/vllm

## 🚀 新版本发布 (New Release)
> Version: v0.19.0
> Date: 2026-04-07T11:36:20.308899

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready ⚠️ Breaking-Change 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 110/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

# vLLM v0.19.0

## Highlights
This release features 448 commits from 197 contributors (54 new)!

* **Gemma 4 support**: Full Google Gemma 4 architecture support including MoE, multimodal, reasoning, and tool-use capabilities (#38826, #38847). Requires `transformers>=5.5.0`. We recommend using pre-built docker image `vllm/vllm-openai:gemma4` for out of box usage.
* **Zero-bubble async scheduling + speculative decoding**: Async scheduling now supports speculative decoding with zero-bubble overlap, significantly improving throughput (#32951).
* **Model Runner V2 maturation**: MRV2 gains piecewise CUDA graphs for pipeline parallelism (#35162), spec decode rejection sampler with greedy/logprobs support (#37238, #37237), multi-modal embeddings for spec decode (#36097), streaming inputs (#37028), and EPLB support (#37488).
* **ViT Full CUDA Graphs**: Vision encoders (ViT) now support full CUDA graph capture for reduced overhead (#35963).
* **General CPU KV cache offloading**: A simple yet general CPU KV cache offloading mechanism for V1, with pluggable cache policy and block-level preemption handling (#37160, #37874, #34805, #36642, #37853).
* **DBO (Dual-Batch Overlap) generalization**: The microbatch optimization (DBO) now works with general models, not just specific architectures (#37926).
* **NVIDIA B300/GB300 (SM 10.3) support**: Allreduce fusion enabled by default with tuned all-reduce communicator (#37755, #37756).
* **Transformers v5 compatibility**: Broad compatibility fixes across many models for HuggingFace Transformers v5 (#37681, #38127, #38090, #38247, #38410).

### Model Support
* New architectures: Gemma 4 (#38826), Cohere ASR (#35809), Cohere Transcribe (#38120), ColQwen3.5 4.5B (#36887), LFM2-ColBERT-350M (#37528), Granite 4.0 1B Speech (#38019), Qwen3-ForcedAligner (#35367).
* Speculative decoding: Eagle3 for Pixtral (#37182), EagleMistralLarge3 fix (#37232).
* LoRA expansion: H2OVL tower/connector LoRA (#31696), `--lora-target-modules` to restrict LoRA to specific modules (#34984), `language_model_only` respected (#37375), Mistral3 fix (#36928), Qwen3.5 fix (#36976), out-of-tree ops replacement (#37181).
* Model fixes: NemotronH MTP + Chunked Prefill (#35447), Qwen3-VL video timestamps (#37439), Qwen3.5 GDN quantized models (#37448), Qwen3Next A_log FP32 (#37810), JAIS ALiBi (#37820), RoBERTa CUDA graph position IDs (#37873), AudioFlamingo3/MusicFlamingo (#37643), Music Flamingo loading (#35535), bge-m3 task selection (#37632), Nemotron Parse loading (#37407), GLM OCR patch merger (#37962), PaddleOCR checkpoint compat (#38232), DeepSeek v3.2 params (#33703), MiniMax NVFP4 weight loading (#37214), gated model HF token (#37920), Parakeet OOM on long audio (#36671).
* Features: Temporal compression for Nemotron-3-VL videos (#36808), NemotronH Puzzle + MTP (#37803), torch.compile for InternVL vision encoder (#38049), multiple embedding types in single call (#35829).
* Performance: GLM-4.xv ViT optimization (#37779).

