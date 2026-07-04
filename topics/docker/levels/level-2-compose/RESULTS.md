# Results — Level 2 (Docker Compose)

| Constraint | Result | Evidence (command + what you observed) |
|------------|--------|--------------------------------------|
| C1: Two services defined | PASS | docker-compose.yml defines web with build directive and redis using redis:alpine |
| C2: Both containers running | PASS | docker compose ps showed both web and redis services Up |
| C3: Web connects to Redis | PASS | GET /health returned {"redis":"connected","status":"ok"} with HTTP 200 |
| C4: Counter increments | PASS | Repeated GET / requests returned increasing visitor numbers |
| C5: Redis data persists | PASS | Counter was visitor #4 before docker compose down/up and continued to visitor #5 after restart |
| C6: DNS networking works | PASS | redis hostname resolved successfully to 172.18.0.2 from the web container |

## Overall

- [x] **CLEARED** — all constraints pass. Docker topic complete.
- [ ] **Not cleared** — constraints above marked FAIL.

## Notes (optional)

Completed Docker Level 2 with Flask, Redis, Docker Compose service networking, persistent Redis volume, health checks, counter persistence, and Docker Compose DNS resolution.
