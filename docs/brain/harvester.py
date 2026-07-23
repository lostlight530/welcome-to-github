"""Profile-driven GitHub document harvester using only the standard library."""
import base64
import datetime as dt
import difflib
import fnmatch
import hashlib
import json
import os
import re
import time
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
        self.token = os.environ.get("GITHUB_TOKEN", "")
        self.dry = os.environ.get("HARVESTER_DRY_RUN", "0") == "1"
        self.profiles = self._json(self.profile_path, {})
        old = self._json(self.state_path, {})
        self.state = self._validated_state(old)

    @staticmethod
    def _json(path, default):
        try:
            return json.loads(Path(path).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return default

    @staticmethod
    def _validated_state(state):
        if not isinstance(state, dict):
            raise ValueError("harvester state must be a mapping")
        repositories = state.get("repositories")
        if repositories is None:
            return {
                "schema_version": 3,
                "legacy_state": state,
                "repositories": {},
            }
        if not isinstance(repositories, dict):
            raise ValueError("harvester state repositories must be a mapping")
        for repo, repo_state in repositories.items():
            if not isinstance(repo_state, dict):
                raise ValueError(f"repository state must be a mapping: {repo}")
            documents = repo_state.get("documents")
            if documents is None:
                repo_state["documents"] = {}
            elif not isinstance(documents, dict):
                raise ValueError(f"repository documents must be a mapping: {repo}")
        return state

    def _blob_text(self, repo, sha):
        blob = self._api(f"https://api.github.com/repos/{repo}/git/blobs/{sha}")
        if not isinstance(blob, dict) or blob.get("encoding") != "base64":
            raise ValueError(f"unsupported blob encoding: {repo}@{sha}")
        return base64.b64decode(blob["content"]).decode("utf-8", errors="replace")

    @staticmethod
    def _move_to_archive(source, destination):
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            if source.read_bytes() != destination.read_bytes():
                raise FileExistsError(f"archive collision: {destination}")
            source.unlink()
            return
        os.replace(source, destination)

    def _api(self, url):
        headers = {"Accept": "application/vnd.github+json", "User-Agent": "Nexus-Document-Harvester/3"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        request = urllib.request.Request(url, headers=headers)
        for attempt in range(3):
            try:
                with urllib.request.urlopen(request, timeout=30) as response:
                    return json.loads(response.read().decode("utf-8"))
            except urllib.error.HTTPError as exc:
                if exc.code not in {429, 500, 502, 503, 504} or attempt == 2:
                    raise
            except urllib.error.URLError:
                if attempt == 2:
                    raise
            time.sleep(2 ** attempt)
        raise RuntimeError(f"unreachable retry state: {url}")
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
            destination = archive / stale.name
            self._move_to_archive(stale, destination)
            archived.append(destination.relative_to(self.inputs).as_posix())
        return archived

    def _source(self, profile):
        repo = profile["repo"]
        meta = self._api(f"https://api.github.com/repos/{repo}")
        tree = self._api(f"https://api.github.com/repos/{repo}/git/trees/{meta['default_branch']}?recursive=1")
        if tree.get("truncated"):
            raise ValueError(f"truncated repository tree: {repo}")
        repo_state = self.state["repositories"].setdefault(repo, {"documents": {}})
        if not isinstance(repo_state, dict) or not isinstance(
            repo_state.get("documents"), dict
        ):
            raise ValueError(f"invalid repository state: {repo}")
        changed = []
        namespace = repo.lower().replace("/", "_").replace("-", "_")
        items = [item for item in tree.get("tree", []) if item.get("type") == "blob" and self._selected(item["path"], profile.get("documents", []), profile.get("ignore_patterns", []))]
        selected_paths = {item["path"] for item in items}
        for item in sorted(items, key=lambda value: value["path"]):
            path, sha = item["path"], item["sha"]
            previous = repo_state["documents"].get(path, {})
            if previous.get("sha") == sha:
                continue
            text = self._blob_text(repo, sha)
            digest = hashlib.sha256(self._normalized(text).encode()).hexdigest()
            if previous.get("content_hash") == digest:
                repo_state["documents"][path] = {**previous, "sha": sha}
                continue
            entity = f"external_doc_{namespace}_{re.sub(r'[^a-z0-9]+', '_', path.lower()).strip('_' )}"
            target = self.inputs / "current" / profile["layer"] / namespace / (path.replace("/", "__") + f"__{sha[:12]}.md")
            old = self._blob_text(repo, previous["sha"]) if previous.get("sha") else ""
            diff = "\n".join(difflib.unified_diff(old.splitlines(), text.splitlines(), fromfile="previous", tofile=sha, n=3))
            provenance = {"source_repo": repo, "source_path": path, "source_sha": sha, "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(), "confidence": 1.0, "primary_owner": profile["primary_owner"], "entity_id": entity}
            rendered = render_snapshot(provenance, text, diff, profile["layer"])
            validate_owned_punctuation(rendered)
            if not self.dry:
                target.parent.mkdir(parents=True, exist_ok=True)
                self._archive_stale(target, path, profile["layer"], namespace)
                atomic_write(target, rendered)
            relative = target.relative_to(self.inputs).as_posix()
            repo_state["documents"][path] = {"sha": sha, "content_hash": digest, "entity_id": entity, "output": relative}
            changed.append(relative)
        for path in sorted(set(repo_state["documents"]) - selected_paths):
            previous = repo_state["documents"][path]
            output = previous.get("output")
            if output and not self.dry:
                snapshot = self.inputs / output
                if snapshot.exists():
                    destination = (
                        self.inputs
                        / "archive"
                        / dt.datetime.now(dt.timezone.utc).strftime("%Y/%m")
                        / profile["layer"]
                        / namespace
                        / snapshot.name
                    )
                    self._move_to_archive(snapshot, destination)
            del repo_state["documents"][path]
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
