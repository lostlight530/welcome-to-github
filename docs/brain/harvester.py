import urllib.request
import json
import os
import datetime
import re
import threading
import hashlib
import difflib
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
                    raw_content = response.read().decode()
                    data = json.loads(raw_content)
                    tag = data.get('tag_name', 'unknown')
                    body = data.get('body', '') or "No description provided."
                    new_etag = response.getheader('ETag')
            except urllib.error.HTTPError as e:
                if e.code == 304:
                    # Not Modified: ETag matched, no new data. Preserve rate limit.
                    return None
                else:
                    raise e

            # Phase IV.2: Double-Clutch Anti-Shake (SHA-256 + Diff)
            # Deterministic noise stripping prior to hash (Zero-Dependency)
            clean_content = re.sub(r'(?i)\b(date|time|updated_at|timestamp)\s*[:=]\s*["\']?\d{4}-\d{2}-\d{2}T?\d{0,2}:?\d{0,2}[:.]?\d{0,3}Z?["\']?', '', raw_content)
            clean_content = re.sub(r'\d{4}-\d{2}-\d{2}', '', clean_content)

            content_hash = hashlib.sha256(clean_content.encode('utf-8')).hexdigest()

            with self.state_lock:
                last_hash = repo_state.get('last_hash')

            if last_hash == content_hash:
                print(f"      => [Anti-Shake] Hash match for {repo} (Noise filtered). Content is structurally identical, aborting digest.")
                with self.state_lock:
                    self.state[repo] = self.state.get(repo, {})
                    self.state[repo]['etag'] = new_etag
                return None

            # Fallback Diff if Hash Changed (checking for trivial whitespace/timestamp changes)
            cache_dir = self.inputs_path / ".raw_cache"
            cache_dir.mkdir(parents=True, exist_ok=True)
            cache_file = cache_dir / f"{repo.replace('/', '_')}.json"

            is_trivial_update = False
            if cache_file.exists() and last_hash:
                with open(cache_file, 'r', encoding='utf-8') as f:
                    old_content = f.read()

                # Zero-dependency diff
                diff = list(difflib.unified_diff(
                    old_content.splitlines(),
                    raw_content.splitlines(),
                    n=0
                ))

                # Check if diff only contains lines with dates, timestamps, or stats
                meaningful_changes = 0
                for line in diff:
                    if line.startswith('+') or line.startswith('-'):
                        if not line.startswith('+++') and not line.startswith('---'):
                            text = line[1:].lower()
                            # If the change is NOT just a date, timestamp, or a number update, it's meaningful
                            if not re.search(r'\b(date|time|updated_at|timestamp)\b|\d{4}-\d{2}-\d{2}', text) and len(text.strip()) > 3:
                                meaningful_changes += 1

                if meaningful_changes == 0 and len(diff) > 0:
                    is_trivial_update = True
                    print(f"      => [Anti-Shake] Diff for {repo} is trivial (timestamps/metadata only). Aborting digest.")

            if is_trivial_update:
                with self.state_lock:
                    self.state[repo] = self.state.get(repo, {})
                    self.state[repo]['etag'] = new_etag
                    self.state[repo]['last_hash'] = content_hash
                with open(cache_file, 'w', encoding='utf-8') as f:
                    f.write(raw_content)
                return None

            # Proceed with the update
            with open(cache_file, 'w', encoding='utf-8') as f:
                f.write(raw_content)

            with self.state_lock:
                if repo not in self.state:
                    self.state[repo] = {}
                self.state[repo]['etag'] = new_etag
                self.state[repo]['last_tag'] = tag
                self.state[repo]['last_hash'] = content_hash

            if tag != last_tag or last_hash != content_hash:
                print(f"   🔥 [Signal] Valid Structural Update: {repo} @ {tag}")
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

    def _read_mission_active_intents(self):
        """Phase V/VI: Self-Driven Intent Probes via SQLite DB Graph Reversal."""
        mission_path = self.brain_path / "memories" / "MISSION_ACTIVE.md"
        if not mission_path.exists(): return

        try:
            with open(mission_path, 'r', encoding='utf-8') as f:
                content = f.read()

            import re
            import sqlite3

            # Phase VI SOP Automation: Extract explicitly declared entities that require SOP execution
            # Match: `python docs/brain/nexus.py connect "ENTITY_NAME" ...`
            matches = re.findall(r'nexus\.py connect\s+"([^"]+)"', content)

            if not matches: return

            db_path = self.brain_path / "cortex.db"
            if not db_path.exists(): return

            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            for entity_name in matches:
                # To resolve abstract entities into actionable targets, find connected 'config_property' or 'concept' elements
                # that might hold URL/Repo references, but specifically we check if the entity itself looks like a repo string

                # Check 1: Does the entity name itself look like a repo?
                if "/" in entity_name and "docs/brain" not in entity_name and len(entity_name.split("/")) == 2:
                    if entity_name not in self.targets:
                        self.targets[entity_name] = ["releases"]
                        print(f"   [Radar Intent] Added direct target from SOP command: {entity_name}")
                    continue

                # Check 2: Cortex DB Graph Lookup for linked whitelist targets
                # If the entity is abstract (e.g. "NEXUS System"), see if there is any target that is a URL repo we monitor
                # In this deterministic system, we map out from the isolated node.
                try:
                    sql = '''
                        SELECT e.name
                        FROM relations r
                        JOIN entities e ON (r.target = e.id OR r.source = e.id)
                        WHERE (r.source = (SELECT id FROM entities WHERE name = ?)
                           OR r.target = (SELECT id FROM entities WHERE name = ?))
                          AND e.name LIKE 'https://github.com/%'
                          AND e.invalid_at IS NULL
                        LIMIT 1
                    '''
                    cursor.execute(sql, (entity_name, entity_name))
                    result = cursor.fetchone()
                    if result:
                        url = result[0]
                        # Extract owner/repo from https://github.com/owner/repo
                        repo_match = re.search(r'github\.com/([a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+)', url)
                        if repo_match:
                            repo_str = repo_match.group(1)
                            # Remove trailing fragments like .md or /main/...
                            repo_parts = repo_str.split('/')
                            if len(repo_parts) >= 2:
                                clean_repo = f"{repo_parts[0]}/{repo_parts[1]}"
                                if clean_repo not in self.targets:
                                    self.targets[clean_repo] = ["releases"]
                                    print(f"   [Radar Intent] Graph Reverse Lookup resolved {entity_name} -> {clean_repo}")
                except Exception as e:
                    print(f"   [Radar Intent] Graph lookup failed for {entity_name}: {e}")

            conn.close()
        except Exception as e:
            print(f"[Harvester Error] Failed to read intents: {e}")

    def fetch_github_data(self):
        print("[Harvester] Initiating asynchronous radar sweep (Zero-Dependency Concurrency)...")
        new_files = []

        # Read self-driven intents before sweeping
        self._read_mission_active_intents()

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
