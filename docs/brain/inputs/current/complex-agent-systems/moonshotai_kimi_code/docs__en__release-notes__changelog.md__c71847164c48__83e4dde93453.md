# MoonshotAI/kimi-code · docs/en/release-notes/changelog.md

> 当前有效引用快照. 完整原文由固定 Git Blob 保存, 当前活动输入不重复内联.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) |
| 来源文件 | [docs/en/release-notes/changelog.md](https://github.com/MoonshotAI/kimi-code/blob/83e4dde93453dd22e89da03d2c96d84999e7d0c2/docs/en/release-notes/changelog.md) |
| 来源版本 | `83e4dde93453dd22e89da03d2c96d84999e7d0c2` |
| 来源目录 Tree | `367f801e6c79fefd04209bbbbdeaa715ccd498e8` |
| 来源内容 Blob | `c71847164c4873ca996b23bf8efdb16bd12c2a49` |
| 摄取时间 | `2026-11-22T01:55:59.330921+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_moonshotai_kimi_code_docs_en_release_notes_changelog_md` |
| 快照模式 | `PINNED_EXTERNAL_REFERENCE` |
| 规范内容 SHA256 | `e5d4557e7ad85c9ee41cb85756cc2d9fa2e47658db9cbed36b60961e043e8260` |
| 原文字节数 | `128367` |
| 原文行数 | `2039` |

## 本次变化

- 新增行数 `2039`.
- 删除行数 `0`.
- 完整 Diff 字节数 `130485`.
- 来源变化不等于本仓执行验证或独立研究次数.

## 阅读导航

- Changelog
- 2.7.2 (2026-11-20)
- Bug Fixes
- 2.7.1 (2026-11-20)
- Bug Fixes
- 2.7.0 (2026-11-19)
- Features
- Bug Fixes
- 2.6.3 (2026-11-17)
- Bug Fixes
- 2.6.2 (2026-11-14)
- Features
- Polish
- Bug Fixes
- 2.6.1 (2026-11-13)
- Bug Fixes
- 2.6.0 (2026-11-12)
- Features
- Polish
- Bug Fixes
- 2.5.3 (2026-11-10)
- Features
- Bug Fixes
- 2.5.2 (2026-11-06)

## 原文完整性与取回

- [按固定源提交读取完整原文](https://github.com/MoonshotAI/kimi-code/blob/83e4dde93453dd22e89da03d2c96d84999e7d0c2/docs/en/release-notes/changelog.md).
- 原文由来源 Blob SHA 与规范内容 SHA256 共同识别.
- 被替换的完整活动快照先原样封存到只追加 Archive.
- Diff 过长时只展示有界预览, 预览不代表完整差异.

<details>
<summary>展开有界版本差异</summary>

```diff
--- previous

+++ c71847164c4873ca996b23bf8efdb16bd12c2a49

@@ -0,0 +1,2039 @@

+---
+outline: 2
+---
+
+# Changelog
+
+This page documents the changes in each Kimi Code CLI release.
+
+## 2.7.2 (2026-11-20)
+
+### Bug Fixes
+
+- Web: Fix the draft thinking effort inherited from the global thinking setting reverting to the model default after sending.
+
+## 2.7.1 (2026-11-20)
+
+### Bug Fixes
+
+- Fix turn-specific fork failures after restoring sessions with in-turn steering.
+- Keep queued prompts pending until background notification turns finish.
+- Web: Fix draft thinking effort selections reverting to the model default after sending.
+- Web: Fix the input composer disappearing when accessed over insecure HTTP.
+
+## 2.7.0 (2026-11-19)
+
+### Features
+
+- Add a Follow-up behavior setting under `/settings`; choose Steer to make Enter steer your message into the running turn instead of queueing it.
+- View running foreground agents and their activity in `/tasks`.
+- Web: Show project and session titles in browser tab titles.
+- Support configuring SSH hosts for Kimi Code projects, with each host using its own Kimi login and optional copied custom model providers.
+- Allow resuming sessions that are open in another client.
+- Support Amazon Bedrock models. See the [Amazon Bedrock configuration guide](https://moonshotai.github.io/kimi-code/en/configuration/providers.html#bedrock).
+- Add experimental next-prompt predictions in the TUI after completed turns. Enable with `KIMI_CODE_EXPERIMENTAL_PROMPT_PREDICTION=1` and press Tab or Right Arrow to accept.
+
+### Bug Fixes
+
+- Fix subagents timing out immediately in `kimi -p` and when `[subagent] timeout_ms = 0` is set.
+- Fix several known issues and make various refinements. See the [changelog on GitHub](https://github.com/MoonshotAI/kimi-code/blob/main/apps/kimi-code/CHANGELOG.md) for more technical entries.
+
+## 2.6.3 (2026-11-17)
+
+### Bug Fixes
+
+- Fix duplicate output and a lingering loading spinner after foreground shell commands.
+- Fix background notifications incorrectly stopping Tower tasks.
+- Fix external Stop hooks not running after each completed turn.
+- Prevent restored background task notifications from starting model requests when sessions are resumed or forked.
+- Fix Windows WebBridge updates failing while the daemon is running.
+- Fix several known issues.
+
+## 2.6.2 (2026-11-14)
+
+### Features
+
+- Support optional `search_url` and `feedback_url` fields on custom registry (`api.json`) providers for `WebSearch` and `/feedback`.
+
+### Polish
+
+- Remove the text-only "No attachment" option from `/feedback` (text-only `/feedback` submissions are no longer available), show the current session's files before confirmation, and include session `request_id` metadata.
+
+### Bug Fixes
+
+- Fix multi-second loading delays when reopening long sessions with many tool calls.
+- Reject failed or unfinished Kimi media uploads instead of caching unusable file references.
+- Fix missing live subagent updates in the Swarm panel during execution.
+- web: Improved interactions and fixed known bugs.
+
+## 2.6.1 (2026-11-13)
+
+### Bug Fixes
+
+- Fix multi-second loading delays when reopening long sessions.
+- Fix long sessions stalling with empty replies instead of compacting when tool results include notes, errors, or timing headers.
+
+## 2.6.0 (2026-11-12)
+
+We recommend switching to fullscreen mode via `/settings -> TUI mode -> Fullscreen` (takes effect after restarting) for a better experience.
+
+### Features
+
+- Fold consecutive tool calls and thinking into summary lines in fullscreen mode and hide Activated skill cards for model-loaded skills; adjust folding in `/settings`, or set `tool_call_density = "ungrouped"` and `thinking = "ungrouped"` under `[transcript]` in `tui.toml` to keep the previous layout.
+- Include hidden and `.gitignore`-ignored paths by default in `@` file path completion, ranking non-ignored files first at equal match quality.
+- Keep same-name workspace skills selectable in a dedicated TUI Skills group, with directory, global, or built-in labels distinguishing their sources.
+- Support copying selected text with `Ctrl-C` or `Cmd-C` in fullscreen mode, and add a Copy on select toggle in `/settings`.
+- Persist user and local-project permission rules (in `config.toml` and trusted `.kimi-code/local.toml`) and apply them when sessions start, with `deny` taking precedence over `ask` and `allow`.
+- Add artifact missions in Tower with key-deliverable review and human acceptance, and show mission kinds in status and mission views.
+
+### Polish
+
+- Copy only to the system clipboard outside SSH and mosh instead of also sending OSC 52 through the terminal; set `KIMI_CODE_CLIPBOARD_OSC52=1` to keep the old behavior.
+- Allow `primary` as an ordinary `[secondary_model]` model alias; Tower reviewers now use the pool default instead of the primary model, so using the primary model requires selecting an explicit pool alias or setting `default_model`.
+- Add the `KIMI_CODE_TUI_ANIMATION_FPS` environment variable (an integer from `1` to `60`) to adjust the frame rate of in-progress title shimmer animations.
+
+### Bug Fixes
+
+- Apply `[[permission.rules]]` from `config.toml` when a session starts, including `deny`, `ask`, and `allow` rules in print mode.
+- Follow the current primary directory for default local workdirs after a primary swap while keeping tools, project configuration, and session indexes in sync; pass an explicit `environmentCwd` to retain pinned-directory behavior.
+- Fix several known issues and make various refinements. See the [changelog on GitHub](https://github.com/MoonshotAI/kimi-code/blob/main/apps/kimi-code/CHANGELOG.md) for more technical entries.
+
+## 2.5.3 (2026-11-10)
+
+### Features
+
+- Improve steer interruption logic.
+
+### Bug Fixes
+
+- web: Improved interactions and fixed known bugs.
+- Fix stdio MCP servers configured with script commands such as `npx` failing to start on Windows.
+
+## 2.5.2 (2026-11-06)
+
+### Bug Fixes
+
+- Fix duplicate tool declaration errors in select_tools when MCP tool definitions change.
+- web: Fix steered messages being incorrectly queued while a session is running.
+- web: Fix project creation when accessing the Web UI over HTTP.
+
+## 2.5.1 (2026-11-05)
+
+### Bug Fixes
+
+- Fix repeated HTTP 400 errors in sessions caused by empty system messages for dynamic tool schemas.
+- Fix missing image and video previews in live and reloaded tool results.
+- Hide sessions belonging to deleted workspaces from session lists.
+- web: Fix session titles not being generated automatically after the first turn of a new session.
+- web: Fix local images not displaying when their paths contain spaces.
+- web: Fix the session info panel automatically floating over and covering chat messages in narrow layouts.
+- web: Hide stale empty implicit workspaces from the workspace list.
+- web: Fix tool call summaries repeatedly expanding and collapsing while a response is in progress.
+
+## 2.5.0 (2026-11-04)
+
+### Features
+
+- Use `/model` and `/effort` while the agent is working; changes apply from the next turn.
+- Merge project-level Skills from the primary and remembered additional directories; the primary wins name conflicts.
+- Create remote sessions in SSH, Docker, or custom-command environments.
+- `[workspace] require_trust = false` treats every workspace as trusted and skips trust prompts after `/reload`; use it only when every workspace is trusted.
+
+### Polish
+
+- Web cross-session full-text search is off by default; set `[database] global_search = true` to enable it.
+- With only `default_model` configured, newly spawned Agent and AgentSwarm subagents use that model; the legacy `force` key is ignored with a warning.
+- Agent and AgentSwarm remove the implicit `primary`; list the main model explicitly in the pool to use it. Without `[secondary_model]`, subagents still inherit the caller's model.
+
+### Bug Fixes
+
... [DIFF_PREVIEW_TRUNCATED]
```

</details>
