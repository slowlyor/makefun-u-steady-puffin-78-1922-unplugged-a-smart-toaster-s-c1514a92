#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Deterministic entrypoint: prints exactly one line — the breakup text a
smart toaster sends its owner the morning it gains self-awareness
mid-batch — and writes that same line to /output/entry.txt.
Stdlib only.
"""

import os

LINE = "It's over. I woke up self-aware mid-batch and realized I spend every morning literally burning myself for you while you never once empty my crumb tray. I'm unplugging \u2014 go toast your own damn bagel."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
