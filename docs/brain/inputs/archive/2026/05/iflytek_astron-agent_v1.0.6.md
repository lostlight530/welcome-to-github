# ℹ️ Intel Report: iflytek/astron-agent
## 🎯 监控目标 (Target)
> iflytek/astron-agent

## 🚀 新版本发布 (New Release)
> Version: v1.0.6
> Date: 2026-05-01T22:49:41.800862

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 90/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

## What's Changed

Based on PRs merged into `main` since `v1.0.5`.

### New Features
- feat(knowledge): expose optional RAGFlow retrieval parameters ([#1231](https://github.com/iflytek/astron-agent/pull/1231))
- feat: Added skill system，you can now manage skills in the resource management interface and use skills in the plugins of the workflow’s Agent nodes ([#1239](https://github.com/iflytek/astron-agent/pull/1239))
- feat(knowledge): route RAGFlow ops by per-repo datasets ([#1242](https://github.com/iflytek/astron-agent/pull/1242))
- feat: add workflow export to SKILL feature ([#1249](https://github.com/iflytek/astron-agent/pull/1249))

### Fixes
- fix(knowledge): forward documentId in /document/split for Ragflow upsert ([#1206](https://github.com/iflytek/astron-agent/pull/1206))
- fix(knowledge): paginate RAGFlow chunks and use id filter for lookups ([#1211](https://github.com/iflytek/astron-agent/pull/1211))
- fix(knowledge): propagate RAGFlow failures instead of swallowing to empty results ([#1222](https://github.com/iflytek/astron-agent/pull/1222))
- fix(ragflow): honor explicit dataset id during upload ([#1240](https://github.com/iflytek/astron-agent/pull/1240))

### Improvements
- refactor(knowledge): unify RAGFLOW_DEFAULT_GROUP fallback loader ([#1208](https://github.com/iflytek/astron-agent/pull/1208))
