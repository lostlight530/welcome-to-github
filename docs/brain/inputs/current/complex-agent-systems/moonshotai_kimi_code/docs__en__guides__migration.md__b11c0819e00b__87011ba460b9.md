# MoonshotAI/kimi-code · docs/en/guides/migration.md

> 当前有效快照. 中文说明只使用英文句号. 外部原文保持来源原貌.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) |
| 来源文件 | [docs/en/guides/migration.md](https://github.com/MoonshotAI/kimi-code/blob/87011ba460b95b8382c57e7a0a6ee8cf6cbc75ae/docs/en/guides/migration.md) |
| 来源版本 | `87011ba460b95b8382c57e7a0a6ee8cf6cbc75ae` |
| 来源目录 Tree | `740f48fdd0e8871d5266f560c5af24ae05ff197d` |
| 来源内容 Blob | `b11c0819e00b4d65573a4ed15d79d00a834274f9` |
| 摄取时间 | `2026-11-25T04:48:05.170856+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_moonshotai_kimi_code_docs_en_guides_migration_md` |

## 本次变化

- 新增行数 `1`.
- 删除行数 `1`.
- 内容哈希变化时才生成新快照.

## 阅读导航

- Migrating from kimi-cli
- What's new
- How to migrate
- What happens during migration

<details>
<summary>展开完整外部原文</summary>

# Migrating from kimi-cli

::: info
Kimi Code CLI has gone through a major version upgrade — moving from Python/uv to Node.js, bringing a simpler install experience, faster startup, and a redesigned terminal UI. The legacy version will gradually be phased out, so we recommend upgrading as soon as possible.
:::

If you are migrating from the legacy version, follow the steps below — a single command migrates your config, MCP servers, and session history to the new version.

## What's new

- **No more Python / uv**: Rebuilt on Node.js — no Python environment needed, simpler to install
- **Native binary, works out of the box**: Faster startup, lighter footprint
- **Redesigned terminal UI**: Smoother, more responsive experience
- **Full data migration**: Config, MCP servers, and session history all carry over seamlessly

## How to migrate

There are two ways to migrate.

The **first time you run `kimi`** after installing kimi-code, it automatically checks whether kimi-cli data exists under `~/.kimi/`. If it finds any, a migration prompt appears, and you can choose to migrate now, do it later, or never be asked again.

You can also **run it manually at any time**:

```sh
kimi migrate
```

You can choose whether to migrate chat sessions as well. If you don't need the history yet, pick **Config only**; otherwise pick **Config + N sessions** to bring everything across in one go. A summary is printed at the end.

## What happens during migration

**What gets migrated**: configuration (`config.toml`), MCP server configuration, input history, and whichever chat sessions you chose to migrate.

**What does not get migrated**: OAuth login credentials and MCP service authorizations are not copied, so you will need to run `/login` again and re-authorize MCP servers after migrating. Legacy [`[experimental]`](../configuration/config-files.md#experimental) flags in `config.toml` and kimi-cli plugins are also not migrated; configure current experimental features in `~/.kimi-code/config.toml` or with `/experiments` after migrating.

::: tip
Migration **never modifies or deletes** any of the old data under `~/.kimi/`. kimi-cli keeps working as before, and the two do not interfere with each other. Migration can also be run repeatedly — sessions that have already been migrated are not imported again.
:::

After migration, sessions imported from kimi-cli are tagged with `[imported]` in the session picker so you can tell them apart from new ones.

</details>

<details>
<summary>展开完整版本差异</summary>

```diff
--- previous

+++ b11c0819e00b4d65573a4ed15d79d00a834274f9

@@ -31,7 +31,7 @@

 
 **What gets migrated**: configuration (`config.toml`), MCP server configuration, input history, and whichever chat sessions you chose to migrate.
 
-**What does not get migrated**: OAuth login credentials and MCP service authorizations are not copied, so you will need to run `/login` again and re-authorize MCP servers after migrating. kimi-cli plugins are also out of scope.
+**What does not get migrated**: OAuth login credentials and MCP service authorizations are not copied, so you will need to run `/login` again and re-authorize MCP servers after migrating. Legacy [`[experimental]`](../configuration/config-files.md#experimental) flags in `config.toml` and kimi-cli plugins are also not migrated; configure current experimental features in `~/.kimi-code/config.toml` or with `/experiments` after migrating.
 
 ::: tip
 Migration **never modifies or deletes** any of the old data under `~/.kimi/`. kimi-cli keeps working as before, and the two do not interfere with each other. Migration can also be run repeatedly — sessions that have already been migrated are not imported again.
```

</details>
