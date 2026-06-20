# Constraints — Level 2 (Docker Compose)

The acceptance checklist. Verify each constraint **manually** by running a command and observing
the result. Then record Pass/Fail + evidence in [RESULTS.md](RESULTS.md).

All commands below assume your terminal is in this folder
(`topics/docker/levels/level-2-compose/`).

## How to check each constraint

1. Build and start the app: `docker compose up --build -d`
2. Wait for both containers to start (run `docker compose ps` to verify).
3. Run the **How to verify** step exactly.
4. Decide **Pass** or **Fail** using the explicit **Pass if** / **Fails if** lines.
5. Write down what you observed as evidence in [RESULTS.md](RESULTS.md).

---

## Constraints

- [ ] **C1: docker-compose.yml defines two services**
  - How to verify: run `cat docker-compose.yml`.
  - Pass if: the file defines at least two services (one for the web app, one named `redis` or
    similar). The web service has a `build` directive. The redis service uses an image
    (`redis:alpine` or similar).
  - Fails if: only one service, or no redis service, or syntax errors.

- [ ] **C2: Both containers are running**
  - How to verify: run `docker compose ps`.
  - Pass if: two services are listed and both show "running" (or "Up"). Both services have
    assigned ports.
  - Fails if: any service shows "exited", "restarting", or is not listed.

- [ ] **C3: Web app connects to Redis**
  - How to verify: run `curl -s http://localhost:5000/health`.
  - Pass if: the response is JSON containing `"redis": "connected"` or similar. HTTP_CODE
    is 200.
  - **Independent check:** stop the redis container (`docker compose stop redis`), then
    `curl -s http://localhost:5000/health` — should show redis as disconnected. Then
    `docker compose start redis` to restore.
  - Fails if: the health endpoint doesn't mention redis, or shows redis as disconnected while
    the redis container is running.

- [ ] **C4: Counter increments across requests**
  - How to verify: run `curl -s http://localhost:5000/` three times.
  - Pass if: the visit count increases with each request (visitor #1, then #2, then #3 — or
    starting from a higher number if you've already visited). The count persists across
    requests.
  - Fails if: the count doesn't increment, or resets to 1 on each request (meaning Redis
    isn't being used).

- [ ] **C5: Redis data persists (volume configured)**
  - How to verify: note the current counter value. Run `docker compose down && docker compose up -d`.
    Then run `curl -s http://localhost:5000/` and compare.
  - Pass if: after restarting both containers, the counter continues from where it left off
    (not reset to 1). The `docker-compose.yml` defines a volume for the redis service.
  - Fails if: counter resets to 1 after restart, or no volume is defined in compose.

- [ ] **C6: Containers communicate via DNS**
  - How to verify: run `docker compose exec web ping -c 1 redis` (or `docker compose exec web python3 -c "import socket; print(socket.gethostbyname('redis'))"`).
  - Pass if: the hostname `redis` resolves to an IP address. The web container can reach
    the redis container by service name.
  - Fails if: hostname `redis` cannot be resolved.

---

## Summary

6 constraints. C1 checks compose file structure. C2 checks both containers run. C3 checks
Redis connectivity. C4 checks counter behavior. C5 checks data persistence. C6 checks DNS
networking. If any fail, see [../../../resources.md](../../../resources.md) — especially
"Docker Compose".
