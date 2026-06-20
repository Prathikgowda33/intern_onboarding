# Learning Path: Where to Start, Where to End, What to Do Now

This doc answers the three questions every intern asks:

1. **Where do I start?**
2. **How do I know I'm done?**
3. **What do I do when I'm stuck?**

If this is your first time here, read this whole page once. Then keep it open as a
reference.

## The path at a glance

```
Month 1 — Foundations         Month 2 — Web & Infra       Month 3 — Real work
─────────────────────         ─────────────────────       ───────────────────
Linux                          HTTP & API design           System design
  ↓                            Web app (full-stack)          ↓
Git                            Docker                      Vibe coding
  ↓                              ↓
Python                       Deployment
  ↓
Databases
  ↓
Testing
```

**Why this order?** Each topic builds on the ones before it:

- You need the **terminal** (Linux) before anything else — every other topic runs in one.
- You need **Git** to track every project you build.
- **Python** is the language most topics use for the build.
- **Databases** and **Testing** are foundational skills for real apps.
- **HTTP/API** and **Web app** combine Python + frontend into something users can touch.
- **Docker** and **Deployment** take your local app and put it on the internet.
- **System design** asks you to think at scale, using everything above.
- **Vibe coding** teaches you to use AI effectively across all of it.

The full topic list with statuses is in [topics/README.md](topics/README.md).

## Where to start

### 1. Set up your environment first

Before touching any topic, make sure you can run commands. Most topics need a **terminal**,
**Python 3**, and **Git**. Install these **once, up front** — don't wait per-topic.

**If you're on Windows (most common stumbling block):**
You need **WSL2** (a Linux terminal inside Windows). This is explained step-by-step in the
[Linux topic Level 1](topics/linux/levels/level-1-basics/README.md) prerequisites — **do
that first, before anything else**. It takes ~20-30 minutes and one reboot. It will not
break your Windows. Once WSL2 is set up, you'll have the terminal everything else uses.

**If you're on macOS or Linux:** you already have a terminal. Just verify Python and Git
(see below).

**Verify all three are working (run these in your terminal):**

```bash
# Terminal works? (you're in it — if you see a prompt, yes)
python3 --version    # should print "Python 3.x.x" — if not, install: see Linux L1 prereqs
git --version        # should print "git version 2.x.x" — if not, install: see Git topic prereqs
```

If any of those fail, the linked topic's Prerequisites section has the exact install
command for your OS. **Don't proceed to building until all three print a version** — every
topic assumes they work.

### 2. Pick your starting topic

For your first topic, start with **Linux** (Month 1). It teaches the terminal everyone
else depends on.

After that, follow the path above. But you don't have to be rigid — if you already know
Linux cold, skip ahead. (See "self-assess" below.)

### 3. For tiered topics, pick a level

Most topics are **tiered** — they have 2-3 levels of increasing difficulty. Open the
topic's README and you'll see a "Pick your level" table.

**Self-assess honestly:** pick the **highest** level you think you can clear.

- Pass it → the whole topic is cleared. You're done with it.
- Fail it → drop to the level below and try again. No penalty.

This is a placement test, not a punishment. If you can already do the hard version, don't
waste time on the easy one.

## How to know you're done

### Done with one topic

A topic is **cleared** when **all constraints pass** in the level you attempted:

1. Open the level's `constraints.md`.
2. Run each constraint's "How to verify" command.
3. Check each against its "Pass if" / "Fails if" criteria.
4. Record Pass/Fail + evidence in the level's `RESULTS.md`.
5. All Pass → topic cleared. Skip the `resources.md` — you didn't need it.
6. Any Fail → study `resources.md` for that gap, fix, re-check.

See [HOW_IT_WORKS.md](HOW_IT_WORKS.md) for the full workflow.

### Done with the whole program

When every topic in [topics/README.md](topics/README.md) shows as cleared for you, you're
done. Realistically this takes most of the 3 months — that's by design. The goal isn't
speed; it's that you can actually *do* these things by the end.

### How long should this take me? (time expectations)

Don't panic if you're slower or faster — these are rough guides so you can self-calibrate.
Most freshers move slower at first and speed up as the basics compound.

| Phase | What | Rough time |
|-------|------|-----------|
| **Setup** | Install WSL2/terminal, Python, Git, verify all work | Half a day (mostly WSL2 on Windows) |
| **Month 1** (Foundations) | Linux, Git, Python, Databases, Testing — one level each | 4-6 weeks of evenings, or ~2 weeks full-time |
| **Month 2** (Web & Infra) | HTTP/API, Web app, Docker, Deployment | 4-6 weeks of evenings, or ~2 weeks full-time |
| **Month 3** (Real work) | System design, Vibe coding | 2-3 weeks |

**If you're spending more than a week stuck on a single topic**, something's wrong — use
[SELF_HELP.md](SELF_HELP.md) aggressively, or drop to a lower level. Don't grind for
weeks in silence.

**If you're flying through** (clearing a topic every couple days), that's fine — the
placement-test model means you skip what you already know. Just make sure you're honestly
passing constraints, not hand-waving.

## What to do when stuck

You will get stuck. Everyone does. There's no mentor to rescue you — and that's fine,
because **AI + forums + docs are more than enough** when you use them well. Here's the
order:

1. **Read the error.** Out loud. Most answers are in the first line.
2. **Check the topic's `resources.md`** — it's curated for exactly your situation, mapped
   to the constraint you failed.
3. **Follow the [self-help playbook](SELF_HELP.md)** — the 10-minute self-debug, then AI
   (Claude/ChatGPT/Gemini with a good prompt), then web search, then forums. This solves
   99% of being stuck.
4. **Drop a level if you're over your head.** Tiered topics exist so you can step down
   instead of grinding on something too hard. No shame — that's what levels are for.
5. **Post to a forum** (Stack Overflow, r/learnprogramming, Discord) — only after you've
   genuinely tried AI and search and documented what you tried. Use the "how to ask for
   help with context" template in [SELF_HELP.md](SELF_HELP.md).

**Don't:** stare at a broken screen for an hour. That's not effort; that's stuck. Either
try something concrete (an AI prompt, a web search, a different command) or post a
well-formed question to a forum.

## Where to track your progress

Progress lives in **several places**, all inside the repo:

### 0. Your personal tracking (set up on day 1)

Copy these two templates so you have your own copies to fill in:

```bash
cp PROGRAM_CHECKLIST.md MY_CHECKLIST.md      # high-level checkboxes for the whole program
cp PROGRESS_TEMPLATE.md  MY_PROGRESS.md      # your personal journal
```

- **MY_CHECKLIST.md** — check off topics as you clear them. The 10-second "how am I doing?"
  view.
- **MY_PROGRESS.md** — your journal: what worked, what blocked you, AI prompts that helped,
  open questions. This is the doc that makes you actually learn (writing it down forces
  understanding) and saves future-you hours.

An example of a filled-in journal: see [WALKTHROUGH.md](WALKTHROUGH.md) — a fresher
walked the program, hit real walls, and logged them.

### 1. Per-topic: `RESULTS.md`

Every level has its own `RESULTS.md` with a table — one row per constraint. This is where
you record:

- **Result** — PASS or FAIL (only these two).
- **Evidence** — the command you ran and what you saw (e.g., `curl ... → HTTP_CODE:201`).

This is your proof of work. If it isn't in RESULTS.md, it didn't happen. (See
[How-we-work.md](How-we-work.md): "If it isn't written down, it didn't happen.")

### 2. Per-topic: the constraint checkboxes

Each `constraints.md` has checkboxes (`- [ ]`) next to each constraint. Check them off
(`- [x]`) as you verify them. A quick visual scan of a level folder tells you how far
along you are.

### 3. Overall: [topics/README.md](topics/README.md)

The topic index has a Status column. Track your own progress by marking topics as
cleared in your own copy, or keep a simple list:

```
[x] Linux          (cleared all 3 levels)
[x] Git            (cleared level 2)
[ ] Python         (in progress — level 1)
[ ] Databases      (not started)
...
```

You don't need fancy tooling. A checked list is progress tracking.

## A typical session

Here's what working on a topic looks like, start to finish:

1. **Pick a topic** from [topics/README.md](topics/README.md). Open its folder.
2. **Read the topic README** → pick a level (if tiered).
3. **Do prerequisites** — verify each tool with the given command.
4. **Read the level's README** → understand what to build.
5. **Build it.** Get stuck? Use [SELF_HELP.md](SELF_HELP.md).
6. **Open `constraints.md`** → run each check, one at a time.
7. **Fill in `RESULTS.md`** as you go (don't wait until the end).
8. **All pass?** Topic cleared. Mark it done.
9. **Some fail?** Open `resources.md` → study the gap → fix → re-check.

Repeat for the next topic.

---

## Related

- [How it works](HOW_IT_WORKS.md) — the detailed per-topic workflow.
- [Self-help](SELF_HELP.md) — how to get unstuck using AI and your own debugging.
- [How we work](How-we-work.md) — the mindset behind all of this.
- [Topics index](topics/README.md) — the full list of topics and their status.
