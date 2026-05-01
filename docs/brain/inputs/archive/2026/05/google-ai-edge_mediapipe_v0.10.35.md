# ℹ️ Intel Report: google-ai-edge/mediapipe
## 🎯 监控目标 (Target)
> google-ai-edge/mediapipe

## 🚀 新版本发布 (New Release)
> Version: v0.10.35
> Date: 2026-05-01T22:49:42.012684

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready

## 🛡️ 信任评分 (Trust Score)
> Score: 90/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

### Framework and core calculator improvements
- Add histogram information to Tensor::DebugString.
- Bump MediaPipe version to 0.10.35.
- Add missing GL memory barrier in TensorsToSegmentationGlBufferConverter.
- Migrate FromImageCalculator to MediaPipe API3 and add test.
- Add api3::Packet::Share function.
- Remove util/analytics references from GitHub build
- Migrate ToImageCalculator to MediaPipe API3 and add tests.
- Fix -Wthread-safety-analysis warning.
- Allow MP Task files to be use in Vite's workers
- Add save-png-by-path test util function.
- Feat: Add configurable policy for handling empty landmarks in smoothing calculators
- #mediapipe Make GPU service optional in ImageToTensorCalculator for iOS.
- Add Host Platform Web and Host System iOS/Android to logging enums

### MediaPipe Tasks update
This section should highlight the changes that are done specifically for any platform and don't propagate to
other platforms.

#### Android
- Allow users to use NPU acceleration with JIT compilation
- Drop unnecessary `tasks/core` deps

#### iOS
- Change MP Tasks CocoaPods types to Framework

#### Javascript
- Remove references to "subgroups-f16"
- Fix broken exports statement in package.json
- Update MP Tasks GenAI README

#### Python
- Small fixes to blockwise int4 compression calculations in LLM converter
- Allow for overriding apply_srq in LLM Converter
- Small blockwise dequant helper for LLM Converter


### MediaPipe Dependencies
- Update Wasm file hashes and URLs in wasm_files.bzl
