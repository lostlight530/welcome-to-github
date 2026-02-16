import os
import ast
import json
import random
import urllib.request
from datetime import datetime

class StaticThinker:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.config_path = os.path.join(root_dir, "docs/brain/brain_config.json")
        self.memories_dir = os.path.join(root_dir, "docs/brain/memories")
        self.config = self._load_config()

    def _load_config(self):
        with open(self.config_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def micro_ast_audit(self):
        """微观自省：解析自身源码结构"""
        print("[Thinker] 🔬 执行 AST 静态自省...")
        audit_results = []
        brain_path = os.path.join(self.root_dir, "docs/brain")

        for filename in sorted(os.listdir(brain_path)):
            if filename.endswith(".py"):
                path = os.path.join(brain_path, filename)
                with open(path, "r", encoding="utf-8") as f:
                    try:
                        tree = ast.parse(f.read())
                        classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
                        methods = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
                        audit_results.append(f"- **{filename}**: Classes={len(classes)} ({', '.join(classes)}), Functions={len(methods)}")
                    except Exception as e:
                        audit_results.append(f"- **{filename}**: AST Parse Error ({e})")

        return "\n".join(audit_results)

    def macro_architecture_study(self):
        """宏观学习：从白名单随机抽取大厂架构进行沉思"""
        sources = self.config["whitelist"]
        topics = list(sources.items())
        random.shuffle(topics) # Shuffle to support retry logic

        # Retry loop: Try up to 3 different sources
        for attempt in range(3):
            if not topics:
                break

            topic, url = topics.pop()
            print(f"[Thinker] 🔭 今日课题 (Attempt {attempt+1}): {topic}")

            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'NEXUS-CORTEX-Scholar'})
                with urllib.request.urlopen(req) as response:
                    content = response.read().decode('utf-8')[:self.config["settings"]["max_read_length"]]

                # Success!
                insight = self._mock_llm_logic(topic, content)
                return topic, url, insight
            except Exception as e:
                print(f"[Thinker] ⚠️ 抓取失败 ({topic}): {e}")
                continue # Try next topic

        print("[Thinker] ❌ 所有尝试均失败。")
        return None, None, None

    def _mock_llm_logic(self, topic, content):
        """模拟架构师思维提取逻辑"""
        # Simple keyword extraction to make it dynamic
        keywords = []
        if "interface" in content.lower(): keywords.append("Interface Design")
        if "async" in content.lower(): keywords.append("Asynchronous Patterns")
        if "immutable" in content.lower(): keywords.append("Immutability")
        if "layer" in content.lower(): keywords.append("Layered Architecture")

        keyword_str = ", ".join(keywords) if keywords else "General Architecture"

        return f"### 🏛️ {topic} 架构洞察\n- **核心模式**: {keyword_str}\n- **设计哲学**: 极致解耦与确定性状态机。\n- **端侧启示**: 保持无状态设计，利用不可变数据结构。"

    def commit_insight(self):
        """将今日沉思固化为物理记忆"""
        today = datetime.now().strftime("%Y-%m-%d")
        ast_report = self.micro_ast_audit()
        topic, url, insight = self.macro_architecture_study()

        if topic:
            filename = f"learning-record-{today}.md"
            filepath = os.path.join(self.memories_dir, filename)

            content = [
                f"# 🧠 NEXUS CORTEX: 每日架构沉思",
                f"> 日期: {today} | 课题: {topic} | [数据源]({url})",
                "",
                "## 🔍 内部 AST 自省 (Internal Audit)",
                ast_report,
                "",
                "## 🏗️ 外部架构感悟 (External Insight)",
                insight,
                "",
                "---",
                "*Self-Evolution recorded by Static Thinker.*"
            ]

            with open(filepath, "w", encoding="utf-8") as f:
                f.write("\n".join(content))
            print(f"[Thinker] 沉思录已保存: {filepath}")

if __name__ == "__main__":
    # Assume running from repo root
    thinker = StaticThinker(root_dir=".")
    thinker.commit_insight()
