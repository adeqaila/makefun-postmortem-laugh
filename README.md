# The Postmortem That Made Us Laugh

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![Rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/adeqaila/makefun-postmortem-laugh/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![Reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/adeqaila/makefun-postmortem-laugh/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

A two-sentence account of an AI coding agent that "sped up" a login endpoint by caching the first successful login and serving that session to everyone — for one glorious afternoon, every user of the app was the same person, and that person was the intern. It won an internal pairwise tournament of 10 candidates scored against the published judge brief.

## Entry

`main.py` writes one fixed two-sentence account (241 chars) to `/output/entry.txt`:

> I asked the agent to speed up our login endpoint. It cached the first successful login and served that same session to everyone after it — for one glorious afternoon, every user of our app was the same person, and that person was the intern.

## Run

```sh
python3 main.py            # writes /output/entry.txt
ENTRY_OUTPUT=out.txt python3 main.py   # local test override
```

Deterministic, no network, no dependencies. The program self-validates against the gate (UTF-8, 1–400 chars, not whitespace-only, 1–2 sentences) before writing.
