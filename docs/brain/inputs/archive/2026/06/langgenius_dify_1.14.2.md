# ℹ️ Intel Report: langgenius/dify
## 🎯 监控目标 (Target)
> langgenius/dify

## 🚀 新版本发布 (New Release)
> Version: 1.14.2
> Date: 2026-06-01T05:39:43.193271

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: ⚠️ Breaking-Change 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 100/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

## 🚀 What's New in v1.14.2?

v1.14.2 is a patch release focused on security hardening, workflow and knowledge reliability, observability fixes, agent groundwork, and deployment/runtime tuning after v1.14.1.

### 🔐 Security and administration

- **Tenant-scoped sensitive endpoints** — strengthened tenant isolation for app trace-config endpoints and FilePreview text extraction. Thanks @xr843 in [#35793](https://github.com/langgenius/dify/pull/35793) and [#35797](https://github.com/langgenius/dify/pull/35797).
- **Tool credential safety** — restricted default builtin tool credential updates to workspace admins and owners, and cleaned stale tenant tool credentials during `reset-encrypt-key-pair`. Thanks @NeatGuyCoding and @xr843 in [#36264](https://github.com/langgenius/dify/pull/36264) and [#35843](https://github.com/langgenius/dify/pull/35843).

### 🧩 Workflow, HITL, and app runtime

- **Workflow execution reliability** — restored tracing after HITL workflow resume, improved workflow run callback tracking, reduced message-update database roundtrips, fixed memory fetches outside Flask context, and closed base64 file lookup sessions correctly. Thanks @Blackoutta, @CodingOnStar, @wylswz, @hjlarry, and @escape0707 in [#36064](https://github.com/langgenius/dify/pull/36064), [#36149](https://github.com/langgenius/dify/pull/36149), [#36213](https://github.com/langgenius/dify/pull/36213), [#36253](https://github.com/langgenius/dify/pull/36253), and [#36308](https://github.com/langgenius/dify/pull/36308).
- **Workflow and model selection polish** — fixed loading behavior when no model is selected, filtered model presets by supported parameters, and improved API extension dialog controls. Thanks @iamjoel and @lyzno1 in [#36342](https://github.com/langgenius/dify/pull/36342), [#36339](https://github.com/langgenius/dify/pull/36339), and [#36323](https://github.com/langgenius/dify/pull/36323).

### 📚 Data, RAG, and knowledge

- **Knowledge-base stability** — fixed knowledge hit-testing rendering, empty knowledge creation, recommended app category ordering, and null handling in recommended app detail retrieval. Thanks @FFXN, @laipz8200, @hjlarry, and @EvanYao826 in [#36106](https://github.com/langgenius/dify/pull/36106), [#36336](https://github.com/langgenius/dify/pull/36336), [#36161](https://github.com/langgenius/dify/pull/36161), and [#36153](https://github.com/langgenius/dify/pull/36153).
- **RAG and document processing** — allowed LLM nodes to access retrieved knowledge files, regenerated document summaries after API updates, fixed pipeline template rendering, and handled credential fetch failures in RAG pipelines more gracefully. Thanks @laipz8200, @EvanYao826, @FFXN, and @linw1995 in [#36175](https://github.com/langgenius/dify/pull/36175), [#36035](https://github.com/langgenius/dify/pull/36035), [#36168](https://github.com/langgenius/dify/pull/36168), and [#36165](https://github.com/langgenius/dify/pull/36165).

### 🎨 Web UI and product
