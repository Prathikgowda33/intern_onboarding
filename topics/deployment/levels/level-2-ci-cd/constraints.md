# Constraints — Level 2 (CI/CD)

The acceptance checklist. Verify each constraint **manually** by observing GitHub Actions output
and running `curl` against your deployed app. Then record Pass/Fail + evidence in
[RESULTS.md](RESULTS.md).

## How to check each constraint

1. Push code to `main` on your GitHub repo.
2. Open the **Actions** tab and find the latest workflow run.
3. Run the **How to verify** step exactly.
4. Decide **Pass** or **Fail** using the explicit **Pass if** / **Fails if** lines.
5. Write down what you observed as evidence in [RESULTS.md](RESULTS.md).

---

## Constraints

- [ ] **C1: GitHub Actions workflow file exists**
  - How to verify: open `.github/workflows/deploy.yml` in your GitHub repo (in the browser or locally).
  - Pass if: the file exists. It contains at least `name:`, `on:`, `jobs:`, and `steps:`
    at the top level. The workflow triggers on `push` to `main`.
  - Fails if: file doesn't exist, or missing required top-level keys.

- [ ] **C2: Workflow runs on push to main**
  - How to verify: push a commit to `main`. Open the Actions tab. Check the latest run.
  - Pass if: a workflow run was triggered by your push. The run shows at least 2 steps (e.g.,
    checkout, build, deploy). The run completed (green checkmark, not red X).
  - Fails if: no run triggered, or the run failed (red X).

- [ ] **C3: Docker build step includes commit hash**
  - How to verify: open the workflow file and check the build step.
  - Pass if: the Docker build command passes `COMMIT_HASH=${{ github.sha }}` (or equivalent
    using the commit SHA). The Dockerfile accepts this as an ARG.
  - Fails if: no commit hash is passed to the build, or the build step doesn't use `github.sha`.

- [ ] **C4: App deployed and accessible**
  - How to verify: after the workflow completes, run `curl -s https://<your-railway-url>/health`.
  - Pass if: HTTP_CODE is 200. The response contains `"status": "ok"`.
  - Fails if: app not reachable, or error response.

- [ ] **C5: /version endpoint shows commit hash**
  - How to verify: run `curl -s https://<your-railway-url>/version`.
  - Pass if: the response JSON contains a `version` field with a value that matches (or starts
    with) your latest commit hash. The commit hash is at least 7 characters long.
  - **Independent check:** copy the commit hash from the response and compare with `git rev-parse HEAD`
    in your local repo — they should match.
  - Fails if: version is empty, missing, or doesn't match the commit hash.

- [ ] **C6: No secrets hardcoded in the workflow file**
  - How to verify: open `.github/workflows/deploy.yml` and search for tokens, passwords, or API keys.
  - Pass if: no tokens, passwords, or API keys appear as literal strings in the workflow file.
    Secrets are referenced via `${{ secrets.SECRET_NAME }}` syntax.
  - Fails if: any token, password, or API key appears as a literal value (not a secret reference).

- [ ] **C7: Workflow has multiple meaningful steps**
  - How to verify: open the Actions tab, click the latest successful run, and review the steps.
  - Pass if: the workflow has at least 3 steps (e.g., checkout → build → deploy). Each step
    has a descriptive name. The steps show in the Actions UI with green checkmarks.
  - Fails if: only 1-2 steps, or all work is crammed into a single step.

---

## Summary

7 constraints. C1 checks the workflow file exists. C2 checks it triggers on push. C3 checks
the commit hash is passed to the build. C4 checks the app is reachable. C5 checks the version
endpoint. C6 checks secrets management. C7 checks workflow structure. If any fail, see
[../../../resources.md](../../../resources.md) — especially "CI/CD with GitHub Actions".
