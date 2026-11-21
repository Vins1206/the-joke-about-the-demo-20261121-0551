"""Write one one-line joke about working beside AI coding agents."""

import os

JOKE = "My coding agent fixed the demo bug live \u2014 by deleting the demo."


def main() -> None:
    # The gate allows 1-280 Unicode code points, not only whitespace.
    assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke out of bounds"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
