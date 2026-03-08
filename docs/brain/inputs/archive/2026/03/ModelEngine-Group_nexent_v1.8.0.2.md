# ℹ️ Intel: ModelEngine-Group/nexent v1.8.0.2
> Source: GitHub Releases
> Date: 2026-03-08T22:33:06.376772
> **Analysis**: 🔗 Agent-Protocol

## 📝 Summary
v1.8.0.2

## 🔍 Changelog (Extract)
# 🚀  Nexent：开源智能体平台 / Nexent: Open Source Intelligent Agent Platform

我们很高兴地宣布Nexent v1.8.0.2正式发布！🎉

Nexent 是一个开源智能体平台，能够将流程的自然语言转化为完整的多模态智能体 —— 无需编排，无需复杂拖拉拽。基于 MCP 工具生态，Nexent 提供强大的模型集成、数据处理、知识库管理、零代码智能体开发能力。我们的目标很简单：将数据、模型和工具整合到一个智能中心中，使日常工作流程更智能、更互联。

We are excited to announce that Nexent v1.8.0.2 is released! 🎉
Nexent is an open-source agent platform that turns process-level natural language into complete multimodal agents — no diagrams, no wiring. Built on the MCP tool ecosystem, Nexent provides model integration, data processing, knowledge-base management, and zero-code agent development. Our goal is simple: to bring data, models, and tools together in one smart hub, making daily workflows smarter and more connected.

## 🔔 本周核心BUG修复 / This Week's Key Bug Fixes

### 1️⃣ BUG修复 / Bug Fixes

- 修复了离线环境无法使用文件解析工具、创建智能体报错、知识库重命名不同步等BUG。
- 重构 4 处代码，优化系统稳定性，持续提升用户体验。

Fixed bugs including unavailable file parsing tool in offline environment, errors during agent creation, and unsynchronized knowledge base renaming. Refactored 4 code modules, optimized system stability, and continuously improved user experience.

## What's Changed
* Enhance Dockerfile: Pre-download tiktoken by @Zhi-a in https://github.com/ModelEngine-Group/nexent/pull/2585
* 🐛 Bugfix: The agent_run process cannot invoke the MCP service with authentication. by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/2587
* 🐛 Bugfix: Clicking on the tenant name does not respond and the tenant name is not selected #2496 by @WMC001 in https://github.com/ModelEngine-Group/nexent/pull/2586
* 🐛 Bugfix: error when update a tool & adding a agent relation by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/2594
* ♻️ The agent should support setting in-group permissions. #2566 by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/2577
* 🐛 Bugfix: Fix various issues when the Agent's permissions are set to … by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/2592
* 🐛 Bugfix: Agent generation occasionally fails to set the duty field #2355 #2262 #2507 by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/2600
* 🐛 Bugfix: error when import agent in speed mode #2590 #2580 by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/2595
* 🐛 Bugfix: error when update a tool & adding a agent relation  by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/2610
* Release/v1.8.0.1 hotfix by @geruihappy-creator in https://github.com/ModelEngine-Group/nexent/pull/2613
* 🐛 Bugfix: knowledgebase rename not synchronized  by @Jasonxia007 in https://github.com/ModelEngine-Group/nexent/pull/2598
* 🐛 Bugfix: Fix the agent version display in resource management page. #2490 by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/2603
* ♻️ Container logs support automatic refresh #2240 by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/2622
* 🐛 Bugfix: Fix dify sync interface by @Zhi-a in h
