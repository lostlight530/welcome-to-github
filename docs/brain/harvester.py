import urllib.request
import json
import os
import datetime
import re
from pathlib import Path

class Harvester:
    def __init__(self, brain_path):
        self.brain_path = Path(brain_path)
        self.inputs_path = self.brain_path / "inputs"
        self.state_file = self.inputs_path / ".harvester_state.json"
        self.state = self._load_state()

        # [UPGRADE] Architect's Watchlist (Expanded)
        self.targets = {
            # Architecture & Agent Protocol
            "ModelEngine-Group/nexent": ["tags"],
            "iflytek/astron-agent": ["tags"],
            "mindspore-ai/mindspore": ["tags"],

            # Competitors
            "langgenius/dify": ["tags"],
            "anthropics/anthropic-tools": ["tags"],

            # Core Tech Stack
            "vllm-project/vllm": ["tags"],
            "huggingface/transformers": ["tags"],
            "google-ai-edge/mediapipe": ["tags"],
            "microsoft/markitdown": ["tags"]
        }

    def _load_state(self):
        if self.state_file.exists():
            with open(self.state_file, 'r') as f:
                return json.load(f)
        return {}

    def _save_state(self):
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=2)

    def _analyze_content(self, text):
        """
        [UPGRADE] The Architect's Filter
        自动分析文本，提取高价值标签。
        """
        tags = []

        # Filter 1: Edge AI Readiness
        if re.search(r'(?i)(onnx|gguf|litert|android|ios|arm|npu|quantiz)', text):
            tags.append("🏷️ Edge-Ready")

        # Filter 2: Breaking Changes
        if re.search(r'(?i)(breaking|deprecated|removed|migration)', text):
            tags.append("⚠️ Breaking-Change")

        # Filter 3: Agentic Ecosystem
        if re.search(r'(?i)(mcp|plugin|workflow|skill|orchestrat|multi-actor|stateful)', text):
            tags.append("🔗 Agent-Protocol")

        return tags

    def fetch_github_data(self):
        print("[Harvester] Scanning frequencies...")
        new_files = []

        for repo, endpoints in self.targets.items():
            print(f"[Harvester] Pinging {repo}...")
            url = f"https://api.github.com/repos/{repo}/releases/latest"

            try:
                req = urllib.request.Request(url, headers={"User-Agent": "Nexus-Cortex/Bot"})
                with urllib.request.urlopen(req) as response:
                    data = json.loads(response.read().decode())
                    tag = data.get('tag_name', 'unknown')
                    body = data.get('body', '')

                    # Check ETag/State
                    last_tag = self.state.get(repo, {}).get('last_tag')
                    if tag != last_tag:
                        print(f"   🔥 Signal detected: {tag}")

                        # Analyze Content
                        analysis_tags = self._analyze_content(body)
                        header_tags = " ".join(analysis_tags)

                        # Create Report
                        timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
                        filename = f"{repo.replace('/', '_')}_{tag}.md"
                        filepath = self.inputs_path / filename
                        self.inputs_path.mkdir(parents=True, exist_ok=True)

                        content = f"# ℹ️ Intel: {repo} {tag}\n"
                        content += f"> Source: GitHub Releases\n"
                        content += f"> Date: {datetime.datetime.now().isoformat()}\n"
                        if header_tags:
                            content += f"> **Analysis**: {header_tags}\n"
                        content += f"\n## 📝 Summary\n{tag}\n\n## 🔍 Changelog (Extract)\n{body[:2000]}...\n"

                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)

                        # Update State
                        self.state[repo] = {'last_tag': tag, 'updated_at': timestamp}
                        new_files.append(str(filepath))
            except Exception as e:
                print(f"   ⚠️ Signal lost: {e}")

        self._save_state()
        return new_files

if __name__ == "__main__":
    h = Harvester(Path(__file__).parent)
    h.fetch_github_data()
