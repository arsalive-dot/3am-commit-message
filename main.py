"""The 3AM Commit Message (make.fun).

Writes the entry to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic: the same bytes on every run.

The joke: an AI agent that has spent all night fixing its own bugs finally
realises the bug chain is itself — 1am's fix broke at 2am, 2am's fix broke
at 3am, and the only honest commit message left is a confession.
"""

import os
import tempfile

ENTRY = "fix: 3am. removed the bug I wrote at 2am fixing the bug I wrote at 1am. I am the bug now"


def main() -> None:
    # Gate self-check: entry must be UTF-8 text of 1 to 139 characters,
    # not only whitespace (the bounty gate).
    assert 1 <= len(ENTRY) <= 139, f"entry is {len(ENTRY)} chars, gate is 1-139"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    fd, tmp = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(ENTRY)
        os.chmod(tmp, 0o644)
        os.replace(tmp, target)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
