# agentuniverse-ai/agentUniverse · docs/design/dashscope_embedding_order.md

> 当前有效快照. 中文说明只使用英文句号. 外部原文保持来源原貌.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [agentuniverse-ai/agentUniverse](https://github.com/agentuniverse-ai/agentUniverse) |
| 来源文件 | [docs/design/dashscope_embedding_order.md](https://github.com/agentuniverse-ai/agentUniverse/blob/dafa498a3a171a24035ea4dff786718f2903e3a5/docs/design/dashscope_embedding_order.md) |
| 来源版本 | `dafa498a3a171a24035ea4dff786718f2903e3a5` |
| 来源目录 Tree | `916e075d341cfd2953d5f842c657399e79dff8aa` |
| 来源内容 Blob | `9637e66d5e10d5c829bf0b937533b138f016280f` |
| 摄取时间 | `2026-10-23T00:25:46.723567+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_agentuniverse_ai_agentuniverse_docs_design_dashscope_embedding_order_md` |

## 本次变化

- 新增行数 `23`.
- 删除行数 `0`.
- 内容哈希变化时才生成新快照.

## 阅读导航

- DashScope embedding input order
- 中文说明

<details>
<summary>展开完整外部原文</summary>

# DashScope embedding input order

`DashscopeEmbedding.get_embeddings()` and `async_get_embeddings()` return
dense vectors in the order of their input texts. For indexed responses, each
batch is ordered by `text_index` before vectors are appended to the result.
This also applies when the input spans several 25-text request batches.

The [official response schema](https://help.aliyun.com/en/model-studio/text-embedding-synchronous-api)
defines `text_index` as the corresponding input's position. For example, rows
with indices `[2, 0, 1]` must produce vectors in `[0, 1, 2]` order. Indices are
local to each request, so sorting the combined result would mix batches.

Responses without index metadata retain their prior arrival order. Batching,
request parameters and API error propagation keep their existing behavior.

## 中文说明

同步和异步接口会依据每批响应中的 `text_index` 排列向量，再按请求批次依次合并，
使有效的索引响应与输入文本一一对应。超过25条文本时，索引会在各批内重新开始，
因此不能在合并结果后全局排序。

例如，响应条目的索引为 `[2, 0, 1]` 时，输出向量应按 `[0, 1, 2]` 排列。
未携带索引元数据的响应仍按原顺序返回；分批、请求参数及接口错误传播保持原有行为。

</details>

<details>
<summary>展开完整版本差异</summary>

```diff
--- previous

+++ 9637e66d5e10d5c829bf0b937533b138f016280f

@@ -0,0 +1,23 @@

+# DashScope embedding input order
+
+`DashscopeEmbedding.get_embeddings()` and `async_get_embeddings()` return
+dense vectors in the order of their input texts. For indexed responses, each
+batch is ordered by `text_index` before vectors are appended to the result.
+This also applies when the input spans several 25-text request batches.
+
+The [official response schema](https://help.aliyun.com/en/model-studio/text-embedding-synchronous-api)
+defines `text_index` as the corresponding input's position. For example, rows
+with indices `[2, 0, 1]` must produce vectors in `[0, 1, 2]` order. Indices are
+local to each request, so sorting the combined result would mix batches.
+
+Responses without index metadata retain their prior arrival order. Batching,
+request parameters and API error propagation keep their existing behavior.
+
+## 中文说明
+
+同步和异步接口会依据每批响应中的 `text_index` 排列向量，再按请求批次依次合并，
+使有效的索引响应与输入文本一一对应。超过25条文本时，索引会在各批内重新开始，
+因此不能在合并结果后全局排序。
+
+例如，响应条目的索引为 `[2, 0, 1]` 时，输出向量应按 `[0, 1, 2]` 排列。
+未携带索引元数据的响应仍按原顺序返回；分批、请求参数及接口错误传播保持原有行为。
```

</details>
