# ℹ️ Intel Report: vllm-project/vllm
## 🎯 监控目标 (Target)
> vllm-project/vllm

## 🚀 新版本发布 (New Release)
> Version: v0.19.1
> Date: 2026-04-18T22:34:08.790223

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready

## 🛡️ 信任评分 (Trust Score)
> Score: 90/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

This is a patch release on top of `v0.19.0` with Transformers v5.5.4 upgrade and bug fixes for Gemma4:
- Update to transformers v5 (#30566)
- [Bugfix] Fix invalid JSON in Gemma 4 streaming tool calls by stripping partial delimiters (#38992)
- [Bugfix][Frontend] Fix Gemma4 streaming HTML duplication after tool calls (#38909)
- [Bugfix] Fix Gemma4 streaming tool call corruption for split boolean/number values (#39114)
- [Tool] adjust_request to reasoning parser, and Gemma4 fixes (#39027)
- [Gemma4] Support quantized MoE (#39045)
- Add Gemma4 Eagle3 support (#39450)
- [Gemma4][Bugfix]: Enable Gemma4ForCasualLM to load lora adapters correctly (#38844)
- [Bugfix] Fix Gemma4 tool parser converting bare null to string "null" (#39679)
- [Model] Fix Gemma 4 token repetition by dynamic BOS injection for PT models (#39842)
- fix(kimi_k25): resolve media_placeholder_token_id from tokenizer (#39344)


