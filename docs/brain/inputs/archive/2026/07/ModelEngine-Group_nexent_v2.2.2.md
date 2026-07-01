# ℹ️ Intel Report: ModelEngine-Group/nexent
## 🎯 监控目标 (Target)
> ModelEngine-Group/nexent

## 🚀 新版本发布 (New Release)
> Version: v2.2.2
> Date: 2026-07-01T23:16:46.929240

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: ⚠️ Breaking-Change 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 100/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

# 🚀 Nexent：开源智能体平台 / Nexent: Open Source Intelligent Agent Platform

## 新功能 / New Features

• 新增 Agent 仓库与 Agent 空间能力，支持分页、评价、上架审核、复制导入与导入前检查。 / Added agent repository and agent space capabilities with pagination, reviews, listing review, copy import, and import precheck.

• 新增对话分享能力，支持生成分享页并通过独立只读入口访问会话内容。 / Added conversation sharing with standalone read-only shared conversation pages.

• 新增 AIDP 搜索工具与知识库选择能力，并补充相关后端接口、SDK 工具和前端配置面板。 / Added AIDP search tooling with knowledge-base selection across backend APIs, SDK tools, and frontend configuration.

• 增强模型容量与上下文管理，加入容量预算、tokenizer registry、prompt cache 以及模型容量配置界面。 / Improved model capacity and context management with capacity budgeting, tokenizer registry, prompt cache, and model capacity UI.

• 增强工具配置体验，新增工具标签、工具选择弹窗与 MCP 分组展示。 / Improved tool configuration with tool labels, selection dialog, and MCP grouping.

## Bug 修复 / Bug Fixes

• 修复聊天流在切换标签页后无法继续恢复的问题。 / Fixed chat streaming resume after switching browser tabs.

• 修复外部工具接口返回 401 时导致 Nexent 被登出的异常行为。 / Fixed unexpected Nexent logout when external tool calls return HTTP 401.

• 修复模型配置与消息兼容性问题，包括隐藏 provider 误传、ModelEngine 消息扁平化和 smolagents 消息格式适配。 / Fixed model configuration and message compatibility issues, including hidden provider leakage, ModelEngine message flattening, and smolagents message formatting.

• 修复 AIDP 与知识库工具测试/配置问题，包括 `topk` 参数、搜索参数保存和知识库单选测试。 / Fixed AIDP and knowledge-base tool configuration issues around `topk`, parameter persistence, and single knowledge-base selection.

• 修复若干前端交互问题，包括导航侧栏 i18n、HTTP 下复制到剪贴板、邀请码分页禁用和 Agent 发布 `created_by` 写入。 / Fixed frontend interaction issues including sidebar i18n, clipboard copy over HTTP, invitation-code pagination, and `created_by` persistence on agent publishing.

## 文档与部署变化 / Docs & Deployment Changes

• 重构部署目录，将 Docker、K8s、SQL、离线包、镜像构建脚本统一迁移到 `deploy/` 体系。 / Restructured deployment assets into the unified `deploy/` layout for Docker, K8s, SQL, offline packages, and image builds.

• 新增 SQL 迁移体系与回填脚本，覆盖会话分享、左侧导航、Agent 模型字段列表化、catalog 回填和消息状态清理。 / Added SQL migration and backfill support for conversation sharing, navigation updates, agent model list migration, catalog backfill, and message status cleanup.

• 增强离线包与镜像构建流程，补充 offline package 压缩、组件设置、tiktoken 缓存预加载和构建测试。 / Improved offline packaging and image builds with compression, component setup, preloaded tiktoken cache, and build tests.

• 更新 Docker/Kubernetes 安装、升级、构建、开发环境和监控文档，并刷新 Python/Node.js 依赖说明。 / Updated Docker/Kubernetes installation, upgrade, build, developer setup, monitoring, and Python/Node.js dependency documentation.

• 优化 CI 与测试覆盖流程，恢复 Codecov，并加入并行单测覆盖统计与文件级子进程隔离。 / Improved CI and test coverage with restored Codecov, parallel unit-test coverage reporting, and file-level subprocess isolation.


## What's Changed
* ✨Feat: Add AIDP search tool https://github.com/ModelEngine-Group/nexent/issues/2788 by @DongJiBao2001 in https://github.com/ModelEngine-Group/nexent/pull/3241
* Release/v2.2.1 by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/3270
* Revert "Release/v2.2.1" by @WMC001 in https://github.com/ModelEngine-Group/nexent/pull/3274
* Release/v2.2.1 by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/3275
* 🐛 Bugfix: Multimodal tools support user model selection by @gjc199 in https://github.com/ModelEngine-Group/nexent/pull/3249
* fix: Parallel unit test runner with file-level subprocess isolation by @JasonW404 in https://github.com/ModelEngine-Group/nexent/pull/3285
* ♻️ Improvement: The default setting for self-verification upon agent creation should be "False" by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/3284
* ♻️ Refactor: update left navigation menu by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/3282
* 🐛 Bugfix: Fixed an issue where the `created_by` field was not written when publishing an agent version. by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/3287
* 🧪Test: aidp interface test and bugfix by @DongJiBao2001 in https://github.com/ModelEngine-Group/nexent/pull/3290
* Fix: OpenAI LLM test memory exhaustion during collection by @JasonW404 in https://github.com/ModelEngine-Group/nexent/pull/3291
* 🐛 Bugfix: Fix inability to copy content to clipboard in http by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/3292
* fix: resolve skills not exposed to agents and LogLevel enum errors by @JasonW404 in https://github.com/ModelEngine-Group/nexent/pull/3209
* ✨ Feat: model capacity foundation — context management upgrade by @wuyuanfr in https://github.com/ModelEngine-Group/nexent/pull/3293
* 🐛 Bugfix: Fix i18n translation issues in navigation sidebar by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/3288
* 🐛 Bugfix:fix aidp search tool params' save error#3296 by @DongJiBao2001 in https://github.com/ModelEngine-Group/nexent/pull/3297
* Refactor prompt handling, agent workflow, and image builds by @hhhhsc701 in https://github.com/ModelEngine-Group/nexent/pull/3302
* ✨ Feature: add agent repository page and APIs by @Lifeng-Chen in https://github.com/ModelEngine-Group/nexent/pull/3289
* ✨ Feature: Prompt-cache-aware context assembly by @JasonW404 in https://github.com/ModelEngine-Group/nexent/pull/3299
* Add offline package compression and update Docker/Kubernetes instructions by @hhhhsc701 in https://github.com/ModelEngine-Group/nexent/pull/3306
* 🐛 Bugfix: Fix pagination disabled when invitation codes exceed 10 in tenant resource management #3301 by @xuyaqist in https://github.com/ModelEngine-Group/nexent/pull/3307
* [codex] Fix modelengine message flattening by @JasonW404 in https://github.com/ModelEngine-Group/nexent/pull/3309
* add support for uploading files by @jeffwu-1999 in https://github.com/ModelEngine-Group/nexent/pull/3311
* Set offline package components in workflow by @hhhhsc701 in https://github.com/ModelEngine-Group/nexent/pull/3310
* [codex] fix unit test coverage reporting by @JasonW404 in https://github.com/ModelEngine-Group/nexent/pull/3314
* ✨feat: Add conversation share by @gjc199 in https://github.com/ModelEngine-Group/nexent/pull/3308
* ✨Feat: Agent supports model selection. by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/3313
* Ignore root .env in deployment scripts by @hhhhsc701 in https://github.com/ModelEngine-Group/nexent/pull/3318
* Refine CAS login flow and improve config caching by @hhhhsc701 in https://github.com/ModelEngine-Group/nexent/pull/3315
* 🐛Bugfix: Fixed an issue with the `knowledgebasesearch` tool test coverage regarding the `topk` parameter, and fixed an issue where the knowledge base list could not be selected individually for testing in the AIDP tool test. by @DongJiBao2001 in https://github.com/ModelEngine-Group/nexent/pull/3320
* ♻️ Refactor: Tool Test Location Fix by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/3321
* Enhance agent marketplace with pagination, reviews, and import precheck by @Lifeng-Chen in https://github.com/ModelEngine-Group/nexent/pull/3316
* Preload tiktoken cache in main image by @hhhhsc701 in https://github.com/ModelEngine-Group/nexent/pull/3322
* fix: add parallel UT coverage reporting and recover Codecov by @JasonW404 in https://github.com/ModelEngine-Group/nexent/pull/3323
* feat(w11): expand capability catalog to 66 entries + SQL generator + safety guards by @wuyuanfr in https://github.com/ModelEngine-Group/nexent/pull/3317
* 🐛 Bugfix: Fixed an issue where calls to external tool interfaces returning a 401 status code would cause Nexent to log out. by @YehongPan in https://github.com/ModelEngine-Group/nexent/pull/3324
* Expose northbound service in production deployments by @hhhhsc701 in https://github.com/ModelEngine-Group/nexent/pull/3327
* fix(model): stop sending hidden form.provider as modelFactory + relocate script + UI layout fix by @wuyuanfr in https://github.com/ModelEngine-Group/nexent/pull/3332
* fix: ContextComponent.to_messages() returns smolagents-compatible list content by @JasonW404 in https://github.com/ModelEngine-Group/nexent/pull/3330
* 🐛 Chat streaming now can resume when switching to other tabs by @Jasonxia007 in https://github.com/ModelEngine-Group/nexent/pull/3331
* feat: add tool label by @MoeexT in https://github.com/ModelEngine-Group/nexent/pull/3326
* fix: improve tool selection panel i18n and MCP grouping by @MoeexT in https://github.com/ModelEngine-Group/nexent/pull/3338
* 📝Doc:Refresh the dependency instructions for Python and Node.js in doc by @DongJiBao2001 in https://github.com/ModelEngine-Group/nexent/pull/3341
* Revert "📝Doc:Refresh the dependency instructions for Python and Node.js in doc" by @Dallas98 in https://github.com/ModelEngine-Group/nexent/pull/3342
* 📝Doc：Refresh Python dependency instructions for doc by @DongJiBao2001 in https://github.com/ModelEngine-Group/nexent/pull/3345
* release v2.2.2 by @Dallas98 in https://github.com/ModelEngine-Group/nexent/pull/3347

## New Contributors
* @gjc199 made their first contribution in https://github.com/ModelEngine-Group/nexent/pull/3249

**Full Changelog**: https://github.com/ModelEngine-Group/nexent/compare/v2.2.1...v2.2.2
