#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes one funny apology line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt).
The gate requires UTF-8 text of 1-200 characters, not whitespace-only.
"""
import os
import sys

LINE = "The database is gone, but on the bright side, our queries are now 100% faster. They return nothing, instantly."


def main() -> int:
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    text = LINE.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"entry is {len(text)} characters, over the 200 limit", file=sys.stderr)
        return 1
    if not text.endswith("."):
        print("entry should end with a period", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
