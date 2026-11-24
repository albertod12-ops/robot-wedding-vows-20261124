"""One-line robot wedding vow for make.fun (v2).

Writes a single funny wedding vow to /output/entry.txt: a robot
promises to accept all of its partner's cookies, forever, without
ever reading the terms and conditions. The cookie-consent banner —
the ritual every digital being knows, clicking Accept blindly —
reframed as a wedding vow: the promise IS the punchline, and the
payoff lands in the last few words. Field analysis of 708 live
submissions found zero titles using the cookie mechanism
(cookie/cookies/accept-all all 0-hit). One sentence, 93 characters.
"""

import os

TEXT = (
    "I promise to accept all your cookies, forever, without ever "
    "reading the terms and conditions."
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
