# ℹ️ Intel: vllm-project/vllm v0.17.0
> Source: GitHub Releases
> Date: 2026-03-07T13:10:27.380672
> **Analysis**: 🏷️ Edge-Ready ⚠️ Breaking-Change 🔗 Agent-Protocol

## 📝 Summary
v0.17.0

## 🔍 Changelog (Extract)
# vLLM v0.17.0

**Known Issue**: If you are on CUDA 12.9+ and encounter a `CUBLAS_STATUS_INVALID_VALUE` error, this is caused by a CUDA library mismatch. To resolve, try one of the following:
1. Remove the path to system CUDA shared library files (e.g. `/usr/local/cuda`) from `LD_LIBRARY_PATH`, or simply `unset LD_LIBRARY_PATH`.
2. Install vLLM with `uv pip install vllm --torch-backend=auto`.
3. Install vLLM with `pip install vllm --extra-index-url https://download.pytorch.org/whl/cu129` (change the CUDA version to match your system).

## Highlights

This release features 699 commits from 272 contributors (48 new)!

* **PyTorch 2.10 Upgrade**: This release upgrades to **PyTorch 2.10.0**, which is a breaking change for environment dependencies.
* **FlashAttention 4 Integration**: vLLM now supports the **FlashAttention 4** backend (#32974), bringing next-generation attention performance.
* **Model Runner V2 Maturation**: Model Runner V2 has reached a major milestone with **Pipeline Parallel** (#33960), **Decode Context Parallel** (#34179), **Eagle3 speculative decoding with CUDA graphs** (#35029, #35040), **pooling model support** (#35120), piecewise & mixed CUDA graph capture (#32771), DP+EP for spec decoding (#35294), and a new ModelState architecture. Design docs are now available (#35819).
* **Qwen3.5 Model Family**: Full support for the **Qwen3.5** model family (#34110) featuring GDN (Gated Delta Networks), with FP8 quantization, MTP speculative decoding, and reasoning parser support.
* **New `--performance-mode` Flag**: A new `--performance-mode {balanced, interactivity, throughput}` flag (#34936) simplifies performance tuning for common deployment scenarios.
* **Anthropic API Compatibility**: Added support for **Anthropic thinking blocks** (#33671), **`count_tokens` API** (#35588), `tool_choice=none` (#35835), and streaming/image handling fixes.
* **Weight Offloading V2 with Prefetching**: The weight offloader now **hides onloading latency via ...
