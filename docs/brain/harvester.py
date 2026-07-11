"""Profile-driven GitHub document harvester using only the standard library."""
import base64
import datetime as dt
import difflib
import fnmatch
import hashlib
import json
import os
import re
import urllib.error
import urllib.request
from pathlib import Path

from document_hygiene import atomic_write, render_snapshot, validate_owned_punctuation


class Harvester:
    def __init__(self, root=None):
        here = Path(__file__).resolve()
        if root is not None and (Path(root) / "inputs").exists():
            self.inputs = Path(root) / "inputs"
            self.profile_path = Path(root) / "source_profiles.json"
        else:
            project = Path(root) if root else here.parents[3]
            self.inputs = project / "data" / "inputs"
            self.profile_path = self.inputs / "source_profiles.json"
        self.state_path = self.inputs / ".harvester_state.json"
        self.cache = self.inputs / ".raw_cache"
        self.token = os.environ.get("GITHUB_TOKEN", "")
        self.dry = os.environ.get("HARVESTER_DRY_RUN", "0") == "1"
        self.profiles = self._json(self.profile_path, {})
        old = self._json(self.state_path, {})
        self.state = old if "repositories" in old else {"schema_version": 3, "legacy_state": old, "repositories": {}}

    @staticmethod
    def _json(path, default):
        try:
            return json.loads(Path(path).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return default

    def _api(self, url):
        headers = {"Accept": "application/vnd.github+json", "User-Agent": "Nexus-Document-Harvester/3"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))

    @staticmethod
    def _selected(path, patterns, ignored):
        value = path.lower()
        if any(fnmatch.fnmatch(value, pattern.lower()) for pattern in ignored):
            return False
        return value == "readme.md" or any(fnmatch.fnmatch(value, pattern.lower()) for pattern in patterns)

    @staticmethod
    def _normalized(text):
        kept = []
        for line in text.splitlines():
            if re.search(r"(?i)(badge|shields\.io|updated[_ -]?at|last[_ -]?updated)", line):
                continue
            line = re.sub(r"\s+", " ", line).strip()
            if line:
                kept.append(line)
        return "\n".join(kept)

    def validate_profiles(self):
        owner = self.profiles.get("owner")
        seen = set()
        for profile in self.profiles.get("sources", []):
            key = profile.get("repo", "").lower()
            if profile.get("primary_owner") != owner:
                raise ValueError(f"owner mismatch: {key}")
            if owner == "zero" and not profile.get("promotion_approved"):
                raise ValueError(f"unapproved source: {key}")
            if key in seen:
                raise ValueError(f"duplicate source: {key}")
            seen.add(key)
        return True

    def _archive_stale(self, target, source_path, layer, namespace):
        prefix = source_path.replace("/", "__") + "__"
        archive = self.inputs / "archive" / dt.datetime.now(dt.timezone.utc).strftime("%Y/%m") / layer / namespace
        archived = []
        for stale in target.parent.glob(prefix + "*.md"):
            if stale == target:
                continue
            archive.mkdir(parents=True, exist_ok=True)
            destination = archive / stale.name
            os.replace(stale, destination)
            archived.append(destination.relative_to(self.inputs).as_posix())
        return archived

    def _source(self, profile):
        repo = profile["repo"]
        meta = self._api(f"https://api.github.com/repos/{repo}")
        tree = self._api(f"https://api.github.com/repos/{repo}/git/trees/{meta['default_branch']}?recursive=1")
        if tree.get("truncated"):
            raise ValueError(f"truncated repository tree: {repo}")
        repo_state = self.state["repositories"].setdefault(repo, {"documents": {}})
        changed = []
        items = [item for item in tree.get("tree", []) if item.get("type") == "blob" and self._selected(item["path"], profile.get("documents", []), profile.get("ignore_patterns", []))]
        for item in sorted(items, key=lambda value: value["path"]):
            path, sha = item["path"], item["sha"]
            previous = repo_state["documents"].get(path, {})
            if previous.get("sha") == sha:
                continue
            blob = self._api(f"https://api.github.com/repos/{repo}/git/blobs/{sha}")
            if blob.get("encoding") != "base64":
                raise ValueError(f"unsupported blob encoding: {repo}/{path}")
            text = base64.b64decode(blob["content"]).decode("utf-8", errors="replace")
            digest = hashlib.sha256(self._normalized(text).encode()).hexdigest()
            if previous.get("content_hash") == digest:
                repo_state["documents"][path] = {**previous, "sha": sha}
                continue
            namespace = repo.lower().replace("/", "_").replace("-", "_")
            entity = f"doc_{namespace}_{re.sub(r'[^a-z0-9]+', '_', path.lower()).strip('_')}_{sha[:12]}"
            target = self.inputs / "current" / profile["layer"] / namespace / (path.replace("/", "__") + f"__{sha[:12]}.md")
            cache = self.cache / namespace / (path.replace("/", "__") + ".txt")
            old = cache.read_text(encoding="utf-8") if cache.exists() else ""
            diff = "\n".join(difflib.unified_diff(old.splitlines(), text.splitlines(), fromfile="previous", tofile=sha, n=3))
            provenance = {"source_repo": repo, "source_path": path, "source_sha": sha, "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(), "confidence": 1.0, "primary_owner": profile["primary_owner"], "entity_id": entity}
            rendered = render_snapshot(provenance, text, diff, profile["layer"])
            validate_owned_punctuation(rendered)
            if not self.dry:
                target.parent.mkdir(parents=True, exist_ok=True)
                cache.parent.mkdir(parents=True, exist_ok=True)
                self._archive_stale(target, path, profile["layer"], namespace)
                atomic_write(target, rendered)
                atomic_write(cache, text)
            relative = target.relative_to(self.inputs).as_posix()
            repo_state["documents"][path] = {"sha": sha, "content_hash": digest, "entity_id": entity, "output": relative}
            changed.append(relative)
        repo_state["last_checked_at"] = dt.datetime.now(dt.timezone.utc).isoformat()
        return changed

    def fetch_github_data(self):
        self.validate_profiles()
        changed, failures = [], []
        for profile in self.profiles.get("sources", []):
            try:
                changed.extend(self._source(profile))
            except (urllib.error.URLError, KeyError, ValueError) as exc:
                failures.append(f"{profile.get('repo')}: {exc}")
        if failures:
            raise RuntimeError("harvest failed: " + " | ".join(failures))
        if not self.dry:
            atomic_write(self.state_path, json.dumps(self.state, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
        print(json.dumps({"updated": len(changed), "failed": 0}, ensure_ascii=False, sort_keys=True))
        return changed
