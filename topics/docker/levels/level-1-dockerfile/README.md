# Level 1 — Dockerfile Basics

<!--
  Level metadata:
    slug: docker/level-1-dockerfile
    skills: Dockerfile, FROM, COPY, RUN, EXPOSE, CMD, docker build, docker run
    difficulty: Medium
    estimated_time: 2-3h
    starter_mode: scratch
-->

## Prerequisites

You need **Docker** installed and running. See the [topic README](../../../README.md) for
installation instructions. **WSL2 required on Windows.**

### Verify

```bash
docker --version && docker run hello-world
```

The `hello-world` container should print a welcome message and exit.

## What to build

Containerize a simple Flask counter app by writing a **Dockerfile**. The starter code is a
minimal Flask app that counts page visits. You write the Dockerfile, build the image, and run
the container.

### The starter app

`starter/app.py` — a Flask app with two endpoints:
- `GET /` — returns "Hello! You are visitor #N" (increments a counter)
- `GET /health` — returns `{"status": "ok"}`

### Step-by-step

1. Copy the starter: `cp starter/app.py .`
2. Write a `Dockerfile` in this folder. The starter only has `app.py` (no
   `requirements.txt`), so you'll install Flask directly in the Dockerfile. Minimal shape:
   ```dockerfile
   FROM python:3.11-slim
   WORKDIR /app
   RUN pip install flask         # install Flask directly (no requirements.txt)
   COPY app.py .
   EXPOSE 5000
   CMD ["python", "app.py"]
   ```
   (This is a starting point — verify it builds and runs, then improve it per C6 best
   practices like a `.dockerignore`, non-root user, etc.)
3. Write a `.dockerignore` file to exclude unnecessary files.
4. Build the image: `docker build -t counter-app .`
5. Run the container: `docker run -d -p 5000:5000 counter-app`
6. Test: `curl http://localhost:5000/` and `curl http://localhost:5000/health`

### How to run

```bash
# Build
docker build -t counter-app .

# Run (detached)
docker run -d -p 5000:5000 --name counter counter-app

# Test
curl http://localhost:5000/
curl http://localhost:5000/health

# Clean up
docker stop counter && docker rm counter
docker rmi counter-app
```

## Why this matters

Docker is how every modern app is deployed. Whether you're running on AWS, Railway, or a
bare-metal server, your app runs inside a container. Writing a Dockerfile that's small,
secure, and correct is a daily skill at any tech company.

## Deliverables

- `Dockerfile` — builds the counter app image
- `.dockerignore` — excludes unnecessary files
- `app.py` — copied from starter (unmodified)
- Image builds and runs successfully

## Starter mode: `scratch` (Dockerfile only)

The starter `app.py` is provided. You write the Dockerfile and .dockerignore from scratch.
Do **not** modify `app.py`.

## How you'll be checked

Open [constraints.md](constraints.md). Each constraint is verified by running a Docker command
and observing the output. Self-report in [RESULTS.md](RESULTS.md). See
[../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the full workflow.

- All constraints pass → Level 1 cleared (and the whole Docker topic is cleared).
- Any constraint fails → study [../../../resources.md](../../../resources.md), fix, re-check.
