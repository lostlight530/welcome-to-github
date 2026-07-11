# ℹ️ Intel Report: langgenius/dify
## 🎯 监控目标 (Target)
> langgenius/dify

## 🚀 新版本发布 (New Release)
> Version: 1.13.2
> Date: 2026-03-25T09:56:13.339954

## 💡 项目洞察 (Insight)
> **Architect's Analysis**: ⚠️ Breaking-Change 🔗 Agent-Protocol

## 🛡️ 信任评分 (Trust Score)
> Score: 100/100

## 🔨 最近提交 (Recent Commits)
*Summary from release notes:*

This patch release fixes several critical regressions and stability issues introduced in v1.13.1, including:

- a severe regression in prompt message transformation that caused multiple LLM-plugin invocation failures across
   LLM-related nodes, including LLM and Question Classifier.
- Knowledge Retrieval node execution failures caused by incompatible enum values
- improper Weaviate client cleanup

---

## Upgrade Guide

> [!IMPORTANT]
> If you use custom `CELERY_QUEUES`, make sure `workflow_based_app_execution` is included.
> If `ENABLE_API_TOKEN_LAST_USED_UPDATE_TASK=true`, also include `api_token`.
>
> For background and details, see **⚠️ Important Upgrade Note** and **🔧 Operational Note** above.

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

> [!NOTE]
>
> If you encounter errors like below
>
> ```bash
> 2025/11/26 11:37:57 /app/internal/db/pg/pg.go:30
> [error] failed to initialize database, got error failed to connect to `host=db_postgres user=postgres database=dify_plugin`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)
>
> 2025/11/26 11:37:57 /app/internal/db/pg/pg.go:34
> [error] failed to initialize database, got error failed to connect to `host=db_postgres user=postgres database=postgres`: hostname > resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)
> 2025/11/26 11:37:57 init.go:99: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres user=postgres database=postgres`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)
> panic: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres user=postgres database=postgres`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)
> ```
> Please use the following command instead. For details, please read this https://github.com/langgenius/dify/issues/28706
>    ```bash
>    docker compose --profile postgresql up -d
>    ```

### Source Code Deployments

1. Stop the API server, Worker, and Web frontend Server.

2. Get the latest code from the release branch:

   ```bash
   git checkout 1.13.2
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


## What's Ch
