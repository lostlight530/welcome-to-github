# ℹ️ Intel: vllm-project/vllm v0.17.1
> Source: GitHub Releases
> Date: 2026-03-11T22:26:33.446219

## 📝 Summary
v0.17.1

## 🔍 Changelog (Extract)
This is a patch release on top of `v0.17.0` to address a few issues:
- Fix passing of activation_type to trtllm fused MoE NVFP4 and FP8 (#36017)
- Fix/resupport nongated fused moe triton (#36412)
- Re-enable EP for trtllm MoE FP8 backend (#36494)
- [Mamba][Qwen3.5] Zero freed SSM cache blocks on GPU (#35219)
- Fix TRTLLM Block FP8 MoE Monolithic (#36296)
- [DSV3.2][MTP] Optimize Indexer MTP handling (#36723)
