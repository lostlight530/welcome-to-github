# 🧠 NEXUS CORTEX: Active Mission (活跃任务)
> Generated (生成时间): 2026-02-16T02:52:03.002431

## 🎯 Objective (目标)
Execute defensive upgrades or bridge knowledge gaps. (执行防御性升级或填补知识缺口。)

## 📋 Targets (目标清单)
### 1. 🔴 google-ai-edge/mediapipe v0.10.32 (`P0`)
- **Trigger (触发原因)**: 🚨 BREAKING CHANGE (破坏性更新)
- **Context (背景)**: Official Release: MediaPipe v0.10.32. Gist: ⚠️ **BREAKING CHANGE**: Potential API breakage or deprecation detected., ✨ **New Capability**: New features or NPU operator support likely added., 🔧 **Engineering Debt**: Bug fixes or maintenance work.
- **Reference (参考资料)**: [View on GitHub](https://github.com/google-ai-edge/mediapipe/releases/tag/v0.10.32)
- **Action Item (行动项)**: Audit API compatibility and update local schema.

### 2. 🔴 microsoft/onnxruntime v1.24.1 (`P0`)
- **Trigger (触发原因)**: 🚨 BREAKING CHANGE (破坏性更新)
- **Context (背景)**: Official Release: ONNX Runtime v1.24.1. Gist: ⚠️ **BREAKING CHANGE**: Potential API breakage or deprecation detected., ✨ **New Capability**: New features or NPU operator support likely added., 🔧 **Engineering Debt**: Bug fixes or maintenance work.
- **Reference (参考资料)**: [View on GitHub](https://github.com/microsoft/onnxruntime/releases/tag/v1.24.1)
- **Action Item (行动项)**: Audit API compatibility and update local schema.

## 📝 Ingestion Protocol (摄入协议)
Use standard MCP tools to commit new insights: (使用 MCP 工具提交洞察：)
```bash
python docs/brain/nexus.py add entity --id <id> --name "<name>"
python docs/brain/nexus.py connect <src> <rel> <dst>
```