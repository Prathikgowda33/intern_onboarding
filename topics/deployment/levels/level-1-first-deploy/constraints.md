# Constraints — Level 1 (First Deploy)

The acceptance checklist. Verify each constraint **manually** by running `curl` against your
deployed Railway URL and observing the result. Then record Pass/Fail + evidence in
[RESULTS.md](RESULTS.md).

## How to check each constraint

1. Find your Railway public URL (shown in Railway dashboard, or via `railway up`).
2. Run the **How to verify** step from your local terminal, replacing `<your-url>` with your
   actual Railway URL.
3. Decide **Pass** or **Fail** using the explicit **Pass if** / **Fails if** lines.
4. Write down what you observed as evidence in [RESULTS.md](RESULTS.md).

---

## Constraints

- [ ] **C1: App is accessible at public URL**
  - How to verify: run `curl -s -w "\nHTTP_CODE:%{http_code}" https://<your-url>/`.
  - Pass if: HTTP_CODE is 200. The response body contains "Hello" and the environment
    value (e.g., "production").
  - Fails if: connection refused, timeout, 404, 500, or DNS error (app not deployed).

- [ ] **C2: Health endpoint works**
  - How to verify: run `curl -s https://<your-url>/health`.
  - Pass if: the response is valid JSON containing `"status": "ok"`. HTTP_CODE is 200.
  - Fails if: non-JSON response, missing "status" key, or error status code.

- [ ] **C3: Environment variable is set**
  - How to verify: run `curl -s https://<your-url>/health` and check the response.
  - Pass if: the JSON response contains an `"environment"` key with the value you set in
    Railway (e.g., `"environment": "production"`).
  - **Independent check:** open Railway dashboard → your service → Variables tab. Verify
    `APP_ENVIRONMENT` is listed with your chosen value.
  - Fails if: `"environment"` is null, empty, or "development" (the default fallback).

- [ ] **C4: App runs from Dockerfile**
  - How to verify: open Railway dashboard → your service → Deployments. Look at the build log.
  - Pass if: the deployment log shows Docker build steps (pulling base image, copying files,
    installing deps, running CMD). The build completed successfully.
  - Fails if: the app is running via a different method (e.g., Nixpacks auto-detection without
    a Dockerfile build).

- [ ] **C5: GitHub repo exists with the starter code**
  - How to verify: open your GitHub repo in a browser. Check that `app.py`, `Dockerfile`,
    and `requirements.txt` are present.
  - Pass if: all three starter files exist in the repo. The `app.py` content matches the
    starter (uses `os.environ` for `APP_ENVIRONMENT`).
  - Fails if: files are missing, or `app.py` was significantly rewritten.

- [ ] **C6: Multiple curl requests work (not one-shot)**
  - How to verify: run `curl -s https://<your-url>/` three times with a 2-second pause between each.
  - Pass if: all three requests return HTTP 200. The app doesn't crash after the first request.
  - Fails if: any request fails, or the app becomes unresponsive.

- [ ] **C7: Deployment logs show app started**
  - How to verify: open Railway dashboard → your service → Logs (or View Logs).
  - Pass if: the logs show the Flask app starting (e.g., "Running on http://0.0.0.0:5000"
    or similar startup message). No error messages in the logs.
  - Fails if: startup errors, or no Flask startup message visible.

---

## Summary

7 constraints. C1/C2 check the app is reachable and responding. C3 checks environment variables.
C4 checks Docker-based deployment. C5 checks GitHub repo. C6 checks stability. C7 checks logs.
If any fail, see [../../../resources.md](../../../resources.md) — especially "Manual deployment
with Railway".
