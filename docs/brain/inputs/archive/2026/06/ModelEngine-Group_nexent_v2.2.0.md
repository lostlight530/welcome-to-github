# ℹ️ Intel Report: ModelEngine-Group/nexent
## 🎯 监控目标 (Target)
> ModelEngine-Group/nexent

## 🚀 新版本发布 (New Release)
> Version: v2.2.0
> Date: 2026-06-14T16:06:29.741500

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 100/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

# 🚀 Nexent：开源智能体平台 / Nexent: Open Source Intelligent Agent Platform

我们很高兴地宣布Nexent v2.2.0 正式发布！🎉

Nexent 是一个开源智能体平台，能够将流程的自然语言转化为完整的多模态智能体 —— 无需编排，无需复杂拖拉拽。基于 MCP 工具生态，Nexent 提供强大的模型集成、数据处理、知识库管理、零代码智能体开发能力。我们的目标很简单：将数据、模型和工具整合到一个智能中心中，使日常工作流程更智能、更互联。

We are excited to announce that Nexent v2.2.0 is released! 🎉
Nexent is an open-source agent platform that turns process-level natural language into complete multimodal agents — no diagrams, no wiring. Built on the MCP tool ecosystem, Nexent provides model integration, data processing, knowledge-base management, and zero-code agent development. Our goal is simple: to bring data, models, and tools together in one smart hub, making daily workflows smarter and more connected.

---
## 新功能 / New Features
- 新增或增强了 Agent 生成模板管理、A2A 相关协作能力、Vision-Language 识别与音频理解工具。 / Added or improved agent generation template management, A2A collaboration capabilities, and vision-language plus audio understanding tools.
- 支持用户配置模型并发限制和超时时间，提升推理资源控制能力。 / Added user-configurable model concurrency limits and timeout settings to improve inference resource control.
- 增强上下文管理，并为 Agent 上下文模块增加基准测试。 / Improved context management and added benchmarks for the agent context module.
- 新增技能、MCP 服务、自定义 header、工具执行日志等平台扩展能力。 / Added platform extensibility for skills, MCP services, custom headers, and tool execution logging.
- 新增资源权限与角色相关能力，例如 `ASSET_OWNER` 角色与资源可见性控制。 / Added resource access features such as the `ASSET_OWNER` role and resource visibility enforcement.
- 扩展多模态与文档能力，包括 office/PDF 图片抽取与检索、TTS 语音模型支持等。 / Expanded multimodal and document capabilities, including image extraction/retrieval for office/PDF files and TTS model support.
## Bug 修复 / Bug Fixes
- 修复外部协作 Agent 保存、权限控制、模型添加、Agent Prompt 生成等问题。 / Fixed external collaboration agent saving, permission control, model addition, and agent prompt generation issues.
- 修复 MCP 集成相关问题，包括代理环境变量干扰与工具调用异常。 / Fixed MCP integration issues, including proxy environment variable interference and tool call failures.
- 修复知识库与会话历史相关问题，例如记录缺少 `embedding_model_id`、会话历史未正确保存。 / Fixed knowledge base and conversation history issues, such as missing `embedding_model_id` and incorrect history persistence.
- 修复调试模式中错误信息不充分、模型输出历史未包含、`iData` 工具调用失败等问题。 / Fixed insufficient error details in debug mode, missing model output history, and `iData` tool call failures.
- 修复登录/注册、技能/工具按钮状态、无网络场景下 VLM 添加、图片预览旋转等体验问题。 / Fixed UX issues around login/register flows, skill/tool button states, VLM addition without network access, and image preview rotation.
- 修复部署持久化、Docker SQL 重复、监控环境变量同步等问题。 / Fixed deployment persistence, Docker SQL duplication, and monitoring environment variable sync issues.
## 文档与部署变化 / Docs & Deployment Changes
- 新增 SQL tools 文档、MCP 服务 API 文档，并更新 skill 相关说明。 / Added SQL tools documentation, MCP service API documentation, and updated skill-related docs.
- 增加离线部署包构建流程，并优化部署脚本与 Helm 指南。 / Added offline deployment package build flow and improved deployment scripts and Helm guidance.
- 增加引导用户 star 仓库的文案与文档提示。 / Added prompts and documentation nudges encouraging users to star the repository.

## What's Changed
* Fix external collaboration agent saving and related bugs by @Dallas98 in https://github.com/ModelEngine-Group/nexent/pull/2993
* Optimize prompt by @2h0u4n in https://github.com/ModelEngine-Group/nexent/pull/2924
* 📃 Add sql tools document by @WMC001 in https://github.com/ModelEngine-Group/nexent/pull/3005
* 🐛 Bugfix: Avoid directly modifying files in the runtime environment using code. #3006 by @WMC001 in https://github.com/ModelEngine-Group/nexent/pull/3007
* 🐛 Bugfix: Auto-clean account when exists in Supabase but not in postgresql by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/3002
* Chore: Add workflow and script for offline deployment package build by @Dallas98 in https://github.com/ModelEngine-Group/nexent/pull/3010
* Chore: Add workflow and script for offline deployment package build by @Dallas98 in https://github.com/ModelEngine-Group/nexent/pull/3011
* feat: add prompt template management for agent generation by @2h0u4n in https://github.com/ModelEngine-Group/nexent/pull/2925
* Refine and internationalize OAuth account completion flow by @hhhhsc701 in https://github.com/ModelEngine-Group/nexent/pull/2984
* Enhance monitoring with OpenTelemetry, Grafana, and new providers by @hhhhsc701 in https://github.com/ModelEngine-Group/nexent/pull/2969
* ✨ Feat: support user to configurate model concurrency limit and timeout seconds by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/2943
* ✨ Support modifying passward #2809 by @WMC001 in https://github.com/ModelEngine-Group/nexent/pull/3016
* ♻️ Mcp Tools Management Page Development by @HelloWorldGitHub114 in https://github.com/ModelEngine-Group/nexent/pull/2771
* ♻️ Performance optimization of the knowledge base file list query interface by @WMC001 in https://github.com/ModelEngine-Group/nexent/pull/3025
* ✨ Skill ability enhancement and bug fix by @Jasonxia007 in https://github.com/ModelEngine-Group/nexent/pull/3017
* 🐛 Fixes the model addition issue in ModelEngine. by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/3026
* Feat: support user to add and use tts model by @wadecrack in https://github.com/ModelEngine-Group/nexent/pull/2959
* 🐛 Bugfix: Cannot generate agent prompt by @Jasonxia007 in https://github.com/ModelEngine-Group/nexent/pull/3028
* ♻️ Refactor: Optimize agent page layout & refactor agent generate page by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/3020
* Optimize deployment scripts and improve Helm chart instructions by @hhhhsc701 in https://github.com/ModelEngine-Group/nexent/pull/3029
* ♻️ Add v2.2.0 shell script to update the directory of skills by @Jasonxia007 in https://github.com/ModelEngine-Group/nexent/pull/3035
* Feat: Add vision-language model classification and audio understanding tools by @827dsl in https://github.com/ModelEngine-Group/nexent/pull/3001
* feat: Support image extraction & retrieval for office/PDF documents by @yzAiden in https://github.com/ModelEngine-Group/nexent/pull/2720
* feat: support multi-turn compare sessions by @2h0u4n in https://github.com/ModelEngine-Group/nexent/pull/3012
* ♻️ Improvement: Supports adding custom headers when adding MCP services. by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/3036
* Fix markdown table code block diaplay eccentrically by @MoeexT in https://github.com/ModelEngine-Group/nexent/pull/2992
* Support adding models individually and Fix audio tools by @827dsl in https://github.com/ModelEngine-Group/nexent/pull/3049
* 🐛 Bugfix: Fix the issue with permission control for released agents. by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/3052
* :bug: Add detail error message in debug mode by @MoeexT in https://github.com/ModelEngine-Group/nexent/pull/2977
* 🐛 Bugfix: Fix iData tool call error. by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/3054
* ✨ Feat: Context management refactoring. Add benchmark for agent context module. by @JasonW404 in https://github.com/ModelEngine-Group/nexent/pull/3039
* ✨ feat: increase agent max_steps default to 15 and widen bounds to 30 by @JasonW404 in https://github.com/ModelEngine-Group/nexent/pull/3057
* 🐛 Bugfix: Fix no password check when creating tenant admin by @WMC001 in https://github.com/ModelEngine-Group/nexent/pull/3061
* refactor: remove unnecessary interactions by @yzAiden in https://github.com/ModelEngine-Group/nexent/pull/3065
* Add Link App OAuth provider support and update configurations by @hhhhsc701 in https://github.com/ModelEngine-Group/nexent/pull/3068
* ✨ Feat: add ASSET_OWNER role, enforce asset visibility, and refine no… by @Lifeng-Chen in https://github.com/ModelEngine-Group/nexent/pull/3042
* knowledge_base_search工具参数中添加index_names输入参数 by @yzAiden in https://github.com/ModelEngine-Group/nexent/pull/3078
* 🐛 Bugfix: Disable tool and skill selection when user is not in edit mode by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/3064
* Bugfix: when user login or register, do not open session expire modal by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/3082
* ♻️ Add log of tool execution by @WMC001 in https://github.com/ModelEngine-Group/nexent/pull/3081
* ♻️ Docker sql duplicate fix by @Jasonxia007 in https://github.com/ModelEngine-Group/nexent/pull/3080
* Style: Align agent dropdown list width with parent component by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/3113
* feat(model): optimize model type labels and max token input by @Dallas98 in https://github.com/ModelEngine-Group/nexent/pull/3117
* 🐛 Bugfix: Disable skill buttons when page is not in edit mode by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/3120
* Fix deployment persistence and sync monitoring environment variables by @hhhhsc701 in https://github.com/ModelEngine-Group/nexent/pull/3127
* Add ASSET_OWNER role with OAuth registration and resource permissions  by @Lifeng-Chen in https://github.com/ModelEngine-Group/nexent/pull/3086
* 🐛 Bugfix: Fix MCP integration by ignoring proxy environment variables by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/3121
* Add deployment script guidance for monitoring and OAuth by @hhhhsc701 in https://github.com/ModelEngine-Group/nexent/pull/3168
* 🐛 Bugfix: Batch add dashscope embedding model failed to calculate embedding dimension by @Jasonxia007 in https://github.com/ModelEngine-Group/nexent/pull/3172
* Bugfix: Store created_by when rolling back version by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/3175
* 📃 Add multimodal tools document by @WMC001 in https://github.com/ModelEngine-Group/nexent/pull/3177
* 🐛 Bugfix: Constraints and Examples falsely generated when user didn't choose any tools or subagents by @Jasonxia007 in https://github.com/ModelEngine-Group/nexent/pull/3179
* Fix: Update DashScope provider for realtime WebSocket and translations by @Dallas98 in https://github.com/ModelEngine-Group/nexent/pull/3178
* add_epub_dependency by @yzAiden in https://github.com/ModelEngine-Group/nexent/pull/3176
* Release v2.2.0  by @DongJiBao2001 in https://github.com/ModelEngine-Group/nexent/pull/3183

## New Contributors
* @HelloWorldGitHub114 made their first contribution in https://github.com/ModelEngine-Group/nexent/pull/2771
* @827dsl made their first contribution in https://github.com/ModelEngine-Group/nexent/pull/3001
* @Lifeng-Chen made their first contribution in https://github.com/ModelEngine-Group/nexent/pull/3042

**Full Changelog**: https://github.com/ModelEngine-Group/nexent/compare/v2.1.1...v2.2.0
