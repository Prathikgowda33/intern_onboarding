# Resources — Databases & SQL

Shared across both Databases levels. This is a **progressive** resource list: it starts from
"what is a database?" and goes up through advanced SQL. **You don't read all of it.** Find the
level you're working on, read only what your failed constraints point to.

This list focuses on databases and SQL specifically. The master cross-topic list is at
[../../resources.md](../../resources.md).

---

## From absolute zero (what is a database?)

If you've never written SQL or don't know what a table is, start here.

| Resource | Type | Why it's here |
|----------|------|---------------|
| [SQLBolt — Introduction](https://sqlbolt.com/lesson/select) | Interactive | C1 — teaches `SELECT` in your browser. The fastest way to understand what SQL does. |
| [Khan Academy — Intro to SQL](https://www.khanacademy.org/computing/computer-programming/sql) | Reading + exercises | C1 — what a database is, what a table is, rows and columns. Gentle and beginner-friendly. |
| [W3Schools — SQL Intro](https://www.w3schools.com/sql/sql_intro.asp) | Reading | C1 — what SQL is, what RDBMS means, and the basic idea of querying data. |

**The mental model you need first:** A **database** contains **tables**. A table has **columns**
(the fields — like "name", "email") and **rows** (the records — one per entity). SQL is the
language you use to **create** tables, **insert** data, and **query** (ask questions about) it.
SQLite is a database that lives in a single file — no server to install.

## Schema design and CRUD (Level 1)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [SQLBolt — Creating Tables](https://sqlbolt.com/lesson/create_tables) | Interactive | C1, C2 — `CREATE TABLE`, column types, `PRIMARY KEY`, `NOT NULL`. |
| [SQLBolt — Insert, Update, Delete](https://sqlbolt.com/lesson/insert) | Interactive | C1, C3 — `INSERT INTO`, `UPDATE`, `DELETE` — the CRUD operations. |
| [SQLBolt — Constraints](https://sqlbolt.com/lesson/select_queries_with_constraints) | Interactive | C1, C3, C4 — `WHERE`, comparison operators, filtering rows. |
| [SQLBolt — Queries with Expressions](https://sqlbolt.com/lesson/select_queries_with_expressions) | Interactive | C1, C3 — `COUNT()`, `SUM()`, `AVG()`, `GROUP BY`. |
| [SQLBolt — Joining Tables](https://sqlbolt.com/lesson/join) | Interactive | C1, C3 — `INNER JOIN`, `ON`, connecting tables with foreign keys. |
| [SQLite Tutorial — Foreign Key](https://www.sqlitetutorial.net/sqlite-primary-key/) | Reading | C2 — how `FOREIGN KEY` constraints link tables together. |

**The mental model for Level 1:** You design tables with `CREATE TABLE`, link them with
`FOREIGN KEY`, populate them with `INSERT`, and query them with `SELECT ... WHERE ... JOIN`.
Every real app stores data this way — even the simplest to-do list needs a tasks table.

## Joins, filtering, and query correctness (Level 1)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [SQLBolt — Outer Joins](https://sqlbolt.com/lesson/outer_joins) | Interactive | C3 — `LEFT JOIN` vs `INNER JOIN`, and when to use each. |
| [SQLite Tutorial — ORDER BY](https://www.sqlitetutorial.net/sqlite-order-by/) | Reading | C3, C4 — sorting results. |
| [SQLite Tutorial — WHERE Clause](https://www.sqlitetutorial.net/sqlite-where/) | Reading | C3 — filtering with `WHERE`, `AND`/`OR`, `LIKE`, `IN`. |
| [SQLite Tutorial — GROUP BY](https://www.sqlitetutorial.net/sqlite-group-by/) | Reading | C3, C4 — grouping and aggregate functions. |

## Views and indexes (Level 2)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [SQLite Tutorial — CREATE VIEW](https://www.sqlitetutorial.net/sqlite-create-view/) | Reading | C1, C2 — what views are, why they matter, how to create them. |
| [SQLite Tutorial — CREATE INDEX](https://www.sqlitetutorial.net/sqlite-index/) | Reading | C3 — what indexes do, when to create them, and how to verify they're being used. |
| [Use The Index, Luke](https://use-the-index-luke.com/) | Reading | C3 — the definitive guide to database indexing. Read the first few chapters. |

## Window functions and transactions (Level 2)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [SQLBolt — Null & Aggregate Functions](https://sqlbolt.com/lesson/select_queries_null) | Interactive | C4, C5 — how `NULL` interacts with aggregations. |
| [Modern SQL — Window Functions](https://modern-sql.com/feature/over) | Reading | C4, C5 — `OVER()`, `PARTITION BY`, `RANK()`, `ROW_NUMBER()`. |
| [SQLite Tutorial — Window Functions](https://www.sqlitetutorial.net/sqlite-window-functions/) | Reading | C4, C5 — practical window function examples in SQLite. |
| [SQLite Tutorial — Transaction](https://www.sqlitetutorial.net/sqlite-transaction/) | Reading | C6 — `BEGIN`, `COMMIT`, `ROLLBACK`, and why transactions matter. |

---

## How to use these

1. Open the `RESULTS.md` of the level you're working on and find which constraints failed.
2. Read the resource(s) next to those constraints above.
3. Fix your solution.
4. Re-run the checks in the level's `constraints.md`.
5. Update `RESULTS.md` with the new evidence.

Don't read everything top to bottom — target the gap.
