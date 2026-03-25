# ℹ️ Intel Report: huggingface/transformers
## 🎯 监控目标 (Target)
> huggingface/transformers

## 🚀 新版本发布 (New Release)
> Version: v5.3.0
> Date: 2026-03-25T09:56:13.358610

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready ⚠️ Breaking-Change

## 🛡️ 信任评分 (Trust Score)
> Score: 100/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

## New Model additions

### EuroBERT

<img width="1080" height="1080" alt="image" src="https://github.com/user-attachments/assets/33603f42-5435-421a-9641-baf72faacb22" />

EuroBERT is a multilingual encoder model based on a refreshed transformer architecture, akin to Llama but with bidirectional attention. It supports a mixture of European and widely spoken languages, with sequences of up to 8192 tokens.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/eurobert) | [Paper](https://huggingface.co/papers/2503.05500) | [Blog Post](https://huggingface.co/blog/EuroBERT/release)
* Add eurobert (#39455) by @ArthurZucker in [#39455](https://github.com/huggingface/transformers/pull/39455)

### VibeVoice ASR

<img width="673" height="464" alt="image" src="https://github.com/user-attachments/assets/e4093a6b-fc6e-4136-a15d-2fcd7b27a69e" />

VibeVoice ASR is an automatic speech recognition model from Microsoft that combines acoustic and semantic audio tokenizers with a causal language model for robust speech-to-text transcription. The model uses VibeVoice's acoustic and semantic tokenizers that process audio at 24kHz, paired with a Qwen2-based language decoder for generating transcriptions. It can process up to 60 minutes of continuous audio input, supports customized hotwords, performs joint ASR/diarization/timestamping, and handles over 50 languages with code-switching support.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/vibevoice_asr) | [Paper](https://huggingface.co/papers/2601.18184)
* Add VibeVoice ASR (#43625) by @ebezzam in [#43625](https://github.com/huggingface/transformers/pull/43625)

### TimesFM2.5

<img width="799" height="497" alt="image" src="https://github.com/user-attachments/assets/1e486803-1b68-496b-aa67-4c3f2055fbeb" />

TimesFM 2.5 is a pretrained time-series foundation model that uses a decoder-only attention architecture with input patching for forecasting. The model is designed to provide accurate zero-shot forecasts across different domains, forecasting horizons and temporal granularities without requiring dataset-specific training. It builds on the original TimesFM architecture with enhancements including rotary attention, QK normalization, per-dimension attention scaling, and continuous quantile prediction.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/timesfm2_5) | [Paper](https://huggingface.co/papers/2310.10688)
* Timesfm 2.5 (#41763) by @kashif in [#41763](https://github.com/huggingface/transformers/pull/41763)

### PP-DocLayoutV2

<img width="1440" height="436" alt="image" src="https://github.com/user-attachments/assets/31d6609b-ef42-4f15-8c34-eeb2c0d679a9" />

PP-DocLayoutV2 is a dedicated lightweight model for layout analysis, focusing specifically on element detection, classification, and reading order prediction. The model is composed of two sequentially connected network
