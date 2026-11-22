# MoonshotAI/kimi-code · README.md

> 当前有效快照. 中文说明只使用英文句号. 外部原文保持来源原貌.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) |
| 来源文件 | [README.md](https://github.com/MoonshotAI/kimi-code/blob/83e4dde93453dd22e89da03d2c96d84999e7d0c2/README.md) |
| 来源版本 | `83e4dde93453dd22e89da03d2c96d84999e7d0c2` |
| 来源目录 Tree | `367f801e6c79fefd04209bbbbdeaa715ccd498e8` |
| 来源内容 Blob | `e3e17adb8c3aeb8a566e7c0024d90a06b384baa5` |
| 摄取时间 | `2026-11-22T01:55:57.567841+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_moonshotai_kimi_code_readme_md` |

## 本次变化

- 新增行数 `126`.
- 删除行数 `0`.
- 内容哈希变化时才生成新快照.

## 阅读导航

- Kimi Code CLI
- What is Kimi Code CLI
- Install
- Quick Start
- Key Features
- Use it in your editor (ACP)
- Docs
- Develop
- Community
- Acknowledgements
- License

<details>
<summary>展开完整外部原文</summary>

# Kimi Code CLI

[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE) [![Docs](https://img.shields.io/badge/docs-online-blue)](https://moonshotai.github.io/kimi-code/en/) <br>
[Documentation](https://moonshotai.github.io/kimi-code/en/) · [Issues](https://github.com/MoonshotAI/kimi-code/issues) · [中文](README.zh-CN.md)

![Demo of using Kimi Code](./docs/media/intro.gif)

## What is Kimi Code CLI

Kimi Code CLI is an AI coding agent that runs in your terminal — it can read and edit code, run shell commands, search files, fetch web pages, and choose the next step based on the feedback it receives. It works out of the box with Moonshot AI’s Kimi models and can also be configured to use other compatible providers.

## Install

Install with the official script. No Node.js required.

- **macOS or Linux**:

```sh
curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash
```

- **Windows (PowerShell)**:

```powershell
irm https://code.kimi.com/kimi-code/install.ps1 | iex
```

> On Windows, install [Git for Windows](https://gitforwindows.org/) before first launch because Kimi Code CLI uses the bundled Git Bash as its shell environment. If Git Bash is installed in a custom location, set `KIMI_SHELL_PATH` to the absolute path of `bash.exe`.

Then, run it with a new shell session:

```sh
kimi --version
```

For npm install, upgrade, uninstall, see [Getting Started](https://moonshotai.github.io/kimi-code/en/guides/getting-started).

## Quick Start

Open a project and start the interactive UI:

```sh
cd your-project
kimi
```

On first launch, run `/login` inside Kimi Code CLI and choose either Kimi Code OAuth or a Moonshot AI Open Platform API key. After login, try your first task:

```
Take a look at this project and explain its main directories.
```

## Key Features

- **Single-binary distribution.** Install with one command: no Node.js setup, PATH gymnastics, or global module conflicts.
- **Blazing-fast startup.** The TUI is ready in milliseconds, so starting a session never feels heavy.
- **Purpose-built TUI.** A carefully tuned interface, optimized end to end for long, focused agent sessions.
- **Video input.** Drop a screen recording or demo clip into the chat and let the agent watch what is hard to describe in words — turn a reference clip into a LUT, a long video into a short, a screen recording into working code, and more.
- **AI-native MCP configuration.** Add, edit, and authenticate Model Context Protocol servers conversationally with `/mcp-config`, without hand-editing JSON.
- **Rich plugin ecosystem.** Install skills, MCP servers, and data sources from the marketplace or any GitHub repo, with each install's trust level surfaced up front.
- **Subagents for focused, parallel work.** Dispatch built-in `coder`, `explore`, and `plan` subagents in isolated contexts while keeping the main conversation clean.
- **Lifecycle hooks.** Run local commands at key points to gate risky tool calls, audit decisions, trigger desktop notifications, or connect to your own automation.
- **Editor & IDE integration (ACP).** Drive a Kimi Code CLI session straight from Zed, JetBrains, or any [Agent Client Protocol](https://agentclientprotocol.com/) client with `kimi acp`.

## Use it in your editor (ACP)

Kimi Code CLI speaks the [Agent Client Protocol](https://agentclientprotocol.com/), so ACP-compatible editors and IDEs (Zed, JetBrains, …) can drive a session over stdio. Log in once, then point your editor at the `kimi acp` subcommand — no extra login needed.

For Zed, add this to `~/.config/zed/settings.json`:

```json
{
  "agent_servers": {
    "Kimi Code CLI": {
      "type": "custom",
      "command": "kimi",
      "args": ["acp"],
      "env": {}
    }
  }
}
```

Then open a new conversation in Zed's Agent panel. See [Using in IDEs](https://moonshotai.github.io/kimi-code/en/guides/ides) for JetBrains setup and troubleshooting, and the [`kimi acp` reference](https://moonshotai.github.io/kimi-code/en/reference/kimi-acp) for the full capability matrix.

## Docs

- [Getting Started](https://moonshotai.github.io/kimi-code/en/guides/getting-started)
- [Interaction and approvals](https://moonshotai.github.io/kimi-code/en/guides/interaction)
- [Sessions](https://moonshotai.github.io/kimi-code/en/guides/sessions)
- [Using in IDEs (ACP)](https://moonshotai.github.io/kimi-code/en/guides/ides)
- [Configuration](https://moonshotai.github.io/kimi-code/en/configuration/config-files)
- [Command reference](https://moonshotai.github.io/kimi-code/en/reference/kimi-command)

## Develop

Requirements: Node.js ≥ 24.15.0, pnpm 10.33.0.

```sh
git clone https://github.com/MoonshotAI/kimi-code.git
cd kimi-code
pnpm install
```

```sh
pnpm dev:cli    # run the CLI in dev mode
pnpm test       # run tests
pnpm typecheck  # TypeScript check
pnpm lint       # oxlint
pnpm build      # build all packages
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full contribution guide.

## Community

- [Issues](https://github.com/MoonshotAI/kimi-code/issues)
- For security vulnerabilities, see [SECURITY.md](SECURITY.md).

## Acknowledgements

Our TUI is built on top of [`pi-tui`](https://github.com/earendil-works/pi-mono/tree/main/packages/tui). We thank the authors of `pi-tui` for their valuable work.

## License

Released under the [MIT License](LICENSE).

</details>

<details>
<summary>展开完整版本差异</summary>

```diff
--- previous

+++ e3e17adb8c3aeb8a566e7c0024d90a06b384baa5

@@ -0,0 +1,126 @@

+# Kimi Code CLI
+
+[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE) [![Docs](https://img.shields.io/badge/docs-online-blue)](https://moonshotai.github.io/kimi-code/en/) <br>
+[Documentation](https://moonshotai.github.io/kimi-code/en/) · [Issues](https://github.com/MoonshotAI/kimi-code/issues) · [中文](README.zh-CN.md)
+
+![Demo of using Kimi Code](./docs/media/intro.gif)
+
+## What is Kimi Code CLI
+
+Kimi Code CLI is an AI coding agent that runs in your terminal — it can read and edit code, run shell commands, search files, fetch web pages, and choose the next step based on the feedback it receives. It works out of the box with Moonshot AI’s Kimi models and can also be configured to use other compatible providers.
+
+## Install
+
+Install with the official script. No Node.js required.
+
+- **macOS or Linux**:
+
+```sh
+curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash
+```
+
+- **Windows (PowerShell)**:
+
+```powershell
+irm https://code.kimi.com/kimi-code/install.ps1 | iex
+```
+
+> On Windows, install [Git for Windows](https://gitforwindows.org/) before first launch because Kimi Code CLI uses the bundled Git Bash as its shell environment. If Git Bash is installed in a custom location, set `KIMI_SHELL_PATH` to the absolute path of `bash.exe`.
+
+Then, run it with a new shell session:
+
+```sh
+kimi --version
+```
+
+For npm install, upgrade, uninstall, see [Getting Started](https://moonshotai.github.io/kimi-code/en/guides/getting-started).
+
+## Quick Start
+
+Open a project and start the interactive UI:
+
+```sh
+cd your-project
+kimi
+```
+
+On first launch, run `/login` inside Kimi Code CLI and choose either Kimi Code OAuth or a Moonshot AI Open Platform API key. After login, try your first task:
+
+```
+Take a look at this project and explain its main directories.
+```
+
+## Key Features
+
+- **Single-binary distribution.** Install with one command: no Node.js setup, PATH gymnastics, or global module conflicts.
+- **Blazing-fast startup.** The TUI is ready in milliseconds, so starting a session never feels heavy.
+- **Purpose-built TUI.** A carefully tuned interface, optimized end to end for long, focused agent sessions.
+- **Video input.** Drop a screen recording or demo clip into the chat and let the agent watch what is hard to describe in words — turn a reference clip into a LUT, a long video into a short, a screen recording into working code, and more.
+- **AI-native MCP configuration.** Add, edit, and authenticate Model Context Protocol servers conversationally with `/mcp-config`, without hand-editing JSON.
+- **Rich plugin ecosystem.** Install skills, MCP servers, and data sources from the marketplace or any GitHub repo, with each install's trust level surfaced up front.
+- **Subagents for focused, parallel work.** Dispatch built-in `coder`, `explore`, and `plan` subagents in isolated contexts while keeping the main conversation clean.
+- **Lifecycle hooks.** Run local commands at key points to gate risky tool calls, audit decisions, trigger desktop notifications, or connect to your own automation.
+- **Editor & IDE integration (ACP).** Drive a Kimi Code CLI session straight from Zed, JetBrains, or any [Agent Client Protocol](https://agentclientprotocol.com/) client with `kimi acp`.
+
+## Use it in your editor (ACP)
+
+Kimi Code CLI speaks the [Agent Client Protocol](https://agentclientprotocol.com/), so ACP-compatible editors and IDEs (Zed, JetBrains, …) can drive a session over stdio. Log in once, then point your editor at the `kimi acp` subcommand — no extra login needed.
+
+For Zed, add this to `~/.config/zed/settings.json`:
+
+```json
+{
+  "agent_servers": {
+    "Kimi Code CLI": {
+      "type": "custom",
+      "command": "kimi",
+      "args": ["acp"],
+      "env": {}
+    }
+  }
+}
+```
+
+Then open a new conversation in Zed's Agent panel. See [Using in IDEs](https://moonshotai.github.io/kimi-code/en/guides/ides) for JetBrains setup and troubleshooting, and the [`kimi acp` reference](https://moonshotai.github.io/kimi-code/en/reference/kimi-acp) for the full capability matrix.
+
+## Docs
+
+- [Getting Started](https://moonshotai.github.io/kimi-code/en/guides/getting-started)
+- [Interaction and approvals](https://moonshotai.github.io/kimi-code/en/guides/interaction)
+- [Sessions](https://moonshotai.github.io/kimi-code/en/guides/sessions)
+- [Using in IDEs (ACP)](https://moonshotai.github.io/kimi-code/en/guides/ides)
+- [Configuration](https://moonshotai.github.io/kimi-code/en/configuration/config-files)
+- [Command reference](https://moonshotai.github.io/kimi-code/en/reference/kimi-command)
+
+## Develop
+
+Requirements: Node.js ≥ 24.15.0, pnpm 10.33.0.
+
+```sh
+git clone https://github.com/MoonshotAI/kimi-code.git
+cd kimi-code
+pnpm install
+```
+
+```sh
+pnpm dev:cli    # run the CLI in dev mode
+pnpm test       # run tests
+pnpm typecheck  # TypeScript check
+pnpm lint       # oxlint
+pnpm build      # build all packages
+```
+
+See [CONTRIBUTING.md](CONTRIBUTING.md) for the full contribution guide.
+
+## Community
+
+- [Issues](https://github.com/MoonshotAI/kimi-code/issues)
+- For security vulnerabilities, see [SECURITY.md](SECURITY.md).
+
+## Acknowledgements
+
+Our TUI is built on top of [`pi-tui`](https://github.com/earendil-works/pi-mono/tree/main/packages/tui). We thank the authors of `pi-tui` for their valuable work.
+
+## License
+
+Released under the [MIT License](LICENSE).
```

</details>
