# ℹ️ Intel Report: iflytek/astron-agent
## 🎯 监控目标 (Target)
> iflytek/astron-agent

## 🚀 新版本发布 (New Release)
> Version: v1.1.0
> Date: 2026-07-09T23:12:22.527388

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 90/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

This release expands the standalone Agent into a more capable execution surface: Agents can now use configured Workflows, Link plugins, and Mem0-backed memory directly from the standard Agent experience. It also includes security hardening for tool-debug URLs, CI/test stabilization, and documentation cleanup for the v1.1 line.

## Highlights

### Agent Capabilities

- **Workflow invocation inside Agents.** Standard Agents can persist workflow capabilities, expose workflows as runtime tool callbacks, and use them from both chat and debug paths. The implementation includes ownership and space-membership validation, workflow runtime service support, response extraction handling, and test coverage for key runtime branches. (#1487)
- **Plugin capability for Standard Agents.** The Agent ability page can import Link plugins from the plugin store, persist selected tools, reload them in bot details, and pass them into debug/chat requests for runtime invocation. Official/admin-owned plugins are handled as trusted import sources. (#1448)
- **Mem0 Agent memory.** Added configurable Mem0 memory support for Agents, including scoped memory settings, improved retrieval, app-level memory isolation, non-blocking memory writes, Chinese memory preservation, and related CI/test fixes. (#1479)

### Security and Stability

- Hardened official tool debug URL validation and trusted-owner handling to reduce unsafe redirect/debug invocation risk. (#1453)
- Addressed GitHub code-scanning alert no. 54 for server-side request forgery. (#1459)
- Stabilized Superteam CI and remote test checks, including S3 client integration-test setup and remaining remote test failures. (#1429, #1431, #1432, #1433)

### Documentation and Maintenance

- Added the v1.0.9 release-notes PDF to homepage resources. (#1442)
- Cleaned up unrelated documentation/files and ignored local agent instruction files in git. (#1438, #1435)

## Upgrade Notes

- To use Agent workflow invocation, deploy the Console/Toolkit changes together so configured workflows can be resolved and executed through the new runtime path.
- Review Agent capability settings after upgrade if you plan to enable plugins, workflow tools, or Mem0 memory for existing Agents.

## Change Scope

- 154 files changed: 6,489 insertions and 6,559 deletions.
- Full comparison: https://github.com/iflytek/astron-agent/compare/v1.0.9...v1.1.0
