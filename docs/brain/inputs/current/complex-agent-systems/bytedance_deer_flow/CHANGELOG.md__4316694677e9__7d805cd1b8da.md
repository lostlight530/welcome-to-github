# bytedance/deer-flow · CHANGELOG.md

> 当前有效引用快照. 完整原文由固定 Git Blob 保存, 当前活动输入不重复内联.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) |
| 来源文件 | [CHANGELOG.md](https://github.com/bytedance/deer-flow/blob/7d805cd1b8daf317370636388cf8828327065bf9/CHANGELOG.md) |
| 来源版本 | `7d805cd1b8daf317370636388cf8828327065bf9` |
| 来源目录 Tree | `cd8a122c3535f94658127e34a85a9bc76b9e0263` |
| 来源内容 Blob | `4316694677e9a2274d264144e1df16357efe6cd5` |
| 摄取时间 | `2026-11-08T01:08:15.133196+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_bytedance_deer_flow_changelog_md` |
| 快照模式 | `PINNED_EXTERNAL_REFERENCE` |
| 规范内容 SHA256 | `0675cb6720fa1bed43dfcc3e6ef9ba5b2087c7530a7d261c90607bb326b316ed` |
| 原文字节数 | `1029419` |
| 原文行数 | `16119` |

## 本次变化

- 新增行数 `62`.
- 删除行数 `1`.
- 完整 Diff 字节数 `5125`.
- 来源变化不等于本仓执行验证或独立研究次数.

## 阅读导航

- Changelog
- [Unreleased]
- Added
- Fixed
- [2.2.0] — 2026-10-29
- Added
- Scheduler
- Agents & runtime
- Memory
- Knowledge & retrieval
- Skills
- Models & integrations
- Channels
- Auth & guardrails
- Extensions & plugins
- Persistence
- Frontend
- Changed
- Fixed
- Security
- Documentation
- Internal
- [2.1.0] — 2026-09-24
- ⚠ Breaking changes

## 原文完整性与取回

- [按固定源提交读取完整原文](https://github.com/bytedance/deer-flow/blob/7d805cd1b8daf317370636388cf8828327065bf9/CHANGELOG.md).
- 原文由来源 Blob SHA 与规范内容 SHA256 共同识别.
- 被替换的完整活动快照先原样封存到只追加 Archive.
- Diff 过长时只展示有界预览, 预览不代表完整差异.

<details>
<summary>展开有界版本差异</summary>

```diff
--- previous

+++ 4316694677e9a2274d264144e1df16357efe6cd5

@@ -24,6 +24,49 @@

 
 ### Fixed
 
+- **community:** A search or fetch API key that ends in a newline no longer
+  leaks into the conversation. GroundRoute (`GROUNDROUTE_API_KEY`), InfoQuest,
+  Tavily, Exa, Jina, Firecrawl, fastCRW and Crawl4AI put the key into an HTTP
+  header as read, so a key from a file (a Kubernetes Secret created with
+  `--from-file`) made the transport fail with `Illegal header value b'Bearer
+  <key>\n'`. That message, key included, became the tool result the model and
+  the conversation history kept, and four of them also logged it. Keys now go
+  through `provider_credentials.resolve_api_key` like the other providers', and
+  a blank configured key falls back to the environment for Tavily, Exa,
+  Firecrawl and fastCRW. fastCRW without a key of its own no longer lets the
+  Firecrawl SDK send `FIRECRAWL_API_KEY` to the fastCRW endpoint, and a blank
+  `TAVILY_API_KEY`, `EXA_API_KEY` or `FIRECRAWL_API_KEY` now counts as missing
+  instead of reaching the SDK as is. ([#7981])
+  
+- **docker:** Images built from a checkout no longer contain its local
+  configuration. `.dockerignore` did not exclude `config.yaml`,
+  `config.yaml.bak`, `extensions_config.json` or `mcp_config.json`, so a
+  checkout that keeps them in the legacy `backend/` location baked its model
+  API keys and MCP credentials into every gateway image layer through
+  `COPY backend ./backend`. `frontend/.env.local` reached the frontend image the
+  same way. They are now excluded at the root and in `backend/`, along with
+  `.env*.local` at any depth, `frontend/*.pem`, and the credential files the
+  extension manager refuses inside extension snapshots. A locally built
+  frontend image no longer inlines `NEXT_PUBLIC_*` values from
+  `frontend/.env.local`; the Docker stack's single nginx origin needs none of
+  them. Published CI images were not affected; rebuild local images that were
+  pushed or shared. ([#7958])
+  
+- **agents:** Unfinished todos no longer trigger additional model calls or
+  tool execution after a loop-detection, run token-budget, provider-safety, or
+  model output-length stop. Todo state is preserved so users can continue in a
+  later run. ([#7953])
+
+- **channels:** Long Feishu/Lark answers are no longer lost. Card text was
+  unbounded and ASCII-escaped, so an answer of about 4,400 CJK characters made
+  the card request exceed Feishu's 30 KB limit (`230025`); the final patch and
+  its reply fallback were both rejected, and the running card stayed on its
+  last streamed text or a bare `▉`. Cards now send CJK unescaped and are
+  budgeted by the bytes they add to the request. A streamed update shows what
+  fits, and a longer final answer continues in up to 10 cards replied to the
+  same message, split at line breaks; a retry resumes after the cards already
+  delivered. ([#7798])
+  
 - **channels:** WeCom group messages now have their own conversation. Every
   message used the sender's userid as both chat and topic ID, so a member's
   private chat and every group they wrote in shared one DeerFlow thread
@@ -35,7 +78,20 @@

   threads. A group bound with its own `/connect` keeps its thread; a legacy
   group binding, which covers every group of the bot, starts a new one in
   each group. ([#7794])
-  
+
+- **skills:** A custom skill name that is a Windows reserved device name
+  (`nul`, `con`, `com1`, ...) is now rejected when the skill is created —
+  `skill_manage` `create` and `.skill` archive install — on every platform. The
+  hyphen-case grammar admitted such names, and the skill name becomes a
+  directory under `custom/`, so creating one "succeeded" on Windows without
+  producing a directory and the first write inside it failed with
+  `FileNotFoundError`; on Linux the install succeeded but could never be
+  copied, mounted or exported to a Windows host. The archive path also refuses
+  member path segments that cannot be created on every host, matching support
+  file writes. Reading and deleting an existing skill stay permissive, so a
+  skill an older release created on a Linux host can still be inspected and
+  removed. ([#7945])
+
 - **sandbox:** Fresh lazy AIO runs with an explicit authorized skill view no
   longer create or acquire a sandbox before the first sandbox-backed tool
   call. Existing sandbox bindings and providers that require skill uploads
@@ -16053,6 +16109,11 @@

 [#7782]: https://github.com/bytedance/deer-flow/pull/7782
 [#7792]: https://github.com/bytedance/deer-flow/pull/7792
 [#7794]: https://github.com/bytedance/deer-flow/pull/7794
+[#7798]: https://github.com/bytedance/deer-flow/pull/7798
 [#7831]: https://github.com/bytedance/deer-flow/pull/7831
 [#7892]: https://github.com/bytedance/deer-flow/pull/7892
 [#7907]: https://github.com/bytedance/deer-flow/pull/7907
+[#7945]: https://github.com/bytedance/deer-flow/issues/7945
+[#7953]: https://github.com/bytedance/deer-flow/issues/7953
+[#7958]: https://github.com/bytedance/deer-flow/pull/7958
+[#7981]: https://github.com/bytedance/deer-flow/pull/7981
```

</details>
