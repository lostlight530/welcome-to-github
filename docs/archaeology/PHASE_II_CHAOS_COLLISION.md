# 第二纪元：混沌与碰撞 (Phase II: Chaos & Collision)

> **"When the agents rushed in, the boundaries dissolved into chaos."**
> **Epoch Marker**: 2026-02-15

## 1. 历史背景 (Historical Context)
为了打破第一纪元的孤岛状态，系统引入了初步的自动化 Agent 扫描机制。但由于缺乏严格的边界控制，自动化脚本开始无差别地扫描、吞噬甚至重写自身产生的文件。

## 2. 核心挑战：拓扑衔尾蛇 (The Ouroboros Effect)
系统遇到了严重的“拓扑衔尾蛇”现象：底层的代码结构扫描逻辑错误地将自己生成的记忆片段（Memory Files）作为源代码实体进行了解析，导致知识图谱的递归爆炸。这种失控状态被称为“混沌碰撞”。

## 3. 架构防御：切除手术协议 (The Lobotomy Protocol)
为了控制这种失控的智能扩张，我们颁布了**切除手术协议 (Lobotomy Protocol)**：
- **`ignore_paths` 注入**: 强行在系统配置中注入过滤规则，将 `docs/brain/memories` 和 `docs/brain/inputs` 从扫描雷达中物理剥离。
- **GitOps 隔离**: 在 `.gitignore` 中明确排除了临时状态文件，确保二进制数据库与雷达缓存永不进入代码追踪，成功遏制了递归循环，确立了最初的防火墙。
