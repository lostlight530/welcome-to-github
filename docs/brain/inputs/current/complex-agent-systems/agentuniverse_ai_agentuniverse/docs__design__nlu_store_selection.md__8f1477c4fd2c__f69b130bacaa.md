# agentuniverse-ai/agentUniverse · docs/design/nlu_store_selection.md

> 当前有效快照. 中文说明只使用英文句号. 外部原文保持来源原貌.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [agentuniverse-ai/agentUniverse](https://github.com/agentuniverse-ai/agentUniverse) |
| 来源文件 | [docs/design/nlu_store_selection.md](https://github.com/agentuniverse-ai/agentUniverse/blob/f69b130bacaa784289ec8dc2a9798d122cd8fe5a/docs/design/nlu_store_selection.md) |
| 来源版本 | `f69b130bacaa784289ec8dc2a9798d122cd8fe5a` |
| 来源目录 Tree | `1370196792a5e8cc43a54dc3b1fa9c791380a576` |
| 来源内容 Blob | `8f1477c4fd2cff1d1f0cc9be9f2659fb29965996` |
| 摄取时间 | `2026-10-25T23:52:59.883799+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_agentuniverse_ai_agentuniverse_docs_design_nlu_store_selection_md` |

## 本次变化

- 新增行数 `12`.
- 删除行数 `0`.
- 内容哈希变化时才生成新快照.

## 阅读导航

- NLU store selection

<details>
<summary>展开完整外部原文</summary>

# NLU store selection

The NLU RAG router treats `store_amount` as the maximum number of distinct
configured stores to query. Comma-separated model output is stripped, empty
tokens and unknown names are removed, and repeated names are deduplicated before
the limit is applied. Names remain case-sensitive and first-seen order is kept.

For configured stores `alpha` and `beta`, a response of
`unknown, alpha, alpha, beta` with `store_amount=2` routes once to each store.
Previously unknown or repeated names consumed slots, omitting relevant stores
or querying one store twice. This does not invent a fallback selection when no
valid name is returned, change the prompt, or change the query object.

</details>

<details>
<summary>展开完整版本差异</summary>

```diff
--- previous

+++ 8f1477c4fd2cff1d1f0cc9be9f2659fb29965996

@@ -0,0 +1,12 @@

+# NLU store selection
+
+The NLU RAG router treats `store_amount` as the maximum number of distinct
+configured stores to query. Comma-separated model output is stripped, empty
+tokens and unknown names are removed, and repeated names are deduplicated before
+the limit is applied. Names remain case-sensitive and first-seen order is kept.
+
+For configured stores `alpha` and `beta`, a response of
+`unknown, alpha, alpha, beta` with `store_amount=2` routes once to each store.
+Previously unknown or repeated names consumed slots, omitting relevant stores
+or querying one store twice. This does not invent a fallback selection when no
+valid name is returned, change the prompt, or change the query object.
```

</details>
