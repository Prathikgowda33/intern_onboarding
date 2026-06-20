# Program Checklist

> The high-level checkbox view of the entire intern onboarding program. **Copy this file
> to `MY_CHECKLIST.md`** and check things off as you clear them. For the *why* and *how*,
> see [LEARNING_PATH.md](LEARNING_PATH.md). For your personal journal, see
> [PROGRESS_TEMPLATE.md](PROGRESS_TEMPLATE.md).
>
> **Rule of thumb:** only check a box when you've **honestly passed every constraint** in
> that level's `constraints.md` and recorded it in that level's `RESULTS.md`. No hand-waving.

**My name:** _______________________  **Start date:** ____________  **Target end:** ____________

---

## Phase 0 — Setup (do this first, once)

- [ ] Read [README.md](README.md) (the intro)
- [ ] Read [LEARNING_PATH.md](LEARNING_PATH.md) (where to start / end / stuck)
- [ ] Read [SELF_HELP.md](SELF_HELP.md) (how to get unstuck — AI, search, forums)
- [ ] Read [HOW_IT_WORKS.md](HOW_IT_WORKS.md) (the per-topic workflow)
- [ ] Skim [How-we-work.md](How-we-work.md) (the mindset — read once, revisit later)
- [ ] Copy [PROGRESS_TEMPLATE.md](PROGRESS_TEMPLATE.md) → `MY_PROGRESS.md` (your journal)
- [ ] Copy this file → `MY_CHECKLIST.md`
- [ ] **Terminal works** (WSL2 on Windows — see [Linux L1](topics/linux/levels/level-1-basics/README.md))
- [ ] **Python 3 installed** (`python3 --version` prints a version)
- [ ] **Git installed** (`git --version` prints a version)
- [ ] **AI tool account** (free Claude.ai or ChatGPT is enough)

**Setup done? → Start Month 1.**

---

## Month 1 — Foundations

### Linux (start here)

- [ ] L1 — Command-Line Basics _(prereqs + build + 7 constraints + RESULTS)_
- [ ] L2 — Log Analyzer _(optional — do if you want more terminal depth)_
- [ ] L3 — Webserver Logs _(optional)_
- [ ] **Linux topic CLEARED** (one level is enough)

### Git & Collaboration

- [ ] L1 — Local Fundamentals _(branching, merging, meaningful commits)_
- [ ] L2 — Collaboration & Conflicts _(optional — do if L1 was easy)_
- [ ] **Git topic CLEARED**

### Python

- [ ] L1 — File Organizer CLI _(skeleton: argparse, os, shutil)_
- [ ] L2 — CSV Analyzer _(optional — do if L1 was easy)_
- [ ] **Python topic CLEARED**

### Databases & SQL

- [ ] L1 — SQL Fundamentals _(schema, CRUD, joins, SQLite)_
- [ ] L2 — Advanced SQL _(optional — views, indexes, window functions, transactions)_
- [ ] **Databases topic CLEARED**

### Testing

- [ ] L1 — Unit Testing _(fix-this: pytest, find the bugs)_
- [ ] L2 — Mocking & Integration _(optional — mock HTTP, integration tests)_
- [ ] **Testing topic CLEARED**

**Month 1 done? → Start Month 2.** _(roughly 4-6 weeks of evenings, or ~2 weeks full-time)_

---

## Month 2 — Web & Infra

### HTTP & API Design

- [ ] L1 — REST API _(Flask bookmark manager, 5 endpoints, curl)_
- [ ] L2 — Validation & Error Handling _(optional — validation, search, logging)_
- [ ] **HTTP-API topic CLEARED**

### Web App (Full-Stack)

- [ ] L1 — Backend + Static HTML _(Flask + Jinja2 guestbook)_
- [ ] L2 — React Frontend _(optional — React + CORS + API)_
- [ ] L3 — Production-Ready _(optional — Docker, validation, error handling)_
- [ ] **Web App topic CLEARED**

### Docker

- [ ] L1 — Dockerfile Basics _(containerize a Flask app)_
- [ ] L2 — Docker Compose _(optional — Flask + Redis multi-container)_
- [ ] **Docker topic CLEARED**

### Deployment

- [ ] L1 — First Deploy _(deploy a Flask app to Railway)_
- [ ] L2 — CI/CD _(optional — GitHub Actions auto-deploy)_
- [ ] **Deployment topic CLEARED**

**Month 2 done? → Start Month 3.** _(roughly 4-6 weeks of evenings, or ~2 weeks full-time)_

---

## Month 3 — Real Work

### System Design

- [ ] Single-level — URL Shortener Design Doc _(7 sections + AI-judged review)_
- [ ] **System Design topic CLEARED**

### Vibe Coding

- [ ] L1 — AI-Assisted Build _(build md2html with AI, keep PROMPT_LOG + VERIFICATION)_
- [ ] L2 — TDD with AI _(optional — tests first, AI implements)_
- [ ] **Vibe Coding topic CLEARED**

**Month 3 done? → Program complete!** _(roughly 2-3 weeks)_

---

## Final

- [ ] All 11 topics CLEARED in `MY_CHECKLIST.md`
- [ ] `MY_PROGRESS.md` retrospectives filled in for each month
- [ ] Optional: write a short "what I learned / advice to next intern" note in `MY_PROGRESS.md`
- [ ] Celebrate 🎉

---

## When you get stuck (don't skip this)

- [ ] Read the error out loud (90% of bugs are unread error messages)
- [ ] Check the topic's `resources.md`
- [ ] Follow [SELF_HELP.md](SELF_HELP.md) — 10-min self-debug → AI → search → forums
- [ ] If stuck >1 week on a single topic: **drop a level** or ask in a forum — don't grind in silence

## Status legend (for your own tracking)

- ☐ = not started
- 🚧 = in progress
- ✅ = CLEARED (all constraints passed + recorded in RESULTS.md)
- ⏭️ = skipped (note why in `MY_PROGRESS.md`)
- ❌ = attempted, failed, retrying

---

## Related

- [LEARNING_PATH.md](LEARNING_PATH.md) — the detailed guide this checklist summarizes.
- [PROGRESS_TEMPLATE.md](PROGRESS_TEMPLATE.md) — copy to `MY_PROGRESS.md` for your journal.
- [topics/README.md](topics/README.md) — the authoritative topic index with current statuses.
- [SELF_HELP.md](SELF_HELP.md) — how to get unstuck.
