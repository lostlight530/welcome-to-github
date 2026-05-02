# ℹ️ Intel Report: ModelEngine-Group/nexent
## 🎯 监控目标 (Target)
> ModelEngine-Group/nexent

## 🚀 新版本发布 (New Release)
> Version: v2.1.0
> Date: 2026-05-02T06:46:00.674692

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 90/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

# 🚀 Nexent：开源智能体平台 / Nexent: Open Source Intelligent Agent Platform

我们很高兴地宣布Nexent v2.1.0正式发布！🎉

Nexent 是一个开源智能体平台，能够将流程的自然语言转化为完整的多模态智能体 —— 无需编排，无需复杂拖拉拽。基于 MCP 工具生态，Nexent 提供强大的模型集成、数据处理、知识库管理、零代码智能体开发能力。我们的目标很简单：将数据、模型和工具整合到一个智能中心中，使日常工作流程更智能、更互联。

We are excited to announce that Nexent v2.1.0 is released! 🎉
Nexent is an open-source agent platform that turns process-level natural language into complete multimodal agents — no diagrams, no wiring. Built on the MCP tool ecosystem, Nexent provides model integration, data processing, knowledge-base management, and zero-code agent development. Our goal is simple: to bring data, models, and tools together in one smart hub, making daily workflows smarter and more connected.

## 新功能 / New Features

### A2A 协议支持 / A2A Protocol Support
平台 Agent 可发布为 A2A 服务，支持外部发现和调用；也可反向发现和调用外部 A2A Agent，支持直接对话。覆盖后端 API、数据库、SDK、前端全链路。
Platform agents can be published as A2A services; external A2A agents can be discovered and called with direct chat support. Covers backend API, database, SDK, and frontend end-to-end.

### SQL 数据库工具 / SQL Database Tools
新增 MySQL、PostgreSQL、MSSQL 数据库执行工具。
Added SQL execute tools for MySQL, PostgreSQL, and MSSQL.

### NL2Skill 多轮对话 / NL2Skill Multi-turn Support
支持多轮自然语言生成技能，复杂技能生成，官方技能预装。
Supports multi-turn skill generation, complicated skill creation, and official skills pre-installation.

### 模型监控 / Model Monitoring
新增模型调用监控，支持 Token 使用追踪和统计。
Added model monitoring with token usage tracking and statistics.

### Agent 上下文管理 / Agent Context Management
新增上下文压缩、Token 估算、指标日志。
Added context compression, token estimation, and metrics logging.

### 模型与版本对比 / Model & Version Comparison
支持不同模型和 Agent 版本对比功能。
Added comparison for different models and agent versions.

### OAuth 重构 & API 转 MCP / OAuth Refactor & API to MCP
OAuth 实现重构；API 到 MCP 服务转换重构。
Refactored OAuth implementation and API to MCP service transformation.

### 个人文件权限隔离 / Personal File Permission Isolation
个人上传文件权限隔离，添加登录认证验证。
Personal file uploads with permission isolation and authentication verification.

---

## Bug 修复 / Bug Fixes

### A2A 相关 / A2A Issues
循环引用、流式终止、URL 选择、连接泄漏等 / Circular import, stream termination, URL selection, connection leak

### 知识库问题 / Knowledge Base Issues
文件预览失败、knowledge_base_names 缺失 / File preview failure, missing knowledge_base_names

### Kubernetes 部署 / Kubernetes Deployment
callbackBaseUrl 配置错误、外部 API 转 MCP 失败 / Incorrect callbackBaseUrl, API to MCP conversion failure

### 多轮对话 / Multi-turn Dialogues
多轮对话和文件上传异常修复 / Fixed multi-turn dialogues and file upload issues

### 其他 / Others
- Session 删除接口报错 / Session deletion error
- Multimodal 工具 502 问题 / Multimodal tool 502 error
- MinIO 懒加载 / MinIO lazy loading
- 技能删除偶发失败 / Intermittent skill deletion failure
- 模型 API Key 安全隐藏 / Hide model API key

---

## What's Changed
* ♻️ Refactor API to MCP service #2187 by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/2778
* Added t
