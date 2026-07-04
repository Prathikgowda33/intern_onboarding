# Results — Level 1 (First Deploy)

| Constraint | Result | Evidence (command + what you observed) |
|---|---|---|
| C1: App is accessible at public URL | PASS | curl to the Railway public URL returned "Hello from production! Environment: production" with HTTP_CODE:200 |
| C2: Health endpoint works | PASS | curl to /health returned valid JSON containing "status":"ok" with HTTP_CODE:200 |
| C3: Environment variable is set | PASS | /health returned "environment":"production" and APP_ENVIRONMENT was configured in Railway Variables |
| C4: App runs from Dockerfile | PASS | Railway Build Logs showed Docker build steps including WORKDIR, COPY requirements.txt, RUN pip install, COPY app.py, Docker image export, and successful image push |
| C5: GitHub repo exists with starter code | PASS | GitHub repository contains app.py, Dockerfile, and requirements.txt; app.py uses APP_ENVIRONMENT from os.environ |
| C6: Multiple curl requests work | PASS | Three curl requests with 2-second pauses all returned the production response with HTTP_CODE:200 |
| C7: Deployment logs show app started | PASS | Railway deploy logs showed Flask app serving on 0.0.0.0:5000 with no startup errors; GET / and GET /health returned HTTP 200 |

## Overall

- [x] **CLEARED** — all constraints pass. Deployment topic complete.
- [ ] **Not cleared** — constraints above marked FAIL.

## Notes (optional)

Successfully deployed the provided Flask starter application to Railway using the Dockerfile, configured APP_ENVIRONMENT=production, generated a public Railway domain, verified the root and health endpoints, confirmed repeated requests, Docker-based build logs, GitHub starter files, and Flask startup logs.
