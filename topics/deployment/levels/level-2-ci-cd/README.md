# Level 2 — CI/CD

<!--
  Level metadata:
    slug: deployment/level-2-ci-cd
    skills: GitHub Actions, workflow YAML, Docker build, automated deployment
    difficulty: Hard
    estimated_time: 3-4h
    starter_mode: skeleton
-->

## Prerequisites

You need a **GitHub account**, a **Railway.app account**, and have completed Level 1 (or
equivalent manual deployment). You should understand what deployment is and how Railway works.

### Verify

- You can log in to <https://github.com> and <https://railway.app>.
- You have deployed an app to Railway before (Level 1 or equivalent).

## What to build

Set up a **GitHub Actions CI/CD pipeline** that automatically builds a Docker image and
deploys to Railway when you push to the `main` branch. The starter code has a Flask app with
a `/version` endpoint that should include the Git commit hash.

### The starter

The `starter/` folder contains:
- `app.py` — Flask app with `/`, `/health`, and `/version` endpoints
- `Dockerfile` — with a `ARG COMMIT_HASH` build argument (you complete it)
- `requirements.txt` — Python dependencies
- `.github/workflows/deploy.yml` — skeleton workflow with TODOs (you complete it)

### Step-by-step

1. Create a **new GitHub repo** (or use a new branch of your Level 1 repo).
2. Copy the starter files into the repo.
3. **Complete the Dockerfile:** pass `COMMIT_HASH` as a build argument and set it as an
   environment variable in the container so the app can access it.
4. **Complete the GitHub Actions workflow.** There are two approaches — **start with the
   simple one**:
   - **Simple (recommended for first-timers):** Configure Railway to auto-deploy from your
     GitHub repo (Railway dashboard → your service → Settings → connect the repo / enable
     auto-deploy on push to `main`). Then your GitHub Actions workflow just needs to
     **build and verify** the Docker image (run `docker build` with the commit hash, run
     the health check) — Railway handles the actual deploy on its own when it sees the push.
   - **Advanced (optional):** Build the image in the workflow, push to GitHub Container
     Registry (ghcr.io), then trigger Railway via its CLI/API. This needs a `RAILWAY_TOKEN`
     secret. Only do this if you want the full pipeline-in-CI pattern.
   Either way, the workflow must:
   - Trigger on push to `main`
   - Checkout code
   - Build the Docker image with `COMMIT_HASH=${{ github.sha }}` so C5 (the /version check)
     works
5. **Set up secrets:** if your workflow needs tokens (e.g., `RAILWAY_TOKEN`), store them in
   GitHub repo Settings → Secrets and variables → Actions.
6. Push to `main` and watch the Actions tab. Verify:
   - The workflow runs successfully
   - Railway picks up the new deployment
   - The `/version` endpoint shows the commit hash

### How to verify

```bash
# After pushing to main and the deploy completes:

curl -s https://<your-railway-url>/version
# Should return: {"version": "<commit-hash>", "app": "ci-cd-app"}

# Check GitHub Actions:
# Open your repo → Actions tab → latest workflow run → should show green checkmarks
```

## Why this matters

At a startup, you don't deploy by hand — you push code and a pipeline builds, tests, and
deploys it automatically. CI/CD (Continuous Integration / Continuous Deployment) is how
teams ship fast without breaking things. GitHub Actions is the most common CI/CD tool
for GitHub repos. Understanding workflow syntax, secrets management, and build triggers
is a skill you'll use at every company.

## Deliverables

- A GitHub repo with the completed workflow in `.github/workflows/deploy.yml`
- The workflow runs successfully on push to `main`
- The app is deployed and the `/version` endpoint shows the commit hash
- Secrets properly configured (not hardcoded)

## Starter mode: `skeleton`

The starter provides a Flask app, a partial Dockerfile, and a skeleton workflow with TODOs.
You complete the missing parts.

## How you'll be checked

Open [constraints.md](constraints.md). Each constraint is verified by observing GitHub
Actions output and `curl`-ing your deployed app. Self-report in [RESULTS.md](RESULTS.md). See
[../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the full workflow.

- All constraints pass → Level 2 cleared (and the whole Deployment topic is cleared).
- Any constraint fails → study [../../../resources.md](../../../resources.md), fix, re-check.
