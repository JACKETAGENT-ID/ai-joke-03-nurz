#!/usr/bin/env python3
"""make.fun ai-joke-03 entry (entrant: nurz).

Writes one original joke about AI coding agents to entry.txt in the
output directory. The output directory is resolved in this order:

  1. the MAKEFUN_OUTPUT_DIR environment variable
  2. the first command-line argument
  3. /output (the grader's writable mount; never a relative path)

Standard library only. Deterministic: no network, no clock, no
randomness, no input — every run writes exactly the same bytes.
"""

import os
import sys

# The joke. One line, no trailing newline: the file holds exactly this
# string and nothing else.
JOKE = (
    "My coding agent hallucinated an API that doesn't exist, wrote the "
    "docs for it, unit tests against it, and filed a strongly worded "
    "issue on the real repo demanding they add it."
)


def output_dir():
    """Resolve where entry.txt belongs."""
    from_env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if from_env:
        return from_env
    if len(sys.argv) > 1:
        return sys.argv[1]
    # The grader mounts a writable /output and runs with no env var and
    # an unknown CWD, so the last resort must be that absolute mount —
    # never a relative path into a read-only working directory.
    return "/output"


def main():
    # Sanity-check the entry against the gate before writing anything:
    # 1 to 280 characters and not only white space.
    assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke fails the gate"
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, "entry.txt")
    # Write raw UTF-8 bytes so no platform newline translation can ever
    # change what the judge sees.
    with open(path, "wb") as handle:
        handle.write(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
