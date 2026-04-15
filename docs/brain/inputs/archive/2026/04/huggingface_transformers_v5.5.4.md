# ℹ️ Intel Report: huggingface/transformers
## 🎯 监控目标 (Target)
> huggingface/transformers

## 🚀 新版本发布 (New Release)
> Version: v5.5.4
> Date: 2026-04-15T21:49:08.792031

## 🛡️ 信任评分 (Trust Score)
> Score: 80/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

# Patch release v5.5.4

This is mostly some fixes that are good to have asap, mostly for tokenizers;
** Fix Kimi-K2.5 tokenizer regression and _patch_mistral_regex Attribute… (#45305) by ArthurZucker

For training:
** Fix #45305 + add regression test GAS (#45349) by florian6973, SunMarc
** Fix IndexError with DeepSpeed ZeRO-3 when kernels rotary is active (#…) by ArthurZucker

And for Qwen2.5-VL :
** Fix Qwen2.5-VL temporal RoPE scaling applied to still images (#45330) by Kash6, zucchini-nlp
