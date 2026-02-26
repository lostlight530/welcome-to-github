# ℹ️ Intel: huggingface/transformers v5.2.0
> Source: GitHub Releases
> Date: 2026-02-16T18:55:53Z

## 📝 Summary
v5.2.0: GLM-5, Qwen3.5, Voxtral Realtime, VibeVoice Acoustic Tokenizer

## 🔍 Changelog (Extract)
## New Model additions

### VoxtralRealtime

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/80e37670-6d70-402b-8c8e-ccfb8c32df2d" />

VoxtralRealtime is a streaming speech-to-text model from [Mistral AI](https://mistral.ai), designed for real-time automatic speech recognition (ASR). Unlike the offline [Voxtral](./voxtral) model which processes complete audio files, VoxtralRealtime is architected for low-latency, incremental transcription by processing audio in chunks as they arrive.

The model combines an audio encoder with a Mistral-based language model decoder, using time conditioning embeddings and causal convolutions with padding caches to enable efficient streaming inference.

* Add Voxtral Realtime (#43769) by @eustlb

### GLM-5 - GlmMoeDsa

<img width="947" height="638" alt="image" src="https://github.com/user-attachments/assets/4c4fff37-7f40-4e86-b4a0-db718f45c93b" />

The zAI team launches GLM-5, and introduces it as such:

> GLM-5, targeting complex systems engineering and long-horizon agentic tasks. Scaling is still one of the most important ways to improve the intelligence efficiency of Artificial General Intelligence (AGI). Compared to GLM-4.5, GLM-5 scales from 355B parameters (32B active) to 744B parameters (40B active), and increases pre-training data from 23T to 28.5T tokens. GLM-5 also integrates DeepSeek Sparse Attention (DSA), largely reducing deployment cost while preserving long-context capacity.
> 
> Reinforcement learning aims to bridge the gap between competence and excellence in pre-trained models. However, deploying it at scale for LLMs is a challenge due to the RL training inefficiency. To this end, we developed [slime](https://github.com/THUDM/slime), a novel asynchronous RL infrastructure that substantially improves training throughput and efficiency, enabling more fine-grained post-training iterations. With advances in both pre-training and post-training, GLM-5 delivers s... (truncated)

## 🤖 Cognitive Analysis Required
- [ ] Is this a major version update? (False)
- [ ] Does it conflict with existing 'tech_stack' nodes?
- [ ] Action: Run `nexus.py add` or `nexus.py connect` to integrate.
