# Constraints — Linux Level 3 (Live Web Server Logs)

The acceptance checklist. Verify each constraint **manually**. Then record Pass/Fail +
evidence in [RESULTS.md](RESULTS.md).

All paths are **relative to this level's folder**
(`topics/linux/levels/level-3-webserver-logs/`).

## How to check each constraint

1. Run the **How to verify** step.
2. Decide **Pass** or **Fail** using the explicit **Pass if** / **Fails if** lines.
3. Write down what you observed as evidence in [RESULTS.md](RESULTS.md).

---

## Constraints

- [ ] **C1: A container was actually used**
  - How to verify: while (or right after) you worked, run `docker ps -a | grep nginx-logs`
    OR check that your [RESULTS.md](RESULTS.md) shows the container id / a `docker`
    command you ran.
  - Pass if: there's evidence a real `nginx-logs` container ran on your machine — either
    `docker ps -a` still lists it (before you clean up) or your RESULTS.md documents the
    container id and the `docker run` you used.
  - Fails if: no evidence a container ran (e.g. the log file looks hand-typed, or no
    docker command was ever used).

- [ ] **C2: captured-access.log is a real nginx access log**
  - How to verify: run `head -3 captured-access.log` and `wc -l captured-access.log`.
  - Pass if: **every line** in `head` starts with an IP address (no
    `/docker-entrypoint.sh:` startup noise) AND the file has a non-trivial number of lines
    (at least ~30 — you should have generated more traffic than that).
  - Fails if: the file is empty, contains startup-noise lines that aren't access logs,
    has only a couple of lines, or the format isn't an access log.
  - Note: if you see `/docker-entrypoint.sh:` lines, you forgot to filter — see the
    README's capture step.

- [ ] **C3: The captured log contains some 4xx responses**
  - How to verify: run `awk '$9 ~ /^4[0-9][0-9]$/' captured-access.log | wc -l`
    (adjust the field number if your nginx log puts status in a different column —
    inspect with `head` first).
  - Pass if: the count is **greater than zero** — i.e. you actually generated 404s by
    requesting missing pages.
  - Fails if: zero 4xx responses (you didn't generate any bad requests) OR the field
    number you used doesn't match the log and the count is implausible.

- [ ] **C4: analyze-live.sh is executable and runs**
  - How to verify: run `./analyze-live.sh captured-access.log` from this folder.
  - Pass if: the script executes (no "permission denied") and prints all four sections
    (Top IPs, Errors, Busiest hour, Total) without crashing.
  - Fails if: permission denied, file not found, or the script errors before producing
    all four sections.

- [ ] **C5: analyze-live.sh requires the log argument**
  - How to verify: run `./analyze-live.sh` with no arguments.
  - Pass if: exits non-zero AND prints a usage message.
  - Fails if: runs anyway or fails silently.

- [ ] **C6: Error counts match the captured log**
  - How to verify: compare the script's "4xx errors" / "5xx errors" numbers against an
    independent count of the status field, e.g.
    `awk '$9 ~ /^4[0-9][0-9]$/' captured-access.log | wc -l` and the same for `5`.
    (Adjust field number to your log's actual layout.)
  - Pass if: both numbers match the independent counts exactly.
  - Fails if: either number is off.

- [ ] **C7: Total count matches wc -l**
  - How to verify: run `wc -l < captured-access.log` and compare to the script's "Total
    requests processed" number.
  - Pass if: the numbers match exactly.
  - Fails if: the count differs from `wc -l`.

- [ ] **C8: Container is cleaned up**
  - How to verify: after you're done analyzing, run `docker ps -a | grep nginx-logs`.
  - Pass if: no `nginx-logs` container remains (you stopped and removed it).
  - Fails if: the container is still running or stopped-but-present. (Real ops work
    leaves nothing dangling.)

---

## Summary

8 constraints. C1–C3 confirm you actually ran a container and captured real logs (the
core of this level — you can't fake it). C4–C7 check your analysis script works on the
logs you produced. C8 checks you cleaned up after yourself — a real-ops habit. If any
fail, see [../../resources.md](../../resources.md), section "Running services in
containers".
