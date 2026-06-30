# ℹ️ Intel Report: iflytek/astron-agent
## 🎯 监控目标 (Target)
> iflytek/astron-agent

## 🚀 新版本发布 (New Release)
> Version: v1.0.9
> Date: 2026-06-30T06:04:14.678207

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: ⚠️ Breaking-Change 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 100/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

This release centers on a major overhaul of the **standalone Agent** (agents created directly in the Console): its chat runtime was rebuilt on Spring AI and gained MCP and Skill capabilities. It also adds team publish approval, an agent workbench redesign, and a round of documentation, examples, and security improvements.

## Highlights

### Standalone Agent

- **Runtime rebuilt on Spring AI.** The standalone agent's chat runtime was migrated from a hand-rolled OpenAI-compatible implementation to Spring AI (`spring-ai-openai`), using `OpenAiChatModel` and `ToolCallback` / `ToolCallingManager` for model calls, streaming, and framework-managed tool execution. Legacy runtime paths were removed. (#1418, #1425)
- **MCP (Model Context Protocol) support.** Standalone agents can now connect external MCP tools by configuring MCP Server URLs on the capability page; the runtime fetches and invokes those tools and lets the model choose them by description. (#1418, #1426)
- **Skill module.** A new Skill block on the capability page reuses the resource-management importable-skill list (search / multi-select / remove, up to 30). At runtime each skill exposes `read_skill_*` (reads `SKILL.md` and referenced resources) and `run_skill_*` (executes commands in the E2B script sandbox via a new `core/agent` endpoint). (#1424, #1427)

### Collaboration & Workbench

- Added a **team publish approval** flow for shared spaces, with OWNER/ADMIN review of workflow/agent publishing. (#1383)
- **Redesigned the agent workbench** with refined settings and interactions. (#1397)
- Added **agent debug conversation history** and improved web-search tool orchestration.

### Docs, Examples & i18n

- Standardized the VitePress docs site with an i18n layout, edit links, and a contribution guide. (#1406)
- Added a **community workflow examples gallery** (scaffold, seeds, lint, docs page) and a submission issue template. (#1407, #1408)
- Supplemented the FAQ with community-sourced Q&A (#1413) and refreshed MiniMax M-series model examples (#1373).

### Security & Stability

- Hardened code-scanning security checks. (#1398, #1402)
- Tightened agent tool-calling boundaries and stabilized order-dependent toolkit tests. (#1403)

## Upgrade Notes

- **Standalone agent model selection:** the two built-in default Spark models were removed from agent creation — choose a model explicitly (e.g., one configured in Model Management).
- **Database migration:** Flyway `V1.38` adds the `chat_bot_base.skills` column and runs automatically on startup.
- **Skill execution (`run_skill`):** requires an E2B script sandbox configured in resource management. The Console backend reaches `core/agent` via the `AGENT_URL` env (defaults to `http://core-agent:${CORE_AGENT_PORT}` in Docker). `read_skill` works without a sandbox.

## Change Scope

- 248 files changed: 18,358 insertions and 6,136 deletions.
- Full comparison: https://github.com/iflytek/astron-agent/compare/v1.0.8...v1.0.9

