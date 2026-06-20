# Git & Collaboration

<!--
  Topic metadata:
    slug: git
    month: 1
    skills: version control, branching, merge, conflict resolution, meaningful commits
    difficulty: Easy (L1) → Medium (L2)
    estimated_time: 1-3h depending on level
    levels: 1,2
-->

This topic is **tiered**. Git skills span from "never used version control" to
"resolving merge conflicts" — so pick the level that matches where you are. You only
need to clear **one** level to clear the topic.

## Pick your level

Self-assess honestly. Choose the **highest** level you think you can clear. Fail it →
drop to the level below and try again. Pass it → topic cleared, you don't need the lower
level.

| Level | For whom | What you do | Est. time |
|-------|----------|-------------|-----------|
| [1 — Local fundamentals](levels/level-1-local-fundamentals/README.md) | Never used Git, or only knows `git clone`/`git add`/`git commit` | Build a small project using proper Git workflow — branching, meaningful commits, merging | 1–2h |
| [2 — Collaboration & conflicts](levels/level-2-collaboration/README.md) | Comfortable with local Git, hasn't resolved conflicts or done PR-style workflows | Simulate collaboration by creating a real merge conflict and resolving it cleanly | 2–3h |

### How to decide

- **Not sure what a branch is, or never used `git merge`?** → Level 1.
- **You've used branches but never had a merge conflict?** → Level 2.

If you start at Level 2 and get stuck on something Level 1 would have taught you, that's
fine — go read that section in [resources.md](resources.md), then come back.

## How the levels relate

The levels build on each other in skill, but are **independent in execution**:

- Level 2 assumes you understand commits, branches, and merging. If you don't, those are
  covered in Level 1's resources.
- Level 2 does not require GitHub — it simulates collaboration entirely within a single
  local repo (you play both "developer" and "teammate").

Open the README inside your chosen level's folder to begin.

## Resources (shared)

[resources.md](resources.md) covers Git **from absolute zero through merge conflicts**,
in one progressive list. Whatever level you're at, find your starting point there and
read outward only as far as your failed constraints require.

## How you'll be checked

Each level has its own [constraints.md](levels/level-1-local-fundamentals/constraints.md)
with manual, observable pass/fail criteria, and its own `RESULTS.md` to self-report into.
See [../../HOW_IT_WORKS.md](../../HOW_IT_WORKS.md) for the overall workflow.
