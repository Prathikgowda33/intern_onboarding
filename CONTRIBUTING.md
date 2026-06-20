# Contributing

How to add a new topic to this repo. The short version: **copy `TEMPLATE/`, fill it in.**

## Add a topic in 6 steps

### 1. Copy the template

```bash
cp -r TEMPLATE topics/<topic-slug>
```

Use a lowercase, hyphenated slug matching the index in
[topics/README.md](topics/README.md) (e.g. `linux`, `http-api`, `vibe-coding`).

### 2. Pick the starter mode

Each topic (or each *level* within a tiered topic — see step 1b) is one of three modes.
Decide which, then set up the `starter/` folder:

| Mode | What it means | `starter/` folder |
|------|---------------|-------------------|
| `scratch` | Intern builds from a prompt only | **Remove** the folder (or leave only `.gitkeep` and note scratch in README) |
| `skeleton` | Intern fills in stub files you provide | Add the stub files (empty functions, placeholder config, etc.) |
| `fix-this` | Intern repairs a deliberately broken solution | Add the broken solution |

State the mode explicitly in the topic's `README.md` front-matter (see
[TEMPLATE/README.md](TEMPLATE/README.md)).

### 1b. (Optional) Tier the topic

Most topics are **single-level** — one project, one constraints file. That's the default
and the right choice for focused skills.

Tier a topic **only** when it genuinely has beginner vs. advanced flavors (e.g. Linux
ranges from "never opened a terminal" to "debugging live container logs"). A tiered
topic restructures into `levels/`:

```
topics/<slug>/
├── README.md            ← level-selection guide (NOT an assignment)
├── resources.md         ← shared, covers all levels from absolute basics
└── levels/
    ├── level-1-<name>/  ← a full single-level topic (README/constraints/RESULTS/starter)
    ├── level-2-<name>/
    └── level-3-<name>/
```

Tiered-topic rules:

- The top-level `README.md` becomes a **"pick your level" guide**: a table of who each
  level is for and what it asks. Interns self-assess, enter at the highest level they
  think they can clear. Fail it → drop a level. Pass it → topic cleared (lower levels
  not needed).
- `resources.md` at the topic root is **shared and progressive** — sectioned from
  absolute basics through advanced, so any level can find its prerequisites. Each level
  *may* have its own `resources.md` pointing back to the relevant section, or just link
  to the shared one.
- Each level folder is otherwise a normal single-level topic.
- Set `levels: 1,2,3` in the top-level front-matter. See `topics/linux/` for a reference.

Don't manufacture tiers for a topic that doesn't need them. Authoring 3 levels is ~3× the
work; only spend it where the skill spread is real.

### 3. Write the assignment (`README.md`)

- **Prerequisites** — REQUIRED as the first section. A fresher should be able to set up
  their machine for this topic from this section alone, without asking anyone. For each
  tool the topic needs: a one-line **verify** command, then install steps for **Windows,
  macOS, and Linux**. Cover all three OSes even if most interns use one — you don't know
  who'll land on what. For a tiered topic, put prerequisites in each **level's** README
  (they differ by level — e.g. Linux L1 needs only a terminal, L3 needs Docker). See
  [TEMPLATE/README.md](TEMPLATE/README.md) for the format.
- **What to build** — concrete and scoped. One small project, not a sprawling one.
- **Deliverables** — exactly which files/outputs the intern must produce.
- **Context** — why this skill matters for the startup's stack.

### 4. Write the constraints (`constraints.md`)

This is the most important file. Constraints check **behavior**, not implementation.
Each one must be manually verifiable with no judgment calls. Use this format:

```markdown
- [ ] **C1: <short name>**
  - How to verify: <exact command or action to run>
  - Pass if: <observable condition>
  - Fails if: <observable condition>
```

Constraint-writing rules:

- **One behavior per constraint.** Don't bundle "starts up AND returns 200" into one.
- **Verify is concrete.** Give the exact command or steps, not "try it."
- **Pass/Fails are observable.** "It works" is not a condition. "GET /health returns
  200 within 500ms" is.
- **High-level, not prescriptive.** Check the *what*, not the *how*. Don't constrain
  language/library choice unless the constraint is literally about that choice.
- Aim for 4–8 constraints per topic. Fewer = too vague. More = intern fatigue.

### 5. Curate the resources (`resources.md`)

Pull the relevant rows from the master [resources.md](resources.md) into the topic's
`resources.md`. An intern who fails a constraint shouldn't get the whole-program
firehose — just the focused material for this topic. Add topic-specific links only if
the master list is missing something essential.

### 6. Update the index

Edit [topics/README.md](topics/README.md): change the topic's status from 🔲 TODO to
✅ READY (or 🚧 IN PROGRESS while writing). Add the folder link.

## The RESULTS.md file

Don't write content in `RESULTS.md` — it's a blank self-report template the intern fills
in. The copy in [TEMPLATE/RESULTS.md](TEMPLATE/RESULTS.md) is the canonical blank. Each
topic ships it empty.

## Quality checklist before marking READY

- [ ] Prerequisites section covers every tool the topic needs, with Windows/macOS/Linux
      install steps and a verify command each.
- [ ] Assignment is scoped to the estimated time, not 2× over.
- [ ] Every constraint is manually verifiable with concrete pass/fail criteria.
- [ ] `starter/` folder matches the declared mode (and `scratch` topics don't have one).
- [ ] `resources.md` is a focused subset, not a copy of the whole master list.
- [ ] `RESULTS.md` is the blank template.
- [ ] Topic is listed in `topics/README.md` with status ✅ READY.
- [ ] You (or someone) attempted the topic yourself and cleared every constraint.
