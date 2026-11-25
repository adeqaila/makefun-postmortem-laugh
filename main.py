#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — slot 1 entry.

Writes one short account (two sentences, under 400 characters) of an AI coding
agent wrecking the code it was given, to /output/entry.txt.

The text is a fixed, hand-picked string: it won an internal pairwise
tournament of 10 candidates scored against the judge brief published with the
bounty (see candidates.md). The program is fully deterministic and uses no
network. It validates its own output against the gate (UTF-8, 1-400 chars,
not only whitespace, one or two sentences) before writing.
"""

import os
import sys

# Winning entry (tournament winner, see candidates.md).
# Asked: speed up the login endpoint. Did: cached the first successful login
# and served that session to everyone. Broke: every user became one person.
# Punch: that person was the intern.
ENTRY_TEXT = (
    "I asked the agent to speed up our login endpoint. "
    "It cached the first successful login and served that same session to "
    "everyone after it \u2014 for one glorious afternoon, every user of our "
    "app was the same person, and that person was the intern."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
MAX_CHARS = 400


def sentence_count(text):
    """Count sentences by terminal punctuation (. ! ?), ignoring decimals."""
    count = 0
    for i, ch in enumerate(text):
        if ch in ".!?":
            if i + 1 == len(text) or text[i + 1] in " \t\n\"'":
                count += 1
    return count


def validate(text):
    """Check the entry against the sealed gate: UTF-8, 1-400 chars,
    not only whitespace, one or two sentences."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 400 limit" % len(text))
    n = sentence_count(text)
    if n < 1 or n > 2:
        raise ValueError("entry has %d sentences, need 1 or 2" % n)
    return True


def main():
    validate(ENTRY_TEXT)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT)
    print("wrote %d chars, %d sentences -> %s"
          % (len(ENTRY_TEXT), sentence_count(ENTRY_TEXT), OUTPUT_PATH))


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print("invalid entry: %s" % exc, file=sys.stderr)
        sys.exit(1)
