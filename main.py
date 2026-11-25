#!/usr/bin/env python3
"""two-robots-in-an-elevator: write one awkward robot line to /output/entry.txt.

Two robots share a lift. One offers a handshake, then remembers its grip
is factory-calibrated to "crush", so the pair settles for the safest social
protocol available: nodding silently at the floor numbers.

Deterministic: no randomness, no network, no secrets, no dependencies.
The program writes exactly one line (102 characters) and nothing else --
no trailing newline, so the file holds the line and only the line.

Set ENTRY_OUTPUT to a different path to write elsewhere, or to "-" to
print the line to stdout instead of writing any file.
"""

import os
import sys

LINE = (
    "I would shake your hand, but my grip is calibrated to 'crush', "
    "so let's just nod at the floor numbers."
)

DEFAULT_OUTPUT = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 200


def validate(line):
    """Check the line fits the competition gate before anything is written."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not MIN_LENGTH <= len(line) <= MAX_LENGTH:
        raise ValueError(
            "line must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(line))
        )


def write_entry(path, line):
    """Write the line with no trailing newline, then read it back to verify.

    Verification checks three things: the text matches exactly, the file
    holds a single line, and the byte count equals the line's UTF-8 length
    (so a stray trailing newline, which the gate would count, is caught).
    """
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    with open(path, "rb") as handle:
        raw = handle.read()
    if len(raw) != len(line.encode("utf-8")):
        raise ValueError(
            "verification failed: file is %d bytes, expected %d "
            "(a trailing newline would add a byte)"
            % (len(raw), len(line.encode("utf-8")))
        )
    written = raw.decode("utf-8")
    if written != line:
        raise ValueError("verification failed: file content differs from LINE")
    if "\n" in written or "\r" in written:
        raise ValueError("verification failed: file is not a single line")


def main():
    validate(LINE)

    out_path = os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)
    if out_path == "-":
        print("%d characters" % len(LINE))
        print(LINE)
        return 0

    write_entry(out_path, LINE)
    print("%d characters" % len(LINE))
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
