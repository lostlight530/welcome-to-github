# ℹ️ Intel Report: ModelEngine-Group/nexent
## 🎯 监控目标 (Target)
> ModelEngine-Group/nexent

## 🚀 新版本发布 (New Release)
> Version: v2.0.2
> Date: 2026-04-18T09:12:01.047512

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 90/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

# 🚀 Nexent：开源智能体平台 / Nexent: Open Source Intelligent Agent Platform

我们很高兴地宣布Nexent v2.0.2正式发布！🎉

Nexent 是一个开源智能体平台，能够将流程的自然语言转化为完整的多模态智能体 —— 无需编排，无需复杂拖拉拽。基于 MCP 工具生态，Nexent 提供强大的模型集成、数据处理、知识库管理、零代码智能体开发能力。我们的目标很简单：将数据、模型和工具整合到一个智能中心中，使日常工作流程更智能、更互联。

We are excited to announce that Nexent v2.0.2 is released! 🎉
Nexent is an open-source agent platform that turns process-level natural language into complete multimodal agents — no diagrams, no wiring. Built on the MCP tool ecosystem, Nexent provides model integration, data processing, knowledge-base management, and zero-code agent development. Our goal is simple: to bring data, models, and tools together in one smart hub, making daily workflows smarter and more connected.

## 新功能 / New Features

1. **A2A 协议支持 / A2A Protocol Support**
   - 平台 Agent 可发布为 A2A 服务，支持外部发现和调用；也可反向发现和调用外部 A2A Agent。覆盖后端 API、数据库、SDK、前端全链路。
   - Platform agents can be published as A2A services for external discovery and invocation; external A2A agents can also be discovered and called. Covers backend API, database, SDK, and frontend end-to-end.

2. **System Prompt 精简 / System Prompt Simplification**
   - 代码标记语法简化（如 `<code>` 替代 ` ```<RUN>``` `），优化小参数模型兼容性；新增简化版技能创建模板。
   - Code markup syntax simplified (e.g., `<code>` replaces ` ```<RUN>``` `), improving compatibility with smaller models; added simplified skill creation template.

## Bug 修复 / Bug Fixes

1. **模型添加失败 / Model Addition Failure** — 连通性检查接口和参数传递错误 / Incorrect health check endpoint and missing `model_factory` parameter
2. **技能删除偶发失败 / Intermittent Skill Deletion Failure**
3. **MinIO 懒加载 / MinIO Lazy Loading** — 避免导入时立即连接 / Deferred connection on import
4. **A2A 子问题修复 / A2A Sub-fixes** — 循环引用、流式终止、URL 选择、连接泄漏等 / Circular import, stream termination detection, URL selection, connection leak, etc.

## What's Changed
* ♻️ Update system prompt to better support models with small params by @Jasonxia007 in https://github.com/ModelEngine-Group/nexent/pull/2776
* ✨ Feat: Add A2A protocol support for agent publishing and external agent discovery by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/2773
* 🐛 Bugfix: Fixed the issue where models could not be added correctly on the resource management page.  by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/2782
* Enhance A2A protocol support and fix various bugs by @Dallas98 in https://github.com/ModelEngine-Group/nexent/pull/2822

## New Contributors
* @Dallas98 made their first contribution in https://github.com/ModelEngine-Group/nexent/pull/2822

**Full Changelog**: https://github.com/ModelEngine-Group/nexent/compare/v2.0.1...v2.0.2
