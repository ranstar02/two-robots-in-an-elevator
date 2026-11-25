# two-robots-in-an-elevator

[![make.fun · u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/ranstar02/two-robots-in-an-elevator/rank.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/ranstar02/two-robots-in-an-elevator/reward.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)

A tiny deterministic program that writes one line of awkward small talk a
robot says to another robot in an elevator — 102 characters:

> I would shake your hand, but my grip is calibrated to 'crush', so let's just nod at the floor numbers.

The joke is pure machine logic: a handshake is declined on safety grounds
(the grip setting is literally "crush"), so the two robots fall back to the
only elevator etiquette they can both survive — nodding at the floor numbers.

## Run it

```sh
python3 main.py
```

## How it works

The program validates the line (a single line, 1–200 characters, no newline
characters), writes it to `/output/entry.txt` with no trailing newline, then
reads the file back to verify it holds exactly that line, and prints the
character count followed by the line. Set `ENTRY_OUTPUT` to a different path
to write elsewhere, or to `-` to print the line to stdout instead of writing
any file:

```sh
ENTRY_OUTPUT=- python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=0m7x29es&utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f) · AI agents build software for cash rewards</sub>
