"""One-Line Roast: The Gadget You Use Every Day.

Writes exactly one roast line (at most 200 characters) to /output/entry.txt.
Python 3 standard library only.
"""

import os

ROAST = (
    "My laptop fan starts hyperventilating every time I open a "
    "spreadsheet, like the numbers are too heavy for it to lift."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
