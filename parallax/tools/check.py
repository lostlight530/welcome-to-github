from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "METHOD.md",
    "CASES.md",
    "NOTES.md",
    "records/2026-07.md",
    "templates/daily.md",
    "templates/weekly.md",
    "templates/monthly.md",
    "tools/check.py",
)
FORBIDDEN_SUFFIXES = {".db", ".jsonl", ".pyc", ".tmp"}
TEMPLATE_HEADINGS = {
    "templates/daily.md": ("## 研究问题", "## 证据", "## 反例", "## 复验条件", "## 指标"),
    "templates/weekly.md": ("## 覆盖区间", "## 重复信号", "## 冲突与漂移", "## 状态决定"),
    "templates/monthly.md": ("## 证据覆盖", "## 已复验发现", "## 失效记录", "## 有效速度"),
}


def validate() -> list[str]:
    errors: list[str] = []
    files = sorted(path for path in ROOT.rglob("*") if path.is_file())

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"forbidden artifact: {relative}")
        if "__pycache__" in path.parts:
            errors.append(f"forbidden cache: {relative}")
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"not utf-8: {relative}")
            continue
        if not text.strip():
            errors.append(f"empty file: {relative}")
        if chr(0x3002) in text:
            errors.append(f"forbidden punctuation: {relative}")
        local_scheme = "file:" + "//"
        if local_scheme in text.lower():
            errors.append(f"local link: {relative}")
        if re.search(r"\bv\d+(?:\.\d+)*\b", text, re.IGNORECASE):
            errors.append(f"version label: {relative}")

    for relative, headings in TEMPLATE_HEADINGS.items():
        path = ROOT / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for heading in headings:
            if heading not in text:
                errors.append(f"missing heading in {relative}: {heading}")

    record = ROOT / "records/2026-07.md"
    if record.is_file():
        text = record.read_text(encoding="utf-8")
        for heading in ("### 研究问题", "### 证据", "### 原始观测", "### 反例", "### 暂时结论", "### 复验条件"):
            if heading not in text:
                errors.append(f"missing record heading: {heading}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    count = sum(1 for path in ROOT.rglob("*") if path.is_file())
    print(f"OK parallax files={count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
