# Suggested Improvements to This Repo

A living list of proposed improvements. Each item has a status:

- 🔲 **Proposed** — idea written down, not started
- 🚧 **In progress** — being implemented
- ✅ **Done** — implemented

> **How to use this:** review the 🔲 items. Tell me which to implement (or reject). I'll
> apply them one at a time so you can review each change.

---

## ✅ Done

### 1. Cross-link the three new docs from README.md *(applied)*

Added links to SELF_HELP.md, LEARNING_PATH.md, and this doc from the main README so
interns discover them. Also added a "First time here?" pointer to LEARNING_PATH.md.

---

## 🔲 Proposed (awaiting your decision)

### 2. Add a single-file `PROGRESS.md` dashboard

**Problem:** Today, progress is scattered — one `RESULTS.md` per level, checkboxes in
`constraints.md`. To see "how far along is this intern?", you have to open ~20 files.

**Proposal:** Add a `PROGRESS.md` at the repo root — a single table an intern fills in
as they go:

```markdown
## My progress

| Month | Topic | Level cleared | Date | Notes |
|-------|-------|---------------|------|-------|
| 1 | Linux | L1, L2, L3 | 2025-01-15 | All cleared |
| 1 | Git | L2 | 2025-01-20 | Skipped L1 |
| 1 | Python | — | in progress | L1 done, L2 stuck on CSV |
| ... |
```

One file, one scan, full picture. Interns update it; mentors read it.

**Cost:** Low. One new file + a pointer from LEARNING_PATH.md.
**Risk:** Interns may forget to update it (mitigation: make it part of the per-topic
workflow — update PROGRESS.md when you mark a topic cleared).

---

### 3. Add a `TROUBLESHOOTING.md` for common errors

**Problem:** Interns hit the same setup errors repeatedly (WSL2 not installed, Flask
import error, Docker permission denied, SQLite version too old for window functions).
Each costs 15-30 minutes.

**Proposal:** A `TROUBLESHOOTING.md` at repo root — a table of `Error → Cause → Fix`:

```markdown
| Error | Cause | Fix |
|-------|-------|-----|
| `bash: docker: command not found` | Docker not installed or not in PATH | Install Docker Desktop (Win/Mac) or `apt install docker.io` (Linux) |
| `Got permission denied while trying to connect to the Docker daemon` | User not in docker group | `sudo usermod -aG docker $USER`, log out/in |
| `ModuleNotFoundError: No module named 'flask'` | Not in venv, or Flask not installed | `pip install flask` (activate venv first) |
| `sqlite3.OperationalError: no such function: ROW_NUMBER` | SQLite < 3.25 | Upgrade SQLite or use Python's bundled version |
```

Grows over time as real interns hit real errors.

**Cost:** Low to start, grows organically.
**Risk:** Can get stale if not maintained. Mitigation: date-stamp entries.

---

### 4. Add a "Start here" banner to the repo root README

**Problem:** New interns land on README.md and see 6 doc links (AUTHORING, CONTRIBUTING,
HOW_IT_WORKS, How-we-work, resources, topics/README). It's not obvious which to read
first as an intern vs. as an author.

**Proposal:** Add a clearly-marked intro section at the very top of README.md:

```markdown
## 👋 First time here?

**If you're an intern:** start with [LEARNING_PATH.md](LEARNING_PATH.md).
**If you're authoring/maintaining topics:** start with [AUTHORING.md](AUTHORING.md).
```

**Cost:** Trivial (3 lines).
**Risk:** None.

---

### 5. Clarify the ✅ READY status (honesty fix)

**Problem:** AUTHORING.md defines ✅ READY as "complete AND the author has attempted it
and verified every constraint." But several topics were marked READY without being
attempted end-to-end by a human. This overstates readiness.

**Proposal:** Either:
- **(a)** Add an intermediate status "📝 AUTHORED" = written but not yet attempted, and
  downgrade the un-attempted topics to it. Keep ✅ READY for actually-verified topics.
- **(b)** Keep ✅ READY but add a column or note: "Attempted by author? Y/N".

**My recommendation:** (a) — it's the honest representation and matches AUTHORING.md.

**Cost:** Low (status legend update + scan topics for which were attempted).
**Risk:** None — this is a correctness fix.

---

### 6. Add estimated time *per level* to the topic index

**Problem:** [topics/README.md](topics/README.md) shows "2-3h per level" for tiered
topics but doesn't break it down. An intern can't tell if they're budgeting 2h or 6h for
a topic.

**Proposal:** Add a "Levels" column showing the count and rough time:

```markdown
| Topic | Levels | Total est. time |
|-------|--------|-----------------|
| Linux | 3 (1-4h) | 3-8h (do one) |
| Git | 2 (1-3h) | 1-3h (do one) |
```

**Cost:** Low.
**Risk:** Minor — estimates are approximate anyway.

---

### 7. Add a `FAQ.md` for cross-topic questions

**Problem:** Some questions don't belong to any topic but come up constantly: "Do I need
WSL2 for everything?", "Which editor should I use?", "Can I use Copilot for the
assessments?", "How do I know if I'm ready for the next topic?".

**Proposal:** A `FAQ.md` with answers. Seed it with 8-10 common questions.

**Cost:** Low to write, needs maintenance.
**Risk:** Overlaps with SELF_HELP.md and LEARNING_PATH.md — must keep scope tight (factual
cross-topic Q&A, not process).

---

### 8. Add an ASCII map of the whole repo at the top of README

**Problem:** Newcomers don't know the folder structure and don't know which files are
"for interns" vs "for authors".

**Proposal:** Add a tree diagram to README.md with annotations:

```
intern_onboarding/
├── README.md              ← start here (interns)
├── LEARNING_PATH.md       ← where to start, where to end
├── SELF_HELP.md           ← how to get unstuck
├── HOW_IT_WORKS.md        ← per-topic workflow
├── How-we-work.md         ← culture / mindset
├── resources.md           ← master resource list
├── AUTHORING.md           ← (authors) how to write a topic
├── CONTRIBUTING.md        ← (authors) how to contribute
├── topics/
│   ├── README.md          ← topic index + statuses
│   ├── linux/             ← each topic is a folder
│   │   ├── README.md      ← topic-level guide
│   │   ├── resources.md   ← curated links for this topic
│   │   └── levels/        ← tiered difficulty levels
│   └── ...
└── TEMPLATE/              ← (authors) file templates
```

**Cost:** Trivial.
**Risk:** Must be kept in sync if structure changes (low churn).

---

## How to decide

My suggested priority order if you want to implement some:

1. **#4 (start-here banner)** + **#8 (repo map)** — zero risk, huge clarity win, do first.
2. **#5 (honesty fix on READY status)** — correctness, should do.
3. **#2 (PROGRESS.md)** — high value, low cost.
4. **#3 (TROUBLESHOOTING.md)** — high value, grows over time, seed it now.
5. **#6 (per-level time)** — nice-to-have.
6. **#7 (FAQ.md)** — defer until real questions accumulate.

Tell me which to implement (e.g., "do 4, 8, 5, 2" or "all of them" or "just 4 and 5").
