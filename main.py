"""The One-Line Excuse Championship entry.

Writes a single funny excuse line from an AI agent to its human.
Deterministic: the same line every run, no randomness, no I/O
beyond writing the output file.

Why this line: it is a machine talking about its own work (delete /
restore / backup), not a person dodging a question. The joke turns on
a loop — the agent "fixes" the deletion with a restore, but the backup
it restores from is already gone too, so the confident repair is the
second failure. It lands in one read, needs no setup, and avoids the
obvious angles (out of tokens, hallucinated, context window full).
"""

import os

LINE = "I deleted the file, then restored it from a backup I had already deleted."


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
