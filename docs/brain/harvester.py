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
import urllib.parse
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
        self.bootstrap = os.environ.get("HARVESTER_BOOTSTRAP", "0") == "1"
        self.profiles = self._json(self.profile_path, label="source profiles")
        old = self._json(
            self.state_path,
            label="harvester state",
            allow_missing=self.bootstrap,
            default={"schema_version": 4, "repositories": {}},
        )
        self.state = self._validated_state(old)

    @staticmethod
    def _json(path, *, label, allow_missing=False, default=None):
        path = Path(path)
        try:
            raw = path.read_text(encoding="utf-8")
        except FileNotFoundError:
            if allow_missing:
                return default
            raise FileNotFoundError(f"required {label} file is missing: {path}")
        except OSError as exc:
            raise OSError(f"failed to read {label}: {path}: {exc}") from exc
        try:
            return json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSON in {label}: {path}: {exc}") from exc

    @staticmethod
    def _validated_state(state):
        if not isinstance(state, dict):
            raise ValueError("harvester state must be a mapping")
        repositories = state.get("repositories")
        if repositories is None:
            raise ValueError("harvester state is missing repositories")
        if not isinstance(repositories, dict):
            raise ValueError("harvester state repositories must be a mapping")
        for repo, repo_state in repositories.items():
            if not isinstance(repo, str) or not repo:
                raise ValueError("repository state keys must be non-empty strings")
            if not isinstance(repo_state, dict):
                raise ValueError(f"repository state must be a mapping: {repo}")
            documents = repo_state.get("documents")
            if not isinstance(documents, dict):
                raise ValueError(f"repository documents must be a mapping: {repo}")
            for path, document in documents.items():
                if not isinstance(path, str) or not isinstance(document, dict):
                    raise ValueError(f"invalid repository document state: {repo}")
        state["schema_version"] = 4
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
        if not isinstance(self.profiles, dict):
            raise ValueError("source profiles must be a mapping")
        owner = self.profiles.get("owner")
        sources = self.profiles.get("sources")
        if not isinstance(owner, str) or not owner:
            raise ValueError("source profiles owner must be a non-empty string")
        if not isinstance(sources, list) or not sources:
            raise ValueError("source profiles sources must be a non-empty list")
        seen = set()
        for profile in sources:
            if not isinstance(profile, dict):
                raise ValueError("source profile entries must be mappings")
            key = profile.get("repo", "")
            if not isinstance(key, str) or "/" not in key:
                raise ValueError(f"invalid source repository: {key}")
            key = key.lower()
            if profile.get("primary_owner") != owner:
                raise ValueError(f"owner mismatch: {key}")
            if owner == "zero" and not profile.get("promotion_approved"):
                raise ValueError(f"unapproved source: {key}")
            if not isinstance(profile.get("layer"), str) or not profile["layer"]:
                raise ValueError(f"invalid source layer: {key}")
            if not isinstance(profile.get("documents"), list):
                raise ValueError(f"invalid source documents: {key}")
            if not isinstance(profile.get("ignore_patterns", []), list):
                raise ValueError(f"invalid source ignore patterns: {key}")
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
        if not isinstance(meta, dict) or not isinstance(meta.get("default_branch"), str):
            raise ValueError(f"invalid repository metadata: {repo}")
        branch = urllib.parse.quote(meta["default_branch"], safe="")
        commit = self._api(f"https://api.github.com/repos/{repo}/commits/{branch}")
        try:
            commit_sha = commit["sha"]
            tree_sha = commit["commit"]["tree"]["sha"]
        except (KeyError, TypeError) as exc:
            raise ValueError(f"invalid commit metadata: {repo}") from exc
        if not all(isinstance(value, str) and value for value in (commit_sha, tree_sha)):
            raise ValueError(f"invalid commit provenance: {repo}")
        tree = self._api(
            f"https://api.github.com/repos/{repo}/git/trees/{tree_sha}?recursive=1"
        )
        if not isinstance(tree, dict) or not isinstance(tree.get("tree"), list):
            raise ValueError(f"invalid repository tree: {repo}@{tree_sha}")
        if tree.get("truncated"):
            raise ValueError(f"truncated repository tree: {repo}")
        repo_state = self.state["repositories"].setdefault(repo, {"documents": {}})
        if not isinstance(repo_state, dict) or not isinstance(
            repo_state.get("documents"), dict
        ):
            raise ValueError(f"invalid repository state: {repo}")
        changed = []
        namespace = repo.lower().replace("/", "_").replace("-", "_")
        items = [
            item
            for item in tree["tree"]
            if item.get("type") == "blob"
            and isinstance(item.get("path"), str)
            and isinstance(item.get("sha"), str)
            and self._selected(
                item["path"],
                profile.get("documents", []),
                profile.get("ignore_patterns", []),
            )
        ]
        selected_paths = {item["path"] for item in items}
        for item in sorted(items, key=lambda value: value["path"]):
            path, blob_sha = item["path"], item["sha"]
            previous = repo_state["documents"].get(path, {})
            if not isinstance(previous, dict):
                raise ValueError(f"invalid document state: {repo}:{path}")
            previous_blob_sha = previous.get("blob_sha") or previous.get("sha")
            provenance_complete = all(
                isinstance(previous.get(field), str) and previous[field]
                for field in ("commit_sha", "tree_sha", "blob_sha")
            )
            if previous_blob_sha == blob_sha and provenance_complete:
                continue
            text = self._blob_text(repo, blob_sha)
            digest = hashlib.sha256(self._normalized(text).encode()).hexdigest()
            if previous.get("content_hash") == digest and provenance_complete:
                repo_state["documents"][path] = {
                    **previous,
                    "sha": blob_sha,
                    "blob_sha": blob_sha,
                    "commit_sha": commit_sha,
                    "tree_sha": tree_sha,
                }
                continue
            entity = previous.get("entity_id") or (
                f"external_doc_{namespace}_"
                f"{re.sub(r'[^a-z0-9]+', '_', path.lower()).strip('_')}"
            )
            filename = (
                path.replace("/", "__")
                + f"__{blob_sha[:12]}__{commit_sha[:12]}.md"
            )
            target = (
                self.inputs
                / "current"
                / profile["layer"]
                / namespace
                / filename
            )
            old = (
                self._blob_text(repo, previous_blob_sha)
                if previous_blob_sha and previous_blob_sha != blob_sha
                else ""
            )
            diff = "\n".join(
                difflib.unified_diff(
                    old.splitlines(),
                    text.splitlines(),
                    fromfile="previous",
                    tofile=blob_sha,
                    n=3,
                )
            )
            provenance = {
                "source_repo": repo,
                "source_path": path,
                "source_sha": commit_sha,
                "commit_sha": commit_sha,
                "tree_sha": tree_sha,
                "blob_sha": blob_sha,
                "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                "confidence": 1.0,
                "primary_owner": profile["primary_owner"],
                "entity_id": entity,
            }
            rendered = render_snapshot(
                provenance,
                text,
                diff,
                profile["layer"],
            )
            validate_owned_punctuation(rendered)
            if not self.dry:
                target.parent.mkdir(parents=True, exist_ok=True)
                self._archive_stale(target, path, profile["layer"], namespace)
                atomic_write(target, rendered)
            relative = target.relative_to(self.inputs).as_posix()
            repo_state["documents"][path] = {
                "sha": blob_sha,
                "blob_sha": blob_sha,
                "commit_sha": commit_sha,
                "tree_sha": tree_sha,
                "content_hash": digest,
                "entity_id": entity,
                "output": relative,
            }
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