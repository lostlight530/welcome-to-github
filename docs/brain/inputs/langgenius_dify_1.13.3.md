# ℹ️ Intel Report: langgenius/dify
## 🎯 监控目标 (Target)
> langgenius/dify

## 🚀 新版本发布 (New Release)
> Version: 1.13.3
> Date: 2026-03-31T05:55:37.067036

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: 🏷️ Edge-Ready ⚠️ Breaking-Change 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 110/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

## 🚀 What's New in v1.13.3?
Our latest patch release, v1.13.3, focuses on stability and correctness across workflow execution, streaming, and knowledge retrieval. Here's a quick look at the most important updates:

### 🎬 New Features
- **Workflow Configuration**: Added variable-reference support for model parameters in LLM, Question Classifier, and Variable Extractor nodes by @scdeng in #33082.

### 🛠️ Bug Fixes
- **Streaming Reliability**: Fixed `StreamsBroadcastChannel` replay and concurrency issues to keep frontend/backend event delivery stable by @QuantumGhost in #34030 and #34061.
- **Workflow Editor Behavior**: Fixed pasted nodes retaining Loop/Iteration metadata and prevented `HumanInput` nodes from being pasted into invalid containers by @majiayu000 and @hjlarry in #29983 and #34077.
- **Runtime Execution**: Restored prompt message transformation logic and corrected `max_retries=0` handling for executor-driven HTTP Request execution by @QuantumGhost, @fatelei, and @kurokobo in #33666, #33619, and #33688.
- **Knowledge Retrieval**: Preserved citation metadata in web responses, fixed crashes when dataset icon metadata is missing, corrected hit-count query filtering, and restored indexed document chunk previews by @Theysua, @copilot-swe-agent, and @fatelei in #33778, #33907, #33757, and #33942.

### 🔧 Under the Hood
- **Patch Stability**: This release prioritizes targeted fixes for workflow runtime behavior, real-time streaming, and knowledge base usability for teams upgrading from v1.13.2.

---

## Upgrade Guide

> [!IMPORTANT]
> We updated the default Python and Node.js paths for Sandbox in the previous release.
> If you already have existing Sandbox configuration files, these values are **not** updated automatically.
> Please manually update both the Python path and the Node.js path in your existing configuration files to match the new defaults.

### Docker Compose Deployments

1. Back up your customized docker-compose YAML file (optional)

   ```bash
   cd docker
   cp docker-compose.yaml docker-compose.yaml.$(date +%s).bak
   ```

2. Get the latest code from the main branch

   ```bash
   git checkout main
   git pull origin main
   ```

3. Stop the service. Please execute in the docker directory

   ```bash
   docker compose down
   ```

4. Back up data

   ```bash
   tar -cvf volumes-$(date +%s).tgz volumes
   ```

5. Upgrade services

   ```bash
   docker compose up -d
   ```

### Source Code Deployments

1. Stop the API server, Worker, and Web frontend Server.

2. Get the latest code from the release branch:

   ```bash
   git checkout 1.13.3
   ```

3. Update Python dependencies:

   ```bash
   cd api
   uv sync
   ```

4. Then, let's run the migration script:

   ```bash
   uv run flask db upgrade
   ```

5. Finally, run the API server, Worker, and Web frontend Server again.

---

## What's Changed
* refactor(web): number inputs to use Base UI Nu
