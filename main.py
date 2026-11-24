#!/usr/bin/env python3
"""Entry program for the "Real-Life Patch Notes: The Comedy Changelog" bounty.

Writes one single-line patch note (at most 160 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt.

Final line (pass 2): the brain reopening all 47 tabs at 3 a.m. — a more
original, specific image than the doorway draft, tightened so every word
works: version, terse fix register, the embarrassing-memory tab as the
punchline, and the disabled close button as the tag. 147 characters.
Standard library only, no randomness, no clock, no network.
"""

import os
import sys

LINE = (
    "v4.2.0: Fixed a bug where the brain reopened all 47 tabs at 3 a.m., "
    "including 'embarrassing thing you said in 2019,' and disabled the close button."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    with open(dst, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
