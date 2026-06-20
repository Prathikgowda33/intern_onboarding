# How It Works

The intern workflow for each topic. Six steps, repeated per topic.

## The core loop

```
pick topic → build it → check constraints manually → self-report in RESULTS.md
                                                          │
                                          ┌───────────────┴───────────────┐
                                          ▼                               ▼
                              all constraints pass             any constraint fails
                                  → topic CLEARED               → study resources.md
                                  → skip the resources               → fix solution
                                                                     → re-check
```

## Step-by-step

### 1. Pick a topic

Open [topics/README.md](topics/README.md). Topics are grouped into three monthly
clusters. Pick one, open its folder: `topics/<topic-slug>/` (for a tiered topic, pick a
level inside `levels/`).

### 2. Set up your prerequisites

Every topic's README starts with a **Prerequisites** section listing exactly what to
install (terminal, Git, Docker, Python, etc.) with Windows / macOS / Linux steps and a
verify command for each. **Do this first**, before reading the assignment — you can't
build anything until the tools work. Each prerequisite has a one-line check (`tool
--version`); if it prints a version, you're set. If a check fails and you can't resolve
it from the steps shown, follow [SELF_HELP.md](SELF_HELP.md) before burning an hour — AI and web search solve most setup issues fast.

### 3. Build the assignment

Read the topic's `README.md`. It tells you:

- **What to build** — the project and its deliverables.
- **Starter mode** — one of:
  - `scratch` — build entirely from a prompt. No `starter/` folder present.
  - `skeleton` — a `starter/` folder is provided with stub files; fill it in.
  - `fix-this` — a `starter/` folder contains a broken/incomplete solution; make it work.

If there's no `starter/` folder, the topic is `scratch`. If the folder is there, the
`README.md` will say whether it's a skeleton or a fix-this.

### 4. Check the constraints manually

Open `constraints.md`. Each constraint looks like this:

```markdown
- [ ] **C1: App starts with one command**
  - How to verify: run `docker compose up` from the topic root
  - Pass if: app reachable at http://localhost:8080 within 60s
  - Fails if: any manual setup step beyond the single command is needed
```

For every constraint, run the **How to verify** step on your solution and decide
**Pass** or **Fail** based on the explicit **Pass if** / **Fails if** lines. There is no
test runner and no automated grader — you observe the result and judge it honestly.
The criteria are written to be unambiguous, so there shouldn't be judgment calls.

### 5. Self-report in RESULTS.md

Open `RESULTS.md` (a template is provided in each topic). Fill in the table:

```markdown
| Constraint | Result | Evidence (what you observed) |
|------------|--------|------------------------------|
| C1         | PASS   | `docker compose up` → 200 OK on :8080 |
| C2         | FAIL   | POST returned 500, missing validation |
```

Then the overall line:

- All PASS → `Overall: ✅ CLEARED`
- Any FAIL → `Overall: ❌ Not cleared → reviewing resources.md, will retry.`

Be honest. The point of self-reporting is to learn, not to manufacture green ticks.
A real FAIL with good evidence is more useful than a fake PASS.

### 6. Pass → done. Fail → study and retry

- **All pass:** the topic is cleared. Move to the next topic. You do **not** need to read
  the topic's `resources.md`.
- **Any fail:** open `resources.md`, study the focused material for that topic, fix your
  solution, then re-run step 3. Repeat until cleared.

## How reviewers use this

Reviewers (the team hiring the intern) don't re-check every constraint. They:

1. Read the intern's `RESULTS.md` per topic — look at evidence, not just PASS/FAIL.
2. Spot-check borderline or failing submissions directly against `constraints.md`.
3. Use the cleared/failed pattern across topics to decide where the intern needs
   support vs. where they can be trusted with real work.

## Tips

- **Do topics in month order** — later topics assume earlier skills.
- **One topic at a time** — don't start three in parallel.
- **A constraint fail is information, not failure** — the resources exist for a reason.
- **Keep your `RESULTS.md` evidence specific** — "works" isn't evidence; "GET /health
  returned 200 in 40ms" is.
