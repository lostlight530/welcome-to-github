# bytedance/deer-flow · README.md

> 当前有效引用快照. 完整原文由固定 Git Blob 保存, 当前活动输入不重复内联.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) |
| 来源文件 | [README.md](https://github.com/bytedance/deer-flow/blob/13e6fc29e54201ce650b5f48743f88444b4d46f5/README.md) |
| 来源版本 | `13e6fc29e54201ce650b5f48743f88444b4d46f5` |
| 来源目录 Tree | `cdc73cc1bc7cc4b03ba4c38416654fe3890223c4` |
| 来源内容 Blob | `e5655b044307a21d0fc6f999f71ebb4131836920` |
| 摄取时间 | `2026-11-12T02:43:53.653127+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_bytedance_deer_flow_readme_md` |
| 快照模式 | `PINNED_EXTERNAL_REFERENCE` |
| 规范内容 SHA256 | `6cb706418b51a8d881fe5c5aa350df8118e08676557f201050d7a5d320295919` |
| 原文字节数 | `10273` |
| 原文行数 | `174` |

## 本次变化

- 新增行数 `51`.
- 删除行数 `4300`.
- 完整 Diff 字节数 `396979`.
- 来源变化不等于本仓执行验证或独立研究次数.

## 阅读导航

- Official Website
- Sister Projects
- Coding Plan from ByteDance Volcengine
- InfoQuest
- One-Line Agent Setup
- Quick Start
- Docker
- Local development
- From Deep Research to Super Agent Harness
- Guides
- Recommended Models
- More Documentation
- ⚠️ Security Notice
- Contributing
- License
- Acknowledgments
- Key Contributors
- Star History

## 原文完整性与取回

- [按固定源提交读取完整原文](https://github.com/bytedance/deer-flow/blob/13e6fc29e54201ce650b5f48743f88444b4d46f5/README.md).
- 原文由来源 Blob SHA 与规范内容 SHA256 共同识别.
- 被替换的完整活动快照先原样封存到只追加 Archive.
- Diff 过长时只展示有界预览, 预览不代表完整差异.

<details>
<summary>展开有界版本差异</summary>

```diff
--- previous

+++ e5655b044307a21d0fc6f999f71ebb4131836920

@@ -1,10 +1,8 @@

-# 🦌 DeerFlow - 2.0
+English | [中文](README_zh.md) | [日本語](README_ja.md) | [Français](README_fr.md) | [Русский](README_ru.md) | [Português](README_pt.md) | [한국어](README_ko.md)
 
-English | [中文](./README_zh.md) | [日本語](./README_ja.md) | [Français](./README_fr.md) | [Русский](./README_ru.md) | [Português](./README_pt.md) | [한국어](./README_ko.md)
-
-[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](./backend/pyproject.toml)
-[![Node.js](https://img.shields.io/badge/Node.js-22%2B-339933?logo=node.js&logoColor=white)](./Makefile)
-[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
+[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](backend/pyproject.toml)
+[![Node.js](https://img.shields.io/badge/Node.js-22%2B-339933?logo=node.js&logoColor=white)](Makefile)
+[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
 
 <a href="https://trendshift.io/repositories/14699" target="_blank"><img src="https://trendshift.io/api/badge/repositories/14699" alt="bytedance%2Fdeer-flow | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
 > On February 28th, 2026, DeerFlow claimed the 🏆 #1 spot on GitHub Trending following the launch of version 2. Thanks a million to our incredible community — you made this happen! 💪🔥
@@ -35,10 +33,6 @@

 
 ## InfoQuest
 
-InfoQuest reader, web search, and image search use a 30-second HTTP connect/read
-inactivity timeout. The crawl `timeout` and `navigation_timeout` settings remain
-separate server-side options; they do not control the local HTTP timeout.
-
 DeerFlow has newly integrated the intelligent search and crawling toolset independently developed by BytePlus — [InfoQuest (supports free online experience)](https://docs.byteplus.com/en/docs/InfoQuest/What_is_Info_Quest)
 
 <a href="https://docs.byteplus.com/en/docs/InfoQuest/What_is_Info_Quest" target="_blank">
@@ -48,76 +42,6 @@

 </a>
 
 ---
-
-## Table of Contents
-
-- [🦌 DeerFlow - 2.0](#-deerflow---20)
-  - [Official Website](#official-website)
-  - [Sister Projects](#sister-projects)
-  - [Coding Plan from ByteDance Volcengine](#coding-plan-from-bytedance-volcengine)
-  - [InfoQuest](#infoquest)
-  - [Table of Contents](#table-of-contents)
-  - [One-Line Agent Setup](#one-line-agent-setup)
-  - [Quick Start](#quick-start)
-    - [Configuration](#configuration)
-    - [Running the Application](#running-the-application)
-      - [Deployment Sizing](#deployment-sizing)
-      - [Option 1: Docker (Recommended)](#option-1-docker-recommended)
-      - [Upgrading an existing checkout](#upgrading-an-existing-checkout)
-      - [Option 2: Local Development](#option-2-local-development)
-      - [Startup Modes](#startup-modes)
-      - [LangGraph Studio (Optional)](#langgraph-studio-optional)
-      - [Docker Production Deployment](#docker-production-deployment)
-    - [Advanced](#advanced)
-      - [Sandbox Mode](#sandbox-mode)
-      - [MCP Server](#mcp-server)
-      - [IM Channels](#im-channels)
-      - [Request Trace Correlation](#request-trace-correlation)
-      - [LangSmith Tracing](#langsmith-tracing)
-      - [Langfuse Tracing](#langfuse-tracing)
-      - [Monocle Tracing](#monocle-tracing)
-      - [Using Multiple Providers](#using-multiple-providers)
-      - [Existing-Run Stream Actions](#existing-run-stream-actions)
-      - [Personal Access Tokens](#personal-access-tokens)
-  - [From Deep Research to Super Agent Harness](#from-deep-research-to-super-agent-harness)
-  - [Core Features](#core-features)
-    - [Skills \& Tools](#skills--tools)
-      - [Exporting Custom Skills](#exporting-custom-skills)
-      - [Claude Code Integration](#claude-code-integration)
-    - [Private Knowledge Retrieval (RAGFlow)](#private-knowledge-retrieval-ragflow)
-    - [Chat Archive](#chat-archive)
-    - [Session Goals](#session-goals)
-    - [Manual Context Compaction](#manual-context-compaction)
-    - [Sub-Agents](#sub-agents)
-    - [Sandbox \& File System](#sandbox--file-system)
-    - [Agentic Browser Control](#agentic-browser-control)
-    - [Context Engineering](#context-engineering)
-    - [Reading a Referenced Conversation](#reading-a-referenced-conversation)
-    - [Current Task Notes](#current-task-notes)
-    - [Long-Term Memory](#long-term-memory)
-  - [Recommended Models](#recommended-models)
-  - [Embedded Python Client](#embedded-python-client)
-  - [Projects](#projects)
-    - [Project instructions](#project-instructions)
-    - [Document shelf](#document-shelf)
-    - [Archive read semantics](#archive-read-semantics)
-    - [Trash](#trash)
-  - [Scheduled Tasks](#scheduled-tasks)
-    - [Preview cron occurrences through the API](#preview-cron-occurrences-through-the-api)
-    - [Upgrade Notes](#upgrade-notes)
-  - [Terminal Workbench (TUI)](#terminal-workbench-tui)
-  - [Documentation](#documentation)
-  - [⚠️ Security Notice](#️-security-notice)
-    - [Improper Deployment May Introduce Security Risks](#improper-deployment-may-introduce-security-risks)
-    - [Gateway Admin Is Equivalent to Code Execution](#gateway-admin-is-equivalent-to-code-execution)
-    - [External Chat Message Roles](#external-chat-message-roles)
-    - [Deployment Defaults](#deployment-defaults)
-    - [Security Recommendations](#security-recommendations)
-  - [Contributing](#contributing)
-  - [License](#license)
-  - [Acknowledgments](#acknowledgments)
-    - [Key Contributors](#key-contributors)
-  - [Star History](#star-history)
 
 ## One-Line Agent Setup
 
@@ -131,1617 +55,32 @@

 
 ## Quick Start
 
-### Configuration
+```bash
+git clone https://github.com/bytedance/deer-flow.git
+cd deer-flow
+make setup          # interactive wizard: writes config.yaml and .env (about 2 minutes)
+```
 
-Application SQL JSON writes normalize non-finite floats (`NaN`, `Infinity`, `-Infinity`) to `null` on SQLite and PostgreSQL, including DB-backed agent definitions and skill-mutation records. Existing rows are not rewritten.
-
-With `run_events.backend: db`, caller-supplied ISO 8601 event timestamps are normalized to UTC before storage, preserving their instant when SQLite drops timezone information. Timestamps without an offset are treated as UTC. Previously stored timestamps are not rewritten.
-
-Run event streams include `run.terminal` for the owning worker's confirmed final
-Run status, while `run.end` continues to describe each root graph completion.
-Terminal publication is best effort; event persistence failure does not undo the
-Run outcome or prevent stream completion. Recovery with built-in SQL Run and Event stores
-sharing an engine uses one pooled connection for each guarded event write, so it
-can publish with only one pool slot available. See [Run Event Stream](backend/docs/RUN_EVENT_STREAM.md#authoritative-run-outcome).
-
-PostgreSQL async ORM connections and the offline command accept `postgres://`
-and `postgresql://` URLs, including `?sslmode=disable` or `?sslmode=verify-full`.
-SSL modes are preserved; conflicting `ssl`/`sslmode` settings are rejected.
-Explicit `channel_binding` options are rejected because asyncpg cannot enforce
-them. Synchronous psycopg and LangGraph DSNs retain their libpq options.
-
-With a fencing-capable SQL RunStore and `DbRunEventStore`, host-authorized
-producer writes validate the persisted Run incarnation, producer epoch and state
-even with `run_events.producer_fencing: "off"`. Stale Journal flushes after
-takeover or deletion may therefore be rejected in the default configuration.
-On PostgreSQL, these writes hold the Thread Fence and RunRow lock through commit.
-Checkpoint and branch history imports use a separate host grant bound to a
-durable thread-operation reservation and the captured thread identity. Strict
-mode permits these imports without treating synthetic turn IDs as admitted Runs;
-deletion, reservation revocation or lease expiry invalidates their grant.
-Messages preceding the first human input retain their existing synthetic turn 0.
-
... [DIFF_PREVIEW_TRUNCATED]
```

</details>
