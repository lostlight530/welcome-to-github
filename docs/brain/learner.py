import os
import ast
import re
import json
import random
import urllib.request
import argparse
from datetime import datetime

class DeterministicScholar:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        # Assuming root_dir is 'docs/brain'
        self.config_path = os.path.join(root_dir, "brain_config.json")
        self.memories_dir = os.path.join(root_dir, "memories")
        self.config = self._load_config()

    def _load_config(self):
        with open(self.config_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def micro_ast_audit(self):
        """Micro-Introspection: AST Topology Metrics"""
        print("[Scholar] 🔬 Executing AST Topology Audit...")
        audit_lines = []
        # root_dir is already docs/brain
        brain_path = self.root_dir

        for filename in sorted(os.listdir(brain_path)):
            if filename.endswith(".py"):
                path = os.path.join(brain_path, filename)
                with open(path, "r", encoding="utf-8") as f:
                    try:
                        tree = ast.parse(f.read())

                        # Topology Metrics
                        class_nodes = [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
                        func_nodes = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
                        import_nodes = [n for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))]

                        complexity_score = len(class_nodes) * 5 + len(func_nodes)

                        audit_lines.append(f"### 📦 {filename}")
                        audit_lines.append(f"- **Complexity Score**: `{complexity_score}`")
                        audit_lines.append(f"- **Structure**: {len(class_nodes)} Classes, {len(func_nodes)} Methods, {len(import_nodes)} Imports")

                        if complexity_score > 50:
                            audit_lines.append(f"- ⚠️ **Entropy Warning**: High complexity detected.")

                    except Exception as e:
                        audit_lines.append(f"- **{filename}**: AST Parse Error ({e})")

        return "\n".join(audit_lines)

    def _extract_architecture_sections(self, text: str) -> str:
        """Regex Anchor Extraction for Architecture/Design Philosophy"""
        # Patterns to find headers like "Architecture", "Design", "Philosophy" and capture the text below
        patterns = [
            r"(#+.*(?:Architecture|Design|Philosophy|Goals|Pattern|Core Concepts).*[\s\S]*?)(?=\n#+ |$)",
            r"(#+.*(?:设计|哲学|架构).*[\s\S]*?)(?=\n#+ |$)"
        ]
        found_sections = []

        # Limit text search to avoid ReDoS on massive files
        search_text = text[:50000]

        for p in patterns:
            matches = re.findall(p, search_text, re.IGNORECASE | re.MULTILINE)
            # Clean up matches
            for m in matches:
                if len(m.split('\n')) > 3: # Only keep significant sections
                    found_sections.append(m.strip())

        # Deduplicate while preserving order
        seen = set()
        unique_sections = []
        for s in found_sections:
            if s not in seen:
                unique_sections.append(s)
                seen.add(s)

        return "\n\n---\n\n".join(unique_sections) if unique_sections else "No explicit architecture definition found via regex anchors."

    def run_daily_contemplation(self, manual_topic: str = None):
        """Execute the Deterministic Learning Loop"""
        today = datetime.now().strftime("%Y-%m-%d")
        sources = self.config["whitelist"]

        # 1. Topic Selection
        if manual_topic:
            # Fuzzy match for manual input
            matches = [k for k in sources.keys() if manual_topic.lower() in k.lower()]
            if matches:
                topic = matches[0]
                url = sources[topic]
            else:
                print(f"[Scholar] Topic '{manual_topic}' not found in whitelist. Falling back to random.")
                topic, url = random.choice(list(sources.items()))
        else:
            topic, url = random.choice(list(sources.items()))

        print(f"[Scholar] 🔭 Learning Subject: {topic}")

        # 2. Fetch Raw Content (Zero Execution)
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'NEXUS-CORTEX-Scholar'})
            with urllib.request.urlopen(req) as response:
                raw_text = response.read().decode('utf-8')

            # 3. Static Extraction
            arch_insight = self._extract_architecture_sections(raw_text)
            ast_report = self.micro_ast_audit()

            # 4. Jules' Deterministic Summary (The "Special Place")
            jules_summary = [
                "### 🤖 Jules' Operational Summary",
                f"- **Extraction Status**: {'✅ Success' if 'No explicit' not in arch_insight else '⚠️ Partial'}",
                f"- **Content Length**: {len(raw_text)} chars parsed.",
                f"- **Focus**: {topic} aligns with 'Small and Stable' philosophy by definition of the whitelist.",
                "- **Next Step**: Ingest into knowledge graph if 'Pattern' entities are detected."
            ]

            # 5. Commit to Memory
            filename = f"learning-record-{today}.md"
            filepath = os.path.join(self.memories_dir, filename)

            content = [
                f"# 🧠 NEXUS CORTEX: Deterministic Learning Record",
                f"> **Date**: {today} | **Subject**: {topic}",
                f"> **Source**: [{url}]({url})",
                "",
                "## 🏛️ Extracted Architecture/Design (Original Text)",
                "> *Extracted via Regex Anchor Pattern Matching*",
                "",
                arch_insight,
                "",
                "## 🔬 Internal System Topology (AST Audit)",
                ast_report,
                "",
                "## 📝 System Self-Reflection",
                "\n".join(jules_summary),
                "",
                "---",
                "*Generated by Deterministic Scholar (No-API)*"
            ]

            with open(filepath, "w", encoding="utf-8") as f:
                f.write("\n".join(content))
            print(f"[Scholar] Knowledge solidified: {filepath}")

        except Exception as e:
            print(f"[Scholar] ❌ Mission Failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", help="Specific topic to learn (fuzzy match whitelist keys)")
    parser.add_argument("--root", default=".", help="Root directory")
    args = parser.parse_args()

    DeterministicScholar(root_dir=args.root).run_daily_contemplation(manual_topic=args.topic)
