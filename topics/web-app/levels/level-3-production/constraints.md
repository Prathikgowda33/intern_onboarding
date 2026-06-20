# Constraints — Level 3 (Production-Ready)

The acceptance checklist. Verify each constraint **manually** by running commands and observing
the result. Then record Pass/Fail + evidence in [RESULTS.md](RESULTS.md).

**Important:** Build and start the app with `docker compose up --build` before running these
checks.

## How to check each constraint

1. Run `docker compose up --build` (Terminal 1, from this folder).
2. Wait for both containers to start (look for "ready" messages in the logs).
3. Open a second terminal in this folder.
4. Run the **How to verify** step exactly.
5. Decide **Pass** or **Fail** using the explicit **Pass if** / **Fails if** lines.
6. Write down what you observed as evidence in [RESULTS.md](RESULTS.md).

---

## Constraints

- [ ] **C1: Docker containers start successfully**
  - How to verify: run `docker compose ps`.
  - Pass if: two services are listed and both show status "running" (or "Up"). The service
    names match your backend and frontend.
  - Fails if: any service shows "exited", "error", or is not listed.

- [ ] **C2: App is accessible via browser**
  - How to verify: run `curl -s -w "\nHTTP_CODE:%{http_code}" http://localhost:3000/`.
  - Pass if: HTTP_CODE is 200. The response contains HTML (the React app served by nginx).
  - Fails if: connection refused, or HTTP_CODE is not 200.

- [ ] **C3: Backend validation rejects empty input**
  - How to verify: run `curl -s -w "\nHTTP_CODE:%{http_code}" -X POST http://localhost:3000/api/entries -H "Content-Type: application/json" -d '{"name": "", "message": "test"}'` (or the backend's direct port if mapped differently).
  - Pass if: HTTP_CODE is 400. The response body contains a JSON error message about the
    empty name field.
  - Fails if: HTTP_CODE is 201 (accepted empty input), or 500 (crashed).

- [ ] **C4: Frontend shows error for invalid input**
  - How to verify: using the React app at `http://localhost:3000`, submit the form with an
    empty name. Observe the UI.
  - Pass if: the frontend displays an error message near the form (not a browser alert).
    The user is informed what went wrong. The page doesn't crash or go blank.
  - Fails if: no error shown, or the page crashes, or a generic alert() appears.

- [ ] **C5: Frontend shows loading state**
  - How to verify: open `http://localhost:3000` and observe the page as it loads. Also check
    the React source: `grep -r "loading\|spinner\|Loading" frontend/src/`.
  - Pass if: the source code contains loading state logic (a loading variable, conditional
    rendering of a loading indicator). When entries are fetched, a loading message or spinner
    is shown before data appears.
  - Fails if: no loading state in the code, or entries appear instantly with no loading
    indicator (even briefly).

- [ ] **C6: docker-compose.yml defines both services**
  - How to verify: run `cat docker-compose.yml`.
  - Pass if: the file defines at least two services (backend and frontend). Each has a
    `build` or `image` directive. Ports are mapped correctly (frontend to 3000, backend
    to a port the frontend can reach).
  - Fails if: only one service defined, or no port mappings.

---

## Summary

6 constraints. C1 checks Docker starts. C2 checks the app is accessible. C3 checks backend
validation. C4 checks frontend error display. C5 checks loading states. C6 checks
docker-compose configuration. If any fail, see [../../../resources.md](../../../resources.md)
— especially "Production features".
