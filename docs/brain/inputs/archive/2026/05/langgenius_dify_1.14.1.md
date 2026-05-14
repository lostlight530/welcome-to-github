# ℹ️ Intel Report: langgenius/dify
## 🎯 监控目标 (Target)
> langgenius/dify

## 🚀 新版本发布 (New Release)
> Version: 1.14.1
> Date: 2026-05-14T12:17:43.636222

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready ⚠️ Breaking-Change 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 100/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

## 🚀 What's New in v1.14.1?

v1.14.1 is a patch release focused on security hardening, workflow and knowledge-base stability, deployment cleanup, and continued UI platform migration after v1.14.0.

### 🔐 Security

- **Self-hosted `SECRET_KEY` hardening** — Docker deployments no longer rely on a public default key. When `SECRET_KEY` is left empty, the API generates and persists a runtime key through the configured storage backend, while explicitly configured keys continue to work as before. Thanks @laipz8200 in [#36049](https://github.com/langgenius/dify/pull/36049).
- **Internal metrics endpoint protection** — `/threads` and `/db-pool-stat` are hardened to avoid unauthenticated exposure of internal runtime and database-pool details. Thanks @orbisai0security in [#35665](https://github.com/langgenius/dify/pull/35665).
- **Account and tool isolation** — fixed an IDOR issue in `GET /account/avatar` and scoped builtin-tool default-credential cleanup to the current tenant. Thanks @NeatGuyCoding and @GareArc in [#35771](https://github.com/langgenius/dify/pull/35771) and [#35887](https://github.com/langgenius/dify/pull/35887).
- **Dependency security** — upgraded LiteLLM for CVE-2026-42208 and refreshed several backend dependencies, including `urllib3`, `gunicorn`, `gitpython`, `mako`, Google SDK packages, storage libraries, and OpenTelemetry exporter packages. Thanks @crazywoola in [#35953](https://github.com/langgenius/dify/pull/35953), [#35779](https://github.com/langgenius/dify/pull/35779), [#35791](https://github.com/langgenius/dify/pull/35791), [#35863](https://github.com/langgenius/dify/pull/35863), [#35864](https://github.com/langgenius/dify/pull/35864), [#35958](https://github.com/langgenius/dify/pull/35958), [#36011](https://github.com/langgenius/dify/pull/36011), [#36012](https://github.com/langgenius/dify/pull/36012), [#36013](https://github.com/langgenius/dify/pull/36013), [#36017](https://github.com/langgenius/dify/pull/36017), and [#36050](https://github.com/langgenius/dify/pull/36050).

### 🧩 Workflow, HITL, and app runtime

- **Workflow stability** — restored workflow-version loading through the backend API, fixed online-user polling for large app lists, prevented preview resize observer loops, and avoided schema model collisions in trial workflows. Thanks @hjlarry and @lyzno1 in [#35817](https://github.com/langgenius/dify/pull/35817), [#35786](https://github.com/langgenius/dify/pull/35786), [#35936](https://github.com/langgenius/dify/pull/35936), and [#36061](https://github.com/langgenius/dify/pull/36061).
- **Workflow authoring polish** — fixed variable reference picker behavior for sub-variables, workflow node title overflow, condition operator popovers, workflow checklist semantics, and KB metadata filter field selection. Thanks @iamjoel, @hjlarry, @lyzno1, and @shawny011717 in [#35732](https://github.com/langgenius/dify/pull/35732), [#35740](https://github.com/langgenius/dify/pull/35740), [#35828](https://github.com/la
