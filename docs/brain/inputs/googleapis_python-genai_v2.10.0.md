# 🎯 监控目标 (Target)
Google Edge AI 与 GenAI 生态核心组件 python-genai 最新版本动态

# 🚀 新版本发布 (New Release)
在 2.10.0 版本中引入了多项重要功能特性
首先为 async generate_content_stream 增加了 Agent Platform MCP 的支持
同时在交互和模型层面均新增了 ComputerUse disabled_safety_policies 选项
此外还为执行步骤增加了 usage 字段
最后加入了视频生成及响应格式的参数设置
文档方面也修复了整个代码库中存在的各类拼写错误

# 💡 架构洞察 (Architectural Insight)
本次更新大幅增强了异步流式处理与 MCP 协议的深度融合，为 Agent 平台的扩展提供了底层基础保障
ComputerUse 禁用安全策略选项的加入为高级开发者赋予了更多自由度与控制权，但也需关注潜在的合规与安全边界
详细的使用量字段统计及多模态参数支持进一步完善了开发者的调试链路与视听觉生成能力，整体演进节奏紧凑且富有建设性
