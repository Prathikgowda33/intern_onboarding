# Results — Level 1 (SQL Fundamentals)

| Constraint | Result | Evidence (command + what you observed) |
|------------|--------|--------------------------------------|
| C1: Schema runs without errors | PASS | sqlite3 tasks.db < schema.sql executed without errors and created tasks.db |
| C2: Three tables with foreign keys | PASS | sqlite3 tasks.db ".schema" showed projects, tasks, task_tags with FOREIGN KEY constraints |
| C3: Queries produce output | PASS | sqlite3 tasks.db < queries.sql returned rows for all required queries |
| C4: Minimum sample data | PASS | Counts returned: projects=3, tasks=10, task_tags=6 |
| C5: Overdue query correctness | PASS | Returned Design homepage \| 2025-01-10 \| pending |
| C6: "Most tasks" query correctness | PASS | Returned Website Redesign \| 4 and count matched actual tasks |
| C7: Schema and queries are readable | PASS | schema.sql and queries.sql contain comments, descriptive names and proper formatting |

## Overall

✅ CLEARED — all constraints pass. Databases topic complete.

## Notes (optional)

Created a task management database with projects, tasks and task_tags tables, populated sample data and verified all required SQL queries.
