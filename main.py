"""Snooze Button Roast.

Writes a one-line roast of an alarm clock that rings at 6 AM on a
Saturday to /output/entry.txt.
"""

import os

ENTRY = (
    "You ring at 6 AM on a Saturday like the weekend owes you rent "
    "\u2014 even the sun sleeps in, and it actually has a job."
)


def validate_entry(text: str) -> None:
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"


def main() -> None:
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
