# Results — Level 2 (Collaboration & Merge Conflicts)

Intern fills this in. See [../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the workflow.

## Constraint results

| Constraint | Result | Evidence (command + what you saw) |
|------------|--------|-----------------------------------|
| C1 | PASS | ls app.py notes/shared.md showed both files; git log --oneline main showed starter project commit |
| C2 | PASS | grep -rn '<<<<<<< \|=======$\|>>>>>>> ' . --include='*.py' --include='*.md' produced no output |
| C3 | PASS | git log --oneline --all --graph showed commit "resolve merge conflict: combine greeting changes from both branches" |
| C4 | PASS | git log --oneline --merges main showed merge commit "merge feature/improve-greeting into main" |
| C5 | PASS | python3 app.py executed successfully and printed "Hello from feature branch and team!" |
| C6 | PASS | git log --oneline --all showed only descriptive commit messages |
| C7 | PASS | git log --oneline --graph --all showed branch divergence and merge (fork + join pattern) |

## Overall

✅ CLEARED — all constraints pass. Git topic complete.

## Notes (optional)

Completed all required collaboration, conflict resolution, and merge workflow steps successfully.
