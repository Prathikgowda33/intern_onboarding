# Constraints — Level 2 (Advanced SQL)

The acceptance checklist. Verify each constraint **manually** by running an SQLite command
and observing the result. Then record Pass/Fail + evidence in [RESULTS.md](RESULTS.md).

All commands below assume your terminal is in this folder
(`topics/databases/levels/level-2-advanced-sql/`).

## How to check each constraint

1. Run the **How to verify** step exactly.
2. Decide **Pass** or **Fail** using the explicit **Pass if** / **Fails if** lines.
3. Write down what you observed as evidence in [RESULTS.md](RESULTS.md).

---

## Constraints

- [ ] **C1: Two views exist and return data**
  - How to verify: run `sqlite3 tasks.db "SELECT name FROM sqlite_master WHERE type='view';"` then
    `sqlite3 tasks.db "SELECT COUNT(*) FROM v_task_summary;"` and `sqlite3 tasks.db "SELECT COUNT(*) FROM v_project_stats;"`.
  - Pass if: at least 2 views are listed in `sqlite_master`. Both views return a count ≥ 0
    without error. `v_task_summary` filters by status (only pending/in_progress). `v_project_stats`
    shows per-project counts.
  - Fails if: fewer than 2 views, or either view returns a SQL error.

- [ ] **C2: v_task_summary filters correctly**
  - How to verify: run `sqlite3 tasks.db "SELECT DISTINCT status FROM v_task_summary;"`.
  - Pass if: the output shows only `pending` and/or `in_progress`. No `completed` status appears.
  - **Independent check:** run `sqlite3 tasks.db "SELECT status, COUNT(*) FROM tasks GROUP BY status;"` — the completed count should NOT appear in v_task_summary.
  - Fails if: `completed` appears in the view's results.

- [ ] **C3: At least 2 indexes exist**
  - How to verify: run `sqlite3 tasks.db "SELECT name, tbl_name FROM sqlite_master WHERE type='index' AND name NOT LIKE 'sqlite_%';"`.
  - Pass if: at least 2 non-auto indexes are listed. They are on meaningful columns
    (e.g., `tasks.project_id`, `tasks.status`, `tasks.due_date` — not just the primary key).
  - Fails if: fewer than 2 indexes, or indexes are only on primary key columns that SQLite
    auto-creates.

- [ ] **C4: Indexes are used by queries**
  - How to verify: run `sqlite3 tasks.db "EXPLAIN QUERY PLAN SELECT * FROM tasks WHERE project_id = 1;"` (or whichever column you indexed).
  - Pass if: the output contains `SEARCH` or `USING INDEX` or `USING COVERING INDEX` for at
    least one of your custom indexes. The index name you created appears in the output.
  - Fails if: only `SCAN TABLE` appears (meaning SQLite is doing a full table scan instead of
    using your index).

- [ ] **C5: Three-table join returns correct results**
  - How to verify: run the multi-table join query from `advanced_queries.sql` that joins
    projects, tasks, and task_tags.
  - Pass if: results include columns from all 3 tables (project name, task title, tag). Tasks
    with multiple tags appear once per tag. No duplicate rows beyond the expected tag
    multiplication.
  - **Independent check:** run `sqlite3 tasks.db "SELECT t.title, tt.tag FROM tasks t JOIN task_tags tt ON t.id = tt.task_id;"` — the task-tag pairs should match your join query.
  - Fails if: no results, or results don't include all 3 tables, or unexpected duplicates.

- [ ] **C6: Window function ranks tasks correctly**
  - How to verify: run the ranking query from `advanced_queries.sql` that uses
    `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)`.
  - Pass if: results show a rank column with sequential numbers (1, 2, 3...) within each
    project. The rank of 1 goes to the highest-priority task in each project. Each project's
    ranking starts over at 1.
  - **Independent check:** for any one project, verify manually that the task with rank 1 has
    the highest priority number: `sqlite3 tasks.db "SELECT title, priority FROM tasks WHERE project_id = <id> ORDER BY priority DESC LIMIT 1;"` — title should match.
  - Fails if: no rank column, or ranks don't start at 1 per project, or the highest-priority
    task doesn't have rank 1.

- [ ] **C7: Transaction is atomic**
  - How to verify: run the transaction test from your `advanced_queries.sql` that intentionally
    causes an error mid-transaction. Before the error test, run the successful version first to
    create the test project and tasks.
  - Pass if: when an error occurs mid-transaction, `ROLLBACK` prevents the first INSERT from
    persisting. Running `SELECT * FROM projects WHERE name = '<test_project_name>'` returns
    no rows after the failed transaction. The successful transaction (without error) creates
    both the project and its tasks.
  - Fails if: partial data persists after a failed transaction (missing ROLLBACK).

---

## Summary

7 constraints. C1/C2 check views exist and filter correctly. C3/C4 check indexes exist and
are used. C5 checks multi-table joins. C6 checks window functions with independent verification.
C7 checks transaction atomicity. If any fail, see [../../../resources.md](../../../resources.md)
— especially "Views and indexes" or "Window functions and transactions".
