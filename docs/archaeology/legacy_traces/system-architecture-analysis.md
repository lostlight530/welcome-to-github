《NEXUS CORTEX PHASE IV：绝对确定性工程落地指南》

一、 最高系统宪法 (The Absolute Axioms)

零内部算力依赖：系统内部永久禁止调用任何大模型推理 API！系统是绝对冷酷的数字主板，只负责 I/O、图论计算与存储，大模型仅作为外部客体通过 MCP 接入

零第三方库红线：严禁使用 pip 安装任何非必需的第三方解析库或渲染库（彻底封杀 Jinja2 等）！所有新增模块必须基于 Python 标准库手搓，确保系统在裸机环境极速启动

二、 scholar.py：全域外部解剖刀 (Universal Digestion)

边界拓宽：从“向内看的自我反思镜”彻底升级为“向外看的全域手术刀”

具体落实：当 Harvester 抓取外部高优生态（如 Nexent、Astron-agent、VLLM）的源码、配置文件或 Release 时，scholar.py 必须针对 JSON/YAML/JS 编写专用的原生解析管道（Parser Pipeline）

输出要求：完全剥离自然语言，强行提取配置树、核心架构节点与依赖属性，转化为纯粹的结构化图谱字典，系统必须靠确定性的代码逻辑去吞噬外部世界的知识骨架

三、 memories 渲染区：零依赖模板引擎 (Zero-Dependency Brutalism)

技术栈锁定：绝不允许引入外部模板依赖

底层实现：利用 Python 最原生的 string.Template，或者结合简单的 re 正则表达式模块，徒手构建一个极简、无坚不摧的 Markdown 渲染引擎

渲染机制：由 reason.py 通过纯数学与图论算出的孤立节点、熵值增量等冰冷数据，直接通过原生字典映射替换模板中的占位符（如 $entropy_score），并在毫秒级瞬间渲染出无任何废话的 cognitive-report.md 与悬赏任务单

四、 harvester.py：双重离合防抖与算力熔断 (Double-Clutch Anti-Shake)

第一重网关（粗筛）：维持网络层的 HTTP ETag 缓存响应，阻挡无意义的轮询

第二重物理防线（精筛）：在内容真正落盘并触发解析前，强制在内存中执行 SHA-256 哈希校验；如果哈希发生变动，再辅以纯文本 Diff 对比，无情过滤掉仅因时间戳改变或排版微调造成的“伪更新”

绝对熔断：只有当真正携带高密度信息的核心代码或架构逻辑发生实质改变时，才放行触发后续的 SQLite 图谱重构与 Evolution 沙盒演化！将无效的自动化算力损耗彻底按死在 0 的刻度上

五、 cortex.py：时序图谱的基建重塑 (Temporal Schema)

时间维度降临：在底层的 SQLite 核心表结构中，强制推行 valid_at 与 invalid_at 时间戳体系

记忆不可变性：知识实体与关系连线永远禁止被覆盖，新版本的获取只能让旧版本知识状态失效，这为未来的 MCP 查询提供确定性的“历史快照对齐”能力，彻底封杀大模型的时空错乱幻觉
