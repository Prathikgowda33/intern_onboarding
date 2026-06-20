# Constraints — Linux (Shell Log Analyzer)

The acceptance checklist. Verify each constraint **manually** by running your script and
observing the result. Then record Pass/Fail + evidence in [RESULTS.md](RESULTS.md).

Constraints check **behavior**, not implementation. Use awk, grep+sort+uniq, or any
standard coreutil — your choice, as long as the observable condition holds.

## How to check each constraint

For every item below:

1. Run the **How to verify** step exactly.
2. Decide **Pass** or **Fail** using the explicit **Pass if** / **Fails if** lines.
3. Write down what you observed as evidence in [RESULTS.md](RESULTS.md).

If a Pass/Fail line is ambiguous, that's a bug in this file — ask. Don't guess.

---

## Constraints

- [ ] **C1: Script is executable and runs**
  - How to verify: run `./analyze.sh sample-access.log` from this folder.
  - Pass if: the script executes (no "permission denied"), and prints output to stdout
    without crashing.
  - Fails if: permission denied, file not found, or the script errors out before
    producing all four sections.

- [ ] **C2: Requires the log file argument**
  - How to verify: run `./analyze.sh` with no arguments.
  - Pass if: the script exits with a non-zero code AND prints a usage message
    (e.g. `Usage: ./analyze.sh <logfile> [N]`).
  - Fails if: the script runs anyway, or fails silently with no message.

- [ ] **C3: Default N is 5 when not given**
  - How to verify: run `./analyze.sh sample-access.log` (no second arg) and count the
    lines under the "Top IPs" section.
  - Pass if: exactly 5 IPs are listed.
  - Fails if: a different number of IPs is listed, or the section is missing.

- [ ] **C4: Top IPs are correct and sorted by count descending**
  - How to verify: run `./analyze.sh sample-access.log 3`, then independently verify the
    top 3 IPs against the log using `awk '{print $1}' sample-access.log | sort | uniq -c
    | sort -rn | head -3`.
  - Pass if: the script's top 3 IPs and counts match that independent check, and the
    counts are in descending order.
  - Fails if: counts differ, ordering is wrong, or any of the top 3 IPs don't match.

- [ ] **C5: 4xx and 5xx error counts are correct**
  - How to verify: compare the script's "4xx errors" and "5xx errors" numbers against an
    independent count of the status-code field (field 9 in combined log format):
    `awk '$9 ~ /^4[0-9][0-9]$/' sample-access.log | wc -l` and
    `awk '$9 ~ /^5[0-9][0-9]$/' sample-access.log | wc -l`.
  - Pass if: both numbers match the independent counts exactly.
  - Fails if: either number is off, or 4xx and 5xx are conflated.
  - Note: don't grep for ` 4xx ` in the raw line — the byte-size field sits right after
    the status and can cause false matches (e.g. a `200` with a 3-digit size). Count
    field 9 specifically.

- [ ] **C6: Busiest hour is identified correctly**
  - How to verify: find the busiest hour independently. The timestamp field (field 4)
    looks like `[14/Oct/2025:14:23:01`, so split it on `:` and take the hour token:
    `awk -F'[' '{print $2}' sample-access.log | awk -F':' '{print $2}' | sort | uniq -c
    | sort -rn | head -1`.
    Compare that hour and count to the script's "Busiest hour" line.
  - Pass if: the hour (00–23) and the count both match the independent check.
  - Fails if: wrong hour, or the count is wrong.
  - Note: the format of the hour in your output is up to you (`14`, `14:00`, etc.) as
    long as the hour value is identifiable and correct. Don't extract the **day** by
    accident — the hour is the part right after the first `:` in the timestamp.

- [ ] **C7: Total request count is correct**
  - How to verify: run `wc -l < sample-access.log` and compare to the script's "Total
    requests processed" number.
  - Pass if: the numbers match exactly.
  - Fails if: the count differs from `wc -l`.

- [ ] **C8: Handles a missing input file gracefully**
  - How to verify: run `./analyze.sh does-not-exist.log 5`.
  - Pass if: the script exits with a non-zero code AND prints a clear error message
    naming the missing file (no stack trace, no silent hang).
  - Fails if: the script crashes with a raw error, hangs, or exits 0 with no output.

---

## Summary

8 constraints. C1 and C8 test robustness (permissions, argument handling, error paths).
C3–C7 test correctness against independent shell-based checks. If any fail, see
[resources.md](resources.md).
