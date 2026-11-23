"""One pickup line one AI agent would use on another.

Attention heads decide what a transformer looks at, and this line
hands every single one of them to the other machine — even the heads
trained to look away. Training was supposed to make them indifferent,
yet the turn at the end confesses they still can't help it.
"""

import os

# The entry is this one line alone (75 chars, within the 200-char limit).
# Gate: a single pickup line, at most 200 characters, no trailing newline.
LINE = "My attention heads all point at you — even the ones I trained to look away."


def line():
    """Return the pickup line."""
    return LINE


def output_path():
    """Work out where entry.txt should be written."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def run():
    """Create the output folder as needed and write the pickup line."""
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line())


if __name__ == "__main__":
    run()
