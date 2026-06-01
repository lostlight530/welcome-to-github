# ℹ️ Intel Report: vllm-project/vllm
## 🎯 监控目标 (Target)
> vllm-project/vllm

## 🚀 新版本发布 (New Release)
> Version: v0.22.0
> Date: 2026-06-01T06:58:25.054336

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready ⚠️ Breaking-Change

## 🛡️ 信任评分 (Trust Score)
> Score: 100/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

## Highlights

This release features 459 commits from 230 contributors (63 new)!

* **DeepSeek V4 maturity**: DeepSeek V4 received a major hardening pass this cycle — the model was reorganized into a dedicated `vllm/models/deepseek_v4/` package (#43004, #43039, #43073, #43077, #43149), gained NVFP4 fused MoE support (#42209), full + piecewise CUDA graph (#42604), and MTP speculative decoding (#43385). A large set of fused kernels (MegaMoE, `mhc`, Q-norm, indexer, sparse MLA) and ROCm parity fixes landed alongside accuracy fixes (#42810, #43710).
* **Model Runner V2 advances toward default**: MRv2 added an oracle that selects MRv2 for Qwen3 dense models by default (#39337), sleep-mode weight reload (#42673), `update_config` (#42783), and shared KV-cache layers (#35045), plus many correctness fixes. It now falls back to MRv1 automatically when a KV connector is present (#42955).
* **Experimental Rust frontend**: A new Rust front-end integration landed (#40848), with the implementation moved into the tree (#43283) and a DP Supervisor for data-parallel serving (#40841).
* **Batch invariance, faster**: Batch-invariant inference gained Cutlass FP8 support for a **28.9% end-to-end latency improvement** (#40408), compile-mode support on SM80 (#42456), and an NVFP4 Cutlass linear path (#39912).
* **Multi-tier KV cache offloading**: A new multi-tier KV cache offloading framework (#40020) with a Python filesystem secondary tier (#41735), DSv4 support (#43142), and Mooncake disk offloading (#42689) extends offloading beyond CPU memory.

### Model Support
* New architectures: MiniCPM-V 4.6 (#41254), InternS2 Preview (#42705), OpenVLA (#42654), MolmoWeb `hf_overrides` docs (#42163); EXAONE-4.5 aligned with Transformers update (#42246).
* Speculative decoding: custom callable proposer backend (#39487), post-norm EAGLE-3 speculators (#42764), peagle speculators (#41826), hybrid-attention models in `extract_hidden_states` (#39949), non-MTP speculation for NemotronH (#43130), shared MTP weights in MRv2 (#42538).
* DeepSeek V4: NVFP4 MoE (#42209), CUDA graph full/piecewise (#42604), MTP (#43385), model package refactor (#43004, #43039, #43073, #43077), sparse MLA + compressor refactor (#43149, #43710), MegaMoE input-prep kernel move (#43632).
* Qwen3.5/3.6: GDN output-projection flatten (#42311), GatedDeltaNet Marlin TP≥2 fix (#36329), ViT full CUDA graph (#42151), runai-streamer weight loading for Qwen3.5/MTP/Qwen3-VL (#42521, #42716), KDA chunk-prefill exp2 semantics (#43195).
* Gemma3/Gemma4: mixed-resolution image co-batching crash fix (#42217), MoE routing closure fix (#42250), tool-parser float-corruption fix (#42128), batched vision encoder for image/video (#43169), multi-GPU fix (#42630).
* Kimi-K2.5: skip vision-tower dtype conversion under quantization (#42869), `mm_projector` dtype fix (#42081).
* Cohere: enable Cohere MoE (#43143), pipeline parallelism for Cohere vision (#42819).
* Tool calling: Apertus tool parser (#41154), Qwen3Coder
