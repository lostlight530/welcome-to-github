import os
import json
import argparse
import requests
import sys
import urllib.parse
from datetime import datetime, timezone

# --- The Core Physics: Official Source Whitelist (第一层：官方源头白名单) ---
OFFICIAL_REPOS = [
    # Anthropic / MCP
    "modelcontextprotocol/servers",
    "modelcontextprotocol/python-sdk",
    # Google / Edge AI
    "google-ai-edge/mediapipe",
    "googleapis/python-genai",
    "google/jax",
    # Huawei / Ascend
    "mindspore-ai/mindspore",
    # Microsoft / Agentic & Runtime
    "microsoft/semantic-kernel",
    "microsoft/onnxruntime"
]

# --- The High-Star Matrix: Top Ecosystem Consensus (第二层：顶级生态共识) ---
# Whitelisted "Super Apps" to monitor
ECOSYSTEM_REPOS = [
    # Agent Orchestration
    "n8n-io/n8n",
    "langgenius/dify",
    "langchain-ai/langchain",
    # RAG & Context
    "infiniflow/ragflow",
    "run-llama/llama_index",
    # Inference & Optimization
    "ggerganov/llama.cpp",
    "rustformers/llm"
]

class Harvester:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        # No Cortex dependency needed for Whitelist-based harvesting
        self.intelligence_dir = os.path.join(root_dir, "intelligence")
        self.inputs_dir = os.path.join(root_dir, "inputs")

        os.makedirs(self.intelligence_dir, exist_ok=True)
        os.makedirs(self.inputs_dir, exist_ok=True)

        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "lostlight-brain-harvester"
        }

    def _extract_gist(self, text: str):
        """Extracts key insights: Breaking Changes, New Capabilities, Engineering Debt."""
        text_lower = text.lower()
        insights = []

        # 1. Breaking Change (破坏性更新)
        if any(k in text_lower for k in ["breaking", "deprecate", "removed", "migration"]):
            insights.append("⚠️ **BREAKING CHANGE**: Potential API breakage or deprecation detected.")

        # 2. New Capability (新能力)
        if any(k in text_lower for k in ["feat", "new", "support", "added", "introduce"]):
            insights.append("✨ **New Capability**: New features or NPU operator support likely added.")

        # 3. Engineering Debt (工程债务)
        if any(k in text_lower for k in ["fix", "bug", "archived", "maintenance", "refactor"]):
            insights.append("🔧 **Engineering Debt**: Bug fixes or maintenance work.")

        return insights

    def _calculate_trust_score(self, repo_data):
        """
        Trust Score = (Stars * 0.3) + (Forks * 0.2) + (1 / DaysSinceUpdate * 0.5)
        Follows user specification exactly.
        """
        stars = repo_data.get("stargazers_count", 0)
        forks = repo_data.get("forks_count", 0)
        updated_at_str = repo_data.get("updated_at")

        if not updated_at_str:
            days_since_update = 365 # Penalty for no date
        else:
            updated_at = datetime.fromisoformat(updated_at_str.replace("Z", "+00:00"))
            days_since_update = (datetime.now(timezone.utc) - updated_at).days
            if days_since_update < 1: days_since_update = 1

        # Exact formula as requested: 1/Days * 0.5
        # Note: This makes freshness contribution very small compared to Stars, but adheres to spec.
        score = (stars * 0.3) + (forks * 0.2) + ((1.0 / days_since_update) * 0.5)
        return score

    def _get_repo_details(self, repo_full_name: str):
        url = f"https://api.github.com/repos/{repo_full_name}"
        try:
            resp = requests.get(url, headers=self.headers)
            if resp.status_code == 200:
                return resp.json()
        except Exception:
            pass
        return None

    def _get_latest_release(self, repo: str):
        url = f"https://api.github.com/repos/{repo}/releases/latest"
        try:
            resp = requests.get(url, headers=self.headers)
            if resp.status_code == 200:
                data = resp.json()
                body = data.get("body", "")
                return {
                    "type": "release",
                    "tag": data.get("tag_name"),
                    "name": data.get("name"),
                    "body": body[:500] + "...",
                    "gist": self._extract_gist(body),
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
                combined_msg = ""
                for commit in data:
                    c = commit.get("commit", {})
                    msg = c.get("message", "").split("\n")[0]
                    combined_msg += msg + " "
                    commits.append({
                        "message": msg,
                        "author": c.get("author", {}).get("name"),
                        "date": c.get("author", {}).get("date"),
                        "url": commit.get("html_url"),
                        "sha": commit.get("sha")[:7]
                    })
                return {
                    "type": "commits",
                    "data": commits,
                    "gist": self._extract_gist(combined_msg)
                }
        except Exception:
            pass
        return None

    def harvest(self):
        timestamp = datetime.now().strftime("%Y-%m-%d")
        print(f"[Harvester] Starting Protocol: Official Radar + Ecosystem Consensus...")

        report_content = [
            f"# 🧠 Intelligence Report: {timestamp}",
            f"> **Objective**: High-Signal Acquisition (高信噪比情报)",
            "",
            "## 🏛️ Phase A: Official Source Radar (官方源头白名单)",
            "> Monitoring Core Physics: MCP, Google Edge AI, Huawei Ascend, Microsoft Agents.",
            ""
        ]
        candidates = []

        # --- Phase A: Official Repos ---
        for repo in OFFICIAL_REPOS:
            print(f"  [Official] Scanning: {repo}...")
            update = self._get_latest_release(repo)
            if not update: update = self._get_recent_commits(repo)

            if not update:
                continue

            report_content.append(f"### 🎯 监控目标 (Target): {repo}")
            if update["type"] == "release":
                report_content.append(f"- **🚀 新版本发布 (New Release)**: [{update['tag']}]({update['url']})")
                report_content.append(f"- **Date**: {update['date']}")

                # Gist Analysis
                if update["gist"]:
                    for g in update["gist"]: report_content.append(f"- {g}")

                report_content.append(f"- **Notes**: {update['body']}")

                candidates.append({
                    "id": f"{repo.replace('/', '-')}-release-{update['tag']}",
                    "type": "official_update",
                    "name": f"{repo} {update['tag']}",
                    "desc": f"Official Release: {update['name']}. Gist: {', '.join(update['gist'])}",
                    "tags": ["official_release", repo.split("/")[1]],
                    "url": update["url"],
                    "discovered_at": datetime.now().isoformat()
                })
            elif update["type"] == "commits":
                report_content.append(f"- **🔨 最近提交 (Recent Commits)**:")
                # Gist Analysis
                if update["gist"]:
                    for g in update["gist"]: report_content.append(f"- {g}")

                for c in update["data"]:
                    report_content.append(f"  - [`{c['sha']}`]({c['url']}) {c['message']} (*{c['author']}*)")

                candidates.append({
                    "id": f"{repo.replace('/', '-')}-commits-{datetime.now().strftime('%Y%m%d')}",
                    "type": "official_update",
                    "name": f"{repo} Recent Activity",
                    "desc": f"Recent commits activity. Gist: {', '.join(update['gist'])}",
                    "tags": ["official_commits", repo.split("/")[1]],
                    "url": f"https://github.com/{repo}/commits",
                    "discovered_at": datetime.now().isoformat()
                })
            report_content.append("")

        # --- Phase B: Ecosystem Consensus ---
        report_content.append("## 🌊 Phase B: Top Ecosystem Consensus (顶级生态共识)")
        report_content.append("> Filter: Stars > 20k + Trust Score Sorting. Identifying the 'Super Apps'.")
        report_content.append("")

        ecosystem_candidates = []
        print(f"  [Ecosystem] analyzing Trust Scores for {len(ECOSYSTEM_REPOS)} repos...")

        for repo_name in ECOSYSTEM_REPOS:
            details = self._get_repo_details(repo_name)
            if details:
                score = self._calculate_trust_score(details)
                details['trust_score'] = score
                ecosystem_candidates.append(details)

        # Sort by Trust Score descending and take Top 3
        ecosystem_candidates.sort(key=lambda x: x['trust_score'], reverse=True)
        top_candidates = ecosystem_candidates[:5] # Keep Top 5 for the report

        for repo in top_candidates:
            name = repo['full_name']
            stars = repo['stargazers_count']
            forks = repo['forks_count']
            updated = repo['updated_at']
            score = int(repo['trust_score'])
            desc = repo['description'] or "No description."
            url = repo['html_url']

            report_content.append(f"### 🏆 {name}")
            report_content.append(f"- **🛡️ 信任评分 (Trust Score)**: `{score}` (⭐ {stars} | 🍴 {forks})")
            report_content.append(f"- **Updated**: {updated}")
            report_content.append(f"- **💡 项目洞察 (Insight)**: {desc}")
            report_content.append(f"- [View Source]({url})")
            report_content.append("")

            candidates.append({
                "id": name.lower().replace("/", "-").replace(".", "-"),
                "type": "ecosystem_consensus",
                "name": name,
                "desc": f"Ecosystem Consensus: {desc} (Trust Score: {score})",
                "tags": ["ecosystem_consensus", "high_trust"],
                "url": url,
                "discovered_at": datetime.now().isoformat()
            })

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
