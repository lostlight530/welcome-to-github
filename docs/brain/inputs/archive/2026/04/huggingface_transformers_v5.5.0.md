# ℹ️ Intel Report: huggingface/transformers
## 🎯 监控目标 (Target)
> huggingface/transformers

## 🚀 新版本发布 (New Release)
> Version: v5.5.0
> Date: 2026-04-04T15:50:57.129148

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready ⚠️ Breaking-Change

## 🛡️ 信任评分 (Trust Score)
> Score: 100/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

# Release v5.5.0

<img width="2786" height="1504" alt="image" src="https://github.com/user-attachments/assets/6c8c878f-042b-4858-9f64-73fd9ccd7e4b" />

## New Model additions

### Gemma4

[Gemma 4](INSET_PAPER_LINK) is a multimodal model with pretrained and instruction-tuned variants, available in 1B, 13B, and 27B parameters. The architecture is mostly the same as the previous Gemma versions. The key differences are a vision processor that can output images of fixed token budget and a spatial 2D RoPE to encode vision-specific information across height and width axis.

<img width="1478" height="1374" alt="image" src="https://github.com/user-attachments/assets/9d88bd1b-02ea-4829-b7d0-fac0e347d436" />


You can find all the original Gemma 4 checkpoints under the [Gemma 4](https://huggingface.co/collections/google/gemma-4-release-67c6c6f89c4f76621268bb6d) release.

The key difference from previous Gemma releases is the new design to process **images of different sizes** using a **fixed-budget number of tokens**. Unlike many models that squash every image into a fixed square (like 224×224), Gemma 4 keeps the image's natural aspect ratio while making it the right size. There a a couple constraints to follow:
- The total number of pixels must fit within a patch budget
- Both height and width must be divisible by **48** (= patch size 16 × pooling kernel 3)

> [!IMPORTANT]
> Gemma 4 does **not** apply the standard ImageNet mean/std normalization that many other vision models use. The model's own patch embedding layer handles the final scaling internally (shifting values to the [-1, 1] range).

The number of "soft tokens" (aka vision tokens) an image processor can produce is configurable. The supported options are outlined below and the default is **280 soft tokens** per image.


| Soft Tokens | Patches (before pooling) | Approx. Image Area |
|:-----------:|:------------------------:|:-------------------:|
| 70          | 630                      | ~161K pixels        |
| 140         | 1,260                    | ~323K pixels        |
| **280**     | **2,520**                | **~645K pixels**    |
| 560         | 5,040                    | ~1.3M pixels        |
| 1,120       | 10,080                   | ~2.6M pixels        |


To encode positional information for each patch in the image, Gemma 4 uses a learned 2D position embedding table. The position table stores up to 10,240 positions per axis, which allows the model to handle very large images. Each position is a learned vector of the same dimensions as the patch embedding. The 2D RoPE which Gemma 4 uses independently rotate half the attention head dimensions for the x-axis and the other half for the y-axis. This allows the model to understand spatial relationships like "above," "below," "left of," and "right of."

### NomicBERT

NomicBERT is a BERT-inspired encoder model that applies Rotary Position Embeddings (RoPE) to create reproducible long context text embeddi
