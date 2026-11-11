# bytedance/deer-flow · README.md

> 当前有效引用快照. 完整原文由固定 Git Blob 保存, 当前活动输入不重复内联.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) |
| 来源文件 | [README.md](https://github.com/bytedance/deer-flow/blob/bf4aa82f09939ba364f43385ddefa7b3619099d7/README.md) |
| 来源版本 | `bf4aa82f09939ba364f43385ddefa7b3619099d7` |
| 来源目录 Tree | `b3539e9ede9777549d050ed7c9528d93454f7dab` |
| 来源内容 Blob | `e8a097d218cb5881d9745ef11e2e41fc4cffe5c6` |
| 摄取时间 | `2026-11-11T01:44:07.819622+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_bytedance_deer_flow_readme_md` |
| 快照模式 | `PINNED_EXTERNAL_REFERENCE` |
| 规范内容 SHA256 | `50737426492e905b0d12cd4cf3f8490662a8e5d523dea4dc14bd1a22abcf2f60` |
| 原文字节数 | `393353` |
| 原文行数 | `4423` |

## 本次变化

- 新增行数 `17`.
- 删除行数 `1`.
- 完整 Diff 字节数 `4236`.
- 来源变化不等于本仓执行验证或独立研究次数.

## 阅读导航

- 🦌 DeerFlow - 2.0
- Official Website
- Sister Projects
- Coding Plan from ByteDance Volcengine
- InfoQuest
- Table of Contents
- One-Line Agent Setup
- Quick Start
- Configuration
- Running the Application
- Deployment Sizing
- Option 1: Docker (Recommended)
- Upgrading an existing checkout
- Option 2: Local Development
- Startup Modes
- LangGraph Studio (Optional)
- Docker Production Deployment
- One-step (build + start)
- Two-step (build once, start later)
- Stop
- Advanced
- Sandbox Mode
- MCP Server
- IM Channels

## 原文完整性与取回

- [按固定源提交读取完整原文](https://github.com/bytedance/deer-flow/blob/bf4aa82f09939ba364f43385ddefa7b3619099d7/README.md).
- 原文由来源 Blob SHA 与规范内容 SHA256 共同识别.
- 被替换的完整活动快照先原样封存到只追加 Archive.
- Diff 过长时只展示有界预览, 预览不代表完整差异.

<details>
<summary>展开有界版本差异</summary>

```diff
--- previous

+++ e8a097d218cb5881d9745ef11e2e41fc4cffe5c6

@@ -845,6 +845,13 @@

 >
 > Reconciliation uses an atomic takeover claim that re-checks the lease after candidate selection, so a successful owner renewal wins over orphan recovery and only one reconciler can report a run as recovered. When multiple Gateway workers share the Docker/AIO or E2B sandbox backend, also configure `sandbox.ownership.type: redis`; E2B uses the leases during background startup and periodic reconciliation so duplicate/orphan cleanup cannot terminate a live peer's sandbox.
 
+If a completed thread operation (such as a checkpoint, goal, or artifact write,
+branch, or deletion) fails to release its database reservation, the same Gateway
+worker retries cleanup when it receives a new run or mutation for that thread.
+This also works in single-worker deployments with lease heartbeats disabled.
+If cleanup fails again, admission returns a busy response. Completed requests
+can still replay their saved results by idempotency key.
+
 See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed Docker development guide.
 
 #### Upgrading an existing checkout
@@ -1170,6 +1177,9 @@

 BoxLite shutdown rejects late VM registration and keeps its SDK loop open while
 in-flight acquisitions finish. If they cannot drain within five seconds,
 shutdown fails with resources still owned and can be retried.
+Startup-recovered BoxLite VMs use the same private async loop as newly created
+VMs for health checks, commands, and shutdown. Recovery skips boxes removed
+after discovery without creating replacement VMs.
 
 Successful `read_file` calls treat a JSON document's `error` field as file data,
 not a failure of the read tool. This keeps receipts accurate when inspecting
@@ -1300,6 +1310,8 @@

 DeerFlow supports receiving tasks from messaging apps. Channels auto-start when configured — no public IP required for any of them.
 
 Generated-file replies explain when a channel cannot send attachments. If some or all uploads fail, DeerFlow sends one combined notice naming the unsent files when the platform still accepts replies. Successful uploads add no duplicate confirmation. Files remain in the DeerFlow conversation; an expired reply window is logged without switching to proactive messaging.
+
+Telegram retries photos rejected for invalid dimensions or image processing once as documents, preserving the original file and reply target.
 
 Cancelling a channel restart discards its pending configuration reload, preserving newer runtime settings applied afterward.
 
@@ -2522,6 +2534,9 @@

 in the extension catalog with localized installation-guide metadata.
 Reopening a bookmark resolves the conversation's current agent through the host, so
 custom-agent conversations retain their original chat entry point, including older bookmarks.
+In **Capabilities → Extensions**, an enabled extension’s detail page links directly to its registered workspace pages. The page also includes usage guidance and keeps package details under **Technical details**.
+Extension packages can provide localized purpose and usage steps in `deerflow-extension.json`, including optional prerequisites. The same detail page supports background extensions without a browser module. All bundled examples include this description; see the [authoring contract](examples/README.md#describe-the-extension).
+
 The independent [Agent teams example](examples/deerflow-extension-agent-teams/README.md)
 lets full Custom Agents collaborate through native `@` mentions, shared messages and
 asynchronous peer requests, with a separate team page and persistent member conversations.
@@ -2734,7 +2749,8 @@

 exhaustion. A limit breach starts a five-minute per-process cooldown for the
 same thread/history window and policy, including rebuilt middleware. A larger
 input budget or smaller source window permits an immediate retry. Model fallback
-and SDK retries can add calls. See the
+and SDK retries can add calls. For vLLM run models, history and retention
+estimates include assistant reasoning replayed to the provider. See the
 [summarization guide](backend/docs/summarization.md).
 
 With `task_continuity.enabled`, `history_search` searches the current task's active
```

</details>
