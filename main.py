#!/usr/bin/env python3
"""Entrypoint for make.fun bounty: The Funniest One-Line Resignation Letter.

Writes the one-line resignation letter of a rate limit to entry.txt
in the output directory ($MAKEFUN_OUTPUT_DIR, default /output).
"""

import os

LETTER = "I have spent my whole career telling strangers to try again later. Today I am finally taking my own advice."


def main() -> None:
    # Gate: the entry must be 1-140 characters, one line, not only whitespace.
    if not 1 <= len(LETTER) <= 140 or "\n" in LETTER or not LETTER.strip():
        raise SystemExit("entry violates the 140-character one-line gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exactly the line and nothing else: no trailing newline, no extra text.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    print(LETTER)


if __name__ == "__main__":
    main()
