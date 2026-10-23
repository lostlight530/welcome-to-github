# agentuniverse-ai/agentUniverse · docs/design/mcp_stdio_connection_options.md

> 当前有效快照. 中文说明只使用英文句号. 外部原文保持来源原貌.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [agentuniverse-ai/agentUniverse](https://github.com/agentuniverse-ai/agentUniverse) |
| 来源文件 | [docs/design/mcp_stdio_connection_options.md](https://github.com/agentuniverse-ai/agentUniverse/blob/dafa498a3a171a24035ea4dff786718f2903e3a5/docs/design/mcp_stdio_connection_options.md) |
| 来源版本 | `dafa498a3a171a24035ea4dff786718f2903e3a5` |
| 来源目录 Tree | `916e075d341cfd2953d5f842c657399e79dff8aa` |
| 来源内容 Blob | `1019b526caf710827daab9d10d9d4a1862fdcd7d` |
| 摄取时间 | `2026-10-23T00:25:46.950752+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_agentuniverse_ai_agentuniverse_docs_design_mcp_stdio_connection_options_md` |

## 本次变化

- 新增行数 `42`.
- 删除行数 `0`.
- 内容哈希变化时才生成新快照.

## 阅读导航

- MCP stdio connection options / MCP 本地进程连接选项

<details>
<summary>展开完整外部原文</summary>

# MCP stdio connection options / MCP 本地进程连接选项

`MCPTool` and `MCPToolkit` merge `connection_kwargs` into their transport
arguments for stdio as well as the existing remote transports. Previously,
the stdio branch returned early, so configured session options were silently
ignored both during tool discovery and during execution of a registered tool.

For example, Python callers can set the MCP SDK's session read timeout:

```python
from datetime import timedelta
from agentuniverse.agent.action.tool.mcp_tool import MCPTool

tool = MCPTool(
    name="echo",
    server_name="local_server",
    transport="stdio",
    command="python",
    args=["my_mcp_server.py"],
    connection_kwargs={
        "session_kwargs": {"read_timeout_seconds": timedelta(seconds=30)},
    },
)
```

The same option works on `MCPToolkit` and the tools it registers. Values are
passed to the existing session manager and native MCP SDK; use their expected
types (the session timeout shown here is a `timedelta`, not a numeric YAML
value). With no additional options, stdio uses the existing defaults. Normal
`command`, `args`, and `env` fields still configure the subprocess. As with
remote transports, explicitly supplied connection options override matching
transport arguments.

`MCPTool` 和 `MCPToolkit` 的 stdio 连接现在也会合并 `connection_kwargs`。
原先 stdio 分支提前返回，导致工具发现阶段和已注册工具执行阶段的会话选项被
静默忽略，例如上面的会话读取超时配置无法生效。

工具包及其注册的工具同样支持该配置。参数继续交给现有会话管理器与原生 MCP
SDK 处理，必须使用它们要求的类型；示例中的超时使用 Python `timedelta`，
不是一个可直接替代它的 YAML 数值。不传额外选项时维持原有默认行为。
`command`、`args`、`env` 仍用于配置本地服务进程；与远程传输一致，额外连接
选项中显式提供的同名参数覆盖原参数。

</details>

<details>
<summary>展开完整版本差异</summary>

```diff
--- previous

+++ 1019b526caf710827daab9d10d9d4a1862fdcd7d

@@ -0,0 +1,42 @@

+# MCP stdio connection options / MCP 本地进程连接选项
+
+`MCPTool` and `MCPToolkit` merge `connection_kwargs` into their transport
+arguments for stdio as well as the existing remote transports. Previously,
+the stdio branch returned early, so configured session options were silently
+ignored both during tool discovery and during execution of a registered tool.
+
+For example, Python callers can set the MCP SDK's session read timeout:
+
+```python
+from datetime import timedelta
+from agentuniverse.agent.action.tool.mcp_tool import MCPTool
+
+tool = MCPTool(
+    name="echo",
+    server_name="local_server",
+    transport="stdio",
+    command="python",
+    args=["my_mcp_server.py"],
+    connection_kwargs={
+        "session_kwargs": {"read_timeout_seconds": timedelta(seconds=30)},
+    },
+)
+```
+
+The same option works on `MCPToolkit` and the tools it registers. Values are
+passed to the existing session manager and native MCP SDK; use their expected
+types (the session timeout shown here is a `timedelta`, not a numeric YAML
+value). With no additional options, stdio uses the existing defaults. Normal
+`command`, `args`, and `env` fields still configure the subprocess. As with
+remote transports, explicitly supplied connection options override matching
+transport arguments.
+
+`MCPTool` 和 `MCPToolkit` 的 stdio 连接现在也会合并 `connection_kwargs`。
+原先 stdio 分支提前返回，导致工具发现阶段和已注册工具执行阶段的会话选项被
+静默忽略，例如上面的会话读取超时配置无法生效。
+
+工具包及其注册的工具同样支持该配置。参数继续交给现有会话管理器与原生 MCP
+SDK 处理，必须使用它们要求的类型；示例中的超时使用 Python `timedelta`，
+不是一个可直接替代它的 YAML 数值。不传额外选项时维持原有默认行为。
+`command`、`args`、`env` 仍用于配置本地服务进程；与远程传输一致，额外连接
+选项中显式提供的同名参数覆盖原参数。
```

</details>
