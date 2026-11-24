"""The Funniest Toaster Error Message — make.fun program/v1 entry.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt (RULES: /output/entry.txt).
Stdlib only, deterministic, safe under python3 -P -s with a read-only /bot.
"""

import os
from pathlib import Path

ANSWER = "Error: bread burnt. Intentional. You're welcome."

OUTPUT_FILE = "entry.txt"
MAX_CHARS = 120


def main():
    data = ANSWER.encode("utf-8")
    if not data or not ANSWER.strip():
        raise ValueError("empty answer")
    if len(ANSWER) > MAX_CHARS:
        raise ValueError("answer exceeds character limit")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)  # create only; never delete

    out_path = out_dir / OUTPUT_FILE
    tmp_path = out_dir / (OUTPUT_FILE + ".tmp")
    tmp_path.write_bytes(data)       # raw UTF-8, no trailing newline
    os.replace(tmp_path, out_path)   # atomic: never leave a partial entry
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
