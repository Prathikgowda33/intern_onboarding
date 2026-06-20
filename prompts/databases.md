# Prompts — Databases & SQL

For the [Databases topic](../topics/databases/). Common situations: schema design, wrong
query results, JOIN confusion, window functions, transactions.

---

## Designing a schema (before writing CREATE TABLE)

**When:** you know what data you have but not how to structure the tables.

```
[CONTEXT] I'm designing a schema for <app — e.g., "a task manager with projects, tasks,
and tags"> using SQLite.
[GOAL] Tables that store <the entities> with the right relationships.

[WHAT'S HAPPENING — my understanding]
Here's what I think the entities and relationships are:
- <Entity 1> has <fields>, relates to <Entity 2> as <one-to-many / many-to-many>.
- <Entity 2> has <fields>.
I think I need <N> tables, with <foreign keys / a join table> for <the many-to-many>.

[WHAT'S WRONG — my hypothesis / what I'm unsure about>
I'm unsure about <e.g., "whether to put tags as a comma-separated string in tasks, or use
a separate task_tags table" / "whether created_at should be TEXT or DATE">.

[ASK] Before I write CREATE TABLE: review my entity design. Correct any normalization
issues (am I about to repeat data? create an update anomaly?). Tell me the idiomatic
schema for my use case and explain WHY each table and key exists. Don't just hand me DDL
— teach me the design reasoning. Then I'll write the SQL myself.
```

---

## Query returns wrong results (or no results)

**When:** your SELECT runs but the rows are wrong, missing, or duplicated.

```
[CONTEXT] I'm querying <table(s)> to <goal — e.g., "find all overdue pending tasks">.
[GOAL] I expected <N> rows matching <criteria>.
[ACTUAL] I got <M rows / 0 rows / wrong rows / duplicated rows>.

[WHAT'S HAPPENING — my understanding]
Here's what I think my query does, clause by clause:
1. FROM <table> — <starts with these rows>
2. JOIN <table> ON <cond> — <combines rows where cond matches>
3. WHERE <cond> — <filters to rows where cond is true>
4. GROUP BY <col> — <groups rows by col>
5. HAVING / ORDER BY / LIMIT — <your understanding>
Correct me where I'm wrong.

[WHAT'S WRONG — my hypothesis]
I think the bug is in <clause> because <e.g., "my WHERE compares a date string '2025-01-15'
but the stored format is different" / "my JOIN is producing a cartesian product because
the ON condition is too loose" / "GROUP BY is collapsing rows I want separate">.

[SCHEMA]
```sql
<paste relevant CREATE TABLE statements>```
[QUERY]
```sql
<paste your query>```
[SAMPLE DATA] A few rows that should/shouldn't match:
```<paste 3-5 sample rows>```

[ASK] Walk through my query with the sample data — show me the row set after each clause.
Pinpoint where the result diverges from my expectation. Give me the corrected query and
explain what my version was doing wrong. Teach me how to debug SQL like this (break the
query into pieces, inspect intermediate results).
```

---

## JOIN confusion (INNER vs LEFT vs which table is "left")

**When:** you're not sure which JOIN to use or why rows are disappearing/duplicating.

```
[CONTEXT] I have tables <A> and <B> related by <A.id = B.a_id>. I want <all A with their
B's, including A's that have no B / only A's that have a B>.
[ACTUAL] <Rows are missing / duplicated / I get NULLs where I don't expect them>.

[WHAT'S HAPPENING — my understanding]
My current understanding of JOINs:
- INNER JOIN: <your interpretation>
- LEFT JOIN: <your interpretation>
- "Left" refers to <the table before JOIN / after JOIN — state which>.
When a row in A has no matching B, <INNER/LEFT> JOIN <keeps it with NULLs / drops it>.

[WHAT'S WRONG — my hypothesis]
I think I'm using the wrong JOIN type, OR my ON condition is wrong, OR I'm joining in the
wrong direction.

[QUERY]
```sql
<paste>```
[SAMPLE] Tables A and B with a few rows each, including one A with no matching B:
```<paste>```

[ASK] First, fix my JOIN mental model (especially "which table is left"). Then for MY
data, show me what INNER vs LEFT produces — concretely, with my rows. Tell me which one
matches my goal and why. Also explain why I might be seeing duplicates (one A appearing
multiple times) and how to fix that.
```

---

## GROUP BY / aggregate gives wrong counts/sums

**When:** your COUNT/SUM/AVG is off — usually due to grouping or JOIN multiplication.

```
[CONTEXT] I want <per-project task counts / average salary per dept / total per category>.
[ACTUAL] The numbers are <too high / too low / not what I expect>.

[WHAT'S HAPPENING — my understanding]
I think GROUP BY <col> works by <your interpretation — "collapses rows with the same col
value into one row, and aggregates compute over each group">. My aggregate is <COUNT/SUM/
AVG> over <column>.

[WHAT'S WRONG — my hypothesis>
I suspect <e.g., "my JOIN to task_tags is multiplying rows — a task with 3 tags gets
counted 3 times" / "I'm grouping by the wrong column" / "COUNT(*) vs COUNT(col) differ
on NULLs">.

[QUERY]
```sql
<paste>```
[SAMPLE DATA + EXPECTED vs ACTUAL]
- Project "Alpha" has <N> tasks. I expected count <N>, got <M>.

[ASK] Confirm my GROUP BY understanding. Diagnose why my number is off — if it's JOIN
multiplication, show me exactly how the rows multiply before grouping. Give me the fix
(usually: subquery the aggregate first, then join; or COUNT DISTINCT). Explain the
principle so I recognize row-multiplication next time.
```

---

## Foreign key / constraint error on INSERT

**When:** "FOREIGN KEY constraint failed" or "UNIQUE constraint failed."

```
[CONTEXT] I'm inserting into <table> and SQLite rejected it.
[ACTUAL]
```<paste exact error>```

[WHAT'S HAPPENING — my understanding]
A FOREIGN KEY constraint means <your interpretation — "the value I'm inserting in the FK
column must already exist in the parent table's primary key">. A UNIQUE constraint means
<your interpretation>. My INSERT:
```sql
<paste>```

[WHAT'S WRONG — my hypothesis]
I think <e.g., "I'm inserting project_id=99 but there's no project with id=99" / "PRAGMA
foreign_keys isn't on so... wait, then why the error?" / "I have a duplicate value in a
UNIQUE column">.

[INFO I GATHERED]
- `SELECT * FROM <parent table> WHERE id = <value>`: <paste — does the parent row exist?>
- `PRAGMA foreign_keys;`: <0 or 1>
- Table schema: <paste CREATE TABLE>

[ASK] Explain what THIS constraint is enforcing and why my INSERT violated it. Note: SQLite
has foreign keys OFF by default — confirm whether that's relevant here. Give me the fix and
show me how to debug constraint errors in general (check the parent row exists, check for
duplicates, check PRAGMA).
```

---

## Window function (ROW_NUMBER, RANK, OVER, PARTITION BY) confusion

**When:** you're trying ranking/running totals and the syntax or output is confusing.

```
[CONTEXT] I want <rank tasks by priority within each project / running total / top-N per
group> using a window function.
[ACTUAL] <Syntax error / wrong ranks / all rows get rank 1 / partitions don't reset>.

[WHAT'S HAPPENING — my understanding]
My understanding of the window function syntax:
- `OVER (...)` defines <the "window" of rows the function operates over>
- `PARTITION BY col` <splits rows into groups per distinct col value>
- `ORDER BY col` inside OVER <determines the order for ranking>
- `ROW_NUMBER()` vs `RANK()` vs `DENSE_RANK()` differ in <your understanding>

[WHAT'S WRONG — my hypothesis]
I think <e.g., "I put ORDER BY outside the OVER clause" / "I forgot PARTITION BY so it
ranks across the whole table" / "ROW_NUMBER and RANK behave the same in my case but I'm
not sure which I want">.

[QUERY]
```sql
<paste>```
[SAMPLE OUTPUT]
```<paste — e.g., "project | task | priority | rank, with ranks not resetting per project">```

[ASK] Fix my mental model of window functions (especially PARTITION BY vs ORDER BY inside
OVER). Show me what my query produces vs what I want, with my data. Give me the corrected
query and explain each clause. Also clarify once and for all: ROW_NUMBER vs RANK vs
DENSE_RANK with a tiny example where they differ.
```

---

## Transaction isn't atomic / ROLLBACK isn't working

**When:** you expected all-or-nothing but partial data persisted after a failure.

```
[CONTEXT] I wrote a transaction (BEGIN ... INSERT ... INSERT ... COMMIT) that should be
atomic. I deliberately caused an error in the middle to test ROLLBACK.
[ACTUAL] After the error, the FIRST insert is still in the database (should have been
rolled back).

[WHAT'S HAPPENING — my understanding]
My understanding: BEGIN starts a transaction, COMMIT makes it permanent, ROLLBACK undoes
everything since BEGIN. If an error occurs mid-transaction and I ROLLBACK, no statement
in that transaction should persist.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "SQLite in the default mode auto-commits each statement, so my BEGIN didn't
actually group them" / "I caught the exception but forgot to call ROLLBACK" / "the error
I caused didn't actually trigger my except block">.

[CODE / SQL]
```<paste your transaction code — Python sqlite3 or raw SQL>```
[WHAT I DID TO TEST]
- I ran the transaction, it errored at <step>.
- Then `SELECT * FROM <table>` shows: <the first row IS there>

[ASK] Explain why my transaction wasn't atomic. Common culprits: SQLite autocommit mode
(you may need `BEGIN IMMEDIATE`), Python's sqlite3 and its implicit transaction handling,
or catching exceptions without rolling back. Diagnose my specific issue, give me the fix,
and teach me how to properly test atomicity.
```

---

## Don't understand a SQL concept (indexes, normalization, etc.)

**When:** you've heard a term but can't explain it or apply it.

```
[CONTEXT] I'm learning SQL. I keep hearing about <concept — e.g., "indexes" /
"normalization" / "EXPLAIN QUERY PLAN" / "ACID"> and I don't really get it.
[GOAL] Understand it well enough to use it in my schema/queries.

[WHAT'S HAPPENING — my current understanding]
Here's what I think `<concept>` means: <your best guess>. I'm confused about <the specific
thing — e.g., "when an index actually helps vs hurts" / "what 3NF means concretely">.

[ASK] Explain `<concept>` like I'm new to databases. Give me: (1) the plain-English "what
problem does this solve," (2) a tiny concrete example with my kind of data (tasks,
projects), (3) when to use it and when NOT to. Avoid jargon. If there's a common
misconception, call it out.
```
