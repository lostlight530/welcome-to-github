# ℹ️ Intel Report: langgenius/dify
## 🎯 监控目标 (Target)
> langgenius/dify

## 🚀 新版本发布 (New Release)
> Version: 1.14.0
> Date: 2026-04-29T04:17:35.658555

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready ⚠️ Breaking-Change 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 100/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

## 🚀 What's New in v1.14.0?

### Collaboration
<img width="2632" height="1190" alt="img_v3_02117_67a67218-1ae5-4d68-a45b-3ada592f87fg" src="https://github.com/user-attachments/assets/1d4a3660-8a6a-4b29-9766-4d5b5fd9a51b" />

Collaboration allows workspace members to edit the same workflow together, with synced graph updates, online presence, and shared visibility into who is working where.

On self-hosted deployments, collaboration is turned off by default. Enable it by setting:

```
ENABLE_COLLABORATION_MODE = true
SERVER_WORKER_CLASS = geventwebsocket.gunicorn.workers.GeventWebSocketWorker
NEXT_PUBLIC_SOCKET_URL = your deployment’s WebSocket URL (e.g., wss://dify.example.com)
```

For more details, see [Full Documentation](https://docs.dify.ai/en/use-dify/build/workflow-collaboration)

### Human-in-the-loop (HITL)

- **Service API for HITL** — programmatic support for human-in-the-loop flows alongside existing console behavior.

### MCP and plugins

- **MCP tool metadata** — refresh after updates so the UI stays in sync.
- **MCP server URL** — fix double `/v1` that could break OAuth and authorization (404).
- **MCP OAuth discovery** — handle malformed JSON safely.
- **MCP schema publishing** — map `checkbox` and `json_object` types correctly.
- **Plugins** — auto-upgrade strategy persistence, local installer and file-input behavior, tenant scoping for inner API end-user lookup.

### Marketplace and OAuth

- **Marketplace and OAuth** — targeted fixes for marketplace flows and OAuth sign-in (including edge cases such as null email on GitHub OAuth).

### UI kit and front-end platform

- **`@langgenius/dify-ui`** — shared primitives (for example **PreviewCard**, **Meter**), design tokens, and broad migration from ad-hoc `web/base/ui` toward the package.
- **Accessibility** — date and time pickers, auto-update strategy picker, scrollbars in plugin and model selectors, and related polish.
- **Goto Anything** — recent items, `/go` command, deeper app sub-sections; fix for **Cmd+K** (removed problematic dynamic import).
- **Prompt editor** — slash-triggered **variable filtering**; keyboard **up/down** in variable lists.
- **Follow-up questions** — improved settings and token limits for suggested questions.
- **Modals** — ApiKey, provider config, and others refactored toward a shared **Dialog** pattern with tests.

### Observability and analytics
- **Langfuse** — optional **time-to-first-token (TTFT)** reporting.
- **Explore** — banner impression tracking; app preview event tracking on cards.

### Billing and quotas

- **Quota v3** integration in the product stack.
- **Billing UI** — Meter-based usage presentation; more resilient cleanup when billing APIs fail.
- **File uploader** — billing-aware behavior and copy updates.

### Data, RAG, and knowledge

- **Summary index and Weaviate** — compatibility fixes when using the summary index with Weaviate.
- **Vector projection** — include `is_summary` an
