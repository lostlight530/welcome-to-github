# ℹ️ Intel Report: google-ai-edge/mediapipe
## 🎯 监控目标 (Target)
> google-ai-edge/mediapipe

## 🚀 新版本发布 (New Release)
> Version: v0.10.33
> Date: 2026-04-02T22:30:37.138485

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready

## 🛡️ 信任评分 (Trust Score)
> Score: 90/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

### Build changes

- [mediapipe] mark mediapipe/gpu:gl_context incompatible on Windows
- [mediapipe] automatically disable gpu (OpenGL) when building for Windows
- [mediapipe] update visibility of gpu:disable_gpu_flag


### Framework and core calculator improvements
- Add Nearest Neighbor interpolation to WarpAffineCalculator.
- Add a Tensor DebugString() function that formats the tensor numpy-style
- Add a Tensor test util
- Create a C API for Holistic Landmarker
- Remove the CPU-only MediaPipe LLM Inference Engine
- Add an AddMultiStreamCallback version that takes a packet map
- BUILD rule cleanup
- API3 subgraph support
- Adds LogImage for mediapipe::Image
- Add support for FULL_RANGE face detection task
- Ads optional RESET input stream to SpectrogramCalculator
- Simplify TaskRunner initialization by adding an options object
- Plumb the host platform and version for all MP Tasks users.
- MediaPipe: Add ROI validation in ImageToTensorOpenCvConverter

### MediaPipe Tasks update
This section should highlight the changes that are done specifically for any platform and don't propagate to
other platforms.


#### Javascript
- Add tests for full-range face detector model.

#### Python
- Re-adding old sources for Holistic Landmarker
- Re-add Holistic Landmarker to Python
- Small patch in old LLM converter
- Support int2 quantization serialization in MP converter
- Removing temporary flag in MP LLM converter
