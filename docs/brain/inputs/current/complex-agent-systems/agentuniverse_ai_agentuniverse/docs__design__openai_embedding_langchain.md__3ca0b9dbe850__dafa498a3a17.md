# agentuniverse-ai/agentUniverse · docs/design/openai_embedding_langchain.md

> 当前有效快照. 中文说明只使用英文句号. 外部原文保持来源原貌.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [agentuniverse-ai/agentUniverse](https://github.com/agentuniverse-ai/agentUniverse) |
| 来源文件 | [docs/design/openai_embedding_langchain.md](https://github.com/agentuniverse-ai/agentUniverse/blob/dafa498a3a171a24035ea4dff786718f2903e3a5/docs/design/openai_embedding_langchain.md) |
| 来源版本 | `dafa498a3a171a24035ea4dff786718f2903e3a5` |
| 来源目录 Tree | `916e075d341cfd2953d5f842c657399e79dff8aa` |
| 来源内容 Blob | `3ca0b9dbe850ff66fd350e904627eaa6228952c1` |
| 摄取时间 | `2026-10-23T00:25:47.205993+00:00` |
| 归属层 | `complex-agent-systems` |
| 可信度 | `1.0` |
| 记忆实体 | `external_doc_agentuniverse_ai_agentuniverse_docs_design_openai_embedding_langchain_md` |

## 本次变化

- 新增行数 `48`.
- 删除行数 `0`.
- 内容哈希变化时才生成新快照.

## 阅读导航

- OpenAI embedding requests through LangChain
- Both use model="text-embedding-3-small" and dimensions=512:
- 通过 LangChain 调用 OpenAI 向量模型

<details>
<summary>展开完整外部原文</summary>

# OpenAI embedding requests through LangChain

`OpenAIEmbedding.as_langchain()` retains the configured `embedding_model_name`
and nonzero `dimensions` when creating the existing LangChain embedding adapter.
These settings apply to synchronous/asynchronous document and query embedding
methods. Reusing the same embedding model and output dimensions matters when
documents and retrieval queries share a vector index.

```python
from agentuniverse.agent.action.knowledge.embedding.openai_embedding import OpenAIEmbedding

embedding = OpenAIEmbedding(
    embedding_model_name="text-embedding-3-small",
    dimensions=512,
)
langchain_embedding = embedding.as_langchain()
# Both use model="text-embedding-3-small" and dimensions=512:
document_vectors = langchain_embedding.embed_documents(["first", "second"])
query_vector = await langchain_embedding.aembed_query("question")
```

In component YAML, the existing `embedding_dims` setting is loaded into
`OpenAIEmbedding.dimensions`; direct Python construction uses `dimensions` as
shown above. Choose a provider/model that supports the requested dimensions.
When the model is unset (`None`), the adapter keeps its existing LangChain
default. Unset or zero dimensions are omitted, matching direct AU embedding
requests. Existing initialized SDK clients continue to be reused; an
uninitialized async client remains supported.

This change concerns request model and dimensions. Client construction,
endpoint settings and LangChain's existing tokenization/normalization behavior
are unchanged.

## 通过 LangChain 调用 OpenAI 向量模型

`OpenAIEmbedding.as_langchain()` 会把配置的 `embedding_model_name` 和非零
`dimensions` 传给既有 LangChain 适配器，同步、异步的文档及查询向量方法均适用。
同一向量索引中的文档和查询应使用一致的模型及输出维度。

上例中的同步文档向量和异步查询向量都会请求 `text-embedding-3-small`，输出维度为
512。组件 YAML 使用既有的 `embedding_dims` 字段，初始化时会映射到
`OpenAIEmbedding.dimensions`；直接创建 Python 对象时使用 `dimensions`。
请选用支持所需维度的服务和模型。

模型未设置（`None`）时仍使用 LangChain 原有默认值；维度未设置或为零时不传递
该参数，与 AU 直接请求保持一致。已有 SDK 客户端继续复用，尚未创建异步客户端时
也能转换。此改动仅处理请求模型和维度，客户端创建、服务地址配置以及 LangChain
已有的分词和向量归一化行为均保持原样。

</details>

<details>
<summary>展开完整版本差异</summary>

```diff
--- previous

+++ 3ca0b9dbe850ff66fd350e904627eaa6228952c1

@@ -0,0 +1,48 @@

+# OpenAI embedding requests through LangChain
+
+`OpenAIEmbedding.as_langchain()` retains the configured `embedding_model_name`
+and nonzero `dimensions` when creating the existing LangChain embedding adapter.
+These settings apply to synchronous/asynchronous document and query embedding
+methods. Reusing the same embedding model and output dimensions matters when
+documents and retrieval queries share a vector index.
+
+```python
+from agentuniverse.agent.action.knowledge.embedding.openai_embedding import OpenAIEmbedding
+
+embedding = OpenAIEmbedding(
+    embedding_model_name="text-embedding-3-small",
+    dimensions=512,
+)
+langchain_embedding = embedding.as_langchain()
+# Both use model="text-embedding-3-small" and dimensions=512:
+document_vectors = langchain_embedding.embed_documents(["first", "second"])
+query_vector = await langchain_embedding.aembed_query("question")
+```
+
+In component YAML, the existing `embedding_dims` setting is loaded into
+`OpenAIEmbedding.dimensions`; direct Python construction uses `dimensions` as
+shown above. Choose a provider/model that supports the requested dimensions.
+When the model is unset (`None`), the adapter keeps its existing LangChain
+default. Unset or zero dimensions are omitted, matching direct AU embedding
+requests. Existing initialized SDK clients continue to be reused; an
+uninitialized async client remains supported.
+
+This change concerns request model and dimensions. Client construction,
+endpoint settings and LangChain's existing tokenization/normalization behavior
+are unchanged.
+
+## 通过 LangChain 调用 OpenAI 向量模型
+
+`OpenAIEmbedding.as_langchain()` 会把配置的 `embedding_model_name` 和非零
+`dimensions` 传给既有 LangChain 适配器，同步、异步的文档及查询向量方法均适用。
+同一向量索引中的文档和查询应使用一致的模型及输出维度。
+
+上例中的同步文档向量和异步查询向量都会请求 `text-embedding-3-small`，输出维度为
+512。组件 YAML 使用既有的 `embedding_dims` 字段，初始化时会映射到
+`OpenAIEmbedding.dimensions`；直接创建 Python 对象时使用 `dimensions`。
+请选用支持所需维度的服务和模型。
+
+模型未设置（`None`）时仍使用 LangChain 原有默认值；维度未设置或为零时不传递
+该参数，与 AU 直接请求保持一致。已有 SDK 客户端继续复用，尚未创建异步客户端时
+也能转换。此改动仅处理请求模型和维度，客户端创建、服务地址配置以及 LangChain
+已有的分词和向量归一化行为均保持原样。
```

</details>
