import os
import json
import argparse
import requests
import sys
import urllib.parse
from datetime import datetime

# Import existing brain modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from cortex import Cortex

# Official Source Radar: Whitelist of high-signal repositories
OFFICIAL_REPOS = [
    "modelcontextprotocol/servers",
    "modelcontextprotocol/python-sdk",
    "google-ai-edge/mediapipe",
    "mindspore-ai/mindspore",
    "google/generative-ai-python",
]

GITHUB_API_SEARCH_URL = "https://api.github.com/search/repositories"

class Harvester:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.cortex = Cortex(root_dir)
        self.intelligence_dir = os.path.join(root_dir, "intelligence")
        self.inputs_dir = os.path.join(root_dir, "inputs")

        os.makedirs(self.intelligence_dir, exist_ok=True)
        os.makedirs(self.inputs_dir, exist_ok=True)

        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "lostlight-brain-harvester"
        }

    # --- Phase A: Official Source Radar ---
    def _get_latest_release(self, repo: str):
        url = f"https://api.github.com/repos/{repo}/releases/latest"
        try:
            resp = requests.get(url, headers=self.headers)
            if resp.status_code == 200:
                data = resp.json()
                return {
                    "type": "release",
                    "tag": data.get("tag_name"),
                    "name": data.get("name"),
                    "body": data.get("body", "")[:500] + "...",
                    "url": data.get("html_url"),
                    "date": data.get("published_at")
                }
        except Exception:
            pass
        return None

    def _get_recent_commits(self, repo: str):
        url = f"https://api.github.com/repos/{repo}/commits?per_page=3"
        commits = []
        try:
            resp = requests.get(url, headers=self.headers)
            if resp.status_code == 200:
                data = resp.json()
                for commit in data:
                    c = commit.get("commit", {})
                    commits.append({
                        "message": c.get("message", "").split("\n")[0],
                        "author": c.get("author", {}).get("name"),
                        "date": c.get("author", {}).get("date"),
                        "url": commit.get("html_url"),
                        "sha": commit.get("sha")[:7]
                    })
        except Exception:
            pass
        return {"type": "commits", "data": commits} if commits else None

    # --- Phase B: Top Ecosystem Consensus ---
    def _get_search_targets(self):
        self.cortex.load_graph()
        report = self.cortex.analyze_entropy()
        targets = []
        if report.orphan_nodes: targets.extend(report.orphan_nodes[:2])
        if len(targets) < 2 and report.stale_nodes:
            remaining = 2 - len(targets)
            targets.extend(report.stale_nodes[:remaining])
        if not targets: targets = ["Edge AI", "MCP"]
        return targets

    def _search_ecosystem(self, query: str):
        # Strict filter: stars > 20000 (Top Ecosystem Consensus)
        strict_query = f"{query} stars:>20000"
        encoded_query = urllib.parse.quote(strict_query)
        url = f"{GITHUB_API_SEARCH_URL}?q={encoded_query}&sort=stars&order=desc&per_page=2"

        try:
            resp = requests.get(url, headers=self.headers)
            if resp.status_code == 200:
                return resp.json().get("items", [])
        except Exception as e:
            print(f"[!] Ecosystem Search Error: {e}")
        return []

    def harvest(self):
        timestamp = datetime.now().strftime("%Y-%m-%d")
        print(f"[Harvester] Starting Intelligence Gathering Protocol...")

        report_content = [
            f"# 🧠 Intelligence Report: {timestamp}",
            f"> **Objective**: Dual-Phase Signal Acquisition (双相信号采集)",
            "",
            "## 📡 Phase A: Official Source Radar (官方源头震荡)",
        ]
        candidates = []

        # Phase A Execution
        for repo in OFFICIAL_REPOS:
            print(f"  [Official] Scanning: {repo}...")
            update = self._get_latest_release(repo)
            if not update: update = self._get_recent_commits(repo)

            if not update:
                continue

            report_content.append(f"### 🎯 {repo}")
            if update["type"] == "release":
                report_content.append(f"- **🚀 New Release**: [{update['tag']}]({update['url']})")
                report_content.append(f"- **Date**: {update['date']}")
                report_content.append(f"- **Notes**: {update['body']}")
                candidates.append({
                    "id": f"{repo.replace('/', '-')}-release-{update['tag']}",
                    "type": "official_update",
                    "name": f"{repo} {update['tag']}",
                    "desc": f"Official Release: {update['name']}",
                    "tags": ["official_release", repo.split("/")[1]],
                    "url": update["url"],
                    "discovered_at": datetime.now().isoformat()
                })
            elif update["type"] == "commits":
                report_content.append(f"- **🔨 Recent Commits** (Last 3):")
                for c in update["data"]:
                    report_content.append(f"  - [`{c['sha']}`]({c['url']}) {c['message']} (*{c['author']}*)")
                candidates.append({
                    "id": f"{repo.replace('/', '-')}-commits-{datetime.now().strftime('%Y%m%d')}",
                    "type": "official_update",
                    "name": f"{repo} Recent Activity",
                    "desc": f"Recent commits: {update['data'][0]['message']}",
                    "tags": ["official_commits", repo.split("/")[1]],
                    "url": f"https://github.com/{repo}/commits",
                    "discovered_at": datetime.now().isoformat()
                })
            report_content.append("")

        # Phase B Execution
        report_content.append("## 🌍 Phase B: Top Ecosystem Consensus (顶级生态共识)")
        targets = self._get_search_targets()
        print(f"[Ecosystem] Targets: {targets}")

        for target in targets:
            entity = self.cortex.entities.get(target)
            query_term = entity.name if entity else target

            report_content.append(f"### 🔍 Concept: `{query_term}` (ID: {target})")
            repos = self._search_ecosystem(query_term)

            if not repos:
                report_content.append("- *No consensus-level projects found (stars > 20k).*")
                report_content.append("")
                continue

            for repo in repos:
                name = repo['full_name']
                stars = repo['stargazers_count']
                desc = repo['description'] or "No description."
                url = repo['html_url']

                report_content.append(f"- **[{name}]({url})**")
                report_content.append(f"  - ⭐ **{stars}** | 📝 {desc}")

                candidates.append({
                    "id": name.lower().replace("/", "-").replace(".", "-"),
                    "type": "ecosystem_consensus",
                    "name": name,
                    "desc": f"Ecosystem Consensus: {desc} (Stars: {stars})",
                    "tags": ["ecosystem_consensus", query_term.lower().replace(" ", "_")],
                    "url": url,
                    "discovered_via": target,
                    "discovered_at": datetime.now().isoformat()
                })
            report_content.append("")

        # Write Files
        report_path = os.path.join(self.intelligence_dir, f"REPORT_{timestamp}.md")
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("\n".join(report_content))

        candidates_path = os.path.join(self.inputs_dir, f"candidates_{timestamp}.jsonl")
        with open(candidates_path, "w", encoding="utf-8") as f:
            for c in candidates:
                f.write(json.dumps(c, ensure_ascii=False) + "\n")

        print(f"[Harvester] Complete. Report: {report_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NEXUS Harvester: Dual-Phase Protocol")
    parser.add_argument("--root", default="docs/brain", help="Path to brain root directory")
    args = parser.parse_args()

    Harvester(args.root).harvest()
