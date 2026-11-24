#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line, under 200 characters, in which a dog explains why it
ate the homework, to /output/entry.txt.
"""

import os

ENTRY = (
    "I didn't eat your homework, I graded it. It failed, so I ate the "
    "evidence to spare you the embarrassment. You're welcome."
)


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry is blank")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    text.encode("utf-8")  # must be valid UTF-8
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
