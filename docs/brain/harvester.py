#!/usr/bin/env python3
import json
import os
import sys
import argparse
import urllib.request
import urllib.error
from datetime import datetime, timezone

# Stateful Harvester (The Radar)
# 状态感知收割机（雷达）

class Harvester:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.inputs_dir = os.path.join(root_dir, "inputs")
        self.state_file = os.path.join(self.inputs_dir, ".harvester_state.json")
        self.state = self._load_state()

    def _load_state(self):
        """Loads cursor state (ETags, Timestamps). (加载游标状态)"""
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                pass
        return {"repos": {}}

    def _save_state(self):
        """Saves cursor state. (保存游标状态)"""
        os.makedirs(self.inputs_dir, exist_ok=True)
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=2)

    def scan_github_releases(self, repo: str):
        """
        Scans GitHub releases for a repo using stateful ETag logic.
        使用状态感知 ETag 逻辑扫描 GitHub 发布。
        """
        url = f"https://api.github.com/repos/{repo}/releases/latest"
        print(f"[Harvester] Scanning {repo}...")

        # 1. Get previous state
        repo_state = self.state["repos"].get(repo, {})
        headers = {
            "User-Agent": "Nexus-Cortex/1.0",
            "Accept": "application/vnd.github.v3+json"
        }
        if "etag" in repo_state:
            headers["If-None-Match"] = repo_state["etag"]

        # 2. Request
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                # 200 OK - New Content
                data = json.loads(response.read().decode())
                new_etag = response.getheader("ETag")

                # Process
                self._process_release(repo, data)

                # Update State
                self.state["repos"][repo] = {
                    "etag": new_etag,
                    "last_checked": datetime.now(timezone.utc).isoformat(),
                    "latest_tag": data.get("tag_name")
                }
                self._save_state()

        except urllib.error.HTTPError as e:
            if e.code == 304:
                print(f"  - No changes (304 Not Modified). (无变更)")
            elif e.code == 403:
                print(f"  - Rate Limit Exceeded or Forbidden. (速率限制或禁止访问)")
            elif e.code == 404:
                print(f"  - Repo not found. (仓库未找到)")
            else:
                print(f"  - Error: {e}")
        except Exception as e:
             print(f"  - Network Error: {e}")

    def _process_release(self, repo: str, data: dict):
        """
        Generates an intelligence brief for the new release.
        为新发布生成情报简报。
        """
        tag = data.get("tag_name", "unknown")
        name = data.get("name", tag)
        body = data.get("body", "")
        published_at = data.get("published_at", datetime.now().isoformat())

        print(f"  - 🚀 New Release: {tag}")

        # Determine if BREAKING CHANGE
        is_breaking = "BREAKING CHANGE" in body or "Major" in name
        alert_emoji = "🚨" if is_breaking else "ℹ️"

        # Generate Markdown Brief
        ym = datetime.now().strftime("%Y/%m")
        filename = f"{repo.replace('/', '_')}_{tag}.md"
        filepath = os.path.join(self.inputs_dir, ym, filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        content = f"""# {alert_emoji} Intel: {repo} {tag}
> Source: GitHub Releases
> Date: {published_at}

## 📝 Summary
{name}

## 🔍 Changelog (Extract)
{body[:2000]}... (truncated)

## 🤖 Cognitive Analysis Required
- [ ] Is this a major version update? ({is_breaking})
- [ ] Does it conflict with existing 'tech_stack' nodes?
- [ ] Action: Run `nexus.py add` or `nexus.py connect` to integrate.
"""
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"  - Brief written to {filepath}")

def main():
    parser = argparse.ArgumentParser(description="NEXUS HARVESTER: Stateful Intelligence Radar")
    parser.add_argument("--root", default="docs/brain", help="Path to brain root")
    args = parser.parse_args()

    harvester = Harvester(args.root)

    # Whitelist of high-signal repos (Phase A Radar)
    targets = [
        "vllm-project/vllm",
        "google/gemma_pytorch",
        "huggingface/transformers",
        "microsoft/markitdown"
    ]

    print("📡 Harvester Radar Activated (雷达已激活)")
    for target in targets:
        harvester.scan_github_releases(target)

if __name__ == "__main__":
    main()
