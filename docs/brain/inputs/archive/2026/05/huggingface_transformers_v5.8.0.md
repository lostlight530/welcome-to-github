# ℹ️ Intel Report: huggingface/transformers
## 🎯 监控目标 (Target)
> huggingface/transformers

## 🚀 新版本发布 (New Release)
> Version: v5.8.0
> Date: 2026-05-11T03:46:53.099773

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: ⚠️ Breaking-Change 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 100/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

# Release v5.8.0


## New Model additions

### DeepSeek-V4

<img width="6604" height="3574" alt="image" src="https://github.com/user-attachments/assets/4c0fdb29-f770-463c-a97b-d24438896a4c" />

DeepSeek-V4 is the next-generation MoE (Mixture of Experts) language model from DeepSeek that introduces several architectural innovations over DeepSeek-V3. The architecture replaces Multi-head Latent Attention (MLA) with a hybrid local + long-range attention design, swaps residual connections for Manifold-Constrained Hyper-Connections (mHC), and bootstraps the first few MoE layers with a static token-id → expert-id hash table. This implementation covers DeepSeek-V4-Flash, DeepSeek-V4-Pro, and their -Base pretrained variants, which share the same architecture but differ in width, depth, expert count and weights.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/deepseek_v4) | [Paper](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash/blob/main/DeepSeek_V4.pdf)
* Add DeepSeek V4 (#45643) by @ArthurZucker in [#45643](https://github.com/huggingface/transformers/pull/45643)

### Gemma 4 Assistant

<img width="2000" height="400" alt="image" src="https://github.com/user-attachments/assets/02c79b0b-a172-4495-b09d-a6a4b625ee66" />

Gemma 4 Assistant is a small, text-only model that enables speculative decoding for Gemma 4 models using the Multi-Token Prediction (MTP) method and associated candidate generator. The model shares the same Gemma4TextModel backbone as other Gemma 4 models but uses KV sharing throughout the entire model, allowing it to reuse the KV cache populated by the target model and skip the pre-fill phase entirely. This architecture includes cross-attention to make the most of the target model's context, allowing the assistant to accurately predict more drafted tokens per drafting round.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/gemma4_assistant)
* First model (#45788) by @SindhuRaghuram97 in [#45788](https://github.com/huggingface/transformers/pull/45788)

### GraniteSpeechPlus

<img width="1310" height="930" alt="image" src="https://github.com/user-attachments/assets/94fc3730-742c-4b9e-ab6a-ed2e5c75d0bf" />

Granite Speech Plus is a variant of Granite Speech that enhances the projector by consuming the concatenation of the encoder's final hidden states with an arbitrary subset of its intermediate hidden states along the feature dimension. It is a multimodal speech-to-text model that can transcribe audio, provide speaker annotation and word level timestamps by responding to text prompts. The model inherits the same architecture components as Granite Speech including the speech encoder, query transformer projector, language model, and optional LoRA adapter.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/granite_speech_plus)
* Support for a new Granite-Speech-Plus model (#45695) by @zvik in [#45695
