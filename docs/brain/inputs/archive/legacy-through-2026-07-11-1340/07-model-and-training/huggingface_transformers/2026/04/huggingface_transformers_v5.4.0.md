# ℹ️ Intel Report: huggingface/transformers
## 🎯 监控目标 (Target)
> huggingface/transformers

## 🚀 新版本发布 (New Release)
> Version: v5.4.0
> Date: 2026-04-01T22:36:40.522484

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready ⚠️ Breaking-Change 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 110/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

## New Model additions

### VidEoMT

<img width="1480" height="460" alt="image" src="https://github.com/user-attachments/assets/bec6fc25-b0ab-4227-8c2b-a838554f37f3" />

Video Encoder-only Mask Transformer (VidEoMT) is a lightweight encoder-only model for online video segmentation built on a plain Vision Transformer (ViT). It eliminates the need for dedicated tracking modules by introducing a lightweight query propagation mechanism that carries information across frames and employs a query fusion strategy that combines propagated queries with temporally-agnostic learned queries. VidEoMT achieves competitive accuracy while being 5x-10x faster than existing approaches, running at up to 160 FPS with a ViT-L backbone.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/videomt) | [Paper](https://huggingface.co/papers/2602.17807)
* Add VidEoMT (#44285) by @NielsRogge in [#44285](https://github.com/huggingface/transformers/pull/44285)

### UVDoc

<img width="1765" height="875" alt="image" src="https://github.com/user-attachments/assets/365e510e-8fb8-46cb-8f4b-e8b7082f0ae2" />

UVDoc is a machine learning model designed for document image rectification and correction. The main purpose of this model is to carry out geometric transformation on images to correct document distortion, inclination, perspective deformation and other problems in document images. It provides both single input and batched inference capabilities for processing distorted document images.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/uvdoc)
* [Model] Add UVDoc Model Support (#43385) by @XingweiDeng in [#43385](https://github.com/huggingface/transformers/pull/43385)

### Jina Embeddings v3

<img width="595" height="513" alt="image" src="https://github.com/user-attachments/assets/2aee0692-8286-4c6b-98db-847b95ab2d40" />

The Jina-Embeddings-v3 is a multilingual, multi-task text embedding model designed for a variety of NLP applications. Based on the XLM-RoBERTa architecture, this model supports Rotary Position Embeddings (RoPE) replacing absolute position embeddings to support long input sequences up to 8192 tokens. Additionally, it features 5 built-in Task-Specific LoRA Adapters that allow the model to generate task-specific embeddings (e.g., for retrieval vs. classification) without increasing inference latency significantly.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/jina_embeddings_v3) | [Paper](https://huggingface.co/papers/2409.10173)
* Add `Jina-Embeddings-V3` Model (#44251) by @Sai-Suraj-27 in [#44251](https://github.com/huggingface/transformers/pull/44251)

### Mistral4

<img width="2429" height="1787" alt="image" src="https://github.com/user-attachments/assets/a6feb0da-8504-4eab-be65-22d6c676336f" />

Mistral 4 is a powerful hybrid model with the capability of acting as both a general instruction model and a reasoning model.
