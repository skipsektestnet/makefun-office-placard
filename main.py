"""Office Artifacts: The One-Line Placard Contest: writes the entry text to /output/entry.txt.

Why this line: a sticky note recast as a ritual object, a prayer for a deadline.
The label craft is complete (catalogue date, material, provenance), the voice is
a dry curator's, and the punch lands on the deadline being moved to Monday.
"""

import os

# The entry itself: one line, 155 characters, the prayer is both the conceit and the punch.
ENTRY = "Sticky Note, c. 2018. Paper, adhesive, fading ink. Found beneath a keyboard. A prayer for a deadline, answered only by being moved to the following Monday."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    assert 1 <= len(ENTRY) <= 180, "entry must be 1-180 characters"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
