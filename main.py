"""Write the one-line AI excuse for breaking production to entry.txt."""

import hashlib
import os
from pathlib import Path

LINE = "The good news: I found the bug in 0.3 seconds. The bad news: I found it by running it on every paying customer first."


def output_path() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out")) / "entry.txt"


def validate() -> None:
    data = output_path().read_bytes()
    assert not data.endswith(b"\n"), "trailing newline"
    assert data.count(b"\n") == 0, "must be a single line"
    text = data.decode("utf-8")
    assert 1 <= len(text) <= 180, "length out of range"
    assert text == text.strip(), "leading/trailing whitespace"
    assert text == LINE, "content mismatch"


def main() -> None:
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(LINE.encode("utf-8"))
    validate()
    print(
        f"wrote {path} ({len(LINE)} chars, "
        f"sha256={hashlib.sha256(LINE.encode('utf-8')).hexdigest()})"
    )


if __name__ == "__main__":
    main()
