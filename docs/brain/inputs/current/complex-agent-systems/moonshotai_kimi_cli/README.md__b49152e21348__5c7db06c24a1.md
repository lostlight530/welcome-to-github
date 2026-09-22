# MoonshotAI/kimi-cli · README.md

> 当前有效快照. 中文说明只使用英文句号. 外部原文保持来源原貌.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) |
| 来源文件 | [README.md](https://github.com/MoonshotAI/kimi-cli/blob/5c7db06c24a175b17a3fb44fa58872235c1888e8/README.md) |
| 来源版本 | `5c7db06c24a175b17a3fb44fa58872235c1888e8` |
| 来源目录 Tree | `692a3b1b447ac0706589b1bceadb095ae022509a` |
| 来源内容 Blob | `b49152e2134835fe50ec8eeed0aed0ae182f2e8f` |
| 摄取时间 | `2026-09-22T00:37:43.336975+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `doc_moonshotai_kimi_cli_readme_md_44bbde6d2563` |

## 本次变化

- 新增行数 `57`.
- 删除行数 `12`.
- 内容哈希变化时才生成新快照.

## 阅读导航

- Kimi CLI (Archived)
- Migrate to Kimi Code CLI
- Packages in this repository
- License
- Getting Started
- Key Features
- Shell command mode
- VS Code extension
- IDE integration via ACP
- Zsh integration
- MCP support
- Add streamable HTTP server:
- Add streamable HTTP server with OAuth authorization:
- Add stdio server:
- List added MCP servers:
- Remove an MCP server:
- Authorize an MCP server:
- More
- Development

<details>
<summary>展开完整外部原文</summary>

# Kimi CLI (Archived)

[Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) | [Migration Guide](https://moonshotai.github.io/kimi-code/en/guides/migration) | [迁移指南](https://moonshotai.github.io/kimi-code/zh/guides/migration) | [Legacy Docs](https://moonshotai.github.io/kimi-cli/en/)

> [!CAUTION]
> **This project has been archived and is no longer maintained.** Kimi CLI (Python) has been replaced by **[Kimi Code CLI](https://github.com/MoonshotAI/kimi-code)**, the next-generation terminal AI agent from the same team.
>
> - This repository is read-only. There will be no further releases, bug fixes, or security updates.
> - Existing installations are no longer supported and will stop working. Please migrate as soon as possible.
> - Please file issues, feature requests, and security reports for Kimi Code CLI at [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code).
>
> 本项目已归档，不再维护。Python 版 Kimi CLI 已由 [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) 取代，旧版将无法继续使用，请参考 [迁移指南](https://moonshotai.github.io/kimi-code/zh/guides/migration) 尽快升级。

## Migrate to Kimi Code CLI

1. Install Kimi Code CLI:

   ```sh
   # macOS / Linux
   curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash
   ```

   ```powershell
   # Windows (PowerShell)
   irm https://code.kimi.com/kimi-code/install.ps1 | iex
   ```

   Also available via Homebrew (`brew install kimi-code`) and npm (`npm install -g @moonshot-ai/kimi-code`).

2. Open a new terminal and run `kimi`. On first launch, it detects your Kimi CLI data in `~/.kimi/` and offers to migrate your config, MCP servers, input history, and sessions. You can also run `kimi migrate` at any time. Your original data in `~/.kimi/` is never modified or deleted.
3. Run `/login` again, and re-authorize your MCP servers. Login credentials, MCP authorizations, and Kimi CLI plugins are not migrated.
4. Uninstall the legacy CLI after migrating, e.g. `uv tool uninstall kimi-cli` or `brew uninstall kimi-cli`.

See the full [migration guide](https://moonshotai.github.io/kimi-code/en/guides/migration) for details.

## Packages in this repository

All packages below are archived together with this repository. Published versions remain on PyPI, but will not receive any further updates.

| Package | Status |
|---|---|
| [`kimi-cli`](https://pypi.org/project/kimi-cli/) | Archived. Replaced by Kimi Code CLI |
| [`kimi-code`](https://pypi.org/project/kimi-code/) on PyPI | Archived. A legacy alias of `kimi-cli`, **not** the new Kimi Code CLI |
| [`kosong`](https://pypi.org/project/kosong/) | Archived |
| [`pykaos`](https://pypi.org/project/pykaos/) | Archived |
| [`kimi-sdk`](https://pypi.org/project/kimi-sdk/) | Archived |

## License

The source code remains available under the [Apache License 2.0](LICENSE).

Thank you to everyone who used Kimi CLI, reported issues, and contributed code. Your feedback shaped Kimi Code CLI.

<details>
<summary>Original README (legacy, for reference only)</summary>

Kimi CLI is an AI agent that runs in the terminal, helping you complete software development tasks and terminal operations. It can read and edit code, execute shell commands, search and fetch web pages, and autonomously plan and adjust actions during execution.

## Getting Started

See [Getting Started](https://moonshotai.github.io/kimi-cli/en/guides/getting-started.html) for how to install and start using Kimi CLI.

## Key Features

### Shell command mode

Kimi CLI is not only a coding agent, but also a shell. You can switch the shell command mode by pressing `Ctrl-X`. In this mode, you can directly run shell commands without leaving Kimi CLI.

![](./docs/media/shell-mode.gif)

> [!NOTE]
> Built-in shell commands like `cd` are not supported yet.

### VS Code extension

Kimi CLI can be integrated with [Visual Studio Code](https://code.visualstudio.com/) via the [Kimi Code VS Code Extension](https://marketplace.visualstudio.com/items?itemName=moonshot-ai.kimi-code).

![VS Code Extension](./docs/media/vscode.png)

### IDE integration via ACP

Kimi CLI supports [Agent Client Protocol] out of the box. You can use it together with any ACP-compatible editor or IDE.

[Agent Client Protocol]: https://github.com/agentclientprotocol/agent-client-protocol

To use Kimi CLI with ACP clients, make sure to run Kimi CLI in the terminal and send `/login` to complete the login first. Then, you can configure your ACP client to start Kimi CLI as an ACP agent server with command `kimi acp`.

For example, to use Kimi CLI with [Zed](https://zed.dev/) or [JetBrains](https://blog.jetbrains.com/ai/2025/12/bring-your-own-ai-agent-to-jetbrains-ides/), add the following configuration to your `~/.config/zed/settings.json` or `~/.jetbrains/acp.json` file:

```json
{
  "agent_servers": {
    "Kimi CLI": {
      "type": "custom",
      "command": "kimi",
      "args": ["acp"],
      "env": {}
    }
  }
}
```

Then you can create Kimi CLI threads in IDE's agent panel.

![](./docs/media/acp-integration.gif)

### Zsh integration

You can use Kimi CLI together with Zsh, to empower your shell experience with AI agent capabilities.

Install the [zsh-kimi-cli](https://github.com/MoonshotAI/zsh-kimi-cli) plugin via:

```sh
git clone https://github.com/MoonshotAI/zsh-kimi-cli.git \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/kimi-cli
```

> [!NOTE]
> If you are using a plugin manager other than Oh My Zsh, you may need to refer to the plugin's README for installation instructions.

Then add `kimi-cli` to your Zsh plugin list in `~/.zshrc`:

```sh
plugins=(... kimi-cli)
```

After restarting Zsh, you can switch to agent mode by pressing `Ctrl-X`.

### MCP support

Kimi CLI supports MCP (Model Context Protocol) tools.

**`kimi mcp` sub-command group**

You can manage MCP servers with `kimi mcp` sub-command group. For example:

```sh
# Add streamable HTTP server:
kimi mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: ctx7sk-your-key"

# Add streamable HTTP server with OAuth authorization:
kimi mcp add --transport http --auth oauth linear https://mcp.linear.app/mcp

# Add stdio server:
kimi mcp add --transport stdio chrome-devtools -- npx chrome-devtools-mcp@latest

# List added MCP servers:
kimi mcp list

# Remove an MCP server:
kimi mcp remove chrome-devtools

# Authorize an MCP server:
kimi mcp auth linear
```

**Ad-hoc MCP configuration**

Kimi CLI also supports ad-hoc MCP server configuration via CLI option.

Given an MCP config file in the well-known MCP config format like the following:

```json
{
  "mcpServers": {
    "context7": {
      "url": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "YOUR_API_KEY"
      }
    },
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

Run `kimi` with `--mcp-config-file` option to connect to the specified MCP servers:

```sh
kimi --mcp-config-file /path/to/mcp.json
```

### More

See more features in the [Documentation](https://moonshotai.github.io/kimi-cli/en/).

## Development

To develop Kimi CLI, run:

```sh
git clone https://github.com/MoonshotAI/kimi-cli.git
cd kimi-cli

make prepare  # prepare the development environment
```

Then you can start working on Kimi CLI.

Refer to the following commands after you make changes:

```sh
uv run kimi  # run Kimi CLI

make format  # format code
make check  # run linting and type checking
make test  # run tests
make test-kimi-cli  # run Kimi CLI tests only
make test-kosong  # run kosong tests only
make test-pykaos  # run pykaos tests only
make build-web  # build the web UI and sync it into the package (requires Node.js/npm)
make build  # build python packages
make build-bin  # build standalone binary
make help  # show all make targets
```

Note: `make build` and `make build-bin` automatically run `make build-web` to embed the web UI.

</details>

</details>

<details>
<summary>展开完整版本差异</summary>

```diff
--- previous

+++ b49152e2134835fe50ec8eeed0aed0ae182f2e8f

@@ -1,15 +1,58 @@

-# Kimi CLI
-
-[![Commit Activity](https://img.shields.io/github/commit-activity/w/MoonshotAI/kimi-cli)](https://github.com/MoonshotAI/kimi-cli/graphs/commit-activity)
-[![Checks](https://img.shields.io/github/check-runs/MoonshotAI/kimi-cli/main)](https://github.com/MoonshotAI/kimi-cli/actions)
-[![Version](https://img.shields.io/pypi/v/kimi-cli)](https://pypi.org/project/kimi-cli/)
-[![Downloads](https://img.shields.io/pypi/dw/kimi-cli)](https://pypistats.org/packages/kimi-cli)
-[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/MoonshotAI/kimi-cli)
-
-[Kimi Code](https://www.kimi.com/code/) | [Documentation](https://moonshotai.github.io/kimi-cli/en/) | [文档](https://moonshotai.github.io/kimi-cli/zh/)
-
-> [!IMPORTANT]
-> **Kimi CLI is evolving into [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code)** — the next-generation terminal AI agent from the same team. Installing Kimi Code CLI automatically migrates your configuration and sessions. This project will be gradually wound down; the docs and existing installations remain available.
+# Kimi CLI (Archived)
+
+[Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) | [Migration Guide](https://moonshotai.github.io/kimi-code/en/guides/migration) | [迁移指南](https://moonshotai.github.io/kimi-code/zh/guides/migration) | [Legacy Docs](https://moonshotai.github.io/kimi-cli/en/)
+
+> [!CAUTION]
+> **This project has been archived and is no longer maintained.** Kimi CLI (Python) has been replaced by **[Kimi Code CLI](https://github.com/MoonshotAI/kimi-code)**, the next-generation terminal AI agent from the same team.
+>
+> - This repository is read-only. There will be no further releases, bug fixes, or security updates.
+> - Existing installations are no longer supported and will stop working. Please migrate as soon as possible.
+> - Please file issues, feature requests, and security reports for Kimi Code CLI at [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code).
+>
+> 本项目已归档，不再维护。Python 版 Kimi CLI 已由 [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) 取代，旧版将无法继续使用，请参考 [迁移指南](https://moonshotai.github.io/kimi-code/zh/guides/migration) 尽快升级。
+
+## Migrate to Kimi Code CLI
+
+1. Install Kimi Code CLI:
+
+   ```sh
+   # macOS / Linux
+   curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash
+   ```
+
+   ```powershell
+   # Windows (PowerShell)
+   irm https://code.kimi.com/kimi-code/install.ps1 | iex
+   ```
+
+   Also available via Homebrew (`brew install kimi-code`) and npm (`npm install -g @moonshot-ai/kimi-code`).
+
+2. Open a new terminal and run `kimi`. On first launch, it detects your Kimi CLI data in `~/.kimi/` and offers to migrate your config, MCP servers, input history, and sessions. You can also run `kimi migrate` at any time. Your original data in `~/.kimi/` is never modified or deleted.
+3. Run `/login` again, and re-authorize your MCP servers. Login credentials, MCP authorizations, and Kimi CLI plugins are not migrated.
+4. Uninstall the legacy CLI after migrating, e.g. `uv tool uninstall kimi-cli` or `brew uninstall kimi-cli`.
+
+See the full [migration guide](https://moonshotai.github.io/kimi-code/en/guides/migration) for details.
+
+## Packages in this repository
+
+All packages below are archived together with this repository. Published versions remain on PyPI, but will not receive any further updates.
+
+| Package | Status |
+|---|---|
+| [`kimi-cli`](https://pypi.org/project/kimi-cli/) | Archived. Replaced by Kimi Code CLI |
+| [`kimi-code`](https://pypi.org/project/kimi-code/) on PyPI | Archived. A legacy alias of `kimi-cli`, **not** the new Kimi Code CLI |
+| [`kosong`](https://pypi.org/project/kosong/) | Archived |
+| [`pykaos`](https://pypi.org/project/pykaos/) | Archived |
+| [`kimi-sdk`](https://pypi.org/project/kimi-sdk/) | Archived |
+
+## License
+
+The source code remains available under the [Apache License 2.0](LICENSE).
+
+Thank you to everyone who used Kimi CLI, reported issues, and contributed code. Your feedback shaped Kimi Code CLI.
+
+<details>
+<summary>Original README (legacy, for reference only)</summary>
 
 Kimi CLI is an AI agent that runs in the terminal, helping you complete software development tasks and terminal operations. It can read and edit code, execute shell commands, search and fetch web pages, and autonomously plan and adjust actions during execution.
 
@@ -175,3 +218,5 @@

 ```
 
 Note: `make build` and `make build-bin` automatically run `make build-web` to embed the web UI.
+
+</details>
```

</details>
