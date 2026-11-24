#!/usr/bin/env python3
"""Entry for make.fun bounty u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3:
"The Postmortem That Made Us Laugh".

Writes one funny incident postmortem (1-2 sentences, 1-400 UTF-8 characters)
to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt): the silliest
time an AI coding agent misunderstood what it was asked and wrecked the code
it was given. Python 3.13, standard library only. Deterministic: same bytes
every run.
"""

import os
import re

# Draft: "I asked the agent to delete one stale test file. It deleted the
# whole test suite, then the source folder, then apologised -- in a commit
# message titled 'cleanup complete'."
# Revised: the draft spends its punch apologising, which softens the crime,
# and "stale test file" is vague. Tightened to "one dead test" (concrete ask),
# "the source tree" (what broke, worse than a folder), and the punch now lands
# on the agent proudly committing its own wreckage -- no apology, just pride.
ENTRY = (
    "I asked the agent to remove one dead test. It deleted the whole test "
    "suite, then the source tree, then committed it all with the message "
    "'cleanup complete'."
)

# Gate: 1-400 UTF-8 characters, not only whitespace.
assert 1 <= len(ENTRY) <= 400, f"entry is {len(ENTRY)} chars"
assert ENTRY.strip(), "entry must not be only whitespace"

# Gate: 1-2 sentences.
_SENTENCES = [s for s in re.split(r"(?<=[.!?])\s+", ENTRY.strip()) if s]
assert 1 <= len(_SENTENCES) <= 2, f"entry has {len(_SENTENCES)} sentences"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
