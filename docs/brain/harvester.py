import urllib.request
import json
import os
import datetime
import re
import threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

class Harvester:
    def __init__(self, brain_path):
        self.brain_path = Path(brain_path)
        self.inputs_path = self.brain_path / "inputs"
        self.state_file = self.inputs_path / ".harvester_state.json"
        self.state_lock = threading.Lock()
        self.state = self._load_state()

        # [Architect's Watchlist] Phase A Radar
        self.targets = {
            "ModelEngine-Group/nexent": ["releases", "commits"],
            "iflytek/astron-agent": ["releases", "commits"],
            "langgenius/dify": ["releases"],
            "vllm-project/vllm": ["releases"],
            "huggingface/transformers": ["releases"],
            "google-ai-edge/mediapipe": ["releases"],
            "microsoft/markitdown": ["releases"],
            "googleapis/python-genai": ["releases"]
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
        """Architect's Filters: Semantic Tagging"""
        tags = []
        # Edge AI
        if re.search(r'(?i)(onnx|gguf|litert|android|ios|arm|npu|quantiz)', text):
            tags.append("🏷️ Edge-Ready")
        # Breaking Changes
        if re.search(r'(?i)(breaking|deprecated|removed|migration)', text):
            tags.append("⚠️ Breaking-Change")
        # Agent Protocol
        if re.search(r'(?i)(mcp|plugin|workflow|skill|orchestrat|hitl)', text):
            tags.append("🔗 Agent-Protocol")
        return tags

    def _fetch_repo_data(self, repo):
        """Thread worker to fetch data for a single repository."""
        print(f"   [Radar] Scanning Target: {repo}...")
        url = f"https://api.github.com/repos/{repo}/releases/latest"
        result_file = None

        try:
            with self.state_lock:
                repo_state = self.state.get(repo, {})
                etag = repo_state.get('etag')
                last_tag = repo_state.get('last_tag')

            # Intent-Driven Whitelist Probes: Use standard library with HTTP Caching (ETag)
            headers = {"User-Agent": "Nexus-Cortex/2.5 (Zero-Dependency)"}
            if etag:
                headers["If-None-Match"] = etag

            req = urllib.request.Request(url, headers=headers)
            try:
                with urllib.request.urlopen(req, timeout=10) as response:
                    data = json.loads(response.read().decode())
                    tag = data.get('tag_name', 'unknown')
                    body = data.get('body', '') or "No description provided."
                    new_etag = response.getheader('ETag')
            except urllib.error.HTTPError as e:
                if e.code == 304:
                    # Not Modified: ETag matched, no new data. Preserve rate limit.
                    return None
                else:
                    raise e

            if tag != last_tag:
                print(f"   🔥 [Signal] High-Velocity Update: {repo} @ {tag}")
                analysis_tags = self._analyze_content(body)
                header_tags = " ".join(analysis_tags)

                # Structure strictly following memory anchors
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
                filename = f"{repo.replace('/', '_')}_{tag}.md"
                filepath = self.inputs_path / filename

                content = f"# ℹ️ Intel Report: {repo}\n"
                content += f"## 🎯 监控目标 (Target)\n> {repo}\n\n"
                content += f"## 🚀 新版本发布 (New Release)\n> Version: {tag}\n> Date: {datetime.datetime.now().isoformat()}\n"

                if header_tags:
                    content += f"\n## 💡 项目洞察 (Insight)\n> **Architect's Analysis**: {header_tags}\n"

                # Trust Score calculation based on tags
                score = 80 + (10 * len(analysis_tags))
                content += f"\n## 🛡️ 信任评分 (Trust Score)\n> Score: {score}/100\n"

                content += f"\n## 🔨 最近提交 (Recent Commits)\n*Summary from release notes:*\n\n{body[:3000]}\n"

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

                with self.state_lock:
                    self.state[repo] = {'last_tag': tag, 'updated_at': timestamp, 'etag': new_etag}
                result_file = str(filepath)
            else:
                # Update ETag even if tag hasn't changed to stay synced
                with self.state_lock:
                    self.state[repo]['etag'] = new_etag

        except Exception as e:
            # Silently degrade on network errors to maintain system anti-fragility
            pass

        return result_file

    def fetch_github_data(self):
        print("[Harvester] Initiating asynchronous radar sweep (Zero-Dependency Concurrency)...")
        new_files = []

        # Liquid Time-Series Graph Injection - Phase 4 Concurrency
        with ThreadPoolExecutor(max_workers=5) as executor:
            future_to_repo = {executor.submit(self._fetch_repo_data, repo): repo for repo in self.targets.keys()}
            for future in as_completed(future_to_repo):
                filepath = future.result()
                if filepath:
                    new_files.append(filepath)

        with self.state_lock:
            self._save_state()

        return new_files
