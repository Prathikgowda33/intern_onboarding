# Results — Level 2 (CI/CD)

| Constraint | Result | Evidence (command + what you observed) |
|---|---|---|
| C1: Workflow file exists | PASS | `.github/workflows/deploy.yml` exists and contains `name`, `on`, `jobs`, and `steps`; workflow triggers on push to main. |
| C2: Workflow triggers on push | PASS | Pushing commit `f32854a` to main triggered GitHub Actions workflow `CI/CD Deployment Level 2`; latest workflow completed successfully with a green checkmark. |
| C3: Docker build uses commit hash | PASS | Workflow Docker build command passes `--build-arg COMMIT_HASH=${{ github.sha }}` and Dockerfile accepts `ARG COMMIT_HASH` and sets `ENV COMMIT_HASH=${COMMIT_HASH}`. |
| C4: App deployed and accessible | PASS | `curl -s -w "\nHTTP_CODE:%{http_code}\n" https://internonboarding-production.up.railway.app/health` returned JSON containing `"status":"ok"` with `HTTP_CODE:200`. |
| C5: /version shows commit hash | PASS | `curl -s https://internonboarding-production.up.railway.app/version` returned version `f32854a43d2b3f1a1bfd10aa3fb40520c1d14bc8`; `git rev-parse HEAD` returned the same commit hash. |
| C6: No hardcoded secrets | PASS | Inspected `.github/workflows/deploy.yml`; no tokens, passwords, API keys, or literal secrets are hardcoded. |
| C7: Multiple meaningful steps | PASS | Latest successful GitHub Actions run showed descriptive steps with green checks: Checkout repository, Set up Docker Buildx, Build Docker image with commit hash, Run Docker container, Verify health endpoint, and Verify version endpoint. |

## Overall

- [x] **CLEARED** — all constraints pass. Deployment topic complete.
- [ ] **Not cleared** — constraints above marked FAIL.

## Notes (optional)

Your Railway URL: https://internonboarding-production.up.railway.app
Your GitHub repo URL: https://github.com/Prathikgowda33/intern_onboarding
Latest commit hash: f32854a43d2b3f1a1bfd10aa3fb40520c1d14bc8
Anything else you want to note: GitHub Actions CI workflow completed successfully, Railway deployment is accessible, and the deployed /version endpoint matches the latest Git commit hash.
