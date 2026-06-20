# Level 1 — SQL Fundamentals

<!--
  Level metadata:
    slug: databases/level-1-sql-fundamentals
    skills: CREATE TABLE, INSERT, SELECT, WHERE, JOIN, GROUP BY, FOREIGN KEY
    difficulty: Medium
    estimated_time: 2-3h
    starter_mode: scratch
-->

## Prerequisites

You need **SQLite** and a **terminal**. Git Bash is fine on Windows — no real Linux behavior
is required. See the [topic README](../../../README.md) for installation instructions.

### Verify

```bash
sqlite3 --version
```

Should print a version number (e.g., `3.39.0`). If not, see the topic README for alternatives
(including Python's built-in `sqlite3` module).

## What to build

Design and populate a **task management database** using SQLite. You'll create tables for
projects, tasks, and tags, then write queries that answer real questions about the data.

### The schema

Create at least these tables:

- **projects** — `id` (PRIMARY KEY), `name`, `description`, `created_at`
- **tasks** — `id` (PRIMARY KEY), `project_id` (FOREIGN KEY → projects), `title`, `status`
  (one of: `'pending'`, `'in_progress'`, `'completed'`), `priority` (integer 1-5), `due_date`,
  `created_at`
- **task_tags** — `id` (PRIMARY KEY), `task_id` (FOREIGN KEY → tasks), `tag` (text, e.g.,
  `'urgent'`, `'backend'`, `'frontend'`)

### Step-by-step

1. **Create** a file called `schema.sql` in this folder. Write all `CREATE TABLE` statements
   there. Use `FOREIGN KEY` constraints to link tasks to projects and task_tags to tasks.
   **Important SQLite gotcha:** foreign keys are **OFF by default** in SQLite. To actually
   enforce them (so you can't insert a task pointing at a nonexistent project), put this at
   the top of your `schema.sql`:
   ```sql
   PRAGMA foreign_keys = ON;   -- must be set per-connection to enforce FKs
   ```
   (Without this, SQLite accepts the `FOREIGN KEY` syntax but doesn't check it — your
   constraint C2 will pass either way, but real databases enforce FKs, so do it properly.)
2. **Run** your schema: `sqlite3 tasks.db < schema.sql`. This creates the database file.
3. **Insert** sample data:
   - At least 3 projects
   - At least 10 tasks spread across projects (vary statuses and priorities)
   - At least 5 tag entries linking tasks to tags
4. **Make** at least one task have `due_date = '2025-01-15'` and `status = 'pending'` — this
   is your "overdue" task for constraint C5. (Yes, 2025-01-15 is a fixed date in the past —
   it's deliberately hardcoded so the overdue check in C5 is deterministic. Don't use
   "today's date" — use this exact value, and make the due_date *before* it.)
5. **Write** a file called `queries.sql` containing all the queries below (one query per
   requirement). Add a comment above each query explaining what it does.
6. **Queries to include:**
   - All tasks in a specific project
   - All pending tasks sorted by priority (highest first)
   - Count of tasks per project
   - Tasks that are overdue (status = 'pending' AND due_date < today — use `'2025-01-15'`
     as "today" so the overdue task is deterministic)
   - The project with the most tasks

### How to run

Put your `INSERT` statements (from step 3) in a file called **`seed.sql`**, then:

```bash
# Create and populate the database
sqlite3 tasks.db < schema.sql
sqlite3 tasks.db < seed.sql

# Run individual queries
sqlite3 tasks.db < queries.sql

# Or open the interactive console
sqlite3 tasks.db
```

### Error handling

If a query produces an error, read the error message — SQLite tells you exactly what's wrong.
Common issues: misspelled column names, missing commas, wrong table names.

## Why this matters

Every web app, mobile app, and backend service stores data in a database. Understanding how to
design a schema (not just "make it work"), write correct queries, and use foreign keys is a
foundational skill. You'll do this every day at a startup.

## Deliverables

- `schema.sql` — all `CREATE TABLE` statements with foreign keys
- `seed.sql` — all `INSERT` statements populating sample data
- `queries.sql` — all required queries with comments
- `tasks.db` — the resulting SQLite database file

## Starter mode: `scratch`

No starter code. You build everything from the assignment above. The constraints check your
SQL schema, data, and query results — not the content of your files.

## How you'll be checked

Open [constraints.md](constraints.md). Each constraint is verified by running an SQLite command
and observing the output. Self-report in [RESULTS.md](RESULTS.md). See
[../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the full workflow.

- All constraints pass → Level 1 cleared (and the whole Databases topic is cleared).
- Any constraint fails → study [../../../resources.md](../../../resources.md), fix, re-check.
