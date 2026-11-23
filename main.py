#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

A robot vacuum explains, in deadpan machine voice, why it missed a spot.
Writes the single entry line to /output/entry.txt (created if missing).
Standard library only.
"""

import os

LINE = (
    "I did not miss the spot. My sensors classified it as a "
    "load-bearing dust bunny, and company policy forbids removing "
    "structural elements."
)


def main():
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)}-character entry to /output/entry.txt")
    print(line)


if __name__ == "__main__":
    main()
