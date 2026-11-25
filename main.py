"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes one short text to $MAKEFUN_OUTPUT_DIR/entry.txt: a single number
in digits and nothing else, the honest count of browser tabs open.
"""

import os

ENTRY_TEXT = "173"
# Why 173: a specific, odd, non-round count in the heavy-hoarder range.
# It reads as a real, counted total (not a round guess like 100 or 200),
# surprising next to a mundane dozen, yet believable as an honest answer
# -- not an absurd shock figure -- and it hints at a life of tabs kept
# open "to read later" that never get closed.


def resolve_output_dir():
    """Return the output directory, honouring MAKEFUN_OUTPUT_DIR."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        return output_dir
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")


def validate(text):
    """Enforce the competition gate: 1-5 chars, ASCII digits only."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 5:
        raise ValueError("entry must be 1 to 5 characters")
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if not all("0" <= ch <= "9" for ch in text):
        raise ValueError("entry must be ASCII digits only")
    return text


def main():
    text = validate(ENTRY_TEXT)
    output_dir = resolve_output_dir()
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Write exactly the digits, no trailing newline: the file must be
    # byte-for-byte the entry, 3 bytes for "173".
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and re-validate so a bad write can never slip through.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    validate(written)
    if written != text:
        raise ValueError("entry.txt does not match the validated entry")


if __name__ == "__main__":
    main()
