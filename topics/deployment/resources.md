# Resources — Deployment

Shared across both Deployment levels. This is a **progressive** resource list: it starts from
"what is deployment?" and goes up through CI/CD. **You don't read all of it.** Find the level
you're working on, read only what your failed constraints point to.

This list focuses on deployment specifically. The master cross-topic list is at
[../../resources.md](../../resources.md).

---

## From absolute zero (what is deployment?)

If you've never deployed an app and "the cloud" feels mysterious, start here.

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Railway — Getting Started](https://docs.railway.app/getting-started) | Reading | C1, C2 — how Railway works, what a project/service is, how to deploy. |
| [Docker — How Docker relates to deployment](https://docs.docker.com/get-started/overview/) | Reading | C1 — why Docker matters for deployment (same image everywhere). |
| [GitHub — What is GitHub?](https://docs.github.com/en/get-started/start-your-journey/hello-world) | Reading | C1 — if you're new to GitHub, start here. |

**The mental model you need first:** "Deployment" means taking code that runs on your laptop
and making it run on a server that anyone on the internet can access. Platforms like Railway
make this easy: you give them your code (or a Dockerfile), and they run it. **Environment
variables** let you configure the app without hardcoding secrets in your code.

## Manual deployment with Railway (Level 1)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Railway — Deploy from GitHub](https://docs.railway.app/deploy/github) | Reading | C1, C2 — how to connect a GitHub repo to Railway and deploy. |
| [Railway — Environment Variables](https://docs.railway.app/develop/variables) | Reading | C3, C4 — how to set environment variables in Railway's dashboard. |
| [Railway — Networking and Domains](https://docs.railway.app/develop/networking) | Reading | C5 — how Railway assigns URLs to your services. |
| [Python — os.environ](https://docs.python.org/3/library/os.html#os.environ) | Reference | C3, C4 — how to read environment variables in Python. |

## CI/CD with GitHub Actions (Level 2)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [GitHub Actions — Quickstart](https://docs.github.com/en/actions/quickstart) | Reading | C1, C2 — what GitHub Actions is, how to write a workflow file. |
| [GitHub Actions — Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions) | Reference | C1, C2 — the full syntax reference for `.github/workflows/*.yml`. |
| [GitHub Actions — Docker Build and Push](https://docs.github.com/en/actions/publishing-packages/publishing-docker-images) | Reading | C3 — how to build a Docker image and push it to a registry in a workflow. |
| [Railway — Deploy with GitHub Actions](https://docs.railway.app/guides/github-actions) | Reading | C4 — how to trigger Railway deploys from GitHub Actions. |
| [GitHub Actions — Environment Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) | Reading | C5 — how to store API keys and tokens securely in GitHub. |

---

## How to use these

1. Open the `RESULTS.md` of the level you're working on and find which constraints failed.
2. Read the resource(s) next to those constraints above.
3. Fix your solution.
4. Re-run the checks in the level's `constraints.md`.
5. Update `RESULTS.md` with the new evidence.

Don't read everything top to bottom — target the gap.
