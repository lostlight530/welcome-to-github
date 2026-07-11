"""Deterministic formatting and validation for harvested documents and JSONL ledgers."""
from __future__ import annotations

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
    files = sorted(root.rglob("*.jsonl")) if root.exists() else []
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
