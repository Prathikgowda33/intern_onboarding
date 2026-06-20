# Constraints — Level 2 (Collaboration & Merge Conflicts)

The acceptance checklist. Verify each constraint **manually** by running a Git or
Python command and observing the result. Then record Pass/Fail + evidence in
[RESULTS.md](RESULTS.md).

All commands below assume your terminal is in this folder
(`topics/git/levels/level-2-collaboration/`).

## How to check each constraint

1. Run the **How to verify** step exactly.
2. Decide **Pass** or **Fail** using the explicit **Pass if** / **Fails if** lines.
3. Write down what you observed as evidence in [RESULTS.md](RESULTS.md).

---

## Constraints

- [ ] **C1: Starter project files committed on main**
  - How to verify: run `git log --oneline main` and `ls app.py notes/shared.md`.
  - Pass if: `app.py` and `notes/shared.md` exist in the folder, and the git log shows at
    least one commit on main that includes these files.
  - Fails if: either file is missing, or no commits on main.

- [ ] **C2: No conflict markers remain in any file**
  - How to verify: run `grep -rn '<<<<<<< \|=======$\|>>>>>>> ' . --include='*.py' --include='*.md'`
    from this folder.
  - Pass if: the command produces **no output** (zero matches). No conflict markers exist
    in any `.py` or `.md` file.
  - Fails if: any line containing `<<<<<<<`, `=======` (at end of line), or `>>>>>>>`
    appears in any tracked file.

- [ ] **C3: A merge conflict resolution commit exists**
  - How to verify: run `git log --oneline --all --graph`.
  - Pass if: the graph shows a point where two branches diverge and rejoin, and there is
    a commit on the feature branch (between the divergence and the final merge to main)
    whose message indicates conflict resolution (e.g., "resolve merge conflict", "fix
    conflict", or similar).
  - Fails if: no evidence of a conflict-resolution commit, or the graph shows only a
    straight line (no conflict occurred).

- [ ] **C4: Feature branch merged into main**
  - How to verify: run `git log --oneline --merges main`.
  - Pass if: at least one merge commit is shown on main (a commit joining the feature
    branch into main).
  - Fails if: no merge commits on main.

- [ ] **C5: app.py runs without errors**
  - How to verify: run `python3 app.py` from this folder.
  - Pass if: the script exits with code 0 and prints the greeting (no traceback, no
    `SyntaxError`, no `NameError`).
  - Fails if: the command crashes with a Python error, or exits non-zero.

- [ ] **C6: All commit messages are meaningful**
  - How to verify: run `git log --oneline --all`.
  - Pass if: every commit message describes what changed or why. No single throwaway
    words ("fix", "update", "wip", "asdf", "x").
  - Fails if: any commit message is a throwaway word.

- [ ] **C7: History shows collaboration pattern**
  - How to verify: run `git log --oneline --graph --all`.
  - Pass if: the graph shows at least two branches that diverge and rejoin (fork+join
    pattern). The commit messages on each branch tell a coherent story of parallel work.
  - Fails if: the graph is a single line, or the history doesn't show two divergent lines.

---

## Summary

7 constraints. C1 checks the starter was committed. C2 checks conflicts were resolved
(no markers). C3 checks the resolution was committed. C4 checks the merge to main.
C5 checks the code still works. C6 checks commit quality. C7 checks the overall
history shows a collaboration pattern. If any fail, see [../../../resources.md](../../../resources.md).
