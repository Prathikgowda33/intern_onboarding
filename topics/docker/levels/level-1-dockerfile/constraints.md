# Constraints — Level 1 (Dockerfile Basics)

The acceptance checklist. Verify each constraint **manually** by running a Docker command and
observing the result. Then record Pass/Fail + evidence in [RESULTS.md](RESULTS.md).

All commands below assume your terminal is in this folder
(`topics/docker/levels/level-1-dockerfile/`).

## How to check each constraint

1. Run the **How to verify** step exactly.
2. Decide **Pass** or **Fail** using the explicit **Pass if** / **Fails if** lines.
3. Write down what you observed as evidence in [RESULTS.md](RESULTS.md).

---

## Constraints

- [ ] **C1: Dockerfile exists and uses correct base image**
  - How to verify: run `cat Dockerfile`.
  - Pass if: a `Dockerfile` exists in this folder. It starts with `FROM python:` (or
    `FROM python:` with a specific version tag like `3.11-slim`). It does NOT use `FROM ubuntu`
    followed by manual Python installation.
  - Fails if: no Dockerfile, or uses a non-Python base image, or installs Python manually
    from a non-Python base.

- [ ] **C2: Image builds successfully**
  - How to verify: run `docker build -t counter-app .` (after copying `app.py` to this folder).
  - Pass if: the build completes with `"Successfully tagged counter-app"` or `"Successfully built ..."`.
    No errors during the build. The build finishes in a reasonable time (not hanging).
  - Fails if: build errors (missing file, syntax error, failed install).

- [ ] **C3: Container starts and serves the app**
  - How to verify: run `docker run -d -p 5000:5000 --name counter counter-app && sleep 2 && curl -s -w "\nHTTP_CODE:%{http_code}" http://localhost:5000/health`.
  - Pass if: HTTP_CODE is 200. The response body contains `"ok"` or `"status"`.
  - Fails if: connection refused, or HTTP_CODE is not 200, or the container exits immediately.

- [ ] **C4: App works inside the container**
  - How to verify: run `curl -s http://localhost:5000/`.
  - Pass if: the response contains "Hello" and "visitor" (the app's message). It includes
    a visit count number.
  - Fails if: no response, error response, or the app's HTML doesn't contain the expected text.

- [ ] **C5: .dockerignore exists**
  - How to verify: run `cat .dockerignore`.
  - Pass if: a `.dockerignore` file exists. It excludes at least one category of unnecessary
    files (e.g., `.git`, `__pycache__`, `.venv`, `*.pyc`, `README.md`, or the `starter/` folder).
  - Fails if: no `.dockerignore` file, or it's empty.

- [ ] **C6: Dockerfile follows best practices**
  - How to verify: run `cat Dockerfile` and check for these patterns.
  - Pass if: the Dockerfile uses at least 3 of these best practices:
    - Specific base image tag (e.g., `3.11-slim`, not just `latest`)
    - Sets `WORKDIR` instead of using `RUN cd ...`
    - Uses `COPY requirements.txt` before `COPY .` (layer caching)
    - Uses `EXPOSE` for the app port
    - Does NOT run as root (has a `USER` directive) — optional but recommended
  - Fails if: the Dockerfile is a single `FROM` + `COPY .` + `RUN pip install` + `CMD` with
    no structure (no WORKDIR, no EXPOSE, no layered COPY).

---

## Summary

6 constraints. C1 checks the Dockerfile exists and uses a proper base image. C2 checks the
build succeeds. C3/C4 check the container runs and the app works. C5 checks .dockerignore. C6
checks best practices. If any fail, see [../../../resources.md](../../../resources.md) —
especially "Dockerfile basics".
