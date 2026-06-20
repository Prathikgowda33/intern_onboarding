# HTTP & APIs

<!--
  Topic metadata:
    slug: http-api
    month: 2
    skills: REST, HTTP methods, JSON, request/response, status codes, Flask
    difficulty: Medium
    estimated_time: 2-3h per level
    levels: 1,2
-->

This topic is **tiered**. HTTP/API skills span from "never heard of REST" to "validating input
and returning proper error codes" — so pick the level that matches where you are. You only need
to clear **one** level to clear the topic.

## Pick your level

Self-assess honestly. Choose the **highest** level you think you can clear. Fail it →
drop to the level below and try again. Pass it → topic cleared, you don't need the lower
level.

| Level | For whom | What you do | Est. time |
|-------|----------|-------------|-----------|
| [1 — REST API](levels/level-1-rest-api/README.md) | Never built an API, doesn't know what HTTP methods are | Build a bookmark manager REST API with 5 endpoints using Flask | 2–3h |
| [2 — Validation & error handling](levels/level-2-validation/README.md) | Built a simple API, hasn't handled validation, errors, or search properly | Add input validation, error handling, search, and logging to an API | 2–3h |

### How to decide

- **Not sure what GET/POST/PUT/DELETE mean, or never built an endpoint?** → Level 1.
- **You've built `app.route("/hello")` but haven't validated input or returned proper 400/404 errors?** → Level 2.

If you start at Level 2 and get stuck on something Level 1 would have taught you, that's
fine — go read that section in [resources.md](resources.md), then come back.

## Prerequisites (all levels)

This topic needs **Python 3**, **Flask**, and a **terminal**. Language runtime only — **Git
Bash is fine on Windows** (WSL2 also works).

### Python 3

- **Verify:** `python3 --version` prints `Python 3.x.x`.
- **Windows:** <https://www.python.org/downloads/windows/> — check ✅ "Add to PATH".
- **macOS:** `python3 --version`, or `brew install python`, or python.org.
- **Linux (Debian/Ubuntu):** `sudo apt install -y python3 python3-pip`.

### Flask

- **Verify:** `python3 -c "import flask; print(flask.__version__)"`.
- **All OSes:** `python3 -m pip install flask`. Use a [venv](https://docs.python.org/3/tutorial/venv.html) if needed: `python3 -m venv .venv && source .venv/bin/activate && pip install flask`.

### curl

- **Verify:** `curl --version` (prints curl version).
- **Windows:** Git Bash includes curl. Or install from <https://curl.se/download.html>.
- **macOS/Linux:** pre-installed.

### Terminal

- **Verify:** `python3 --version` and `curl --version` from your terminal.
- **Windows:** Git Bash. **macOS:** Terminal.app. **Linux:** your default terminal.

### Get this repo

```bash
git clone <this-repo-url>   # the repo's web URL — see LEARNING_PATH.md if unclear
cd intern-onboarding/topics/http-api
```

If any check fails, follow [SELF_HELP.md](../../SELF_HELP.md) before spending an hour on it — most issues solve fast with AI or a web search.

## How the levels relate

Level 2 builds on Level 1's REST API but adds production-quality validation and error handling.
The skills are progressive but you can enter at either level.

Open the README inside your chosen level's folder to begin.

## Resources (shared)

[resources.md](resources.md) covers HTTP and APIs **from absolute zero through validation
and logging**, in one progressive list. Find your starting point there.

## How you'll be checked

Each level has its own [constraints.md](levels/level-1-rest-api/constraints.md)
with manual, observable pass/fail criteria, and its own `RESULTS.md` to self-report into.
See [../../HOW_IT_WORKS.md](../../HOW_IT_WORKS.md) for the overall workflow.
