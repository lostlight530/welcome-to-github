const translations = {
  zh: {
    meta: {
      title: "lostlight | 2025-2026 年度回顾",
      description:
        "端侧 AI × Agent 架构 × 开源生态，聚焦能力复用、系统协议设计与可观测工程实践",
      keywords: [
        "lostlight",
        "Edge AI",
        "Agent",
        "MCP",
        "Skills",
        "Nexent",
        "Astron-agent",
        "MediaPipe",
        "OpenCV",
        "PyTorch"
      ]
    },
    title: "lostlight | 2025-2026 年度回顾",
    nav: {
      home: "首页",
      achievements: "年度成就",
      ecosystem: "生态贡献",
      projects: "核心项目",
      philosophy: "工程哲学"
    },
    hero: {
      role: "端侧 AI × Agent 系统工程者 | Early Career",
      tagline: "低调 务实 <br><span class='gradient-text'>协议优先，系统为先</span>",
      description:
        "专注端侧 AI、Agent 架构与能力复用层设计，长期打磨可落地、可复用、可观测的工程系统，在 Google 与国内 AI 生态之间持续连接实践与抽象",
      primaryCta: "查看生态贡献",
      secondaryCta: "浏览核心项目"
    },
    stats: {
      items: [
        { value: "15", label: "Google 开发者徽章" },
        { value: "5", label: "国家级 / 省级竞赛成果" },
        { value: "4", label: "公开架构讨论贡献" },
        { value: "20+", label: "长期维护中的工程资产" }
      ]
    },
    achievements: {
      title: "2025-2026 关键成就",
      googleBadges: "15 枚 Google 开发者徽章",
      awards: "5 项国家级 / 省级竞赛成果",
      awardList: [
        "第9届华为ICT昇腾AI全国总决赛二等奖+湖北特等奖",
        "华为ICT仓颉语言全国初赛二等奖",
        "金砖国家技能大赛鸿蒙赛道带队晋级国赛+个人优胜",
        "华为昇思MindSpore创新训练营团队二等奖",
        "第16届蓝桥杯智能体开发大学组省三+语言类国赛入围",
        "持续沉淀 20+ 工程资产与公开作品"
      ],
      summary:
        "这一年不只是在做项目，而是在把学习、工具链与生态参与沉淀成长期可复用的系统能力"
    },
    ecosystem: {
      title: "生态贡献与架构输出",
      intro:
        "相比单点项目，我更在意能力抽象、系统分层与生态可复用性，以下内容更能代表我的真实技术方向",
      items: [
        {
          name: "Nexent #2179",
          title: "Skills 作为能力复用层",
          desc: "澄清 Sub-agent 与 Skills 的正交关系，把 Skills 定义为经验与能力的沉淀层，而不是新的 Agent",
          tech: "Agent Abstraction / Reusable Skills",
          link: "https://github.com/ModelEngine-Group/nexent/discussions/2179"
        },
        {
          name: "Nexent #2056",
          title: "Plugin 机制与语义工作流可视化",
          desc: "提出 Plugin = MCP 工具 + Prompt 模板 + 默认小型 workflow，并建议为进阶用户提供工作流查看与轻量编辑能力",
          tech: "MCP / Plugin / Workflow Visualization",
          link: "https://github.com/ModelEngine-Group/nexent/discussions/2056"
        },
        {
          name: "Nexent #1982",
          title: "MCP 一键导入体验优化",
          desc: "提出预部署 MCP 的一键导入与自动同步设想，建议获得维护者公开正面回应并进入后续计划讨论",
          tech: "MCP Distribution / DX",
          link: "https://github.com/ModelEngine-Group/nexent/discussions/1982"
        },
        {
          name: "Astron-agent #824",
          title: "多模型 AgentFlow 简历分析系统",
          desc: "设计多模态输入、多模型协作、状态驱动的 AgentFlow 系统，支持 PDF OCR、多轮补全、评估与岗位推荐闭环",
          tech: "AgentFlow / OCR / Multi-model",
          link: "https://github.com/iflytek/astron-agent/discussions/824"
        }
      ]
    },
    projects: {
      title: "核心项目矩阵",
      intro:
        "项目选择偏向强约束场景与真实系统能力，关注端侧、工业、训练平台与交互式智能系统",
      items: [
        {
          name: "MediaPipe Engine AI",
          desc: "面向端侧算力场景的动作纠错引擎，以状态机解耦复杂动作序列，通过关键点拓扑与规则融合实现实时反馈",
          tech: "Android / Kotlin / MediaPipe / FSM"
        },
        {
          name: "Fire Panel Perception",
          desc: "工业级高精度视觉解算方案，针对透视畸变与复杂光照，结合轮廓、仿射对齐与 RANSAC 重建实现 128 点状态诊断",
          tech: "OpenCV / RANSAC / Python"
        },
        {
          name: "ClassVision Distributed",
          desc: "分布式课堂感知与诊断系统，支持考勤、行为分析与设备检测，强调服务解耦、容器部署与可扩展诊断能力",
          tech: "FastAPI / YOLOv8 / WebSocket / Docker"
        },
        {
          name: "Tiezhitong Agent",
          desc: "语义驱动的铁路查询助手，通过指令解耦与工具挂载实现多源数据收敛查询，体现早期 Agent 工具链整合思路",
          tech: "Python / Semantic Routing / Tool Orchestration"
        },
        {
          name: "CifarLab Trainer",
          desc: "模块化深度学习训练平台，集成混合精度、余弦退火与配置化实验管理，支持从经典模型到快速验证流程的统一训练接口",
          tech: "PyTorch / AMP / YAML"
        },
        {
          name: "Persona Chat Studio",
          desc: "轻量化大模型交互界面，基于 Int4 量化与流式上下文管理，在受限算力下平衡推理速度、显存占用与回复质量",
          tech: "Qwen / Gradio / Int4"
        },
        {
          name: "spec-X",
          desc: "架构哲学 + 自建Skills系统（repo-audit/stack-detect/test-autopilot）",
          tech: "Skills System / Architecture / Automation"
        },
        {
          name: "virtu-tutor-dkt",
          desc: "DKT+强化学习虚拟偶像 Clean Architecture",
          tech: "DKT / RL / Clean Architecture"
        }
      ]
    },
    philosophy: {
      title: "工程哲学",
      points: [
        "小而稳，高于大而乱",
        "协议优先，胜过一次性堆功能",
        "每一个 Skill，都是一次经验闭环与能力封装",
        "在静中追求收敛，在笃中完成演进",
        "拒绝短期热度，坚持构建可复用的精密架构"
      ],
      content:
        "我更相信可测试、可复用、可维护的长期系统价值，而不是短期炫目的功能堆叠"
    },
    footer: {
      greeting: "© 2026 LOSTLIGHT | 记录每一次工程自觉",
      note: "Quietly building reusable systems"
    }
  },

  en: {
    meta: {
      title: "lostlight | 2025-2026 Year in Review",
      description:
        "Edge AI × Agent Architecture × Open-source Influence, focused on reusable capability layers, protocol-oriented system design, and observable engineering",
      keywords: [
        "lostlight",
        "Edge AI",
        "Agent Architecture",
        "MCP",
        "Skills",
        "Nexent",
        "Astron-agent",
        "MediaPipe",
        "OpenCV",
        "PyTorch"
      ]
    },
    title: "lostlight | 2025-2026 Year in Review",
    nav: {
      home: "Home",
      achievements: "Highlights",
      ecosystem: "Ecosystem",
      projects: "Projects",
      philosophy: "Philosophy"
    },
    hero: {
      role: "Edge AI × Agent Systems Engineer | Early Career",
      tagline:
        "Quietly building <br><span class='gradient-text'>protocol-first systems</span>",
      description:
        "Focused on Edge AI, agent architecture, and reusable capability layers Bridging hands-on engineering with ecosystem-level abstractions across Google and domestic AI platforms",
      primaryCta: "View Ecosystem Work",
      secondaryCta: "Explore Projects"
    },
    stats: {
      items: [
        { value: "15", label: "Google Developer Badges" },
        { value: "5", label: "National / Provincial Awards" },
        { value: "4", label: "Public Architecture Contributions" },
        { value: "20+", label: "Long-term Engineering Assets" }
      ]
    },
    achievements: {
      title: "2025-2026 Highlights",
      googleBadges: "15 Google Developer Badges",
      awards: "5 National / Provincial Achievements",
      awardList: [
        "2nd Prize, 9th Huawei ICT Ascend AI National Finals + Hubei Grand Prize",
        "2nd Prize, Huawei ICT Cangjie Language National Preliminaries",
        "Team Leader Finalist & Individual Excellence, BRICS Skills HarmonyOS Track",
        "2nd Prize, Huawei MindSpore Innovation Bootcamp Team",
        "3rd Prize Provincial & National Finalist (Language), 16th Lanqiao Cup AI Agent",
        "20+ evolving engineering assets and public works"
      ],
      summary:
        "This year was not only about building projects, but about turning learning, tooling, and ecosystem participation into reusable system capability"
    },
    ecosystem: {
      title: "Ecosystem Contributions",
      intro:
        "More than standalone projects, this section reflects my core direction — system abstraction, capability packaging, and architecture-level contribution",
      items: [
        {
          name: "Nexent #2179",
          title: "Skills as a reusable capability layer",
          desc: "Clarified the orthogonal relationship between sub-agents and Skills, positioning Skills as an abstraction for reusable, stable execution patterns rather than another agent",
          tech: "Agent Abstraction / Reusable Skills",
          link: "https://github.com/ModelEngine-Group/nexent/discussions/2179"
        },
        {
          name: "Nexent #2056",
          title: "Plugin mechanism and semantic workflow visibility",
          desc: "Proposed Plugin = MCP tools + prompt templates + a default workflow, plus optional workflow visualization and lightweight editing for advanced users",
          tech: "MCP / Plugin / Workflow Visualization",
          link: "https://github.com/ModelEngine-Group/nexent/discussions/2056"
        },
        {
          name: "Nexent #1982",
          title: "One-click MCP import proposal",
          desc: "Suggested a one-click import flow for pre-deployed MCP services The idea received a positive maintainer response and was connected to follow-up feature planning",
          tech: "MCP Distribution / DX",
          link: "https://github.com/ModelEngine-Group/nexent/discussions/1982"
        },
        {
          name: "Astron-agent #824",
          title: "Multi-model AgentFlow resume system",
          desc: "Designed a state-driven AgentFlow system combining OCR, multi-model collaboration, multi-round completion, evaluation, and job recommendation",
          tech: "AgentFlow / OCR / Multi-model",
          link: "https://github.com/iflytek/astron-agent/discussions/824"
        }
      ]
    },
    projects: {
      title: "Project Matrix",
      intro:
        "My projects tend to focus on constrained real-world scenarios — edge deployment, industrial vision, modular training systems, and interactive AI interfaces",
      items: [
        {
          name: "MediaPipe Engine AI",
          desc: "An edge-oriented motion correction engine that uses FSM-based sequence decoupling and keypoint topology for real-time exercise feedback",
          tech: "Android / Kotlin / MediaPipe / FSM"
        },
        {
          name: "Fire Panel Perception",
          desc: "An industrial-grade visual computing pipeline for 128-key panel diagnosis under severe perspective distortion and complex lighting conditions",
          tech: "OpenCV / RANSAC / Python"
        },
        {
          name: "ClassVision Distributed",
          desc: "A distributed classroom sensing and diagnostics system covering attendance, behavior analysis, and device detection with containerized deployment",
          tech: "FastAPI / YOLOv8 / WebSocket / Docker"
        },
        {
          name: "Tiezhitong Agent",
          desc: "A semantic-driven railway assistant that integrates tools and instructions for converged multi-source querying, reflecting an early agent toolchain design mindset",
          tech: "Python / Semantic Routing / Tool Orchestration"
        },
        {
          name: "CifarLab Trainer",
          desc: "A modular training platform with AMP, cosine annealing, and configuration-driven experimentation for fast and reproducible deep learning workflows",
          tech: "PyTorch / AMP / YAML"
        },
        {
          name: "Persona Chat Studio",
          desc: "A lightweight LLM interface using Int4 quantization and streaming context control to balance latency, memory footprint, and response quality",
          tech: "Qwen / Gradio / Int4"
        },
        {
          name: "spec-X",
          desc: "Architecture Philosophy + Custom Skills System (repo-audit/stack-detect/test-autopilot)",
          tech: "Skills System / Architecture / Automation"
        },
        {
          name: "virtu-tutor-dkt",
          desc: "DKT + RL Virtual Idol Clean Architecture",
          tech: "DKT / RL / Clean Architecture"
        }
      ]
    },
    philosophy: {
      title: "Engineering Philosophy",
      points: [
        "Small and stable over large and messy",
        "Protocols before feature stacking",
        "Every Skill should be a closed loop of reusable experience",
        "Seek convergence in silence, evolve through rigor",
        "Refuse hype, build precise systems for the long term"
      ],
      content:
        "I care more about testability, reusability, and maintainability than short-lived novelty Engineering should leave behind durable structure"
    },
    footer: {
      greeting: "© 2026 LOSTLIGHT | Engineering with intention",
      note: "Quiet Pragmatic Reusable"
    }
  }
};

export default translations;
