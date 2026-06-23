# Results — Level 1 (Local Git Fundamentals)

Intern fills this in. See [../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the workflow.

## Constraint results

| Constraint | Result | Evidence (command + what you saw) |
|------------|--------|-----------------------------------|
| C1 | PASS | ls -R showed README.md, notes.md, summary.md, scripts/hello.sh and .git directory |
| C2 | PASS | git log --oneline main showed meaningful commits with descriptive messages |
| C3 | PASS | git log --oneline --all --graph showed branch add-summary diverging and merging back into main |
| C4 | PASS | Feature branch add-summary had 2 commits before merge |
| C5 | PASS | git log --oneline --merges main showed merge commit "merge add-summary feature" |
| C6 | PASS | git log --oneline --graph --all showed clear fork and merge history |

## Overall

✅ CLEARED — all constraints pass. Git topic complete.

## Notes (optional)

Completed all required Git branching, commit, and merge workflow steps.
