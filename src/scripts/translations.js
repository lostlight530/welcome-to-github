const translations = {
    zh: {
        title: "lostlight | 2025-2026 年度回顾",
        nav: {
            home: "首页",
            achievements: "年度成就",
            projects: "核心项目",
            philosophy: "工程哲学"
        },
        hero: {
            role: "端侧 AI 开发者 | Early Career",
            tagline: "低调 务实 <br><span class='gradient-text'>极致工程化</span>",
            description: "专注端侧 AI 生态集成与极致工程化，深耕 Google Vertex AI、MediaPipe 与华为昇腾生态，在“混乱-重整-收敛”中打磨可落地、可产品化的精密工具"
        },
        achievements: {
            title: "2025 荣耀时刻",
            googleBadges: "13 枚 Google 开发者勋章",
            awards: "4 项国家级/省级竞赛奖项",
            awardList: [
                "华为 ICT 大赛中国总决赛二等奖",
                "昇思 MindSpore 创新训练营二等奖",
                "蓝桥杯智能体开发省赛三等奖",
                "金砖国家技能大赛鸿蒙赛道晋级",
                "生产环境资产：20+ Repositories"
            ]
        },
        projects: {
            title: "核心项目矩阵",
            items: [
                {
                    name: "MediaPipe Engine AI",
                    desc: "针对端侧算力的实时健身纠错引擎，采用 FSM 状态机解耦复杂动作序列，通过 MediaPipe 提取拓扑关键点，实现亚秒级异常判定与反馈",
                    tech: "Android / Kotlin / FSM"
                },
                {
                    name: "Fire Panel Perception",
                    desc: "工业级高精度视觉解算算法，针对极端透视畸变，通过 RANSAC 鲁棒投影与网格重建，实现全自动物理坐标映射与 128 点状态诊断",
                    tech: "OpenCV / RANSAC / Python"
                },
                {
                    name: "ClassVision Distributed",
                    desc: "容器化大规模行为感知平台，利用消息队列解耦端云算力，支持千级并发处理，提供毫秒级动态反馈与多维情感评估指标",
                    tech: "YOLOv5 / Redis / Docker"
                },
                {
                    name: "Tiezhitong Agent v0",
                    desc: "基于语义驱动的枢纽控制助手，通过指令集解耦与工具动态挂载，实现多源异构数据的收敛查询。符合 MCP 协议早期的语义闭环模型",
                    tech: "MCP / Semantic Kernel / Python"
                },
                {
                    name: "CifarLab SOTA Trainer",
                    desc: "模块化深度学习训练框架，集成余弦退火、16位混合精度及 AMP 技术，支持 YAML 语义化定义架构，支撑从 ResNet 到 SOTA 的快速验证",
                    tech: "PyTorch / Mixed Precision"
                },
                {
                    name: "Persona LLM Interface",
                    desc: "端侧大语言模型轻量化方案，采用 Int4 量化提升推理吞吐量，集成上下文流式管理，在受限算力环境下寻求生成质量与速度的最优解",
                    tech: "Qwen / Gradio / Int4"
                }
            ]
        },
        philosophy: {
            title: "工程哲学",
            content: "“小而稳”高于“大而乱”，每一项 Skill 都是一次经验的闭环封装。在“静”中寻求技术的收敛，在“笃”中完成工具的进化，拒绝追逐短期热度，坚持构建可复用的精密架构"
        },
        footer: {
            greeting: "© 2026 LOSTLIGHT | 记录每一次工程自觉"
        }
    },
    en: {
        title: "lostlight | 2025-2026 Year in Review",
        nav: {
            home: "Home",
            achievements: "Achievements",
            projects: "Projects",
            philosophy: "Philosophy"
        },
        hero: {
            role: "Edge AI Developer | Early Career",
            tagline: "Quietly tinkering with <br><span class='gradient-text'>Python + AI.</span>",
            description: "Focusing on Edge AI integration and engineering excellence. Deeply experienced in Google Vertex AI, MediaPipe, and Huawei/Ascend architectures. Refining chaotic ideas into product-ready, resilient instruments."
        },
        achievements: {
            title: "2025 Highlights",
            googleBadges: "13 Google Developer Badges",
            awards: "4 National/Provincial Awards",
            awardList: [
                "2nd Prize, Huawei ICT Competition China Finals",
                "2nd Prize, MindSpore Innovation Bootcamp",
                "3rd Prize, Lanqiao Cup AI Agent Development",
                "Finalist, BRICS Skills HarmonyOS Track",
                "Production Assets: 20+ Repositories" // New
            ]
        },
        projects: {
            title: "Project Matrix",
            items: [
                {
                    name: "MediaPipe Engine AI",
                    desc: "Edge-based fitness validation system using FSM for action tracking. Sub-second keypoint detection optimized for senior care interaction.",
                    tech: "Android / Kotlin / FSM"
                },
                {
                    name: "Fire Panel Vision",
                    desc: "Industrial-grade algorithm for 128-key panel detection. Utilizes RANSAC for grid reconstruction under extreme perspective distortion.",
                    tech: "OpenCV / RANSAC / Python"
                },
                {
                    name: "ClassVision System",
                    desc: "Distributed education diagnostic platform using message queues for compute decoupling and large-scale behavior sensing.",
                    tech: "YOLOv5 / Docker / Redis"
                },
                {
                    name: "Tiezhitong Agent",
                    desc: "Semantic-driven railway agent featuring instruction decoupling and dynamic tool mounting. Prototype implementation of MCP protocol.",
                    tech: "MCP / Semantic Kernel / Python"
                },
                {
                    name: "CifarLab Trainer",
                    desc: "Modular DL experimental platform with pre-integrated FP16 and Cosine Annealing practices. YAML-driven rapid architecture switching.",
                    tech: "PyTorch / Mixed Precision / YAML"
                },
                {
                    name: "Persona Chat Studio",
                    desc: "Lightweight LLM interface with Int4 quantization for increased edge throughput, balancing memory usage and response quality.",
                    tech: "Qwen / Gradio / Int4 Quant"
                }
            ]
        },
        philosophy: {
            title: "Engineering Philosophy",
            content: "'Small and Stable' over 'Fast and Messy'. Every Skill is a closed experience encapsulation. Crafting precision in silence, refusing Hype, building for the future."
        },
        footer: {
            greeting: "© 2026 LOSTLIGHT | Engineering Excellence"
        }
    }
};

export default translations;
