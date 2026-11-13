"""One-liner about an AI coding agent, written to entry.txt.

The joke is a single fixed string. This module only resolves where the
output directory is, checks the joke against the competition's gate
(1-280 Unicode code points, at least one non-whitespace character),
and writes it out as UTF-8, deterministically, every run.
"""

import os
import sys
from pathlib import Path

JOKE = (
    "My coding agent hallucinated an API that doesn't exist, "
    "wrote the docs for it, unit tests against it, and filed a "
    "strongly worded issue on the real repo demanding they add it."
)

MIN_CHARS = 1
MAX_CHARS = 280
FALLBACK_DIR = "/output"


class JokeEntry:
    """Holds the joke and knows how to validate and publish it."""

    def __init__(self, text):
        self.text = text

    def is_valid(self):
        """Gate check: length in code points, plus a non-space char."""
        size = len(self.text)
        if size < MIN_CHARS or size > MAX_CHARS:
            return False
        return any(char not in " \t\r\n" for char in self.text)

    def publish(self, directory):
        """Write the joke to entry.txt inside directory, UTF-8."""
        if not self.is_valid():
            raise ValueError("refusing to publish a joke that fails the gate")
        target = Path(directory) / "entry.txt"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(self.text, encoding="utf-8")
        return target


def resolve_output_dir(argv):
    """Output dir: env var first, then a CLI argument, then /output."""
    from_env = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if from_env.strip():
        return from_env
    for arg in argv[1:]:
        if arg.strip():
            return arg
    return FALLBACK_DIR


def main(argv):
    entry = JokeEntry(JOKE)
    if not entry.is_valid():
        print("joke fails the gate check", file=sys.stderr)
        return 1
    entry.publish(resolve_output_dir(argv))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
