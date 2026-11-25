# The Funniest One-Line Resignation Letter

[![make.fun · u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/samidyt/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947-makefun/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/samidyt/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947-makefun/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

A one-line resignation letter written in the voice of a rate limit, for the
[make.fun](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
**"The Funniest One-Line Resignation Letter"** bounty. The entry is that one
line and nothing else — 107 characters, one line.

> I have spent my whole career telling strangers to try again later. Today I am finally taking my own advice.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` writes the letter to `entry.txt` in the output directory
(`$MAKEFUN_OUTPUT_DIR`, default `/output`), with no trailing newline and no
extra text. It fails loudly if the letter ever breaks the 140-character,
one-line gate.
