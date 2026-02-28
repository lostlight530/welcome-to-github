# ℹ️ Intel: vllm-project/vllm v0.15.1
> Source: GitHub Releases
> Date: 2026-02-04T20:48:08Z

## 📝 Summary
v0.15.1

## 🔍 Changelog (Extract)
v0.15.1 is a patch release with security fixes, RTX Blackwell GPU fixes support, and bug fixes.

## Security

- **CVE-2025-69223**: Updated aiohttp dependency (#33621)
- **CVE-2026-0994**: Updated Protobuf dependency (#33619)

## Highlights

### Bugfix Hardware Support
- **RTX Blackwell (SM120)**: Fixed NVFP4 MoE kernel support for RTX Blackwell workstation GPUs. Previously, NVFP4 MoE models would fail to load on these GPUs (#33417)
- **FP8 kernel selection**: Fixed FP8 CUTLASS group GEMM to properly fall back to Triton kernels on SM120 GPUs (#33285)

### Model Support
- **Step-3.5-Flash**: New model support (#33523)

### Bugfix Model Support
- **Qwen3-VL-Reranker**: Fixed model loading (#33298)
- **Whisper**: Fixed FlashAttention2 with full CUDA graphs (#33360)

### Performance
- **torch.compile cold-start**: Fixed regression that increased cold-start compilation time (Llama3-70B: ~88s → ~22s) (#33441)
- **MoE forward pass**: Optimized by caching layer name computation (#33184)

### Bug Fixes
- Fixed prefix cache hit rate of 0% with GPT-OSS style hybrid attention models (#33524)
- Enabled Triton MoE backend for FP8 per-tensor dynamic quantization (#33300)
- Disabled unsupported Renormalize routing methods for TRTLLM per-tensor FP8 MoE (#33620)
- Fixed speculative decoding metrics crash when no tokens generated (#33729)
- Disabled fast MoE cold start optimization with speculative decoding (#33624)
- Fixed ROCm skinny GEMM dispatch logic (#33366)

### Dependencies
- Pinned LMCache >= v0.3.9 for API compatibility (#33440)

## New Contributors 🎉
* @zaristei2 made their first contribution in https://github.com/vllm-project/vllm/pull/33621

**Full Changelog**: https://github.com/vllm-project/vllm/compare/v0.15.0...v0.15.1... (truncated)

## 🤖 Cognitive Analysis Required
- [ ] Is this a major version update? (False)
- [ ] Does it conflict with existing 'tech_stack' nodes?
- [ ] Action: Run `nexus.py add` or `nexus.py connect` to integrate.
