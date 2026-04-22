# ℹ️ Intel Report: huggingface/transformers
## 🎯 监控目标 (Target)
> huggingface/transformers

## 🚀 新版本发布 (New Release)
> Version: v5.6.0
> Date: 2026-04-22T22:46:55.645298

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready ⚠️ Breaking-Change 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 110/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

# Release v5.6.0


## New Model additions

### OpenAI Privacy Filter

OpenAI Privacy Filter is a bidirectional token-classification model for personally identifiable information (PII) detection and masking in text. It is intended for high-throughput data sanitization workflows where teams need a model that they can run on-premises that is fast, context-aware, and tunable. The model labels an input sequence in a single forward pass, then decodes coherent spans with a constrained Viterbi procedure, predicting probability distributions over 8 privacy-related output categories for each input token.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/openai_privacy_filter)
* [`Privacy Filter`] Add model (#45580) by @vasqu in [#45580](https://github.com/huggingface/transformers/pull/45580)

### QianfanOCR

Qianfan-OCR is a 4B-parameter end-to-end document intelligence model developed by Baidu that performs direct image-to-text conversion without traditional multi-stage OCR pipelines. It supports a broad range of prompt-driven tasks including structured document parsing, table extraction, chart understanding, document question answering, and key information extraction all within one unified model. The model features a unique "Layout-as-Thought" capability that generates structured layout representations before producing final outputs, making it particularly effective for complex documents with mixed element types.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/qianfan_ocr) | [Paper](https://huggingface.co/papers/2603.13398)
* add Qianfan-OCR model definition (#45280) by @marvinzh in [#45280](https://github.com/huggingface/transformers/pull/45280)

### SAM3-LiteText

SAM3-LiteText is a lightweight variant of SAM3 that replaces the heavy SAM3 text encoder (353M parameters) with a compact MobileCLIP-based text encoder optimized through knowledge distillation, while keeping the SAM3 ViT-H image encoder intact. This reduces text encoder parameters by up to 88% while maintaining segmentation performance comparable to the original model. The model enables efficient vision-language segmentation by addressing the redundancy found in text prompting for segmentation tasks.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/sam3_lite_text) | [Paper](https://huggingface.co/papers/2602.12173)
* Add SAM3-LiteText (#44320) by @NielsRogge in [#44320](https://github.com/huggingface/transformers/pull/44320)

### SLANet

SLANet and SLANet_plus are lightweight models designed for table structure recognition, focusing on accurately recognizing table structures in documents and natural scenes. The model improves accuracy and inference speed by adopting a CPU-friendly lightweight backbone network PP-LCNet, a high-low-level feature fusion module CSP-PAN, and a feature decoding module SLA Head that aligns structural and positional information
