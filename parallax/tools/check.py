from __future__ import annotations

import re
import sys
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "METHOD.md",
    "CASES.md",
    "NOTES.md",
    "audits/README.md",
    "records/2026-07.md",
    "specials/README.md",
    "templates/daily.md",
    "templates/special.md",
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
SPECIAL_HEADINGS = DAILY_HEADINGS
AUDIT_HEADINGS = (
    "## 审计信息",
    "## 覆盖区间",
    "## 纳入记录",
    "## 覆盖情况",
    "## 重复信号",
    "## 冲突与漂移",
    "## 特殊专题维护",
    "## 反例检查",
    "## 状态决定",
    "## 下一阶段控制项",
    "## 验证结果",
)
TEMPLATE_HEADINGS = {
    "templates/daily.md": DAILY_HEADINGS,
    "templates/special.md": SPECIAL_HEADINGS,
    "templates/weekly.md": AUDIT_HEADINGS,
    "templates/monthly.md": (
        "## 覆盖区间",
        "## 记录构成",
        "## 证据覆盖",
        "## 已复验发现",
        "## 候选与观察",
        "## 失效记录",
        "## 有效速度",
    ),
}
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
URL_PATTERN = re.compile(r"https?://[^\s)]+")
DAILY_PATTERN = re.compile(r"^records/(\d{4}-\d{2})/(\d{4}-\d{2}-\d{2})\.md$")
SPECIAL_PATTERN = re.compile(
    r"^specials/(\d{4}-\d{2})/(\d{4}-\d{2}-\d{2})-[a-z0-9-]+\.md$"
)
AUDIT_PATTERN = re.compile(r"^audits/(\d{4}-W\d{2})\.md$")
RECORD_ID_PATTERN = re.compile(r"^- 记录 ID:\s*(\S+)\s*$", re.MULTILINE)
NOTE_PATTERN = re.compile(r"^## (N-\d+).*?(?=^## |\Z)", re.MULTILINE | re.DOTALL)
NOTE_SUPPORT_PATTERN = re.compile(r"PX-(?:S-)?\d{8}-P\d+")


HISTORICAL_MONTHLY_PATTERN = re.compile(
    r'^## (\d{4}-\d{2}-\d{2})\s*\n(.*?)(?=^## |\Z)',
    re.MULTILINE | re.DOTALL,
)


def metadata(text: str, label: str) -> list[str]:
    return re.findall(rf"^- {re.escape(label)}:\s*(.+?)\s*$", text, re.MULTILINE)


def parse_single_date(
    text: str, label: str, relative: str, errors: list[str]
) -> date | None:
    values = metadata(text, label)
    if len(values) != 1:
        errors.append(f"{label} count is {len(values)}: {relative}")
        return None
    try:
        return date.fromisoformat(values[0])
    except ValueError:
        errors.append(f"invalid {label}: {relative} -> {values[0]}")
        return None


def validate_local_links(path: Path, text: str, errors: list[str]) -> None:
    for target in LINK_PATTERN.findall(text):
        target = target.split("#", 1)[0]
        if not target or target.startswith(("https://", "http://", "#")):
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            errors.append(
                f"link escapes parallax: {path.relative_to(ROOT).as_posix()} -> {target}"
            )
            continue
        if not resolved.exists():
            errors.append(
                f"broken local link: {path.relative_to(ROOT).as_posix()} -> {target}"
            )


def read_labeled_count(
    text: str, source: str, label: str, errors: list[str]
) -> int | None:
    matches = re.findall(rf"^- {re.escape(label)}:\s*(\d+)\s*$", text, re.MULTILINE)
    if len(matches) != 1:
        errors.append(f"{source} {label} count is {len(matches)}")
        return None
    return int(matches[0])


def validate() -> list[str]:
    errors: list[str] = []
    files = sorted(path for path in ROOT.rglob("*") if path.is_file())
    record_windows: dict[str, date] = {}
    historical_record_windows: dict[str, date] = {}
    daily_dates: list[date] = []
    topic_windows: list[date] = []
    daily_files: list[Path] = []
    special_files: list[Path] = []
    audit_files: list[Path] = []
    audit_record_refs: dict[str, set[str]] = {}
    cases_path = ROOT / "CASES.md"
    cases_text = cases_path.read_text(encoding="utf-8") if cases_path.is_file() else ""

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    monthly_files = sorted((ROOT / "records").glob("????-??.md"))
    if not monthly_files:
        errors.append("missing monthly record")

    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        if path.is_symlink():
            errors.append(f"symlink not allowed: {relative}")
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
        prose = URL_PATTERN.sub("", text)
        if re.search(
            r"\bParallax(?:\s+(?:version|release|版本))?\s+v\d+(?:\.\d+)*\b",
            prose,
            re.IGNORECASE,
        ):
            errors.append(f"version label: {relative}")
        for phrase in PUBLIC_FORBIDDEN:
            if phrase in text:
                errors.append(f"forbidden public phrase in {relative}: {phrase}")
        validate_local_links(path, text, errors)

        daily_match = DAILY_PATTERN.fullmatch(relative)
        special_match = SPECIAL_PATTERN.fullmatch(relative)
        audit_match = AUDIT_PATTERN.fullmatch(relative)
        if daily_match:
            daily_files.append(path)
            file_date_text = daily_match.group(2)
            try:
                file_date = date.fromisoformat(file_date_text)
                daily_dates.append(file_date)
            except ValueError:
                errors.append(f"invalid daily date: {relative}")
                continue
            if daily_match.group(1) != file_date_text[:7]:
                errors.append(f"daily record in wrong month: {relative}")
            if metadata(text, "记录类型") != ["每日专题"]:
                errors.append(f"daily record type mismatch: {relative}")
            assigned = parse_single_date(text, "上海归属日期", relative, errors)
            executed = parse_single_date(text, "实际执行日期", relative, errors)
            window = parse_single_date(text, "独立时间窗口", relative, errors)
            if assigned and assigned != file_date:
                errors.append(f"daily assigned date mismatch: {relative}")
            if executed and window and executed != window:
                errors.append(f"daily execution window mismatch: {relative}")
            if window:
                topic_windows.append(window)
            expected_monthly = ROOT / "records" / f"{file_date_text[:7]}.md"
            if expected_monthly.is_file() and path.name not in expected_monthly.read_text(
                encoding="utf-8"
            ):
                errors.append(f"daily record missing from monthly index: {relative}")
            for heading in DAILY_HEADINGS:
                if heading not in text:
                    errors.append(f"missing daily heading in {relative}: {heading}")
            ids = RECORD_ID_PATTERN.findall(text)
            if len(ids) != 1:
                errors.append(f"daily record ID count is {len(ids)}: {relative}")
            else:
                record_id = ids[0]
                expected_prefix = f"PX-{file_date_text.replace('-', '')}-P"
                if not re.fullmatch(r"PX-\d{8}-P\d+", record_id):
                    errors.append(f"invalid daily record ID: {relative} -> {record_id}")
                elif not record_id.startswith(expected_prefix):
                    errors.append(f"daily record ID date mismatch: {relative} -> {record_id}")
                if expected_monthly.is_file():
                    monthly_text = expected_monthly.read_text(encoding="utf-8")
                    if record_id not in monthly_text:
                        errors.append(f"daily record ID missing from monthly index: {record_id}")
                case_ids = metadata(text, "案例 ID")
                if len(case_ids) != 1 or f"## {case_ids[0]} " not in cases_text:
                    errors.append(f"daily case reference mismatch: {relative}")
                elif path.name not in cases_text:
                    errors.append(f"daily record missing from CASES: {relative}")
                if window:
                    if record_id in record_windows:
                        errors.append(f"duplicate record ID: {record_id}")
                    record_windows[record_id] = window

        if special_match:
            special_files.append(path)
            event_date_text = special_match.group(2)
            try:
                event_date = date.fromisoformat(event_date_text)
            except ValueError:
                errors.append(f"invalid special event date: {relative}")
                continue
            if special_match.group(1) != event_date_text[:7]:
                errors.append(f"special record in wrong month: {relative}")
            if metadata(text, "记录类型") != ["特殊专题"]:
                errors.append(f"special record type mismatch: {relative}")
            recorded_event = parse_single_date(text, "事件日期", relative, errors)
            verified = parse_single_date(text, "实际核验日期", relative, errors)
            window = parse_single_date(text, "独立时间窗口", relative, errors)
            if recorded_event and recorded_event != event_date:
                errors.append(f"special event date mismatch: {relative}")
            if verified and window and verified != window:
                errors.append(f"special execution window mismatch: {relative}")
            if window:
                topic_windows.append(window)
            special_index = ROOT / "specials" / "README.md"
            if special_index.is_file() and path.name not in special_index.read_text(
                encoding="utf-8"
            ):
                errors.append(f"special record missing from special index: {relative}")
            monthly = ROOT / "records" / f"{event_date_text[:7]}.md"
            if monthly.is_file() and path.name not in monthly.read_text(encoding="utf-8"):
                errors.append(f"special record missing from monthly index: {relative}")
            for heading in SPECIAL_HEADINGS:
                if heading not in text:
                    errors.append(f"missing special heading in {relative}: {heading}")
            ids = RECORD_ID_PATTERN.findall(text)
            if len(ids) != 1:
                errors.append(f"special record ID count is {len(ids)}: {relative}")
            else:
                record_id = ids[0]
                expected_prefix = f"PX-S-{event_date_text.replace('-', '')}-P"
                if not re.fullmatch(r"PX-S-\d{8}-P\d+", record_id):
                    errors.append(f"invalid special record ID: {relative} -> {record_id}")
                elif not record_id.startswith(expected_prefix):
                    errors.append(f"special record ID date mismatch: {relative} -> {record_id}")
                if special_index.is_file():
                    special_text = special_index.read_text(encoding="utf-8")
                    if record_id not in special_text:
                        errors.append(f"special record ID missing from special index: {record_id}")
                if monthly.is_file() and record_id not in monthly.read_text(encoding="utf-8"):
                    errors.append(f"special record ID missing from monthly index: {record_id}")
                case_ids = metadata(text, "案例 ID")
                if len(case_ids) != 1 or f"## {case_ids[0]} " not in cases_text:
                    errors.append(f"special case reference mismatch: {relative}")
                elif path.name not in cases_text:
                    errors.append(f"special record missing from CASES: {relative}")
                if window:
                    if record_id in record_windows:
                        errors.append(f"duplicate record ID: {record_id}")
                    record_windows[record_id] = window

        if audit_match:
            audit_files.append(path)
            period = audit_match.group(1)
            if metadata(text, "记录类型") != ["周期审计"]:
                errors.append(f"audit record type mismatch: {relative}")
            audit_ids = metadata(text, "审计 ID")
            expected_audit_id = f"PA-{period}"
            if audit_ids != [expected_audit_id]:
                errors.append(
                    f"audit ID mismatch: {relative} -> {', '.join(audit_ids)}"
                )
            parse_single_date(text, "审计日期", relative, errors)
            for heading in AUDIT_HEADINGS:
                if heading not in text:
                    errors.append(f"missing audit heading in {relative}: {heading}")
            audit_index = ROOT / "audits" / "README.md"
            if audit_index.is_file() and path.name not in audit_index.read_text(
                encoding="utf-8"
            ):
                errors.append(f"audit missing from audit index: {relative}")
            audit_record_refs[relative] = set(NOTE_SUPPORT_PATTERN.findall(text))

    for monthly_path in monthly_files:
        monthly_relative = monthly_path.relative_to(ROOT).as_posix()
        monthly_text = monthly_path.read_text(encoding='utf-8')
        for match in HISTORICAL_MONTHLY_PATTERN.finditer(monthly_text):
            section_date_text = match.group(1)
            section = match.group(0)
            ids = RECORD_ID_PATTERN.findall(section)
            if not ids:
                continue
            if len(ids) != 1:
                errors.append(
                    f'historical monthly record ID count is {len(ids)}: '
                    f'{monthly_relative}#{section_date_text}'
                )
                continue
            record_id = ids[0]
            expected_prefix = 'PX-' + section_date_text.replace('-', '') + '-P'
            if not re.fullmatch(r'PX-\d{8}-P\d+', record_id):
                errors.append(f'invalid historical record ID: {record_id}')
                continue
            if not record_id.startswith(expected_prefix):
                errors.append(f'historical record ID date mismatch: {record_id}')
            window = parse_single_date(
                section,
                '独立时间窗口',
                f'{monthly_relative}#{section_date_text}',
                errors,
            )
            executed = parse_single_date(
                section,
                '实际执行日期',
                f'{monthly_relative}#{section_date_text}',
                errors,
            )
            if executed and window and executed != window:
                errors.append(f'historical execution window mismatch: {record_id}')
            case_ids = metadata(section, '案例 ID')
            if len(case_ids) != 1 or f'## {case_ids[0]} ' not in cases_text:
                errors.append(f'historical case reference mismatch: {record_id}')
            if window:
                if record_id in record_windows or record_id in historical_record_windows:
                    errors.append(f'duplicate record ID: {record_id}')
                historical_record_windows[record_id] = window

    if daily_dates:
        ordered_dates = sorted(daily_dates)
        present_dates = set(ordered_dates)
        cursor = ordered_dates[0]
        while cursor <= ordered_dates[-1]:
            if cursor not in present_dates:
                errors.append(f"missing daily record in date chain: {cursor.isoformat()}")
            cursor += timedelta(days=1)
        if len(ordered_dates) != len(present_dates):
            errors.append("duplicate daily assigned date")

        readme_path = ROOT / "README.md"
        if readme_path.is_file():
            readme = readme_path.read_text(encoding="utf-8")
            latest = metadata(readme, "最新每日归属日期")
            if len(latest) != 1:
                errors.append(f"README latest daily date count is {len(latest)}")
            elif latest[0] != ordered_dates[-1].isoformat():
                errors.append(
                    "README latest daily date mismatch: "
                    f"{latest[0]} != {ordered_dates[-1].isoformat()}"
                )
            daily_count = read_labeled_count(readme, "README", "每日专题", errors)
            special_count = read_labeled_count(readme, "README", "特殊专题", errors)
            batch_count = read_labeled_count(readme, "README", "当前专题研究批次", errors)
            window_count = read_labeled_count(
                readme, "README", "当前专题独立执行日期窗口", errors
            )
            if daily_count is not None and daily_count != len(daily_files):
                errors.append(
                    f"README daily count mismatch: {daily_count} != {len(daily_files)}"
                )
            if special_count is not None and special_count != len(special_files):
                errors.append(
                    f"README special count mismatch: {special_count} != {len(special_files)}"
                )
            expected_batches = len(daily_files) + len(special_files)
            if batch_count is not None and batch_count != expected_batches:
                errors.append(
                    f"README topic batch count mismatch: {batch_count} != {expected_batches}"
                )
            expected_windows = len(set(topic_windows))
            if window_count is not None and window_count != expected_windows:
                errors.append(
                    f"README topic window count mismatch: {window_count} != {expected_windows}"
                )
            audit_count = read_labeled_count(readme, "README", "周期审计", errors)
            if audit_count is not None and audit_count != len(audit_files):
                errors.append(
                    f"README audit count mismatch: {audit_count} != {len(audit_files)}"
                )

    for monthly_path in monthly_files:
        month = monthly_path.stem
        monthly_text = monthly_path.read_text(encoding="utf-8")
        month_daily = [path for path in daily_files if path.parent.name == month]
        month_special = [path for path in special_files if path.parent.name == month]
        source = monthly_path.relative_to(ROOT).as_posix()
        daily_count = read_labeled_count(monthly_text, source, "每日专题", errors)
        special_count = read_labeled_count(monthly_text, source, "特殊专题", errors)
        batch_count = read_labeled_count(
            monthly_text, source, "当前专题研究批次", errors
        )
        window_count = read_labeled_count(
            monthly_text, source, "当前专题独立执行日期窗口", errors
        )
        if daily_count is not None and daily_count != len(month_daily):
            errors.append(
                f"monthly daily count mismatch: {daily_count} != {len(month_daily)}"
            )
        if special_count is not None and special_count != len(month_special):
            errors.append(
                f"monthly special count mismatch: {special_count} != {len(month_special)}"
            )
        expected_batches = len(month_daily) + len(month_special)
        if batch_count is not None and batch_count != expected_batches:
            errors.append(
                f"monthly topic batch count mismatch: {batch_count} != {expected_batches}"
            )
        month_windows = {
            record_windows[record_id]
            for record_id in record_windows
            if record_id[3:9] == month.replace("-", "")
            or record_id[5:11] == month.replace("-", "")
        }
        if window_count is not None and window_count != len(month_windows):
            errors.append(
                f"monthly topic window count mismatch: {window_count} != {len(month_windows)}"
            )
    for relative, headings in TEMPLATE_HEADINGS.items():
        path = ROOT / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for heading in headings:
            if heading not in text:
                errors.append(f"missing heading in {relative}: {heading}")

    for audit_relative, references in audit_record_refs.items():
        if not references:
            errors.append(f"audit has no research record references: {audit_relative}")
        for reference in references:
            if (
                reference not in record_windows
                and reference not in historical_record_windows
            ):
                errors.append(
                    f"audit references missing record {reference}: {audit_relative}"
                )

    notes_path = ROOT / "NOTES.md"
    if notes_path.is_file():
        notes = notes_path.read_text(encoding="utf-8")
        for match in NOTE_PATTERN.finditer(notes):
            note_id = match.group(1)
            section = match.group(0)
            supports = set(NOTE_SUPPORT_PATTERN.findall(section))
            if len(supports) < 3:
                errors.append(f"long-term note has fewer than three support records: {note_id}")
            windows: set[date] = set()
            for support in supports:
                if support in record_windows:
                    windows.add(record_windows[support])
                elif support in historical_record_windows:
                    windows.add(historical_record_windows[support])
                else:
                    errors.append(
                        f"long-term note references missing record {support}: {note_id}"
                    )
            if len(windows) < 2:
                errors.append(f"long-term note has fewer than two time windows: {note_id}")
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
    daily = sum(1 for path in ROOT.rglob("*.md") if DAILY_PATTERN.fullmatch(path.relative_to(ROOT).as_posix()))
    special = sum(1 for path in ROOT.rglob("*.md") if SPECIAL_PATTERN.fullmatch(path.relative_to(ROOT).as_posix()))
    audits = sum(1 for path in ROOT.rglob("*.md") if AUDIT_PATTERN.fullmatch(path.relative_to(ROOT).as_posix()))
    print(
        f"OK parallax files={count} daily_topics={daily} "
        f"special_topics={special} audits={audits}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
