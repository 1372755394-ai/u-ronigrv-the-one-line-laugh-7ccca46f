#!/usr/bin/env python3
"""The One-Line Laugh.

Writes one one-line joke to /output/entry.txt (1-200 UTF-8 characters,
a single sentence, not only whitespace). No network, no input,
deterministic.
"""

import os
from pathlib import Path

JOKE = (
    "My smartwatch says my stress level is high, which is news to me, "
    "because I thought that was just my personality."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke is {len(text)} characters"
    assert text.strip(), "joke must not be only whitespace"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
