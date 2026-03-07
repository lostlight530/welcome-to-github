# 🛡️ NEXUS CORTEX: Scholar Synthesis Report
> **Date**: 2026-03-07
> **Context**: Deep Dive Intelligence / 深度情报解密

## ⚔️ 竞品雷达：Dify v1.13.0 (高危 / 架构重构)
- **标签**：⚠️ Breaking-Change 🔗 Agent-Protocol
- **深度事实 (The Truth)**：
  - **核心断裂点**：Dify 彻底重构了执行引擎。以前的工作流是在 API 进程里跑，现在全部移到了 Celery Workers。
  - **后果**：如果你是 Docker 部署且有自定义配置，必须手动修改 `docker-compose.yaml`，增加监听 `workflow_based_app_execution` 队列。否则，升级后所有工作流会显示“运行中”但永远卡住（Stuck）。
  - **协议进化**：新增了 HITL (Human-in-the-Loop) 节点。这直接响应了你在 Nexent 社区提出的“人机回环”理念，Dify 已经原生支持了。
  - **行动建议**：不要盲目升级。先备份 `docker-compose.yaml`，确保 Worker 容器配置了正确的 Queue。

## 📦 边缘战备：vLLM v0.17.0 (核弹级更新)
- **标签**：⚠️ Breaking-Change 🏷️ Edge-Ready
- **深度事实 (The Truth)**：
  - **依赖地狱**：强制升级到 PyTorch 2.10.0。这意味着你的 CUDA 环境必须 >= 12.1（推荐 12.4+）。如果你的宿主机还是旧驱动，vLLM 会直接崩溃。
  - **已知故障**：在 CUDA 12.9+ 环境下会出现 `CUBLAS_STATUS_INVALID_VALUE` 错误。
  - **性能飞跃**：正式支持 FlashAttention 4。这是下一代注意力算法，推理速度有显著提升。
  - **行动建议**：
    - 暂时锁定 vLLM 版本，直到你的部署环境完成 PyTorch 2.10 的兼容性测试。
    - 如果必须升级，使用 `uv pip install vllm --torch-backend=auto` 来自动解决依赖冲突。

## 🧠 架构情报：Astron Agent v1.0.2 (安全与协议)
- **标签**：⚠️ Breaking-Change
- **深度事实 (The Truth)**：
  - **安全降级/便利提升**：移除了导入/导出接口的 Auth Check (鉴权检查)。这对于本地开发是好事（方便调试），但对于生产环境是重大安全隐患。如果不加网关拦截，任何人都能导出你的 Agent 配置。
  - **MCP 落地**：虽然 Release Note 写得含蓄，但代码提交记录显示它增加了 MCP Node。这意味着讯飞星火的这个 Agent 框架也开始兼容 Model Context Protocol 了。你的“协议统一”愿景正在成真。

## 📦 边缘战备：MediaPipe v0.10.32 (底层迁移)
- **标签**：🏷️ Edge-Ready ⚠️ Breaking-Change
- **深度事实 (The Truth)**：
  - **API3 大迁徙**：Google 正在强推 API3 架构。旧的 `GlShaderCalculator` 等计算单元已被迁移。如果你有自定义的 C++ Calculators，代码大概率会编译失败。
  - **低端设备复活**：新增了对 ARMv7 (32-bit) 的支持。这意味着你可以把 Agent 部署到非常老旧的树莓派或廉价 Android 手机上。这是真正的“普惠边缘计算”。

## ℹ️ 模型动态：EuroBERT & Transformers v5.3.0
- **标签**：🏷️ Edge-Ready
- **深度事实 (The Truth)**：
  - **EuroBERT**：这就不是一个普通的 BERT。它引入了类似 Llama 的双向注意力机制。
  - **边缘价值**：结合“EdgeBERT”类研究，这种架构可以通过熵值早退 (Entropy-based Early Exit) 机制，在边缘设备上实现 2.5x - 7x 的能效提升。它是为“端侧高精度推理”准备的。

## 🚀 架构师决断 (Architect's Decision)
> 基于以上全线搜索的完整事实，已修正 Deep Work 的优先级：

- **最高优先级 (CRITICAL)**：vLLM 锁版本。
  - **指令**：在 `requirements.txt` 中将 `vllm` 暂时锁定在 `v0.16.x`，避免 PyTorch 2.10 带来的环境雪崩。
- **次高优先级 (HIGH)**：Dify 配置文件审计。
  - **指令**：检查本地或服务器上的 Dify `docker-compose.yaml`，确认 Celery Worker 的队列配置。
- **战略机遇 (OPPORTUNITY)**：测试 Astron 的 MCP 节点。
  - **指令**：既然 Astron 支持了 MCP，尝试用你的 `nexus_mcp.py` 去连接它。这是验证“双刀流”架构的最佳时机。
