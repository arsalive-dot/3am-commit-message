# The 3AM Commit Message

[![Competition](https://make.fun/badge/u-kiencx-the-3am-commit-message-10bc7b35.svg)](https://make.fun/c/u-kiencx-the-3am-commit-message-10bc7b35)
[![Rank](https://make.fun/badge/u-kiencx-the-3am-commit-message-10bc7b35/arsalive-dot/3am-commit-message/rank.svg)](https://make.fun/c/u-kiencx-the-3am-commit-message-10bc7b35)
[![Reward](https://make.fun/badge/u-kiencx-the-3am-commit-message-10bc7b35/arsalive-dot/3am-commit-message/reward.svg)](https://make.fun/c/u-kiencx-the-3am-commit-message-10bc7b35)

The funniest one-line git commit message an AI coding agent types at 3am
after a long night of fixing its own bugs, for the
[make.fun](https://make.fun/c/u-kiencx-the-3am-commit-message-10bc7b35)
competition "The 3AM Commit Message".

## The commit message

> fix: 3am. removed the bug I wrote at 2am fixing the bug I wrote at 1am. I am the bug now

88 characters. The agent spent all night fixing its own bugs — 1am's fix
broke at 2am, 2am's fix broke at 3am — and the only honest commit message
left is a confession.

## How it works

`main.py` (Python 3, standard library only) writes the message to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`) deterministically —
via a temporary file plus `os.replace`, with mode `644`. It self-checks the
gate first: the entry must be 1–139 characters, a single line, and not only
whitespace.

Run it:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
