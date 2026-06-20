# Authoring Guide — How to Build a Topic

This is the consolidated "lessons learned" from building the first topic (Linux). Every
convention below was earned the hard way — several by shipping a bug and catching it in
verification. **Follow it for every new topic.** It exists so each topic hits the same
quality bar without re-deriving the rules.

For the mechanical "copy TEMPLATE / fill in" steps, see
[CONTRIBUTING.md](CONTRIBUTING.md). This guide is about the *quality rules* and the
*common traps*.

---

## The non-negotiables

These are the rules that, when skipped, produced real bugs in the Linux topic.

### 1. Verify every constraint by attempting the topic yourself

This is the single most important rule. Before marking a topic READY, you (the author)
must actually **build the solution** and run every constraint against it. This caught four
real bugs in Linux:

| Bug | How it was caught |
|-----|-------------------|
| C5's `grep ' 4[0-9]{2} '` false-matched byte sizes | Running it vs an independent awk count |
| C6's `substr($4,2,2)` extracted the *day*, not the hour | Comparing script output to the independent check |
| L3's `docker cp /var/log/nginx/access.log` copied a `/dev/stdout` symlink (captured nothing) | Actually running the capture step |
| 6 `HOW_IT_WORKS.md` links were off by one `../` after moving into `levels/` | Running a link-resolution script |

If you skip this step, the topic ships broken. No amount of careful writing substitutes
for running it. See [CONTRIBUTING.md](CONTRIBUTING.md) quality checklist, last item.

### 2. Prerequisites come first, per-OS, with verify commands

Every topic's README starts with a **Prerequisites** section. A fresher must be able to
set up their machine from this section alone, without asking anyone. Rules:

- **Cover Windows, macOS, AND Linux** — you don't know what OS an intern uses.
- Each tool: a one-line **verify** command (`tool --version`) + install steps per OS.
- **WSL2 vs Git Bash decision** (Windows users): this bit us. Use this rule:
  - Topic checks **real Linux behavior** (permissions, `chown`, GNU tools, `/var`
    paths, containers) → **WSL2 is required for Windows**. Git Bash's permissions are a
    no-op (NTFS), so it would make those constraints meaningless.
  - Topic only runs a **language runtime or git** (Python, Node, Git CLI) → **Git Bash
    is fine**; WSL2 optional.
  - State which case applies for *this* topic.
- Link the official install page for the heavy installs (WSL2, Docker Desktop, etc.) so
  instructions don't go stale — link out rather than copy.
- Always end with a pointer to [SELF_HELP.md](SELF_HELP.md) (e.g., "follow SELF_HELP.md
  before spending an hour on it") — setup is the #1 day-one dropout point; this program is
  self-directed (no mentor), so interns need to know AI + forums are the help.

### 3. Constraints check behavior, not implementation

Each constraint must be **manually verifiable with no judgment calls**. Format:

```markdown
- [ ] **C1: <short name>**
  - How to verify: <exact command or action>
  - Pass if: <observable condition>
  - Fails if: <observable condition>
```

Rules:

- **One behavior per constraint.** "Starts AND responds" is two constraints.
- **Verify is concrete.** Give the exact command, not "try it."
- **Pass/Fails are observable.** "It works" isn't a condition; "GET /health returns 200
  in <500ms" is.
- **High-level, not prescriptive.** Check the *what*, not the *how* (unless the
  constraint is specifically about a tool choice).
- **4–8 constraints per topic.** Fewer = vague; more = fatigue.
- **Provide an independent check** for correctness constraints — a second command (awk,
  wc, etc.) that the intern/reviewer can run to confirm the script's answer is right.
  This is how you avoid a constraint that passes for the wrong reason.

### 4. Tier topics only when the skill genuinely spans levels

Don't manufacture tiers. The default is a single-level topic. Tier **only** when:

- The topic realistically has beginner-vs-advanced flavors (Linux: "never used a
  terminal" → "debugging live container logs"), AND
- The startup would actually hire people at different points on that curve.

Authoring 3 levels is ~3× the work. See [CONTRIBUTING.md §1b](CONTRIBUTING.md) for the
tiered folder structure.

When you DO tier:
- Top-level README = "pick your level" guide, not an assignment.
- Shared `resources.md` = progressive (absolute zero → advanced), sectioned by level.
- Each level links back to the shared resources by section, not by duplicating.
- **Mind the relative-link depth**: a level file is at
  `topics/<topic>/levels/<level>/`, so repo-root docs need **four** `../`. (This was a
  bug in Linux — see lesson #1.)

### 5. Resources are focused subsets, read only on failure

- Each topic's `resources.md` is a **focused subset** of the master
  [resources.md](resources.md), not a copy.
- Map each resource to the specific constraint(s) it unblocks: "If you failed C4, read
  this."
- **For foundational topics, start from absolute zero.** Don't assume the intern knows
  what a terminal is. Order resources: concept → basics → the specific skill →
  advanced. An intern who fails reads only their gap.
- The intern's rule: pass all constraints → skip resources entirely. The resources exist
  *for* failure, not as required reading.

---

## The mechanical checklist (per topic)

Stolen from [CONTRIBUTING.md](CONTRIBUTING.md)'s "Quality checklist before marking READY"
— repeat it for every topic:

- [ ] Prerequisites section covers every tool the topic needs, Windows/macOS/Linux, with
      verify commands. WSL2/Git-Bash decision is correct for the topic.
- [ ] Assignment is scoped to the estimated time, not 2× over.
- [ ] Every constraint is manually verifiable with concrete pass/fail criteria.
- [ ] An independent check exists for each correctness constraint.
- [ ] `starter/` folder matches the declared mode (scratch topics have none).
- [ ] `resources.md` is a focused subset mapped to constraints; foundational topics start
      from absolute zero.
- [ ] `RESULTS.md` is the blank template.
- [ ] Topic is listed in `topics/README.md` with status.
- [ ] **You attempted the topic yourself and cleared every constraint.**
- [ ] A link-resolution script reports 0 broken links (excluding template placeholders).

---

## Common traps (from the Linux build)

1. **Relative links after restructuring.** Moving files into `levels/` changed every
   relative path. Always re-run a link check after any folder move.
2. **Constraints that pass for the wrong reason.** A grep that "matches the status code"
   but also matches the byte-size field. Always provide an independent verification
   command (different tool, same data) and compare.
3. **Assuming a tool behaves the same everywhere.** `docker cp` of an nginx log path
   returns a symlink to `/dev/stdout`. Git Bash's `chmod` is a no-op. Test on the actual
   environment the intern will use.
4. **Scaffolding that ships unverified.** A scaffold (TODO placeholders) is fine;
   shipping "complete" constraints that nobody ran is not. The difference is whether
   you've attempted the topic.
5. **Resources that assume prior knowledge.** A fresher reading "defensive bash
   scripting" before they know what a terminal is will learn nothing. Start from zero for
   foundational topics.
6. **Stale illustrative numbers.** If your README example shows output values, make sure
   they match the actual sample data the intern will produce — otherwise it reads as a
   contradiction. (Linux L2's example initially had made-up numbers that didn't match the
   sample log.)

---

## The workflow when authoring a new topic

1. **Copy `TEMPLATE/`** to `topics/<slug>/` (or `topics/<slug>/levels/<level>/` for
   tiered).
2. **Fill metadata** (front-matter): slug, month, skills, difficulty, est. time, mode,
   levels.
3. **Write Prerequisites** — per-OS, with verify commands. Pick WSL2-vs-Git-Bash for
   Windows using rule #2.
4. **Write the assignment** — one small, scoped project.
5. **Write constraints** — 4–8, each manually verifiable, each with an independent check
   where correctness is involved.
6. **Curate resources** — focused subset mapped to constraints; from absolute zero if
   foundational.
7. **Ship RESULTS.md** as the blank template.
8. **Attempt the topic yourself** — build the solution, run every constraint, fix
   anything broken. This is the step that catches bugs.
9. **Run a link-resolution check** across the topic.
10. **Update `topics/README.md`** status to ✅ READY.

## Status conventions in topics/README.md

- 🔲 TODO — not built (or scaffolded with TODO placeholders only)
- 🚧 IN PROGRESS — being authored
- ✅ READY — complete AND attempted/verified by the author
- 📝 SCAFFOLDED — folder exists with metadata + prereqs, but assignment/constraints are
  TODO placeholders awaiting authoring + verification

Use 📝 SCAFFOLDED for the "phase 1" state we're creating now: structure + per-OS
prerequisites filled in, real assignment/constraints pending. This signals to a reader
"this exists but isn't ready to assign to an intern yet."
