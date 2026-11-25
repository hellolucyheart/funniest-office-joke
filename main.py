#!/usr/bin/env python3
"""The Funniest Office Joke: one short line about office life.

The entry is one sentence of at most 200 characters, written to
``/output/entry.txt`` -- the one path the grader reads. The gate checks
that file is UTF-8 text of 1 to 200 characters and not only whitespace,
so the program validates its own line before writing it, and writes the
exact text with no trailing newline and nothing else in the file.

The joke is built on a detail anyone who has worked in an office
recognises: the lift that has been broken for so long it became
furniture. The setup states the broken elevator and the plant
facilities put inside it; the turn reframes that dead space as the
office's best meeting room, because it is the only one with natural
light. The punchline lands last, in one sentence, with nothing left
to explain. The line as written is 134 characters long, verified by
running the program twice locally and checking the file it wrote.

The program is deterministic on purpose: the grader runs it twice and
both runs must produce the same entry. It reads nothing from the
network, the environment (beyond the output directory the grader
itself sets), or the git history -- the joke lives in this file, and
this file alone.
"""

from __future__ import annotations

import os
import sys

# One original line about office life: the elevator that has been
# "out of order" for so long it grew a plant, and what it became.
JOKE = (
    "The elevator has been 'out of order' so long that facilities "
    "put a plant in it, and now it's the only meeting room with "
    "natural light."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 200


def check_line(line: str) -> str:
    """Return the line when it meets the contest gate, else fail loudly.

    The gate is the brief itself: one sentence, 1 to 200 characters,
    no line breaks, nothing but the joke.
    """
    text = line.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.endswith(".") or text.count(".") != 1:
        raise ValueError("entry must be exactly one sentence")
    return text


def main() -> int:
    text = check_line(JOKE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
