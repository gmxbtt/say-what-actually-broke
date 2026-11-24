#!/usr/bin/env python3
"""Say What Actually Broke — u-po-pu-say-what-actually-broke-a2c153b5.

Writes one line of brutally honest error copy to /output/entry.txt.
The line names a real failure (a botched database migration), is funny
on a single read, and is copy a team could actually ship in an error
dialog.
"""

import os

ENTRY = (
    "The database is down because last night's migration renamed "
    "the users table to users_final_FINAL_v2. We're renaming it back."
)


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)  # exactly one line, no trailing newline


if __name__ == "__main__":
    main()
