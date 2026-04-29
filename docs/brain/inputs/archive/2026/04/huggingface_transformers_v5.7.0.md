# ℹ️ Intel Report: huggingface/transformers
## 🎯 监控目标 (Target)
> huggingface/transformers

## 🚀 新版本发布 (New Release)
> Version: v5.7.0
> Date: 2026-04-29T22:56:01.242884

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 100/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

# Release v5.7.0


## New Model additions

### Laguna

<img width="699" height="176" alt="image" src="https://github.com/user-attachments/assets/d3bae269-bea7-4ddf-a53f-d4718befdb17" />

Laguna is Poolside's mixture-of-experts language model family that extends standard SwiGLU MoE transformers with two key innovations. It features per-layer head counts allowing different decoder layers to have different query-head counts while sharing the same KV cache shape, and implements a sigmoid MoE router with auxiliary-loss-free load balancing that uses element-wise sigmoid of gate logits plus learned per-expert bias for router scoring.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/laguna)
* Laguna XS.2 implementation (#45673) by @joerowell in [#45673](https://github.com/huggingface/transformers/pull/45673)

### DEIMv2

<img width="2874" height="908" alt="image" src="https://github.com/user-attachments/assets/fc8c59fe-f964-42ce-ae8e-c7fcace9beb7" />

DEIMv2 (DETR with Improved Matching v2) is a real-time object detection model that extends DEIM with DINOv3 features and spans eight model sizes from X to Atto for diverse deployment scenarios. It uses a Spatial Tuning Adapter (STA) for larger variants to convert DINOv3's single-scale output into multi-scale features, while ultra-lightweight models employ pruned HGNetv2 backbones. The unified design achieves superior performance-cost trade-offs, with DEIMv2-X reaching 57.8 AP with only 50.3M parameters and DEIMv2-S being the first sub-10M model to exceed 50 AP on COCO.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/deimv2) | [Paper](https://huggingface.co/papers/2509.20787)
* model: Add DEIMv2 to Transformers (#44339) by @harshaljanjani in [#44339](https://github.com/huggingface/transformers/pull/44339)



## Attention

Several attention-related bugs were fixed across multiple models, including a cross-attention cache type error in T5Gemma2 for long inputs, incorrect cached forward behavior in Qwen3.5's gated-delta-net linear attention, and a crash in GraniteMoeHybrid when no Mamba layers are present. Attention function dispatch was also updated to align with the latest model implementations.


* Fix cross-attention cache layer type for T5Gemma2 long inputs (#45540) by @Beichen-Ma in [#45540]
* [Qwen3.5] Fix GDN linear attention multi-token cached forward (#45513) by @kashif in [#45513]
* Fix GraniteMoeHybrid _update_mamba_mask crash on attention-only models (#45514) by @tianhaocui in [#45514]
* Align latest model attention function dispatch (#45598) by @Cyrilvallez in [#45598]



## Tokenizers

There was a bug in AutoTokenizer that caused the wrong tokenizer class to be initialized. This caused regressions in models like DeepSeek R1. 

* change got reverted (#45680) by @itazap in [#45680]


## Generation

Continuous batching generation received several fixes and improvements, includin
