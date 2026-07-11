# ℹ️ Intel Report: ModelEngine-Group/nexent
## 🎯 监控目标 (Target)
> ModelEngine-Group/nexent

## 🚀 新版本发布 (New Release)
> Version: v2.2.1
> Date: 2026-06-30T23:14:26.148224

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: ⚠️ Breaking-Change 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 100/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

# 🚀 Nexent：开源智能体平台 / Nexent: Open Source Intelligent Agent Platform

## 概览 / Overview
- 本次发布围绕 Agent 增强、MCP/知识库/内存工具改进、前端体验修复与部署流程优化展开，同时包含若干文档和版本管理变更。 / This release focuses on Agent enhancements, improvements to MCP/knowledge-base/memory tools, frontend experience fixes, and deployment optimizations, along with documentation and version management updates.

## 新功能 / New Features
- 新增了 Agent 问候语与示例问题配置，提升对话冷启动体验。 / Added agent greeting messages and example questions to improve conversation onboarding.
- 新增了 Active Memory 工具（`StoreMemoryTool`、`SearchMemoryTool`），支持主动存储与检索记忆。 / Added active memory tools (`StoreMemoryTool`, `SearchMemoryTool`) for proactive memory storage and retrieval.
- 知识库向量化后新增可选保留源文件的能力，便于源数据溯源。 / Added optional source file retention after knowledge base vectorization for better traceability.
- 新增 Word 文档生成、预览与下载能力，扩展文档输出格式。 / Added Word document generation, preview, and download support to expand document export options.
- 集成了 OpenJiuwen 并优化了提示词优化流程，同时修复了相关问题。 / Integrated OpenJiuwen for prompt optimization and fixed related issues.
- 新增 CAS 单点登录集成并改进了登出逻辑，强化身份认证与退出体验。 / Added CAS SSO integration and improved logout handling to strengthen authentication and exit flow.
- 新增了 Agent 市场仓库与子代理版本锁定，便于统一管理外部 Agent 来源。 / Added agent marketplace repository and version pinning for sub-agents.
- Agent 新增验证配置及相关组件更新，提升 Agent 发布前校验能力。 / Added verification configuration for agents and updated related components.
- 新增多条北向 API，扩展平台对外集成能力。 / Added several northbound APIs to extend platform integration capabilities.
- 数据库迁移中补充了对应版本 SQL 变更。 / Added supplementary SQL migration for this release.

## 改进 / Improvements
- API 转 MCP 转换服务支持配置请求头，适配更多下游服务鉴权与链路要求。 / API-to-MCP conversion service now supports configurable headers for downstream authentication and traceability.
- 增强了对 Memory Bank 中 ES 索引名称的处理逻辑。 / Enhanced processing of Elasticsearch index names in memory banks.
- 将当前时间从系统提示词移至用户消息中，提升 prompt cache 稳定性。 / Moved current time from the system prompt into the user message to improve prompt cache stability.
- 简化了部署脚本，移除了未使用的变量与函数，降低维护成本。 / Simplified deployment scripts by removing unused variables and functions.

## Bug 修复 / Bug Fixes
- 修复了技能名称与描述未加载到上下文的问题。 / Fixed an issue where skill names and descriptions were not loaded into context.
- 修复了工具调用报错时的 attribution 关联错误，避免链路归因异常。 / Fixed attribution errors during tool calling failures.
- 修复了容器化方式下无法添加 MCP 服务的问题。 / Fixed an issue preventing MCP services from being added via containerization.
- 修复了更新 FastMCP 版本后无法正确添加 MCP 服务的问题。 / Fixed an issue where MCP services could not be added correctly after updating the FastMCP version.
- 修复了 Kubernetes Pod 中 MCP 服务启动失败的问题。 / Fixed an issue where MCP services failed to start in Kubernetes pods.
- 修复了会话期间上传文本文件无法解析的问题。 / Fixed an issue where uploaded text files could not be parsed during a session.
- 修复了窗口大小改变后租户资源页显示不完整的问题。 / Fixed incomplete display of the tenant resources page after window resize.
- 修复了无法从 Agent Space 选择 Agent 进行编辑的问题。 / Fixed an issue preventing agent selection from the agent space for editing.
- 调整了 Agent 详情页 UI 布局，适配新增的“自验证”字段。 / Adjusted agent detail UI layout to accommodate the new self-verification field.
- 修复了导入 Agent 后一键重命名功能失效的问题。 / Fixed an issue where one-click rename failed after importing an agent.
- 修复了 `knowledge_base_search_tool` 调用时的 TypeError。 / Fixed a TypeError in `knowledge_base_search_tool`.
- 修复了保存会话历史时附件被错误带入助手侧的问题。 / Fixed an issue where attachments were incorrectly included from the assistant when saving conversation history.
- 更新了数据代理与 ME CAS 集成文档，修复文档与现状不一致问题。 / Updated data agent and ME CAS integration documentation.

## 其他变更 / Other Changes
- 工具/技能池标签新增已选数量徽标，提升界面可读性。 / Added selected count badges to tool/skill pool labels.
- 将版本号从 v2.2.0 升级至 v2.2.1，并完成发布流程。 / Bumped the application version from v2.2.0 to v2.2.1 and completed the release process.

## 新贡献者 / New Contributors
- @jeffwu-1999 首次贡献 / First contribution
- @wuyuanfr 首次贡献 / First contribution

## What's Changed
* Add agent greeting message and example questions by @jeffwu-1999 in https://github.com/ModelEngine-Group/nexent/pull/3185
* feat(knowledge-base): optional source file retention after vectorization by @Lifeng-Chen in https://github.com/ModelEngine-Group/nexent/pull/3189
* ♻️ Improvement: API to MCP conversion service supports configuring headers. by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/3194
* ♻️ Improvement: Enhance processing of ES index names in memory banks. by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/3196
* ✨ Feat: add active memory tools (StoreMemoryTool, SearchMemoryTool) by @JasonW404 in https://github.com/ModelEngine-Group/nexent/pull/3197
* 🐛 Bugfix: skill names and descriptions never load to context by @Jasonxia007 in https://github.com/ModelEngine-Group/nexent/pull/3205
* add selected count badges to tool/skill pool labels by @jeffwu-1999 in https://github.com/ModelEngine-Group/nexent/pull/3206
* 🐛 Bugfix: Fix attribution error when tool calling error by @WMC001 in https://github.com/ModelEngine-Group/nexent/pull/3208
* ✨ Feat: Add support for Word document generation, preview, and download by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/3191
* ✨Feat:Enhance prompt optimization by integrating openjiuwen and fix related bugs by @DongJiBao2001 in https://github.com/ModelEngine-Group/nexent/pull/3190
* Add CAS SSO integration and improve logout handling by @hhhhsc701 in https://github.com/ModelEngine-Group/nexent/pull/3072
* 🐛 Bugfix: skill names and descriptions never load to context by @Jasonxia007 in https://github.com/ModelEngine-Group/nexent/pull/3207
* 🐛Bugfix: Remove unnecessary dependency exclusions and upgrade huggingface_hub version in pyproject.toml by @DongJiBao2001 in https://github.com/ModelEngine-Group/nexent/pull/3211
* refactor: move current time from system prompt to user message for prompt cache stability by @wuyuanfr in https://github.com/ModelEngine-Group/nexent/pull/3203
* 🐛 Bugfix: Fixed the issue of being unable to add MCP services via containerization. by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/3213
* 🐛 Bugfix: Fixed the issue where uploaded text files could not be parsed during a session. by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/3219
* 🐛 Bugfix: Fixed an issue where the MCP service could not be added correctly after updating the FastMCP version. by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/3222
* 🐛 Bugfix: Fix incomplete display of tenant resources page after window resize by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/3215
* Add agent marketplace repository and version pinning for sub-agents by @Lifeng-Chen in https://github.com/ModelEngine-Group/nexent/pull/3239
* feat(agent): add verification configuration for agents and update related components by @Dallas98 in https://github.com/ModelEngine-Group/nexent/pull/3174
* 🐛 Bugfix: Fix inability to select agent from agent space to edit by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/3240
* Update data agent and ME CAS integration documentation by @hhhhsc701 in https://github.com/ModelEngine-Group/nexent/pull/3242
* ✨ Add several northbound apis by @Jasonxia007 in https://github.com/ModelEngine-Group/nexent/pull/3223
* refactor: simplify deployment script by removing unused variables and functions by @Dallas98 in https://github.com/ModelEngine-Group/nexent/pull/3245
* 🐛 Bugfix: Adjust agent detail UI layout to accommodate newly added "self-verification" field by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/3246
* 补充sql by @hhhhsc701 in https://github.com/ModelEngine-Group/nexent/pull/3248
* 🐛 Bugfix: Fixed an issue where the MCP service failed to start in a Kubernetes pod. by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/3254
* 🐛 Bugfix: knowledge_base_search_tool called with TypeError by @Jasonxia007 in https://github.com/ModelEngine-Group/nexent/pull/3259
* 🐛 Bugfix: Fixed an issue where the one-click rename function failed after importing an agent. by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/3258
* 🐛 Bugfix: Exclude attachments from assistant when saving conversation history by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/3261
* Bump APP_VERSION from v2.2.0 to v2.2.1 by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/3268
* Release/v2.2.1 by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/3269
* Revert "Release/v2.2.1" by @WMC001 in https://github.com/ModelEngine-Group/nexent/pull/3272
* Release/v2.2.1 by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/3273

**Full Changelog**: https://github.com/ModelEngine-Group/nexent/compare/v2.2.0...v2.2.1
