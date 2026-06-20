# Level 1 — First Deploy

<!--
  Level metadata:
    slug: deployment/level-1-first-deploy
    skills: Railway.app, environment variables, Docker deployment, public URL
    difficulty: Medium
    estimated_time: 2-3h
    starter_mode: skeleton
-->

## Prerequisites

You need a **GitHub account**, a **Railway.app account** (free trial tier), and **Git**. See
the [topic README](../../../README.md) for setup.

> **Heads up on Railway's trial:** Railway offers a free trial with a small credit (≈$5),
> but **requires a credit/GitHub-backed card to verify** (to prevent abuse). You won't be
> charged during the trial, and a tiny Flask app costs pennies to run. If you can't add a
> card, ask your instructor/program whether an alternative host (Fly.io, Render) is
> acceptable — the concepts transfer.

### Verify

- You can log in to <https://github.com>.
- You can log in to <https://railway.app> (sign up with your GitHub account at
  <https://railway.app/login>).

## What to build

Deploy a provided Flask app to **Railway.app** so it's accessible at a public URL. The starter
code is a complete, working Flask app with a Dockerfile — you just need to get it running on
Railway.

### The starter

The `starter/` folder contains:
- `app.py` — Flask app with `/` and `/health` endpoints, uses an environment variable
- `Dockerfile` — ready to build
- `requirements.txt` — Python dependencies

Your job: push this code to a GitHub repo, connect it to Railway, set the environment variable,
and verify it works.

### Step-by-step

1. Create a **new GitHub repo** (private is fine) — e.g., `my-first-deploy`.
2. Copy the starter files into the repo root (or use the starter folder as-is).
3. Push the code to GitHub. First create an empty repo on GitHub (github.com → New repository,
   name it `my-first-deploy`, **don't** initialize with README, click Create). Then:
   ```bash
   git init
   git add .
   git commit -m "initial deploy app"
   git branch -M main                      # ensure your default branch is 'main'
   git remote add origin <your-repo-url>   # the URL GitHub shows you after creating the repo
   git push -u origin main
   ```
   If `git push` asks for credentials, GitHub now requires a Personal Access Token (not your
   password) — see GitHub's "creating a personal access token" guide, or use the `gh` CLI
   (`gh auth login`).
4. Go to <https://railway.app> → New Project → Deploy from GitHub repo.
5. Select your `my-first-deploy` repo. Railway will detect the Dockerfile and build it.
6. Set an environment variable in Railway:
   - Variable: `APP_ENVIRONMENT`
   - Value: `production`
7. Wait for the deployment to finish (check Railway logs for "Application startup complete").
8. Railway assigns a public URL. Open it and test.

### How to test

```bash
# Railway gives you a URL like https://my-first-deploy-production.up.railway.app
# Replace <your-url> with the actual URL:

curl -s https://<your-url>/
# Should return: "Hello from production! Environment: production"

curl -s https://<your-url>/health
# Should return: {"status": "ok", "environment": "production"}
```

## Why this matters

Code on your laptop is invisible to the world. Deployment is how you make it real. Every
startup ships code to users through deployment. The sooner you've deployed something, the
sooner you understand the full loop: write code → push → build → deploy → user sees it.

## Deliverables

- A GitHub repo containing the starter code
- The app running on Railway.app at a public URL
- An environment variable set in Railway
- `curl` commands from your local machine confirming the app works

## Starter mode: `skeleton`

The starter code in `starter/` is a complete, working app. Your job is to deploy it, not modify
it. You may push it to GitHub as-is.

## How you'll be checked

Open [constraints.md](constraints.md). Each constraint is verified by running `curl` against
your deployed URL and observing the result. Self-report in [RESULTS.md](RESULTS.md). See
[../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the full workflow.

- All constraints pass → Level 1 cleared (and the whole Deployment topic is cleared).
- Any constraint fails → study [../../../resources.md](../../../resources.md), fix, re-check.
