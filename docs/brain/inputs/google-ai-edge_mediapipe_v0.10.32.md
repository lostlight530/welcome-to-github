# ℹ️ Intel: google-ai-edge/mediapipe v0.10.32
> Source: GitHub Releases
> Date: 2026-03-07T13:10:27.703183
> **Analysis**: 🏷️ Edge-Ready ⚠️ Breaking-Change

## 📝 Summary
v0.10.32

## 🔍 Changelog (Extract)
### Build changes

- Enables ml drift metal delegate as inference calculator backend.
- [mediapipe] support armv7 (32 bit in mediapipe tasks)
- Do not assume canvas is BGRA in RenderToWebGpuCanvas.
- Fix sampling logic in ImageToTensorConverterWebGpu.
- Migrate GlShaderCalculator to API3.
- Migrate gl_shader_calculator_test to use API3 builder.

### Bazel changes

- [mediapipe] verion bump to 0.10.27
- Dawn has completed these changes, so the old paths are no longer used.
- Integrate tiny Juno inpainting graph into GenAiProcessor
- Readme for API3
- Add Resources::ResolveId to enable placeholder resource ids usage.
- Web LLM: a few more small edits for Gemma3n
- Include headers from global namespace
- Add comment to Eigen version in WORKSPACE to remind about synchronization with TensorFlow's Eigen dependency
- Migrating VisibilityCopyCalculator to API3.
- Update from Bazel v6.5.0 to v7.4.1, Protobuf v3.19.1 to v5.28.3. Other packages also update the version within WORKSPACE.
- Fix for weight cache on Windows.
- Create Selfie Segmentation Demo App for LiteRT NPU.
- Add Any support for API3
- Adding AudioBuffer support to web LLM Inference API to handle more audio input types for MM models
- Provide API3 interface for PassThroughCalculator using newly added Any type.
- Migrate MergeCalculator to API3 and newly introduced Any type.
- pybind11 version and py_proto_library macro update.
- Add test for PacketResamplerCalculator with a very short video.
- Initial version of sync function runner for API3
- Fix function runner error reporting.
- [mediapipe] version bump
- Migrate CombinedPredictionCalculator to API3
- Clean up CombinedPredictionCalculator
- Currently, wrapping a TextureFrame in a media-pipe Packet assumes the texture is 8-bit RGBA. This patch allows specifying other texture formats to support common color formats like RGBA16F for HDR content.
- Support timestamp bound updates in function runner.
- Migrate TensorsToSegmenta...
