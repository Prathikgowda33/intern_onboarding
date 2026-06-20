# Constraints — Level 1 (SQL Fundamentals)

The acceptance checklist. Verify each constraint **manually** by running an SQLite command
and observing the result. Then record Pass/Fail + evidence in [RESULTS.md](RESULTS.md).

All commands below assume your terminal is in this folder
(`topics/databases/levels/level-1-sql-fundamentals/`).

## How to check each constraint

1. Run the **How to verify** step exactly.
2. Decide **Pass** or **Fail** using the explicit **Pass if** / **Fails if** lines.
3. Write down what you observed as evidence in [RESULTS.md](RESULTS.md).

---

## Constraints

- [ ] **C1: Schema file runs without errors**
  - How to verify: run `sqlite3 tasks.db < schema.sql`.
  - Pass if: no error output. The file `tasks.db` is created (or re-created). The command
    exits with no error messages.
  - Fails if: any SQL syntax error is printed (e.g., "near ...", "no such column", "duplicate
    column name").

- [ ] **C2: Three tables exist with foreign keys**
  - How to verify: run `sqlite3 tasks.db ".schema"` and read the output.
  - Pass if: `CREATE TABLE` statements appear for at least 3 tables. At least two `FOREIGN KEY`
    constraints are present (e.g., tasks → projects, task_tags → tasks). The foreign key
    columns reference the correct parent tables.
  - Fails if: fewer than 3 tables, or no `FOREIGN KEY` constraints, or the foreign keys point
    to wrong tables.

- [ ] **C3: Queries file produces meaningful output**
  - How to verify: run `sqlite3 tasks.db < queries.sql`.
  - Pass if: query results are printed to the terminal (not empty). At least 5 queries produce
    output (one for each required query type). The results look like data rows, not errors.
  - Fails if: fewer than 5 queries produce output, or any query produces a SQL error.

- [ ] **C4: Minimum sample data populated**
  - How to verify: run `sqlite3 tasks.db "SELECT COUNT(*) FROM projects; SELECT COUNT(*) FROM tasks; SELECT COUNT(*) FROM task_tags;"`.
  - Pass if: projects count ≥ 3, tasks count ≥ 10, task_tags count ≥ 5. All three numbers are
    printed.
  - Fails if: any count is below the minimum (3, 10, or 5).

- [ ] **C5: Overdue query returns the correct task(s)**
  - How to verify: run `sqlite3 tasks.db "SELECT title, due_date, status FROM tasks WHERE status = 'pending' AND due_date < '2025-01-15';"`.
  - Pass if: at least one row is returned. The task(s) shown have `status = pending` and a
    `due_date` before `2025-01-15`.
  - **Independent check:** run `sqlite3 tasks.db "SELECT title FROM tasks WHERE status = 'pending' AND due_date < '2025-01-15';"` — same task title(s) should appear.
  - Fails if: no rows returned (meaning no overdue task was seeded correctly), or returned tasks
    have wrong status or a due_date ≥ '2025-01-15'.

- [ ] **C6: "Most tasks" query returns the correct project**
  - How to verify: run the query in `queries.sql` that finds the project with the most tasks
    (or `sqlite3 tasks.db "SELECT p.name, COUNT(t.id) as task_count FROM projects p JOIN tasks t ON p.id = t.project_id GROUP BY p.id ORDER BY task_count DESC LIMIT 1;"`).
  - Pass if: one project name is returned with a count. The count matches the actual number
    of tasks in that project.
  - **Independent check:** run `sqlite3 tasks.db "SELECT COUNT(*) FROM tasks WHERE project_id = (SELECT id FROM projects WHERE name = '<the_project_name>');"` — the count should match.
  - Fails if: no result, or the count doesn't match the actual number of tasks in that project.

- [ ] **C7: Schema and queries are readable**
  - How to verify: open `schema.sql` and `queries.sql` in your editor.
  - Pass if: each SQL statement has a comment explaining what it does. Table and column
    names are descriptive (not `t1`, `col1`). The files are formatted with consistent
    indentation and line breaks.
  - Fails if: no comments, or names are cryptic single-letter/number abbreviations.

---

## Summary

7 constraints. C1 checks the schema runs. C2 checks table structure and foreign keys. C3 checks
queries execute. C4 checks minimum data. C5 and C6 check query correctness with independent
verification. C7 checks code quality. If any fail, see [../../../resources.md](../../../resources.md)
— especially "Schema design and CRUD" or "Joins, filtering, and query correctness".
