# ℹ️ Intel Report: vllm-project/vllm
## 🎯 监控目标 (Target)
> vllm-project/vllm

## 🚀 新版本发布 (New Release)
> Version: v0.18.1
> Date: 2026-04-01T05:46:05.160543

## 🛡️ 信任评分 (Trust Score)
> Score: 80/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

This is a patch release on top of v0.18.0 to address a few issues:
- Change default SM100 MLA prefill backend back to TRT-LLM (#38562)
- Fix mock.patch resolution failure for standalone_compile.FakeTensorMode on Python <= 3.10 (#37158)
- Disable monolithic TRTLLM MoE for Renormalize routing #37605
- Pre-download missing FlashInfer headers in Docker build #38391
- Fix DeepGemm E8M0 accuracy degradation for Qwen3.5 FP8 on Blackwell (#38083)

