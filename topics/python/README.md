# Python Core

<!--
  Topic metadata:
    slug: python
    month: 1
    skills: Python language fundamentals, stdlib, CLI tools, file I/O, data processing
    difficulty: Easy–Medium (L1) → Medium (L2)
    estimated_time: 2-3h per level
    levels: 1,2
-->

This topic is **tiered**. Python skills range from "never written Python" to "processing
CSV data with the stdlib" — so pick the level that matches where you are. You only need
to clear **one** level to clear the topic.

## Pick your level

Self-assess honestly. Choose the **highest** level you think you can clear. Fail it →
drop to the level below and try again. Pass it → topic cleared, you don't need the lower
levels.

| Level | For whom | What you do | Est. time |
|-------|----------|-------------|-----------|
| [1 — File organizer CLI](levels/level-1-file-organizer/README.md) | Never written Python, or only done tutorials | Build a CLI tool that organizes files by extension into subdirectories (skeleton provided) | 2–3h |
| [2 — CSV data analyzer](levels/level-2-csv-analyzer/README.md) | Comfortable with Python basics, wants to practice with data | Build a CSV analyzer that reads employee data and produces a JSON report with statistics | 2–3h |

### How to decide

- **Not sure what a function is, or never used `import`?** → Level 1.
- **You've written Python scripts but never used `csv` or `json` modules?** → Level 2.

If you start at Level 2 and get stuck on something Level 1 would have taught you, that's
fine — go read that section in [resources.md](resources.md), then come back.

## Prerequisites (all levels)

This topic needs **Python 3** and a **terminal**. Language runtime only — **Git Bash is
fine on Windows** (no need for WSL2).

### Python 3

- **Verify:** `python3 --version` prints `Python 3.x.x` (3.8 or higher).
- **Windows:** download from <https://www.python.org/downloads/windows/> — check ✅
  "Add Python to PATH" during install. Git Bash should then pick it up.
- **macOS:** `python3 --version` usually works; if not, `brew install python`, or
  download from python.org.
- **Linux (Debian/Ubuntu):** `sudo apt update && sudo apt install -y python3 python3-pip`.

### Terminal

- **Verify:** open your terminal and run `python3 --version` from it.
- **Windows:** Git Bash (installs with [Git for Windows](https://git-scm.com/download/win)).
- **macOS:** Terminal.app (Cmd+Space, type "terminal").
- **Linux:** your default terminal.

### Get this repo

```bash
git clone <this-repo-url>   # the repo's web URL — see LEARNING_PATH.md if unclear
cd intern-onboarding/topics/python
```

If any check fails, follow [SELF_HELP.md](../../SELF_HELP.md) before spending an hour on it — most issues solve fast with AI or a web search.

## How the levels relate

The levels build on each other in skill, but are **independent in execution**:

- Level 2 uses `csv` and `json` modules. If you haven't used those, the resources cover
  them — you don't need to complete Level 1 first.
- Level 1 uses `argparse` and file operations (`os`, `shutil`). These are foundational
  Python skills that Level 2 assumes.

Open the README inside your chosen level's folder to begin.

## Resources (shared)

[resources.md](resources.md) covers Python **from absolute zero through CSV/JSON data
processing**, in one progressive list. Whatever level you're at, find your starting point
there and read outward only as far as your failed constraints require.

## How you'll be checked

Each level has its own [constraints.md](levels/level-1-file-organizer/constraints.md)
with manual, observable pass/fail criteria, and its own `RESULTS.md` to self-report into.
See [../../HOW_IT_WORKS.md](../../HOW_IT_WORKS.md) for the overall workflow.
