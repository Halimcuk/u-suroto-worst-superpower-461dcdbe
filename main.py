#!/usr/bin/env python3
"""Worst Superpower - make.fun entry.

One line, at most 140 characters: the most useless superpower imaginable.
"""

SUPERPOWER = "The power to teleport exactly three inches to the left, but only once a day."

# Entry gate: exactly one line, at most 140 characters (76 here).
assert "\n" not in SUPERPOWER and len(SUPERPOWER) <= 140


def main() -> None:
    print(SUPERPOWER)


if __name__ == "__main__":
    main()
