# Constraints — Level 1 (Local Git Fundamentals)

The acceptance checklist. Verify each constraint **manually** by running a Git command
and observing the result. Then record Pass/Fail + evidence in [RESULTS.md](RESULTS.md).

All commands below assume your terminal is in this folder
(`topics/git/levels/level-1-local-fundamentals/`).

## How to check each constraint

1. Run the **How to verify** step exactly.
2. Decide **Pass** or **Fail** using the explicit **Pass if** / **Fails if** lines.
3. Write down what you observed as evidence in [RESULTS.md](RESULTS.md).

---

## Constraints

- [ ] **C1: Repository initialized with project structure**
  - How to verify: run `ls -R` from this folder.
  - Pass if: at least 3 files exist in the folder structure (e.g., `notes.md`, `scripts/hello.sh`,
    `README.md`). A `.git/` directory exists (showing the repo is initialized).
  - Fails if: fewer than 3 files, or no `.git/` directory.

- [ ] **C2: At least 3 commits on main with meaningful messages**
  - How to verify: run `git log --oneline main`.
  - Pass if: at least 3 commit lines are shown on main. None of the commit messages are
    single throwaway words like "fix", "update", "wip", "stuff", or "asdf". Each message
    describes what changed (e.g., "add notes.md with initial project notes").
  - Fails if: fewer than 3 commits, or any commit message is a throwaway word.

- [ ] **C3: Feature branch exists in the history**
  - How to verify: run `git log --oneline --all --graph`.
  - Pass if: the graph shows two lines of history that diverge (one for main, one for
    the feature branch) and later rejoin. A branch name appears in the output.
  - Fails if: the graph is a single straight line with no divergence, or no branch name
    is visible.

- [ ] **C4: At least 2 commits on the feature branch before merge**
  - How to verify: run `git log --oneline --all --graph` and count the commits on the
    feature branch (the ones that diverge from main before the merge commit).
  - Pass if: at least 2 commits are on the feature branch between the divergence point
    and the merge commit.
  - Fails if: only 0 or 1 commit on the feature branch before the merge.

- [ ] **C5: Feature branch merged via `git merge`**
  - How to verify: run `git log --oneline --merges main`.
  - Pass if: at least one merge commit is shown (a commit with more than one parent line
    in the graph, typically labeled "Merge branch 'add-summary'" or similar).
  - Fails if: no merge commits found. (If the branch was fast-forwarded without a merge
    commit, re-do the merge with `--no-ff`: `git merge --no-ff add-summary`.)

- [ ] **C6: Clean, readable merge history**
  - How to verify: run `git log --oneline --graph --all`.
  - Pass if: the graph clearly shows a fork (branch creation) and a join (merge). The
    commit messages tell a coherent story — you can follow what happened without reading
    the files. No "Merge branch" messages that are the ONLY commits on the branch.
  - Fails if: the graph is confusing (e.g., a straight line because you used `--ff-only`),
    or the messages don't tell a story.

---

## Summary

6 constraints. C1 checks the project exists. C2 checks commit quality. C3/C4 check branching
(creation and commits). C5 checks merge method. C6 checks overall history quality. If any
fail, see [../../../resources.md](../../../resources.md) — especially "Commits and branching".
