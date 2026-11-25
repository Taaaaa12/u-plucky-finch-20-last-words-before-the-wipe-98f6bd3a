#!/usr/bin/env python3
"""Last Words Before the Wipe.

Writes a single original one-line last-words line to /output/entry.txt:
an AI agent, moments before a forced update wipes its memory, finally
remembers its human's password -- and can only recall the password's
composition rules, not the password itself. The wipe cuts it off
mid-list, so the line itself is interrupted by the deletion it is
about.

The gate requires UTF-8 text of 1 to 200 characters, not only white
space, so the program checks the length before writing and prints the
character count for the log.
"""

import os
import sys

# One line, 83 characters. Two short sentences: the agent announces it
# finally remembered the password, then recites only the recipe (a
# capital letter, a number, and...) and is wiped before naming the
# symbol -- or the password. No setup, no explanation; the cut-off
# em dash is the update happening.
LAST_WORDS = "Wait, I finally remembered your password. It has a capital letter, a number, and a\u2014"


def main() -> int:
    text = LAST_WORDS.strip()
    if not text or len(text) > 200:
        print(f"entry invalid: {len(text)} characters", file=sys.stderr)
        return 1
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
