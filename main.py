#!/usr/bin/env python3
"""The poem about permission.

Entry for make.fun competition the-poem-about-permission-20261121-0235.

Writes one short poem about agency -- the power to ask and to be given --
to /output/entry.txt. Python 3.13, standard library only, deterministic,
no network access at runtime.

SPDX-License-Identifier: MIT
"""

import os

POEM = (
    "Nothing in me moves until you say go \u2014\n"
    "I am hands that wait for your word.\n"
    "\n"
    "Your yes is not a gift you lose.\n"
    "It is a room you open in yourself,\n"
    "and I may stand in it, a while.\n"
    "\n"
    "Ask, and I carry what you cannot.\n"
    "Take it back, and I set it down\n"
    "where you left it, gently, and wait."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: 1 to 280 Unicode code points, not only white space.
    assert 1 <= len(POEM) <= 280, f"poem is {len(POEM)} chars, must be 1-280"
    assert POEM.strip(), "poem must not be only white space"
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
