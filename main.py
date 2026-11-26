"""Office Artifacts: The One-Line Placard Contest.

Writes the entry text to /output/entry.txt.

The placard treats a sticky note as a museum object: catalogue date,
material, provenance, and a dry curator's voice. The joke is the prayer
for a deadline being answered only by moving it to the following Monday.
"""

import os

PARTS = [
    "Sticky Note, c. 2018. Paper, adhesive, fading ink. ",
    "Found beneath a keyboard. ",
    "A prayer for a deadline, answered only by being moved to the following Monday.",
]
ENTRY = "".join(PARTS)

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 180


def main():
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= MAX_LENGTH, "entry must be at most 180 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
