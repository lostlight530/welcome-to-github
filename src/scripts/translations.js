const translations = {
    zh: {
        title: "lostlight 2025-2026 年度回顾",
        nav: {
            home: "首页",
            engines: "双引擎驱动",
            projects: "核心项目",
            collaboration: "人机协作"
        },
        hero: {
            role: "端侧 AI 实践者",
            tagline: "低调 务实<br><span class='gradient-text'>极致工程化</span>",
            description: "专注 Python AI 深耕 Google 生态与国产 AI 架构 追求代码可读性 可测性与可维护性"
        },
        engines: {
            title: "双引擎技术底座",
            google: {
                name: "Google 生态",
                items: ["MediaPipe 端侧推理", "Vertex AI 模型构建", "Gemini 代理集成"],
                evidence: "13 枚官方开发者勋章"
            },
            domestic: {
                name: "华为 国产生态",
                items: ["昇腾 Ascend 硬件适配", "昇思 MindSpore 框架开发", "鸿蒙 HarmonyOS 应用集成"],
                evidence: "华为 ICT 大赛与昇思创新赛奖项"
            }
        },
        projects: {
            title: "核心项目矩阵",
            items: [
                {
                    name: "MediaPipe Tasks AI 助手",
                    desc: "端侧健身手指操纠错 状态机逻辑 低延迟姿态识别",
                    tech: "Android MediaPipe Kotlin"
                },
                {
                    name: "消防面板视觉检测",
                    desc: "128 键复杂面板检测 仿射变换 RANSAC 鲁棒算法",
                    tech: "OpenCV Python RANSAC"
                },
                {
                    name: "ClassVision 分布式系统",
                    desc: "FastAPI YOLOv8 课堂诊断 容器化部署 自动化监控",
                    tech: "Docker FastAPI YOLOv8"
                },
                {
                    name: "MindSpore Lite 移动端部署",
                    desc: "昇思模型量化 移动端推理性能优化 算子适配",
                    tech: "MindSpore C++ NDK"
                },
                {
                    name: "HarmonyOS AI 集成",
                    desc: "鸿蒙原生 AI 能力调用 分布式算力协同",
                    tech: "ArkTS HarmonyOS SDK"
                },
                {
                    name: "Vertex AI Agent Builder",
                    desc: "企业级 Agent 构建 知识库检索增强 自动化流调优",
                    tech: "Vertex AI Python LangChain"
                }
            ]
        },
        collaboration: {
            title: "人机协作证据",
            agentEvidence: "12 个 AI Agent 协作分支 覆盖安全 重构 测试 规范",
            humanEvidence: "lostlight 核心架构设计 业务逻辑决策 性能极限调优",
            philosophy: "推崇 DDD 领域驱动设计 每一个 Commit 都是对小而稳承诺的践行"
        },
        footer: {
            greeting: "新春快乐 HAPPY CHINESE NEW YEAR 2026"
        }
    },
    en: {
        title: "lostlight 2025-2026 Year in Review",
        nav: {
            home: "Home",
            engines: "Dual Engines",
            projects: "Projects",
            collaboration: "AI-Human"
        },
        hero: {
            role: "Edge AI Practitioner",
            tagline: "Quiet Pragmatic<br><span class='gradient-text'>Engineering Excellence</span>",
            description: "Focusing on Python AI Google Ecosystem and Domestic AI Architectures Dedicated to Readability Testability and Maintainability"
        },
        engines: {
            title: "Dual Engine Foundations",
            google: {
                name: "Google Ecosystem",
                items: ["MediaPipe Edge Inference", "Vertex AI Model Building", "Gemini Agent Integration"],
                evidence: "13 Official Developer Badges"
            },
            domestic: {
                name: "Huawei Ecosystem",
                items: ["Ascend Hardware Adaptation", "MindSpore Framework Development", "HarmonyOS Integration"],
                evidence: "Huawei ICT and MindSpore Awards"
            }
        },
        projects: {
            title: "Core Project Matrix",
            items: [
                {
                    name: "MediaPipe Tasks AI",
                    desc: "Edge fitness hand exercise correction State machine logic Low latency posture recognition",
                    tech: "Android MediaPipe Kotlin"
                },
                {
                    name: "Fire Panel Vision Detection",
                    desc: "128 key complex panel detection Affine Transform RANSAC robust algorithm",
                    tech: "OpenCV Python RANSAC"
                },
                {
                    name: "ClassVision Distributed System",
                    desc: "FastAPI YOLOv8 diagnostic platform Containerized deployment Automated monitoring",
                    tech: "Docker FastAPI YOLOv8"
                },
                {
                    name: "MindSpore Lite Deployment",
                    desc: "MindSpore model quantization Mobile inference performance optimization Operator adaptation",
                    tech: "MindSpore C++ NDK"
                },
                {
                    name: "HarmonyOS AI Integration",
                    desc: "Native HarmonyOS AI capability calling Distributed computing synergy",
                    tech: "ArkTS HarmonyOS SDK"
                },
                {
                    name: "Vertex AI Agent Builder",
                    desc: "Enterprise Agent construction RAG workflow optimization",
                    tech: "Vertex AI Python LangChain"
                }
            ]
        },
        collaboration: {
            title: "AI-Human Collaboration",
            agentEvidence: "12 AI Agent branches covering Security Refactoring Testing Consistency",
            humanEvidence: "lostlight core architecture design Business logic decision Performance tuning",
            philosophy: "Advocating for DDD Every commit is a practice of Small and Stable"
        },
        footer: {
            greeting: "HAPPY CHINESE NEW YEAR 2026"
        }
    }
};

export default translations;
