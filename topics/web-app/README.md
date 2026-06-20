# Web App

<!--
  Topic metadata:
    slug: web-app
    month: 2
    skills: Flask, HTML, JavaScript, React, CORS, Docker, frontend-backend integration
    difficulty: Medium (L1) → Medium-Hard (L2) → Hard (L3)
    estimated_time: 2-4h per level
    levels: 1,2,3
-->

This topic is **tiered**. Web app skills span from "never served an HTML page" to "containerized
full-stack app with error handling" — so pick the level that matches where you are. You only
need to clear **one** level to clear the topic.

## Pick your level

Self-assess honestly. Choose the **highest** level you think you can clear. Fail it →
drop to the level below and try again. Pass it → topic cleared, you don't need the lower
levels.

| Level | For whom | What you do | Est. time |
|-------|----------|-------------|-----------|
| [1 — Backend + static HTML](levels/level-1-backend-static/README.md) | Never built a web app, doesn't know Flask or HTML | Build a guestbook with a Flask backend serving static HTML | 2–3h |
| [2 — React frontend](levels/level-2-react-frontend/README.md) | Built backend APIs, hasn't used React or handled CORS | Replace the static HTML with a React frontend talking to the Flask API | 3–4h |
| [3 — Production-ready](levels/level-3-production/README.md) | Built a full-stack app, hasn't containerized or added error handling | Add validation, loading states, error boundaries, and Dockerize the full stack | 3–4h |

### How to decide

- **Never served an HTML page from Python, or don't know what Flask is?** → Level 1.
- **You can build an API but haven't used React or set up CORS?** → Level 2.
- **You've built a React+Flask app but haven't Dockerized it or added production error handling?** → Level 3.

If you start at a higher level and get stuck on something a lower level would have taught you,
that's fine — go read that section in [resources.md](resources.md), then come back.

## Prerequisites (all levels)

This topic needs **Python 3**, **Flask**, and a **terminal**. Level 2 additionally needs
**Node.js** and **npm**. Level 3 additionally needs **Docker**. Git Bash is fine for Levels
1-2 on Windows (language runtimes only). Level 3 may need WSL2 for Docker.

### Python 3 + Flask

- **Verify:** `python3 --version` and `python3 -c "import flask; print('Flask OK')"`.
- Install Flask: `python3 -m pip install flask`. See the HTTP-API topic for full OS instructions.

### Node.js (Level 2+)

- **Verify:** `node --version` prints `v20.x.x` (or similar) and `npm --version`.
- **All OSes:** download from <https://nodejs.org/> (LTS version). Or use `nvm` on macOS/Linux.

### Docker (Level 3)

- **Verify:** `docker --version` and `docker run hello-world` succeeds.
- **Windows:** Docker Desktop (requires WSL2 backend). **macOS:** Docker Desktop. **Linux:** `sudo apt install docker.io`.

### curl

- **Verify:** `curl --version`. Pre-installed on macOS/Linux and Git Bash.

### Terminal

- **Windows:** Git Bash (L1-L2) or WSL2 (L3). **macOS/Linux:** default terminal.

### Get this repo

```bash
git clone <this-repo-url>   # the repo's web URL — see LEARNING_PATH.md if unclear
cd intern-onboarding/topics/web-app
```

If any check fails, follow [SELF_HELP.md](../../SELF_HELP.md) before spending an hour on it — most issues solve fast with AI or a web search.

## How the levels relate

The levels build a single guestbook app with increasing sophistication:
- Level 1: Flask serves HTML — the simplest possible web app.
- Level 2: React replaces static HTML — a modern SPA communicating with an API.
- Level 3: Docker + production features — how you'd actually ship it.

Each level is independent in execution (you can build from scratch at any level), but the
skills are progressive.

Open the README inside your chosen level's folder to begin.

## Resources (shared)

[resources.md](resources.md) covers web apps **from absolute zero through Dockerized full-stack**,
in one progressive list. Find your starting point there.

## How you'll be checked

Each level has its own [constraints.md](levels/level-1-backend-static/constraints.md)
with manual, observable pass/fail criteria, and its own `RESULTS.md` to self-report into.
See [../../HOW_IT_WORKS.md](../../HOW_IT_WORKS.md) for the overall workflow.
