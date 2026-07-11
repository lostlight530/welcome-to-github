"""Idempotent entrypoint for the human-readable report renderer."""
import sys
from pathlib import Path

from report_hygiene_core import main


def already_formatted(mode, memories):
    pattern = "*-quantitative-dashboard.md" if mode == "welcome" else "*-cognitive-report.md"
    files = sorted(Path(memories).glob(pattern))
    if not files:
        return False
    first_line = files[-1].read_text(encoding="utf-8").splitlines()[0]
    return first_line in {"# 每日认知仪表盘", "# 每日认知报告"}


if __name__ == "__main__":
    if len(sys.argv) == 3 and already_formatted(sys.argv[1], sys.argv[2]):
        print("formatted=0")
    else:
        main()
