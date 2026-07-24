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
    "templates/daily.md",
    "templates/weekly.md",
    "templates/monthly.md",
    "tools/check.py",
)
FORBIDDEN_SUFFIXES = {
    ".db",
    ".jsonl",
    ".lock",
    ".pyc",
    ".sqlite",
    ".sqlite3",
    ".tmp",
}
FORBIDDEN_DIRS = {"__pycache__", ".cache", "cache"}
PUBLIC_FORBIDDEN = (
    "完整任务" + " Prompt",
    "选题" + "权重",
    "私人" + " SOP",
    "内部" + "推理",
    "用户" + "信息",
)
DAILY_HEADINGS = (
    "## 记录信息",
    "## 研究摘要",
    "## 研究问题",
    "## 可证伪假设",
    "## 历史背景",
    "## 证据矩阵",
    "## 控制条件",
    "## 实验设计",
    "## 原始观测",
    "## 试验比较",
    "## 历史比较",
    "## 指标结果",
    "## 反例检查",
    "## 暂时结论",
    "## 历史关系",
    "## 复验条件",
    "## 验证结果",
)
TEMPLATE_HEADINGS = {
    "templates/daily.md": DAILY_HEADINGS,
    "templates/weekly.md": ("## 覆盖区间", "## 重复信号", "## 冲突与漂移", "## 状态决定"),
    "templates/monthly.md": ("## 证据覆盖", "## 已复验发现", "## 失效记录", "## 有效速度"),
}
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
DATE_FILE_PATTERN = re.compile(r"^(\d{4}-\d{2}-\d{2})\.md$")
RECORD_ID_PATTERN = re.compile(r"^- 记录 ID:\s*(\S+)\s*$", re.MULTILINE)
NOTE_PATTERN = re.compile(r"^## (N-\d+).*?(?=^## |\Z)", re.MULTILINE | re.DOTALL)
NOTE_SUPPORT_PATTERN = re.compile(r"PX-\d{8}-P\d+")


def validate_local_links(path: Path, text: str, errors: list[str]) -> None:
    for target in LINK_PATTERN.findall(text):
        target = target.split("#", 1)[0]
        if not target or target.startswith(("https://", "http://", "#")):
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            errors.append(f"link escapes parallax: {path.relative_to(ROOT).as_posix()} -> {target}")
            continue
        if not resolved.exists():
            errors.append(f"broken local link: {path.relative_to(ROOT).as_posix()} -> {target}")


def validate() -> list[str]:
    errors: list[str] = []
    files = sorted(path for path in ROOT.rglob("*") if path.is_file())
    record_ids: dict[str, str] = {}

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    monthly_files = sorted((ROOT / "records").glob("????-??.md"))
    if not monthly_files:
        errors.append("missing monthly record")

    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"forbidden artifact: {relative}")
        if any(part.lower() in FORBIDDEN_DIRS for part in path.parts):
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
        if "file:" + "//" in text.lower():
            errors.append(f"local scheme: {relative}")
        if re.search(r"\bv\d+(?:\.\d+)*\b", text, re.IGNORECASE):
            errors.append(f"version label: {relative}")
        for phrase in PUBLIC_FORBIDDEN:
            if phrase in text:
                errors.append(f"forbidden public phrase in {relative}: {phrase}")
        validate_local_links(path, text, errors)

        date_match = DATE_FILE_PATTERN.match(path.name)
        if path.parent.parent.name == "records" and date_match:
            expected_month = date_match.group(1)[:7]
            if path.parent.name != expected_month:
                errors.append(f"daily record in wrong month: {relative}")
            if f"- 上海日期: {date_match.group(1)}" not in text:
                errors.append(f"daily date mismatch: {relative}")
            for heading in DAILY_HEADINGS:
                if heading not in text:
                    errors.append(f"missing daily heading in {relative}: {heading}")
            ids = RECORD_ID_PATTERN.findall(text)
            if len(ids) != 1:
                errors.append(f"daily record ID count is {len(ids)}: {relative}")
            elif ids[0] in record_ids:
                errors.append(f"duplicate record ID {ids[0]}: {record_ids[ids[0]]}, {relative}")
            else:
                record_ids[ids[0]] = relative
            monthly = ROOT / "records" / f"{expected_month}.md"
            if monthly.is_file() and path.name not in monthly.read_text(encoding="utf-8"):
                errors.append(f"daily record missing from monthly index: {relative}")

    for relative, headings in TEMPLATE_HEADINGS.items():
        path = ROOT / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for heading in headings:
            if heading not in text:
                errors.append(f"missing heading in {relative}: {heading}")

    notes_path = ROOT / "NOTES.md"
    if notes_path.is_file():
        notes = notes_path.read_text(encoding="utf-8")
        for match in NOTE_PATTERN.finditer(notes):
            note_id = match.group(1)
            section = match.group(0)
            supports = set(NOTE_SUPPORT_PATTERN.findall(section))
            if len(supports) < 3:
                errors.append(f"long-term note has fewer than three support records: {note_id}")
            windows = {support[3:11] for support in supports}
            if len(windows) < 2:
                errors.append(f"long-term note has fewer than two time windows: {note_id}")
            for support in supports:
                if support not in record_ids:
                    errors.append(f"long-term note references missing record {support}: {note_id}")
            if "### 反例检查" not in section:
                errors.append(f"long-term note missing counterexample check: {note_id}")
            if "失效条件" not in section:
                errors.append(f"long-term note missing invalidation condition: {note_id}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    count = sum(1 for path in ROOT.rglob("*") if path.is_file())
    daily = sum(1 for path in (ROOT / "records").glob("????-??/????-??-??.md"))
    print(f"OK parallax files={count} daily_records={daily}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
