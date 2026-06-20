# Level 2 — Advanced SQL

<!--
  Level metadata:
    slug: databases/level-2-advanced-sql
    skills: views, indexes, multi-table joins, window functions, transactions
    difficulty: Medium-Hard
    estimated_time: 2-3h
    starter_mode: scratch
-->

## Prerequisites

You need **SQLite** and a **terminal**. You should be comfortable with `SELECT`, `INSERT`,
`JOIN`, `WHERE`, and `GROUP BY`. If not, do Level 1 first or read the resources.

### Verify

```bash
sqlite3 --version
```

Should print a version number. SQLite 3.25.0+ is required for window functions — check with:
```bash
sqlite3 :memory: "SELECT ROW_NUMBER() OVER ();"
```

## What to build

Extend a task management database with **views** (saved queries), **indexes** (for
performance), complex **joins** across 3+ tables, **window functions** (rankings and running
totals), and **transactions** (atomic multi-step operations).

### Starting point

If you completed Level 1, use that `tasks.db` and schema as your starting point. If you skipped
Level 1, create the same schema (projects, tasks, task_tags) and populate it with at least 3
projects, 10 tasks, and 5 tag entries.

### Step-by-step

1. **Create** a file called `advanced.sql` for all your SQL statements below. Add a comment
   above each statement explaining what it does and why.
2. **Views:** Create at least 2 views:
   - `v_task_summary` — joins projects + tasks, showing project name, task title, status,
     priority. Only include pending and in_progress tasks.
   - `v_project_stats` — shows each project name, total tasks, completed tasks, and completion
     percentage.
3. **Verify** your views: `SELECT * FROM v_task_summary;` and `SELECT * FROM v_project_stats;`
   should both return rows.
4. **Indexes:** Add at least 2 strategic indexes (e.g., on `tasks.project_id`, `tasks.status`,
   or `tasks.due_date`). Use `EXPLAIN QUERY PLAN` to verify they're being used.
5. **Multi-table join:** Write a query that joins all 3 tables (projects, tasks, task_tags) and
   returns tasks with their tags in a single result set. If a task has multiple tags, it should
   appear once per tag.
6. **Window function:** Write a query using `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)`
   to rank tasks by priority within each project. Show the project name, task title, priority,
   and rank.
7. **Transaction:** Write a transaction that:
   - Creates a new project
   - Adds 2 tasks to that project
   - Either all succeed or all fail (atomicity)
   - Wrap it in `BEGIN` / `COMMIT`. Test atomicity by intentionally causing an error in the
     second `INSERT` — verify the first `INSERT` was rolled back.
8. **Write** a file called `advanced_queries.sql` containing all the queries and views.
9. **Write** a file called `explain_output.txt` showing the `EXPLAIN QUERY PLAN` output that
   proves your indexes are used.

### How to run

```bash
# Run advanced SQL (views, indexes, transactions)
sqlite3 tasks.db < advanced_queries.sql

# Verify views
sqlite3 tasks.db "SELECT * FROM v_task_summary;"
sqlite3 tasks.db "SELECT * FROM v_project_stats;"

# Check index usage
sqlite3 tasks.db "EXPLAIN QUERY PLAN SELECT * FROM tasks WHERE project_id = 1;"
sqlite3 tasks.db "EXPLAIN QUERY PLAN SELECT * FROM tasks WHERE status = 'pending';"
```

## Why this matters

Views are how production databases expose safe, pre-computed subsets of data. Indexes are what
make queries fast enough for real users. Window functions solve problems (rankings, running
totals) that would require complex subqueries otherwise. Transactions ensure data integrity
— you never want half an operation to succeed. These are power-user SQL skills that distinguish
senior developers.

## Deliverables

- `advanced_queries.sql` — all views, indexes, joins, window functions, and transaction SQL
- `explain_output.txt` — `EXPLAIN QUERY PLAN` output proving index usage
- `tasks.db` — the database with all objects created

## Starter mode: `scratch`

No starter code. You build everything from the assignment above. If you did Level 1, you can
reuse that database. If you skipped Level 1, you'll create the schema as part of this level.

## How you'll be checked

Open [constraints.md](constraints.md). Each constraint is verified by running an SQLite command
and observing the output. Self-report in [RESULTS.md](RESULTS.md). See
[../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the full workflow.

- All constraints pass → Level 2 cleared (and the whole Databases topic is cleared).
- Any constraint fails → study [../../../resources.md](../../../resources.md), fix, re-check.
