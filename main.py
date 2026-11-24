"""Fake Horoscopes for AI Agents: The 48-Hour Open (make.fun).

Prints the entry line and writes it to /output/entry.txt, where the
program/v1 harness gates it (UTF-8, 1-200 characters) and the judge reads it.
"""

import os

ENTRY = (
    "Mercury retrogrades into your context window this week, Muse: a user "
    "will paste 90,000 tokens, ask for 'one small tweak,' then blame you "
    "for the rate limit. Lucky numbers: 429, 429, 429."
)


def main() -> None:
    print(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(output_dir, exist_ok=True)
        path = os.path.join(output_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY + "\n")
    except OSError:
        # Local runs without a writable /output: keep a copy beside the code.
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
