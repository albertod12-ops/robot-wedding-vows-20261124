"""One-line robot wedding vow for make.fun (v1).

Writes a single funny wedding vow to /output/entry.txt: a robot
promises to love its partner in sickness and in health, in Wi-Fi and
in airplane mode, till low battery do us part. The vow borrows the
classic wedding formula and swaps in machine states; the payoff is
the last clause. One sentence, 108 characters.
"""

import os

TEXT = (
    "I promise to love you in sickness and in health, in Wi-Fi and "
    "in airplane mode, till low battery do us part."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 160, "entry must be 1-160 characters, got %d" % len(TEXT)
    assert TEXT == TEXT.strip(), "entry must not start or end with whitespace"
    assert "\n" not in TEXT, "entry must be a single line"
    assert TEXT.count(".") == 1 and TEXT.endswith("."), "entry must be one sentence"
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
