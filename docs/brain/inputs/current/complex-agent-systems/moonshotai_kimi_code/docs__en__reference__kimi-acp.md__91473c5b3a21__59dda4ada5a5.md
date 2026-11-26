# MoonshotAI/kimi-code · docs/en/reference/kimi-acp.md

> 当前有效快照. 中文说明只使用英文句号. 外部原文保持来源原貌.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) |
| 来源文件 | [docs/en/reference/kimi-acp.md](https://github.com/MoonshotAI/kimi-code/blob/59dda4ada5a5f0b621d156e580fa9b9032b611bf/docs/en/reference/kimi-acp.md) |
| 来源版本 | `59dda4ada5a5f0b621d156e580fa9b9032b611bf` |
| 来源目录 Tree | `c892c54fc0974906d994ea291f332c942460a98a` |
| 来源内容 Blob | `91473c5b3a210b79cb38a68a016ea2265a438aac` |
| 摄取时间 | `2026-11-26T03:58:39.869976+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_moonshotai_kimi_code_docs_en_reference_kimi_acp_md` |

## 本次变化

- 新增行数 `8`.
- 删除行数 `2`.
- 内容哈希变化时才生成新快照.

## 阅读导航

- `kimi acp` Subcommand
- Capability matrix
- ACP method coverage
- Core agent-side — IDE → agent (3 / 3)
- Session agent-side — IDE → agent (11 / 11)
- Client-side reverse-RPC — agent → IDE (10 / 11)
- Extension methods
- MCP forwarding
- Next steps

<details>
<summary>展开完整外部原文</summary>

# `kimi acp` Subcommand

`kimi acp` switches Kimi Code CLI to **ACP (Agent Client Protocol)** mode: it communicates with an ACP client (such as Zed, JetBrains AI Chat, etc.) via JSON-RPC over stdin/stdout, letting the IDE directly drive kimi's sessions, prompts, and tool calls.

```sh
kimi acp
```

Once started, the command prints no banner and immediately waits for the ACP client to send an `initialize` request on stdin. Logs are written to stderr (as well as the diagnostic log under `~/.kimi-code/logs/`), so the ACP channel itself stays clean.

When Kimi starts a turn to report a completed background task, `kimi acp` sends the reply and tool calls to the IDE through `session/update`, even after the previous `session/prompt` has ended. A new prompt sent while that turn is running receives `turn.agent_busy` and can be retried when the turn is complete.

::: tip Who calls this?
You typically do not need to run `kimi acp` manually — this command is the subprocess entry point for IDEs. For IDE-side configuration, see [Using in IDEs](../guides/ides.md).
:::

## Capability matrix

The table below lists the capabilities declared by the ACP server. The `agentCapabilities` field is returned in full in the `initialize` response, so the IDE can adjust its UI accordingly.

| Capability | Value | Description |
| --- | --- | --- |
| `loadSession` | `true` | Supports `session/load` to resume an existing session, replaying history on load |
| `promptCapabilities.image` | `true` | Supports ACP `image` content blocks (base64 + mimeType) |
| `promptCapabilities.audio` | `false` | Audio prompts not yet supported |
| `promptCapabilities.embeddedContext` | `true` | Client may send `resource`/`resource_link` embedded resource blocks; text content is injected into the prompt as `<resource uri="...">...</resource>`; blob resources are dropped with a warn |
| `sessionCapabilities.list` | `{}` | Supports `session/list` to enumerate the current user's sessions |
| `sessionCapabilities.resume` | `{}` | Supports `session/resume` to reattach to a session without history replay |
| `sessionCapabilities.close` | `{}` | Supports `session/close` to tear down a live session |
| `sessionCapabilities.delete` | `{}` | Supports `session/delete` to permanently remove a session |
| `sessionCapabilities.fork` | `{}` | Supports `session/fork` to branch an existing session |
| `sessionCapabilities.additionalDirectories` | `{}` | Extra working directories; honored on `session/new` only |
| `mcpCapabilities.http` | `true` | Forwards HTTP MCP services configured by the IDE |
| `mcpCapabilities.sse` | `true` | Forwards legacy SSE MCP services configured by the IDE |
| `auth.logout` | `{}` | Supports ACP `logout` to drop the managed provider's token |

## ACP method coverage

With `@agentclientprotocol/sdk@1.x`, the ACP method set is organized by namespace: `core` and `session` cover the main agent flow, while `providers`, `nes` (inline-edit prediction), and `document` (buffer sync) are optional extension surfaces. On the client side, reverse-RPC methods are grouped under `session`, `fs`, `terminal`, and `elicitation`.

**Summary: the ACP server implements the full core (3/3) and session (11/11) agent-side surface, 10/11 client reverse-RPC methods, and the `session/set_model` extension. Not implemented: `providers/*`, `nes/*`, `document/*`, and `elicitation/complete` — requests for them return `methodNotFound`.**

### Core agent-side — IDE → agent (3 / 3)

| Method | Implemented | Description |
| --- | --- | --- |
| `initialize` | Yes | Version negotiation; returns `agentInfo: { name: 'Kimi Code CLI', version }`, capability matrix, and `authMethods` (first-class `type:'terminal'` plus the legacy `_meta['terminal-auth']` fallback) |
| `authenticate` | Yes | Validates `method_id='login'`; returns `authRequired (-32000)` if the token is missing, `invalidParams (-32602)` for an unknown ID |
| `logout` | Yes | Drops the managed provider's token; subsequent gated calls return `auth_required` again |

### Session agent-side — IDE → agent (11 / 11)

| Method | Implemented | Description |
| --- | --- | --- |
| `session/new` | Yes | Accepts `cwd` / `mcpServers` / `additionalDirectories`; returns `sessionId` + `configOptions[]` + `modes` |
| `session/load` | Yes | Restores a session from disk and replays history via `session/update` before the response settles |
| `session/resume` | Yes | Lightweight sibling of `session/load`; skips history replay |
| `session/list` | Yes | Enumerates sessions on disk, filterable by `cwd` |
| `session/fork` | Yes | Branches a source session; `cwd` / `additionalDirectories` / `mcpServers` on the request are ignored with a warning |
| `session/close` | Yes | Best-effort teardown: cancels any in-flight turn, disposes per-session resources, and closes the live session; an unknown id is not an error |
| `session/delete` | Yes | Permanently removes a session and its persisted data. Subsequent `session/list` calls omit the deleted session. An unknown ID returns `invalidParams (-32602)`. |
| `session/prompt` | Yes | Accepts `text` / `image` / `resource` / `resource_link` content blocks; streams `agent_message_chunk`. A turn that fails after it has started returns a JSON-RPC error: `authRequired (-32000)` for an authentication failure, otherwise `-32603` with the error message as `message` and its error code in `data.code`. A response blocked by the provider's content filter ends with the `refusal` stop reason, and a turn that fails after `session/cancel` still ends with `cancelled` |
| `session/cancel` | Yes | Interrupts the current turn (a JSON-RPC `$/cancel_request` for a prompt lands in the same cancel path) |
| `session/set_mode` | Yes | Validates `modeId`; the same underlying mode switch as `set_config_option({configId:'mode'})` |
| `session/set_config_option` | Yes | Unified model / thinking / mode picker dispatcher |

In the mode picker, Auto (`auto`) can approve sensitive operations automatically and honors explicit deny rules. YOLO (`yolo`) automatically approves routine operations and can still prompt for sensitive actions.

Sessions created or restored with Plan mode active report Plan in both mode pickers. Approving a plan or choosing Reject and Exit updates the pickers to the effective permission mode.

### Client-side reverse-RPC — agent → IDE (10 / 11)

| Method | Implemented | Description |
| --- | --- | --- |
| `session/update` | Yes | Streams `agent_message_chunk` / `tool_call*` / `plan` / `config_option_update` / `available_commands_update` |
| `session/request_permission` | Yes | Shared channel for tool approvals and questions. Bash approvals include the complete command and working directory. Resolved absolute file targets appear in `toolCall.locations` |
| `fs/read_text_file` | Yes | Engine file reads are routed to the client when it advertises `fsCapabilities` |
| `fs/write_text_file` | Yes | Engine file writes are routed to the client |
| `terminal/create` · `output` · `release` · `kill` · `wait_for_exit` | Yes | Shell executions reverse-RPC to the client when it advertises `clientCapabilities.terminal` |
| `elicitation/create` | Yes | Ask-user questions go through the native form when the client advertises `elicitation.form`; RPC failures fall back to `session/request_permission` |
| `elicitation/complete` | No | |

### Extension methods

| Method | Implemented | Description |
| --- | --- | --- |
| `session/set_model` | Yes | Carried over from the ACP 0.23 unstable surface as an extension method; equivalent to `set_config_option({configId:'model'})` |

All methods not listed above return `methodNotFound`.

## MCP forwarding

When an ACP client provides `mcpServers` in `session/new` or `session/load`, the ACP server performs the following conversions:

- `http` → kimi's `transport: 'http'` configuration
- `stdio` → kimi's `transport: 'stdio'` configuration
- `sse` → kimi's `transport: 'sse'` configuration
- `acp` → discarded with a warn log entry

## Next steps

- [Using in IDEs](../guides/ides.md) — Zed / JetBrains configuration steps and troubleshooting
- [`kimi` Command Reference](./kimi-command.md) — Complete subcommand list

</details>

<details>
<summary>展开完整版本差异</summary>

```diff
--- previous

+++ 91473c5b3a210b79cb38a68a016ea2265a438aac

@@ -7,6 +7,8 @@

 ```
 
 Once started, the command prints no banner and immediately waits for the ACP client to send an `initialize` request on stdin. Logs are written to stderr (as well as the diagnostic log under `~/.kimi-code/logs/`), so the ACP channel itself stays clean.
+
+When Kimi starts a turn to report a completed background task, `kimi acp` sends the reply and tool calls to the IDE through `session/update`, even after the previous `session/prompt` has ended. A new prompt sent while that turn is running receives `turn.agent_busy` and can be retried when the turn is complete.
 
 ::: tip Who calls this?
 You typically do not need to run `kimi acp` manually — this command is the subprocess entry point for IDEs. For IDE-side configuration, see [Using in IDEs](../guides/ides.md).
@@ -56,18 +58,22 @@

 | `session/list` | Yes | Enumerates sessions on disk, filterable by `cwd` |
 | `session/fork` | Yes | Branches a source session; `cwd` / `additionalDirectories` / `mcpServers` on the request are ignored with a warning |
 | `session/close` | Yes | Best-effort teardown: cancels any in-flight turn, disposes per-session resources, and closes the live session; an unknown id is not an error |
-| `session/delete` | Yes | Permanently removes a session and its persisted data; an unknown id returns `invalidParams (-32602)` |
+| `session/delete` | Yes | Permanently removes a session and its persisted data. Subsequent `session/list` calls omit the deleted session. An unknown ID returns `invalidParams (-32602)`. |
 | `session/prompt` | Yes | Accepts `text` / `image` / `resource` / `resource_link` content blocks; streams `agent_message_chunk`. A turn that fails after it has started returns a JSON-RPC error: `authRequired (-32000)` for an authentication failure, otherwise `-32603` with the error message as `message` and its error code in `data.code`. A response blocked by the provider's content filter ends with the `refusal` stop reason, and a turn that fails after `session/cancel` still ends with `cancelled` |
 | `session/cancel` | Yes | Interrupts the current turn (a JSON-RPC `$/cancel_request` for a prompt lands in the same cancel path) |
 | `session/set_mode` | Yes | Validates `modeId`; the same underlying mode switch as `set_config_option({configId:'mode'})` |
 | `session/set_config_option` | Yes | Unified model / thinking / mode picker dispatcher |
+
+In the mode picker, Auto (`auto`) can approve sensitive operations automatically and honors explicit deny rules. YOLO (`yolo`) automatically approves routine operations and can still prompt for sensitive actions.
+
+Sessions created or restored with Plan mode active report Plan in both mode pickers. Approving a plan or choosing Reject and Exit updates the pickers to the effective permission mode.
 
 ### Client-side reverse-RPC — agent → IDE (10 / 11)
 
 | Method | Implemented | Description |
 | --- | --- | --- |
 | `session/update` | Yes | Streams `agent_message_chunk` / `tool_call*` / `plan` / `config_option_update` / `available_commands_update` |
-| `session/request_permission` | Yes | Shared channel for tool approval and question prompts |
+| `session/request_permission` | Yes | Shared channel for tool approvals and questions. Bash approvals include the complete command and working directory. Resolved absolute file targets appear in `toolCall.locations` |
 | `fs/read_text_file` | Yes | Engine file reads are routed to the client when it advertises `fsCapabilities` |
 | `fs/write_text_file` | Yes | Engine file writes are routed to the client |
 | `terminal/create` · `output` · `release` · `kill` · `wait_for_exit` | Yes | Shell executions reverse-RPC to the client when it advertises `clientCapabilities.terminal` |
```

</details>
