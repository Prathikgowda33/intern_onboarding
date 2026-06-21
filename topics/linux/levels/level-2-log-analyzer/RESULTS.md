# Results — Linux (Shell Log Analyzer)

Intern fills this in. See [../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the workflow.

## Constraint results

| Constraint | Result | Evidence (what you observed) |
|------------|--------|------------------------------
 | C1 | PASS | ./analyze.sh sample-access.log ran and printed Top IPs, Errors, Busiest hour, and Total |
| C2 | PASS | ./analyze.sh -> Usage: ./analyze.sh <logfile> [N] |
| C3 | PASS | ./analyze.sh sample-access.log used default Top 5 IPs |
| C4 | PASS | Top 3 IPs matched awk sort uniq -c sort -rn head -3 |
| C5 | PASS | 4xx errors: 2 and 5xx errors: 2 matched independent counts |
| C6 | PASS | Busiest hour reported 14:00 (count: 4) |
| C7 | PASS | Total requests processed: 7 matched wc -l |
| C8 | PASS | ./analyze.sh does-not-exist.log 5 -> Error: File 'does-not-exist.log' not found |
- `Result` is `PASS` or `FAIL` only.
- `Evidence` is specific: the command you ran and what you saw. "Works" is not evidence.
  Example: "C4 — script top 3 IPs match `awk \| sort \| uniq -c \| sort -rn \| head -3`
  exactly."

## Overall

Delete whichever doesn't apply:

- ✅ **CLEARED** — all constraints pass. Topic complete. Skipping `resources.md`.
- ❌ **Not cleared** — constraints above marked FAIL. Reviewing `resources.md`, will
  retry and update this file.

## Notes (optional)

<Any blockers, assumptions you made, or follow-ups.>
