# ℹ️ Intel Report: ModelEngine-Group/nexent
## 🎯 监控目标 (Target)
> ModelEngine-Group/nexent

## 🚀 新版本发布 (New Release)
> Version: v2.0.1
> Date: 2026-04-10T22:36:50.273595

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 90/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

# 🚀  Nexent：开源智能体平台 / Nexent: Open Source Intelligent Agent Platform

我们很高兴地宣布Nexent v2.0.1正式发布！🎉

Nexent 是一个开源智能体平台，能够将流程的自然语言转化为完整的多模态智能体 —— 无需编排，无需复杂拖拉拽。基于 MCP 工具生态，Nexent 提供强大的模型集成、数据处理、知识库管理、零代码智能体开发能力。我们的目标很简单：将数据、模型和工具整合到一个智能中心中，使日常工作流程更智能、更互联。

We are excited to announce that Nexent v2.0.1 is released! 🎉
Nexent is an open-source agent platform that turns process-level natural language into complete multimodal agents — no diagrams, no wiring. Built on the MCP tool ecosystem, Nexent provides model integration, data processing, knowledge-base management, and zero-code agent development. Our goal is simple: to bring data, models, and tools together in one smart hub, making daily workflows smarter and more connected.

## 🔔 本周核心BUG修复 / This Week's Key Bug Fixes

### 1️⃣ BUG修复 / Bug Fixes

- 修复了智能体创建保存后，无法退出创建模式的问题。
Fixed the issue where the creation mode could not be exited after an agent was created and saved.
- 恢复了智能体市场的连接，保障功能正常。
Restored the connection to the Agent Marketplace to ensure normal functionality.
- 修复 max_step 参数默认传递错误的问题。
Fixed the incorrect default passing of the max_step parameter.

## What's Changed
* 🐛 Bugfix: Fixed issues where clicking save after creating an agent would not exit creation mode and select the agent, and also fixed the issue of incorrect max_step parameter passing by default. #2737 by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/2744
* 📝 Add Kubernetes installation and upgrade guides. by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/2743
* ✨ new implement :  support Rerank models in model management and agent configurations by @wadecrack in https://github.com/ModelEngine-Group/nexent/pull/2700
* 🐛 Bugfix: Fixed issues where clicking save after creating an agent would not exit creation mode and select the agent, and also fixed the issue of incorrect max_step parameter passing by default. #2737 by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/2749
* ✨ Enhance ToolConfigModal and ToolTestPanel with knowledge base selec… by @Zhi-a in https://github.com/ModelEngine-Group/nexent/pull/2745
* ♻️ Clean unnecessary skill logs by @Jasonxia007 in https://github.com/ModelEngine-Group/nexent/pull/2751
* 🧪 Fix test file by @Jasonxia007 in https://github.com/ModelEngine-Group/nexent/pull/2753
* 🐛 Fix agent market disconnected by @WMC001 in https://github.com/ModelEngine-Group/nexent/pull/2752
* 🧪 Add test file by @Jasonxia007 in https://github.com/ModelEngine-Group/nexent/pull/2754
* ✨ One-click API-to-MCP transform #2187 by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/2765
* ♻️ Fix 3 Regex DoS vulnerability by @Jasonxia007 in https://github.com/ModelEngine-Group/nexent/pull/2764
* ✨ File preview: add page range support and implement file preview frontend component by @Stockton11 in https://github.com/ModelEngine-Group/nexent/pull/2709
* Develop by @geruihappy-creator in https://github.com/ModelEngine-Group/nexent/pull/276
