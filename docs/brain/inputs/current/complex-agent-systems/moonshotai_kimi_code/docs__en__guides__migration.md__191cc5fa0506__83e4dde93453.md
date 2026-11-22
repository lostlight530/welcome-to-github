# MoonshotAI/kimi-code · docs/en/guides/migration.md

> 当前有效快照. 中文说明只使用英文句号. 外部原文保持来源原貌.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) |
| 来源文件 | [docs/en/guides/migration.md](https://github.com/MoonshotAI/kimi-code/blob/83e4dde93453dd22e89da03d2c96d84999e7d0c2/docs/en/guides/migration.md) |
| 来源版本 | `83e4dde93453dd22e89da03d2c96d84999e7d0c2` |
| 来源目录 Tree | `367f801e6c79fefd04209bbbbdeaa715ccd498e8` |
| 来源内容 Blob | `191cc5fa05064af7415b12344b5279fc52b3ed21` |
| 摄取时间 | `2026-11-22T01:55:58.527880+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_moonshotai_kimi_code_docs_en_guides_migration_md` |

## 本次变化

- 新增行数 `40`.
- 删除行数 `0`.
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

**What does not get migrated**: OAuth login credentials and MCP service authorizations are not copied, so you will need to run `/login` again and re-authorize MCP servers after migrating. kimi-cli plugins are also out of scope.

::: tip
Migration **never modifies or deletes** any of the old data under `~/.kimi/`. kimi-cli keeps working as before, and the two do not interfere with each other. Migration can also be run repeatedly — sessions that have already been migrated are not imported again.
:::

After migration, sessions imported from kimi-cli are tagged with `[imported]` in the session picker so you can tell them apart from new ones.

</details>

<details>
<summary>展开完整版本差异</summary>

```diff
--- previous

+++ 191cc5fa05064af7415b12344b5279fc52b3ed21

@@ -0,0 +1,40 @@

+# Migrating from kimi-cli
+
+::: info
+Kimi Code CLI has gone through a major version upgrade — moving from Python/uv to Node.js, bringing a simpler install experience, faster startup, and a redesigned terminal UI. The legacy version will gradually be phased out, so we recommend upgrading as soon as possible.
+:::
+
+If you are migrating from the legacy version, follow the steps below — a single command migrates your config, MCP servers, and session history to the new version.
+
+## What's new
+
+- **No more Python / uv**: Rebuilt on Node.js — no Python environment needed, simpler to install
+- **Native binary, works out of the box**: Faster startup, lighter footprint
+- **Redesigned terminal UI**: Smoother, more responsive experience
+- **Full data migration**: Config, MCP servers, and session history all carry over seamlessly
+
+## How to migrate
+
+There are two ways to migrate.
+
+The **first time you run `kimi`** after installing kimi-code, it automatically checks whether kimi-cli data exists under `~/.kimi/`. If it finds any, a migration prompt appears, and you can choose to migrate now, do it later, or never be asked again.
+
+You can also **run it manually at any time**:
+
+```sh
+kimi migrate
+```
+
+You can choose whether to migrate chat sessions as well. If you don't need the history yet, pick **Config only**; otherwise pick **Config + N sessions** to bring everything across in one go. A summary is printed at the end.
+
+## What happens during migration
+
+**What gets migrated**: configuration (`config.toml`), MCP server configuration, input history, and whichever chat sessions you chose to migrate.
+
+**What does not get migrated**: OAuth login credentials and MCP service authorizations are not copied, so you will need to run `/login` again and re-authorize MCP servers after migrating. kimi-cli plugins are also out of scope.
+
+::: tip
+Migration **never modifies or deletes** any of the old data under `~/.kimi/`. kimi-cli keeps working as before, and the two do not interfere with each other. Migration can also be run repeatedly — sessions that have already been migrated are not imported again.
+:::
+
+After migration, sessions imported from kimi-cli are tagged with `[imported]` in the session picker so you can tell them apart from new ones.
```

</details>
