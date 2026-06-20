# Level 2 — Docker Compose

<!--
  Level metadata:
    slug: docker/level-2-compose
    skills: docker compose, multi-container, services, networking, volumes, Redis
    difficulty: Medium-Hard
    estimated_time: 2-3h
    starter_mode: scratch
-->

## Prerequisites

You need **Docker** installed and running (including compose). You should be comfortable with
Dockerfile basics (Level 1 skills). See the [topic README](../../../README.md) for installation.
**WSL2 required on Windows.**

### Verify

```bash
docker --version && docker compose version
```

Both should print version numbers. Modern Docker includes compose as a plugin.

## What to build

Write a multi-container app using **docker compose**: a Flask web app that stores its counter
in **Redis** instead of in-memory. This teaches you how containers communicate and how to
add a database/cache as a service.

### Architecture

Two containers:
- **web**: Flask app (you write the app and its Dockerfile)
- **redis**: official Redis image (pull from Docker Hub)

The Flask app connects to Redis at hostname `redis` (compose creates a DNS entry) and uses
Redis to store the visit counter. When Redis restarts, the counter should persist (use a
volume).

### The starter

`starter/app.py` — a Flask skeleton with Redis TODOs. You complete the Redis integration.

### Step-by-step

1. Copy the starter: `cp starter/app.py .`
2. Complete the Flask app:
   - Install the `redis` Python package (add it to your Dockerfile's `pip install`, or
     create a `requirements.txt` with `flask` and `redis`).
   - Connect to Redis at `redis:6379`. **Why `redis` as the hostname?** Docker Compose
     creates a DNS entry for each service name, so the `web` container can reach the
     `redis` container by the name `redis`. (This is the key compose concept — if you use
     `localhost` it will FAIL because each container has its own localhost.)
   - `GET /` — increment a Redis counter key and return "Hello! You are visitor #N"
     (the Redis command is `r.incr("visit_count")`).
   - `GET /health` — return `{"status": "ok", "redis": "connected"}` (ping Redis with
     `r.ping()` to verify the connection).
3. Write `Dockerfile` for the Flask app.
4. Write `docker-compose.yml` with two services:
   - `web`: build from your Dockerfile, port 5000, depends on redis
   - `redis`: image `redis:alpine`, volume for data persistence
5. Build and run: `docker compose up --build`
6. Test: `curl http://localhost:5000/` multiple times — counter should increment.

### How to run

```bash
# Build and start both containers
docker compose up --build

# Test (in another terminal)
curl http://localhost:5000/
curl http://localhost:5000/
curl http://localhost:5000/health

# Stop
docker compose down

# Stop and remove volumes
docker compose down -v
```

## Why this matters

Real apps have multiple services: a web server, a database, a cache, a queue. Docker compose
lets you define and run all of them together with a single command. Understanding how
containers communicate (networking) and persist data (volumes) is essential for deploying
any multi-service application.

## Deliverables

- `app.py` — Flask app with Redis integration
- `Dockerfile` — for the Flask app
- `docker-compose.yml` — defines both services
- `requirements.txt` — Python dependencies (flask, redis)
- Both containers running and communicating

## Starter mode: `scratch` (Dockerfile + compose)

The starter `app.py` has a Flask skeleton with Redis TODOs. You complete the app, write the
Dockerfile, and write the docker-compose.yml.

## How you'll be checked

Open [constraints.md](constraints.md). Each constraint is verified by running a command and
observing the output. Self-report in [RESULTS.md](RESULTS.md). See
[../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the full workflow.

- All constraints pass → Level 2 cleared (and the whole Docker topic is cleared).
- Any constraint fails → study [../../../resources.md](../../../resources.md), fix, re-check.
