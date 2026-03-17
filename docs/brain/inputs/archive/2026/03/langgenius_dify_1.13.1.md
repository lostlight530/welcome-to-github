# ℹ️ Intel Report: langgenius/dify
## 🎯 监控目标 (Target)
> langgenius/dify

## 🚀 新版本发布 (New Release)
> Version: 1.13.1
> Date: 2026-03-17T11:57:40.044260

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready ⚠️ Breaking-Change 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 110/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

## 🚀 Major Functional Changes

### Data platform and dataset operations

- Added **Hologres** as a supported backend option for both vector retrieval and full-text search.
- Added Service API endpoints for dataset document downloads:
  - Batch ZIP download for selected documents.
  - Signed URL download for single-document original files.

### Workflow and chat experience improvements

- **Breaking change:** HITL email content now uses markdown rendering before delivery.
  Existing email templates that relied on raw/plain behavior may render differently after upgrade.
- Draft variables are now user-scoped instead of app-scoped. Historical draft variables will not be available after upgrading.
- Added edge context menu support in workflow canvas, including direct edge deletion.
- Preserved existing connections when changing node types in workflow editing.
- Added configurable send-key behavior (`Enter` vs `Shift+Enter`) for embedded chat input.
- Added file payloads in message-end stream responses.
- Removed GPT-4-specific hardcoded behavior from default model selection logic.
- Added a new `export-app-messages` CLI command to export application messages and related feedback to `JSONL.GZ` (local or cloud storage).

## 🔐 Security Updates

- Prevented SQL injection risks in vector-store query paths by switching to parameterized SQL in affected implementations.
- Hardened HITL email delivery:
  - Sanitize subject and body content.
  - Strip CR/LF from subjects to prevent SMTP header-injection vectors.
- Enforced ownership checks for conversation deletion APIs.
- Cleared stale provider credentials during plugin uninstall to reduce residual credential risk.
- Improved enterprise API error handling and license-enforcement behavior for invalid/expired license states.

## 🏗️ Configuration, Architecture, and Deployment Updates

### Deployment and operations
- Added a dedicated Celery queue: `dataset_summary` for LLM-heavy summary generation tasks.
  - Ensure workers subscribe to this queue to avoid summary-job backlog.
- Added telemetry metrics for retention cleanup tasks (messages/workflow runs), plus flush behavior for short-lived command jobs.

### Configuration changes

- Added `REDIS_MAX_CONNECTIONS`.
- Deprecated `PUBSUB_*` event-bus settings in favor of `EVENT_BUS_*` settings.

## 🛠 Other Noteworthy Changes

- Fixed `workflow_runs.started_at` being overwritten on resume.
- Fixed metadata batch-edit silent failures caused by split-transaction edge cases.
- Fixed metadata filter extraction issues in knowledge retrieval (`{{...}}` conditions).
- Restored citation visibility in advanced chat applications.
- Fixed conversation variable reset behavior after HITL nodes.
- Fixed a page crash in knowledge-retrieval node configuration flow.
- Fixed chat assistant blocking response-mode behavior.
- Added `doc_type` handling in Weaviate vector attributes for better compatibility.
- Upgraded OpenTelemetry dep
