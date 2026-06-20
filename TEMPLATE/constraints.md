# Constraints — <Topic Name>

The acceptance checklist. Verify each constraint **manually** by running your solution
and observing the result. Then record Pass/Fail + evidence in
[RESULTS.md](RESULTS.md).

Constraints check **behavior**, not implementation. As long as the observable condition
holds, how you achieved it is up to you (unless a constraint explicitly limits a choice).

## How to check each constraint

For every item below:

1. Run the **How to verify** step exactly.
2. Decide **Pass** or **Fail** using the explicit **Pass if** / **Fails if** lines.
3. Write down what you observed as evidence in [RESULTS.md](RESULTS.md).

If a Pass/Fail line is ambiguous, that's a bug in this file — ask. Don't guess.

---

## Constraints

- [ ] **C1: <short name>**
  - How to verify: <exact command or action, e.g. `docker compose up`, then `curl http://localhost:8080/health`>
  - Pass if: <observable condition, e.g. "returns HTTP 200 within 5s">
  - Fails if: <observable condition, e.g. "any error, timeout, or extra manual step needed">

- [ ] **C2: <short name>**
  - How to verify: <...>
  - Pass if: <...>
  - Fails if: <...>

<!-- Add C3, C4, ... as needed. Aim for 4–8 constraints total. -->

---

## Writing good constraints (for topic authors)

When authoring a real topic's constraints, keep these rules in mind (see
[../CONTRIBUTING.md](../CONTRIBUTING.md) for the full guide):

- **One behavior per constraint.** Split bundled checks ("starts AND responds") into two.
- **Verify is concrete.** Give the exact command, not "try it."
- **Pass/Fails are observable.** "It works" isn't a condition; "GET /health returns 200
  in <500ms" is.
- **High-level, not prescriptive.** Check the *what*, not the *how*.
- **4–8 constraints.** Fewer feels vague; more causes fatigue.
