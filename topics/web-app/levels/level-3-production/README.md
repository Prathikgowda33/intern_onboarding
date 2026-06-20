# Level 3 — Production-Ready

<!--
  Level metadata:
    slug: web-app/level-3-production
    skills: Docker, input validation, error handling, loading states, multi-container
    difficulty: Hard
    estimated_time: 3-4h
    starter_mode: scratch
-->

## Prerequisites

You need **Python 3**, **Flask**, **Node.js**, **npm**, and **Docker**. You should have
completed Level 2's skills (React + Flask API) or equivalent. See the [topic README](../../../README.md)
for installation. **Docker requires WSL2 on Windows** — see the Linux topic for WSL2 setup.

### Verify

```bash
python3 --version && node --version && docker --version
```

## What to build

Take the guestbook app from Level 2 and make it **production-ready**: add input validation
on the backend, error handling on both frontend and backend, loading states in React, and
Dockerize the entire stack with `docker compose`.

### New requirements beyond Level 2

1. **Backend validation:**
   - `name` must be non-empty, max 100 characters
   - `message` must be non-empty, max 500 characters
   - Return 400 with JSON error for invalid input

2. **Error handling:**
   - Backend: custom 404 handler, 500 handler, structured JSON errors
   - Frontend: error boundary component that catches React crashes
   - Frontend: display API errors to the user (network failure, 4xx, 5xx)

3. **Loading states:**
   - Frontend shows a loading indicator while fetching entries
   - Frontend disables the submit button and shows a spinner while posting

4. **Docker:**
   - `Dockerfile` for the Flask backend
   - `Dockerfile` for the React frontend (build stage + nginx serve)
   - `docker-compose.yml` that starts both containers
   - App accessible at `http://localhost:3000` via nginx

### Step-by-step

1. Build the Flask API with validation and error handling.
2. Build the React app with error boundary, error display, and loading states.
3. Create `backend/Dockerfile` (Python image, install deps, run app).
4. Create `frontend/Dockerfile` (Node build stage, copy dist to nginx image).
5. Create `docker-compose.yml` (two services: backend + frontend).
6. Run `docker compose up --build` and test at `http://localhost:3000`.

### How to run

```bash
docker compose up --build
# Open http://localhost:3000 in your browser
# When done: docker compose down
```

## Why this matters

This is how you ship real apps. Docker ensures your app works the same on your laptop, in CI,
and in production. Input validation prevents bad data from corrupting your database. Error
handling prevents a single crash from taking down the whole user experience. These are the
skills that separate a prototype from a product.

## Deliverables

- `backend/` — Flask API with validation and error handling
- `frontend/` — React app with error boundary, loading states, error display
- `backend/Dockerfile` and `frontend/Dockerfile`
- `docker-compose.yml`
- App running via `docker compose up`

## Starter mode: `scratch`

No starter code. Build on your Level 2 code or start fresh.

## How you'll be checked

Open [constraints.md](constraints.md). Each constraint is verified by running commands and
observing output. Self-report in [RESULTS.md](RESULTS.md). See
[../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the full workflow.

- All constraints pass → Level 3 cleared (and the whole Web App topic is cleared).
- Any constraint fails → study [../../../resources.md](../../../resources.md), fix, re-check.
