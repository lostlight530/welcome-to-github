# bytedance/deer-flow · README.md

> 当前有效引用快照. 完整原文由固定 Git Blob 保存, 当前活动输入不重复内联.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) |
| 来源文件 | [README.md](https://github.com/bytedance/deer-flow/blob/3b05ab7dc3a7dc6df00601ab348b6ed691ff273b/README.md) |
| 来源版本 | `3b05ab7dc3a7dc6df00601ab348b6ed691ff273b` |
| 来源目录 Tree | `a02807088d53022c1905de7b01173463a6373ee5` |
| 来源内容 Blob | `272675321ab4a39caf35b3391ed18f29c475bec0` |
| 摄取时间 | `2026-11-09T01:28:46.249169+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_bytedance_deer_flow_readme_md` |
| 快照模式 | `PINNED_EXTERNAL_REFERENCE` |
| 规范内容 SHA256 | `1bf3d47f322a4368f588dc71319f6c8af2183133ce8f052e56b9e1e1211b6436` |
| 原文字节数 | `388511` |
| 原文行数 | `4356` |

## 本次变化

- 新增行数 `42`.
- 删除行数 `17`.
- 完整 Diff 字节数 `25457`.
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

- [按固定源提交读取完整原文](https://github.com/bytedance/deer-flow/blob/3b05ab7dc3a7dc6df00601ab348b6ed691ff273b/README.md).
- 原文由来源 Blob SHA 与规范内容 SHA256 共同识别.
- 被替换的完整活动快照先原样封存到只追加 Archive.
- Diff 过长时只展示有界预览, 预览不代表完整差异.

<details>
<summary>展开有界版本差异</summary>

```diff
--- previous

+++ 272675321ab4a39caf35b3391ed18f29c475bec0

@@ -280,6 +280,8 @@

 
    Jina, Browserless, and InfoQuest web fetches resolve relative links and image sources using the requested page URL (or a usable HTML base URL), so returned Markdown includes complete destinations. Link resolution preserves the surrounding HTML source, including malformed-page formatting.
 
+   Direct Python calls to `web_fetch_tool` return `(content, artifact)` so Browserless can keep the target page's HTTP status out of page prose. Callers that previously expected a string should unpack the tuple; Agent tool calls continue to expose content and artifact through LangChain's tool result.
+
    Self-hosted Browserless, Crawl4AI, Firecrawl, and fastCRW fetch backends require outbound isolation from private, loopback, link-local, and cloud-metadata networks before setting `network_isolation_confirmed: true` on each tool. DeerFlow rejects private or unverifiable backends by default because those services handle redirects, DNS resolution, and subresources themselves. `allow_private_addresses` permits intentional internal target URLs and does not bypass the backend check. See [delegated fetch deployment](backend/docs/CONFIGURATION.md#delegated-fetch-backend-isolation); `make doctor` reports backend configurations that would be refused.
 
    Jina fetches support opt-in bounded retries via `max_retries` (default `0`) and `retry_budget_seconds` (default `30`) in the tool configuration. Valid `Retry-After` hints set a minimum wait for HTTP 429/503; 429 without a valid hint stays terminal. Hints that cannot fit the remaining budget stop retries. Local backoff remains randomized. Retries may increase upstream requests and cost; see [Jina fetch retries](backend/docs/CONFIGURATION.md#jina-fetch-retries).
@@ -335,7 +337,7 @@

    Administrators can open **Settings → Models** to select a provider and enter
    only its **API Key** and **model ID**. Endpoints, authentication and adapters are
    backend presets for OpenAI, Anthropic, DeepSeek, Alibaba Cloud Bailian/Qwen,
-   Volcengine/Doubao, Moonshot/Kimi, Zhipu/Z.AI and MiniMax. Region and plan-specific
+   Volcengine/Doubao, Moonshot/Kimi, Zhipu/Z.AI, MiniMax and StepFun. Region and plan-specific
    entries are explicitly distinguished. Arbitrary model IDs are accepted; internal
    names are generated automatically and remain stable when a model ID changes.
    Newly saved models are enabled and immediately refresh existing chat and Agent
@@ -1258,9 +1260,9 @@

 
 When deferred MCP tool discovery is enabled, `tool_search` supports opt-in literal keyword queries such as `keywords:notebook jupyter`. Keywords match names and descriptions in any order, ranked by distinct term coverage and then name hits; ties retain catalog order. This mode uses the first 256 characters after the prefix and at most 16 unique whitespace-separated terms, returning up to five tools. Punctuation stays literal. Bare queries and `+required` ranking keep their existing regular-expression semantics; `select:tool_a,tool_b` still fetches all exact, case-sensitive name matches.
 
-MCP routing hints can also prefer a specific MCP tool for matching requests without forbidding other tools. When `tool_search` defers MCP schemas, matching routing metadata can auto-promote up to `tool_search.auto_promote_top_k` deferred schemas before the model call.
-
-Deferred MCP schema promotions last for the current user turn. They remain active across that turn's model/tool loop and checkpoint resume, then become deferred again when a new user message starts the next turn; the next turn must discover them again through `tool_search` or match their routing hints. Resuming a legacy in-flight checkpoint preserves previously searched tools even when routing hints also match that turn.
+MCP routing metadata describes tool capabilities as advisory context. Matching a keyword in user text does not reveal a deferred schema or establish that the user requested a tool. The agent selects appropriate tools via `tool_search`; the legacy `auto_promote_top_k` configuration is accepted but does not trigger automatic promotion.
+
+Deferred MCP schema selections last for the current user turn. They remain active across that turn's model/tool loop and checkpoint resume, then become deferred again when a new user message starts the next turn. Legacy in-flight checkpoints retain previously searched tools in their original scope.
 
 Deferred `tool_search` regex queries share a 100 ms execution budget across the catalog, including `+required` ranking. Patterns are limited to 256 characters and searchable names/descriptions to 65,536 characters each. Queries that exceed a limit return a retry hint without promoting partial results; use a simpler pattern, `keywords:`, or `select:` with exact names. Oversized catalog fields are reported with the tool name, field and length, and logged with the MCP server name when available; use `keywords:` or `select:` because simplifying the pattern cannot shrink a catalog field. Exact selection remains uncapped and bypasses regex limits; the literal `keywords:` mode also bypasses regex limits. Invalid regex syntax still falls back to a literal substring match.
 
@@ -1467,6 +1469,7 @@

 - Slack stop waits up to five seconds for an in-flight Socket Mode connection and its cleanup. If cleanup is still pending, the previous instance stays tracked and a restart can be retried after it finishes. SDK cleanup failures report their original error and remain retryable.
 - In Telegram private chats, text, attachment and streaming replies (including "Working on it...") can still be delivered if their referenced user or bot message was deleted, such as after clearing chat history during a run. Group reply-target requirements remain unchanged to preserve forum routing.
 - In Telegram groups, replying to a delivered bot response or attachment continues its DeerFlow conversation. Reply mappings survive restarts and stay scoped to the user's connection when one is bound. New, unrelated group messages still start separate conversations; private-chat routing is unchanged.
+- New Telegram final-reply sends use the bot API's rate-limit wait up to 60 seconds per retry. Missing, invalid, or shorter hints use the usual backoff. The "Working on it..." acknowledgment is best effort.
 - Feishu/Lark now queues rapid follow-up messages per mapped DeerFlow `thread_id` instead of immediately surfacing the generic busy reply, and topic replies keep a per-message card with a compact source-message preview across queued/running/final patches.
 - Streaming IM channels treat backend `error` events like transport failures and follow the same reply and retry path. The channel logs the error type and message for diagnosis.
 
@@ -1631,8 +1634,7 @@

 result-quality guard phase changes. It records loop-detection decisions and
 deferred MCP tool promotions for both the lead agent and ordinary task
 subagents. Promotion
-events identify newly promoted deferred-tool names and whether routing metadata or
-`tool_search` selected them, without copying the search query, routing keywords,
+events identify deferred-tool names selected by `tool_search`, without copying the search query, routing keywords,
 schemas, arguments, results, or catalog hash into the promotion event itself.
 
 #### LangSmith Tracing
@@ -2717,8 +2719,9 @@

 
 With `task_continuity.enabled`, `history_search` searches the current task's active
 and compacted history. Its optional `role` accepts `user`, `assistant`, or `tool`
-and filters before the eight-result limit; omitting it or passing `null` preserves
-search across all roles.
+and filters before limiting results to eight distinct sources. Omitting `role` or
+passing `null` preserves search across all roles. Repeated archives of one source
+share one result slot.
 Search excerpts contain at most 600 characters around the earliest locatable
 matching occurrence that fits and include `excerpt_start` / `excerpt_end`, a
 zero-based, half-open character range
@@ -2745,6 +2748,8 @@

 limit stops a run, unfinished todos are retained for a later user run; todo
... [DIFF_PREVIEW_TRUNCATED]
```

</details>
