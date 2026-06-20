# Testing

<!--
  Topic metadata:
    slug: testing
    month: 1
    skills: pytest, unit testing, mocking, test design, edge cases, test-driven thinking
    difficulty: Medium
    estimated_time: 2-3h per level
    levels: 1,2
-->

This topic is **tiered**. Testing skills span from "never written a test" to "mocking
external dependencies and writing integration tests" — so pick the level that matches where you
are. You only need to clear **one** level to clear the topic.

## Pick your level

Self-assess honestly. Choose the **highest** level you think you can clear. Fail it →
drop to the level below and try again. Pass it → topic cleared, you don't need the lower
level.

| Level | For whom | What you do | Est. time |
|-------|----------|-------------|-----------|
| [1 — Unit testing](levels/level-1-unit-testing/README.md) | Never written a test, or doesn't know what pytest is | Fix bugs in a calculator module by writing tests that expose them, then fix the code to make all tests pass | 2–3h |
| [2 — Mocking & integration](levels/level-2-mocking-integration/README.md) | Comfortable writing unit tests, hasn't mocked external APIs | Write tests for a module that calls external HTTP APIs using mocks, plus a small integration test | 2–3h |

### How to decide

- **Never used `pytest`, or don't know what an assertion is?** → Level 1.
- **You can write `assert x == 5` but haven't used `unittest.mock` or tested code that calls external services?** → Level 2.

If you start at Level 2 and get stuck on something Level 1 would have taught you, that's
fine — go read that section in [resources.md](resources.md), then come back.

## Prerequisites (all levels)

This topic needs **Python 3** and **pytest**, plus a **terminal**. Language runtime only —
**Git Bash is fine on Windows** (WSL2 also works).

### Python 3

- **Verify:** `python3 --version` prints `Python 3.x.x`.
- **Windows:** <https://www.python.org/downloads/windows/> — check ✅ "Add to PATH".
- **macOS:** `python3 --version`, or `brew install python`, or python.org.
- **Linux (Debian/Ubuntu):** `sudo apt install -y python3 python3-pip`.

### pytest

- **Verify:** `pytest --version` prints a version number. If not installed:
- **All OSes:** `python3 -m pip install pytest`. On Linux/macOS you may need a
  [venv](https://docs.python.org/3/tutorial/venv.html): `python3 -m venv .venv && source .venv/bin/activate && pip install pytest`.

### Terminal

- **Verify:** `python3 --version` and `pytest --version` from your terminal.
- **Windows:** Git Bash, or WSL2. **macOS:** Terminal.app. **Linux:** your default terminal.

### Get this repo

```bash
git clone <this-repo-url>   # the repo's web URL — see LEARNING_PATH.md if unclear
cd intern-onboarding/topics/testing
```

If any check fails, follow [SELF_HELP.md](../../SELF_HELP.md) before spending an hour on it — most issues solve fast with AI or a web search.

## How the levels relate

Level 2 builds on Level 1's pytest skills (assertions, fixtures, parametrize) but adds
mocking and external dependency handling. The skills are progressive but you can enter at
either level.

Open the README inside your chosen level's folder to begin.

## Resources (shared)

[resources.md](resources.md) covers testing **from absolute zero through mocking and
integration**, in one progressive list. Find your starting point there.

## How you'll be checked

Each level has its own [constraints.md](levels/level-1-unit-testing/constraints.md)
with manual, observable pass/fail criteria, and its own `RESULTS.md` to self-report into.
See [../../HOW_IT_WORKS.md](../../HOW_IT_WORKS.md) for the overall workflow.
