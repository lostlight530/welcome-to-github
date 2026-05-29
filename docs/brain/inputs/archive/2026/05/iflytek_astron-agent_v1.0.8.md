# ℹ️ Intel Report: iflytek/astron-agent
## 🎯 监控目标 (Target)
> iflytek/astron-agent

## 🚀 新版本发布 (New Release)
> Version: v1.0.8
> Date: 2026-05-29T23:14:36.553362

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: ⚠️ Breaking-Change 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 100/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

This release focuses on production readiness across observability, credential management, workflow execution security, and deployment operations. It adds health checks, gateway authentication, platform account management, and several security hardening fixes.

## Highlights

### Core Capabilities
- Added health check endpoints for core services, including Agent, Workflow, Knowledge, and Memory, making container orchestration, operational checks, and incident diagnosis easier (#1358).
- Added platform account management to centralize platform-level runtime credentials and connect the Console, Knowledge, AI Tools, and plugin invocation paths (#1348).
- Added Workflow gateway authentication based on tenant application credentials (#1352).
- Added script sandbox execution for Workflow code nodes, with related node debugging and sandbox configuration support (#1333).
- Added Astron Agent website deployment support for GitHub Pages and Vercel (#1344).

### Security and Stability
- Strengthened tool-debug redirect validation to reduce SSRF risk (#1338).
- Hardened database DML execution checks to prevent SQL injection (#1340).
- Fixed bot list sort direction handling to avoid invalid query parameters affecting query stability (#1342).
- Fixed credential loading across AI Tools, Knowledge document upload, voice, and model invocation paths by moving them to platform account configuration (#1348).
- Removed an unused Agent service database dependency to simplify service startup requirements (#1358).

### Deployment and Documentation
- Updated Docker Compose, Helm, Nginx, and authenticated deployment guides with platform account, gateway authentication, and core service configuration notes (#1348, #1352).
- Aligned core router and workflow documentation to reduce integration and troubleshooting overhead (#1335).

## Upgrade Notes
- Before upgrading, review the Docker, Helm, and env example changes for platform account, AI Tools, Knowledge, and Workflow configuration.
- If your deployment relies on health checks or gateway authentication, update the related gateway, tenant, and service configuration together.

## Change Scope
- 155 files changed: 6,629 insertions and 2,304 deletions.
- Full comparison: https://github.com/iflytek/astron-agent/compare/v1.0.7...v1.0.8

