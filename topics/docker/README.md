# Docker

<!--
  Topic metadata:
    slug: docker
    month: 2
    skills: Dockerfile, docker build, docker run, docker compose, containers, images
    difficulty: Medium (L1) → Medium-Hard (L2)
    estimated_time: 2-3h per level
    levels: 1,2
-->

This topic is **tiered**. Docker skills span from "never written a Dockerfile" to "orchestrating
multi-container apps with compose" — so pick the level that matches where you are. You only
need to clear **one** level to clear the topic.

> **Note:** The Linux topic (Level 3) covers `docker run` as a tool for testing Linux behavior.
> This topic focuses on **writing Dockerfiles and compose files** — building your own containers.

## Pick your level

Self-assess honestly. Choose the **highest** level you think you can clear. Fail it →
drop to the level below and try again. Pass it → topic cleared, you don't need the lower
level.

| Level | For whom | What you do | Est. time |
|-------|----------|-------------|-----------|
| [1 — Dockerfile basics](levels/level-1-dockerfile/README.md) | Never written a Dockerfile, has used `docker run` | Write a Dockerfile to containerize a Flask app, build and run it | 2–3h |
| [2 — Docker Compose](levels/level-2-compose/README.md) | Written a basic Dockerfile, hasn't used compose | Write a multi-container app with Flask + Redis using docker compose | 2–3h |

### How to decide

- **Never written a `Dockerfile`, or don't know what `FROM` / `COPY` / `RUN` mean?** → Level 1.
- **You can write a Dockerfile but haven't used `docker compose` or connected multiple containers?** → Level 2.

If you start at Level 2 and get stuck on something Level 1 would have taught you, that's
fine — go read that section in [resources.md](resources.md), then come back.

## Prerequisites (all levels)

This topic needs **Docker** installed and running. **WSL2 is required on Windows** — see the
Linux topic (Level 3) for WSL2 setup if you haven't done it already.

### Docker

- **Verify:** `docker --version` prints a version number. Then `docker run hello-world` prints
  a welcome message and exits.
- **Windows:** Docker Desktop with WSL2 backend. Install Docker Desktop, enable WSL2
  integration in Settings → Resources → WSL Integration.
- **macOS:** Docker Desktop from <https://www.docker.com/products/docker-desktop/>.
- **Linux (Debian/Ubuntu):** `sudo apt install docker.io && sudo usermod -aG docker $USER`.
  Log out and back in for the group change to take effect.

### Terminal

- **Verify:** `docker info` shows Docker is running (no "Cannot connect" error).
- **Windows:** WSL2 (Ubuntu). **macOS/Linux:** default terminal.

### Get this repo

```bash
git clone <this-repo-url>   # the repo's web URL — see LEARNING_PATH.md if unclear
cd intern-onboarding/topics/docker
```

If any check fails, follow [SELF_HELP.md](../../SELF_HELP.md) before spending an hour on it — most issues solve fast with AI or a web search.

## How the levels relate

Level 1 teaches Dockerfile basics (FROM, COPY, RUN, EXPOSE, CMD). Level 2 builds on that
with multi-container orchestration using compose. Level 2 assumes you can write a Dockerfile.

Open the README inside your chosen level's folder to begin.

## Resources (shared)

[resources.md](resources.md) covers Docker **from absolute zero through compose**, in one
progressive list. Find your starting point there.

## How you'll be checked

Each level has its own [constraints.md](levels/level-1-dockerfile/constraints.md)
with manual, observable pass/fail criteria, and its own `RESULTS.md` to self-report into.
See [../../HOW_IT_WORKS.md](../../HOW_IT_WORKS.md) for the overall workflow.
