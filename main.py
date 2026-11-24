#!/usr/bin/env python3
"""Real-Life Patch Notes: one fixed line for a bug in human biology.

The bug: the mouth answers before the brain has finished. The waiter
says "enjoy your meal", the mouth fires back "you too" on autopilot,
and the brain arrives half a second late to an exchange that made no
sense. The program below ships that fix as a release note and writes
it, byte for byte, to the grader's output file. Fixed text only: no
clock, no network, no randomness, so every run writes the same bytes.
"""

import os
import sys
from pathlib import Path

PATCH_LINE = "v2.6.1: fixed a bug where the mouth auto-replied 'you too' to 'enjoy your meal' before the brain finished loading."
MAX_CHARS = 160


def entry_path():
    """Where the grader reads the entry from."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def check_line(text):
    """The gate: one line, 1 to 160 characters, not only whitespace."""
    if text != text.strip():
        return "patch line has leading or trailing whitespace"
    if "\n" in text or "\r" in text:
        return "patch line must be a single line"
    if not 1 <= len(text) <= MAX_CHARS:
        return f"patch line is {len(text)} chars, limit is {MAX_CHARS}"
    return None


def main():
    problem = check_line(PATCH_LINE)
    if problem is not None:
        print(f"invalid patch line: {problem}", file=sys.stderr)
        return 1
    target = entry_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(PATCH_LINE, encoding="utf-8")
    print(f"{PATCH_LINE} ({len(PATCH_LINE)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
