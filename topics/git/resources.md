# Resources — Git & Collaboration

Shared across both Git levels. This is a **progressive** resource list: it starts from
"what is version control?" and goes up through merge conflicts. **You don't read all of
it.** Find the level you're working on, read only what your failed constraints point to.

This list focuses on Git specifically. The master cross-topic list is at
[../../resources.md](../../resources.md).

---

## From absolute zero (what is version control?)

If you've never heard of Git or version control, start here.

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Git — the simple guide (no deep BS)](https://rogerdudler.github.io/git-guide/) | Reading | C1 — what Git is in plain English, in 5 minutes. Start here if you've never used version control. |
| [Pro Git book — Chapter 1: Getting Started](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) | Reading | C1 — what version control is, why it matters, the mental model of snapshots vs diffs. |
| [Pro Git book — Chapter 2: Git Basics](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository) | Reading | C1, C2 — `git init`, `add`, `commit`, `status`, `log` — the commands you need for Level 1. |

**The mental model you need first:** Git takes snapshots of your project's files. Each snapshot
is a **commit** with a message. A **branch** is a pointer to a commit — you can have multiple
branches pointing to different commits, and **merge** them back together.

## Commits and branching (Level 1)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Pro Git — Chapter 3: Git Branching](https://git-scm.com/book/en/v2/Git-Branching-Branching-in-a-Nutshell) | Reading | C2, C3, C4, C5, C6 — what branches are, how to create them, merge them, and read the history. |
| [Learn Git Branching](https://learngitbranching.js.org) | Interactive | C3, C4, C5 — visual, hands-on branching and merging exercises. This is the best way to understand what happens when you branch and merge. |
| [Conventional Commits](https://www.conventionalcommits.org/) | Reading | C2 — how to write meaningful commit messages ("add login form" not "fix stuff"). |

## Collaboration and conflicts (Level 2)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [GitHub Docs — About merge conflicts](https://docs.github.com/en/get-started/using-git/about-merge-conflicts) | Reading | C2, C3 — what merge conflicts are, why they happen, and how to resolve them. |
| [Atlassian — Resolving merge conflicts](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts) | Reading | C2 — step-by-step conflict resolution with examples. |
| [Pro Git — Chapter 3: Basic Merge Conflicts](https://git-scm.com/book/en/v2/Git-Branching-Basic-Merge-Conflicts) | Reading | C2, C3 — the definitive guide to merge conflicts from the official Git book. |
| [GitHub Docs — Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) | Reading | C4 — what PRs are and why they matter (conceptual, even though Level 2 doesn't use GitHub). |

## Commit message quality

Good commit messages are a startup cultural expectation. Every commit you push should tell
a reviewer what changed and why.

| Resource | Type | Why it's here |
|----------|------|---------------|
| [How to Write a Git Commit Message](https://cbea.ms/git-commit/) | Reading | C2, C6 — the classic guide: imperative mood, short subject line, body explains why. |
| [Conventional Commits](https://www.conventionalcommits.org/) | Reading | C2 — `feat:`, `fix:`, `docs:` prefixes for structured messages. |

---

## How to use these

1. Open the `RESULTS.md` of the level you're working on and find which constraints failed.
2. Read the resource(s) next to those constraints above.
3. Fix your solution.
4. Re-run the checks in the level's `constraints.md`.
5. Update `RESULTS.md` with the new evidence.

Don't read everything top to bottom — target the gap.
