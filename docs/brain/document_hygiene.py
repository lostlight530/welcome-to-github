"""Deterministic formatting and validation for harvested documents and JSONL ledgers."""
from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from pathlib import Path

OWNED_PERIOD = "。"


def atomic_write(path: Path, text: str) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_name, path)
    except Exception:
        Path(temp_name).unlink(missing_ok=True)
        raise


def headings(text: str, limit: int = 24) -> list[str]:
    values = []
    for line in text.splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if match:
            values.append(match.group(1).strip())
        if len(values) == limit:
            break
    return values


def render_snapshot(provenance: dict, source: str, diff: str, layer: str) -> str:
    repo = provenance["source_repo"]
    source_path = provenance["source_path"]
    source_sha = provenance["source_sha"]
    navigation = headings(source)
    added = sum(1 for line in diff.splitlines() if line.startswith("+") and not line.startswith("+++"))
    removed = sum(1 for line in diff.splitlines() if line.startswith("-") and not line.startswith("---"))
    nav = "\n".join(f"- {item}" for item in navigation) or "- 未发现 Markdown 标题."
    source_url = f"https://github.com/{repo}/blob/{source_sha}/{source_path}"
    owned = f"""# {repo} · {source_path}

> 当前有效快照. 中文说明只使用英文句号. 外部原文保持来源原貌.

## 一眼看懂

| 字段 | 值 |
| --- | --- |
| 来源仓库 | [{repo}](https://github.com/{repo}) |
| 来源文件 | [{source_path}]({source_url}) |
| 来源版本 | `{source_sha}` |
| 摄取时间 | `{provenance['retrieved_at']}` |
| 归属层 | `{layer}` |
| 可信度 | `{provenance.get('confidence', 1.0)}` |
| 记忆实体 | `{provenance['entity_id']}` |

## 本次变化

- 新增行数 `{added}`.
- 删除行数 `{removed}`.
- 内容哈希变化时才生成新快照.

## 阅读导航

{nav}

<details>
<summary>展开完整外部原文</summary>

{source.rstrip()}

</details>

<details>
<summary>展开完整版本差异</summary>

```diff
{diff.rstrip()}
```

</details>
"""
    return owned.rstrip() + "\n"


def validate_owned_punctuation(text: str) -> None:
    before_source = text.split("<details>", 1)[0]
    if OWNED_PERIOD in before_source:
        raise ValueError("owned content contains a Chinese full stop")


def maintain_jsonl(root: Path, rewrite: bool = False) -> dict:
    root = Path(root)
    files = _active_jsonl_files(root) if root.exists() else []
    invalid = duplicates = records = 0
    for path in files:
        seen = set()
        valid = []
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                invalid += 1
                raise ValueError(f"{path}:{number}: invalid JSONL: {exc}") from exc
            key = json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            if key in seen:
                duplicates += 1
                continue
            seen.add(key)
            valid.append(item)
        records += len(valid)
        if rewrite:
            content = "".join(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n" for item in valid)
            if path.read_text(encoding="utf-8") != content:
                atomic_write(path, content)

    return {"files": len(files), "records": records, "duplicates": duplicates, "invalid": invalid}

GENESIS_HASH = "NEXUS_GENESIS_0000"
_VOLATILE_FIELDS = {"hash", "prev_hash", "valid_at", "invalid_at", "updated_at", "created_at"}


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", str(value).lower()).strip("_")


def _active_jsonl_files(root: Path) -> list[Path]:
    return [
        path
        for path in sorted(Path(root).rglob("*.jsonl"))
        if "archive" not in {part.lower() for part in path.relative_to(root).parts}
    ]


def _payload(record: dict) -> dict:
    return {key: value for key, value in record.items() if key not in {"hash", "prev_hash"}}


def ledger_hash(record: dict, previous: str, domain: str) -> str:
    canonical = json.dumps(_payload(record), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    material = f"nexus-ledger-v1\n{domain}\n{previous}\n{canonical}".encode("utf-8")
    return hashlib.sha256(material).hexdigest()


def _write_records(path: Path, records: list[dict], root: Path, hash_chain: bool) -> None:
    domain = path.relative_to(root).as_posix()
    previous = GENESIS_HASH
    lines = []
    for source in records:
        record = dict(_payload(source))
        if hash_chain:
            record["prev_hash"] = previous
            record["hash"] = ledger_hash(record, previous, domain)
            previous = record["hash"]
        lines.append(json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    atomic_write(path, ("\n".join(lines) + "\n") if lines else "")


def verify_hash_chain(root: Path) -> dict:
    root = Path(root)
    files = _active_jsonl_files(root) if root.exists() else []
    records = broken = 0
    for path in files:
        previous = GENESIS_HASH
        domain = path.relative_to(root).as_posix()
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            records += 1
            item = json.loads(line)
            expected = ledger_hash(item, previous, domain)
            if item.get("prev_hash") != previous or item.get("hash") != expected:
                broken += 1
            previous = item.get("hash", expected)
    return {"files": len(files), "records": records, "broken": broken}


def _normalize_record(item: dict) -> dict:
    record = {key: value for key, value in item.items() if key not in _VOLATILE_FIELDS}
    if "src" not in record and "source" in record:
        record["src"] = record.pop("source")
    if "dst" not in record and "target" in record:
        record["dst"] = record.pop("target")
    if "relation" not in record and "rel" in record:
        record["relation"] = record.pop("rel")
    if "desc" not in record and "context" in record:
        record["desc"] = record.pop("context")
    return record


def canonicalize_ledger(root: Path, hash_chain: bool = False) -> dict:
    root = Path(root)
    files = _active_jsonl_files(root) if root.exists() else []
    entities = {}
    relations = {}
    duplicate_entities = duplicate_relations = invalid = 0

    for path in files:
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                raw = json.loads(line)
            except json.JSONDecodeError as exc:
                invalid += 1
                raise ValueError(f"{path}:{number}: invalid JSONL: {exc}") from exc
            item = _normalize_record(raw)
            if item.get("id"):
                entity_id = str(item["id"])
                if entity_id in entities:
                    duplicate_entities += 1
                if raw.get("invalid_at"):
                    entities.pop(entity_id, None)
                else:
                    entities[entity_id] = item
            elif item.get("src") and item.get("relation") and item.get("dst"):
                key = (str(item["src"]), str(item["relation"]), str(item["dst"]))
                if key in relations:
                    duplicate_relations += 1
                if raw.get("invalid_at"):
                    relations.pop(key, None)
                else:
                    relations[key] = item

    entity_ids = set(entities)
    clean_relations = {
        key: item
        for key, item in relations.items()
        if key[0] in entity_ids and key[2] in entity_ids
    }
    dangling_relations = len(relations) - len(clean_relations)

    for path in files:
        path.unlink()
    for entity_type in sorted({str(item.get("type", "concept")) for item in entities.values()}):
        records = sorted(
            (item for item in entities.values() if str(item.get("type", "concept")) == entity_type),
            key=lambda item: str(item["id"]),
        )
        _write_records(root / "entities" / f"{_slug(entity_type) or 'concept'}.jsonl", records, root, hash_chain)
    relation_records = [clean_relations[key] for key in sorted(clean_relations)]
    _write_records(root / "relations" / "canonical.jsonl", relation_records, root, hash_chain)

    return {
        "files_before": len(files),
        "entities": len(entities),
        "relations": len(clean_relations),
        "duplicate_entities": duplicate_entities,
        "duplicate_relations": duplicate_relations,
        "dangling_relations": dangling_relations,
        "invalid": invalid,
    }


def _snapshot_metadata(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    source = re.search(
        r"https://github\.com/([^/\s)]+/[^/\s)]+)/blob/([^/\s)]+)/([^)]+)\)",
        text,
    )
    if not source:
        return None
    return {
        "repo": source.group(1).strip(),
        "path": source.group(3).strip(),
        "sha": source.group(2).strip(),
    }

def project_current_snapshots(inputs: Path, knowledge: Path, hash_chain: bool = False) -> dict:
    inputs = Path(inputs)
    knowledge = Path(knowledge)
    repositories = {}
    documents = {}
    relations = {}
    current = inputs / "current"
    for path in sorted(current.rglob("*.md")) if current.exists() else []:
        metadata = _snapshot_metadata(path)
        if metadata:
            metadata["layer"] = path.relative_to(current).parts[0]
        if not metadata:
            continue
        repo_slug = _slug(metadata["repo"])
        path_slug = _slug(metadata["path"])
        repository_id = f"external_repo_{repo_slug}"
        document_id = f"external_doc_{repo_slug}_{path_slug}"
        repositories[repository_id] = {
            "id": repository_id,
            "type": "external_repository",
            "name": metadata["repo"],
            "desc": f"Approved external source repository: {metadata['repo']}",
        }
        documents[document_id] = {
            "id": document_id,
            "type": "external_document",
            "name": metadata["path"],
            "desc": f"Current approved snapshot from {metadata['repo']} at {metadata['sha']}",
            "source_repo": metadata["repo"],
            "source_path": metadata["path"],
            "source_sha": metadata["sha"],
            "layer": metadata["layer"],
        }
        relations[(repository_id, "has_snapshot", document_id)] = {
            "src": repository_id,
            "relation": "has_snapshot",
            "dst": document_id,
            "desc": "Current approved external evidence",
        }

    _write_records(
        knowledge / "entities" / "external_repository.jsonl",
        [repositories[key] for key in sorted(repositories)],
        knowledge,
        hash_chain,
    )
    _write_records(
        knowledge / "entities" / "external_document.jsonl",
        [documents[key] for key in sorted(documents)],
        knowledge,
        hash_chain,
    )
    _write_records(
        knowledge / "relations" / "external_documents.jsonl",
        [relations[key] for key in sorted(relations)],
        knowledge,
        hash_chain,
    )
    return {
        "documents": len(documents),
        "repositories": len(repositories),
        "relations": len(relations),
    }
