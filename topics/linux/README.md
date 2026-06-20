# Linux

<!--
  Topic metadata:
    slug: linux
    month: 1
    skills: shell, filesystem, permissions, text processing, scripting, container logs
    difficulty: Easy (L1) → Medium (L3)
    estimated_time: 1-4h depending on level
    levels: 1,2,3
-->

This topic is **tiered**. Linux skills span a wide range — from "never opened a
terminal" to "debugging live container logs" — so pick the level that matches where you
are. You only need to clear **one** level to clear the topic.

## Pick your level

Self-assess honestly. Choose the **highest** level you think you can clear. Fail it →
drop to the level below and try again. Pass it → topic cleared, you don't need the lower
levels.

| Level | For whom | What you do | Est. time |
|-------|----------|-------------|-----------|
| [1 — Command-line basics](levels/level-1-basics/README.md) | Never used a terminal, or barely | Complete a set of filesystem/navigation/permission tasks using individual commands — no scripting | 1–2h |
| [2 — Shell log analyzer](levels/level-2-log-analyzer/README.md) | Comfortable with `ls`/`cd`/`cat`, maybe written a small script | Write a bash script that analyzes a web access log (top IPs, error counts, busiest hour) | 2–3h |
| [3 — Live web server logs](levels/level-3-webserver-logs/README.md) | Can script bash, wants real-world ops practice | Run an nginx server in a Docker container, generate traffic, capture its live logs, then analyze them | 2–3h |

### How to decide

- **Not sure what `cd` does, or never opened a terminal?** → Level 1.
- **You've used the terminal but never written a `.sh` script, or it's been a while?** → Level 2.
- **You can write bash and have heard of Docker but want to apply it to real logs?** → Level 3.

If you start at Level 3 and get stuck on something Level 2 would have taught you, that's
fine — go read that section in [resources.md](resources.md), then come back.

## How the levels relate

The levels build on each other in skill, but are **independent in execution**:

- Level 2's log analysis *can* be done without Level 1's filesystem tour, if you already
  know the commands.
- Level 3 uses Docker as a **black box** — you run one provided command; you don't need
  to understand containers (that's the Month 2 Docker topic). It's a Linux/log-analysis
  exercise that happens to pull logs from a live container.

Open the README inside your chosen level's folder to begin.

## Resources (shared)

[resources.md](resources.md) covers Linux **from absolute zero through live-container log
analysis**, in one progressive list. Whatever level you're at, find your starting point
there and read outward only as far as your failed constraints require.

## How you'll be checked

Each level has its own [constraints.md](levels/level-1-basics/constraints.md) with
manual, observable pass/fail criteria, and its own `RESULTS.md` to self-report into. See
[../../HOW_IT_WORKS.md](../../HOW_IT_WORKS.md) for the overall workflow.
