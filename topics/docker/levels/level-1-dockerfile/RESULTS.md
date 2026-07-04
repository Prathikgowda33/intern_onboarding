# Results — Level 1 (Dockerfile Basics)

| Constraint | Result | Evidence (command + what you observed) |
|------------|--------|--------------------------------------|
| C1: Dockerfile exists, correct base | PASS | cat Dockerfile showed FROM python:3.11-slim |
| C2: Image builds successfully | PASS | docker build -t counter-app . completed successfully and created counter-app:latest |
| C3: Container starts, /health works | PASS | Container started and /health returned {"status":"ok"} with HTTP_CODE:200 |
| C4: App works inside container | PASS | curl http://localhost:5000/ returned Hello! You are visitor with a visit count |
| C5: .dockerignore exists | PASS | .dockerignore excludes .git, __pycache__, *.pyc, .venv, README.md, and starter/ |
| C6: Best practices followed | PASS | Dockerfile uses python:3.11-slim, WORKDIR, EXPOSE, USER appuser, and --no-cache-dir |

## Overall

- [x] **CLEARED** — all constraints pass. Docker topic complete.
- [ ] **Not cleared** — constraints above marked FAIL.

## Notes (optional)

Completed Docker Level 1 by containerizing the provided Flask counter app with a Python slim base image, non-root user, .dockerignore, successful image build, health check, and working counter endpoint.
