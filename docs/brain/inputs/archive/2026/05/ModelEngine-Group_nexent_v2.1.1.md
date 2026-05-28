# ℹ️ Intel Report: ModelEngine-Group/nexent
## 🎯 监控目标 (Target)
> ModelEngine-Group/nexent

## 🚀 新版本发布 (New Release)
> Version: v2.1.1
> Date: 2026-05-28T23:18:26.730517

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 90/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

# 🚀 Nexent：开源智能体平台 / Nexent: Open Source Intelligent Agent Platform

我们很高兴地宣布Nexent v2.1.1 正式发布！🎉

Nexent 是一个开源智能体平台，能够将流程的自然语言转化为完整的多模态智能体 —— 无需编排，无需复杂拖拉拽。基于 MCP 工具生态，Nexent 提供强大的模型集成、数据处理、知识库管理、零代码智能体开发能力。我们的目标很简单：将数据、模型和工具整合到一个智能中心中，使日常工作流程更智能、更互联。

We are excited to announce that Nexent v2.1.1 is released! 🎉
Nexent is an open-source agent platform that turns process-level natural language into complete multimodal agents — no diagrams, no wiring. Built on the MCP tool ecosystem, Nexent provides model integration, data processing, knowledge-base management, and zero-code agent development. Our goal is simple: to bring data, models, and tools together in one smart hub, making daily workflows smarter and more connected.

---

## 新功能 / New Features
### Nacos A2A Client 支持 / Nacos A2A Client Support
支持通过 Nacos 发现和调用外部 A2A Agent，实现跨平台 Agent 互操作。
Support discovering and calling external A2A agents via Nacos for cross-platform agent interoperability.

### 新文件类型支持 / New File Type Support
扩展文件解析能力，支持更多文件格式（如 JSON 等），新增 JSON chunk processor。
Extended file parsing capabilities to support more file formats with new JSON chunk processor.

### 向量数据库自动摘要 / Auto Summary for Vector Database
向量数据库自动生成文档摘要，支持自定义摘要频率。
Auto-generate document summaries for vector databases with customizable frequency.

### 数据处理性能优化 / Data Processing Performance Optimization
优化文件处理流程，提升数据处理速度，改进文件分割策略。
Optimized file processing pipeline and improved data processing speed with better file splitting strategies.

### 最终答案提示增强 / Enhanced Final Answer Prompts
达到最大步骤限制时，增强提示要求提供全面总结。
Enhanced prompts to request comprehensive summaries when maximum step limit is reached.

### 语音模型支持 / Voice Model Support
新增阿里云和火山引擎 STT/TTS 模型导入支持。
Added support for importing Alibaba Cloud and Volcengine STT/TTS models.

---

## Bug 修复 / Bug Fixes
### A2A 相关 / A2A Issues
K8s 外部北向 URL、创建模式保存外部协作 agent 失败 / External northbound URL in K8s, saving external collaboration agent fails in create mode

### 文件处理 / File Processing
文件转发失败、缺失 ijson 依赖、dashscope 添加模型失败、model_appid SQL 初始化 / File forward failed, missing ijson, dashscope model add failed, model_appid SQL initialization

### Agent 调试 / Agent Debugging
模型输出历史未包含、工具调用未正确处理 / Model output history not included, tool calls not processed correctly

### 知识库 / Knowledge Base
知识库记录缺少 embedding_model_id / Missing embedding_model_id in knowledge base records

### 会话历史 / Conversation History
会话历史未正确保存 / Conversation history not saved correctly

### 其他 / Others
循环引用（延迟导入解耦）、无网络时 VLM 添加失败、图片预览旋转反向 / Circular import (lazy import decoupling), VLM add failed without internet, image preview rotation reversed

---

## 文档更新 / Documentation
更新 skill 文档、MCP 服务 API 文档、添加 star 提示 / Updated skill docs, MCP service API docs, added star prompt


## What's Changed
* Release/v2.1.0 by @Dallas98 in https://github.com/ModelEngine-Group/nexent/pull/2912
* 🐛 Bugfix: Resolve rotation reverse issue and replace scrollbar with dra
