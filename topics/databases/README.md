# Databases & SQL

<!--
  Topic metadata:
    slug: databases
    month: 1
    skills: SQL, schema design, queries, indexes, views, transactions
    difficulty: Medium
    estimated_time: 2-3h per level
    levels: 1,2
-->

This topic is **tiered**. Database skills span from "never written SQL" to "optimizing
queries with indexes and window functions" — so pick the level that matches where you are.
You only need to clear **one** level to clear the topic.

## Pick your level

Self-assess honestly. Choose the **highest** level you think you can clear. Fail it →
drop to the level below and try again. Pass it → topic cleared, you don't need the lower
levels.

| Level | For whom | What you do | Est. time |
|-------|----------|-------------|-----------|
| [1 — SQL fundamentals](levels/level-1-sql-fundamentals/README.md) | Never written SQL, doesn't know what a database is | Design a schema and write queries for a task management app using SQLite | 2–3h |
| [2 — Advanced SQL](levels/level-2-advanced-sql/README.md) | Comfortable with basic SELECT/INSERT, wants indexes, views, joins, window functions | Build on the same schema with views, strategic indexes, complex joins, window functions, and transactions | 2–3h |

### How to decide

- **Not sure what `SELECT` does, or never opened a SQL console?** → Level 1.
- **You can write `SELECT * FROM table WHERE x = 1` but haven't used `JOIN`, `GROUP BY`,
  `CREATE INDEX`, or window functions?** → Level 2.

If you start at Level 2 and get stuck on something Level 1 would have taught you, that's
fine — go read that section in [resources.md](resources.md), then come back.

## Prerequisites (all levels)

This topic needs **SQLite** (zero-install) and a **terminal**. **Git Bash is fine on
Windows** — no real Linux behavior is required.

### SQLite

- **Verify:** `sqlite3 --version` prints a version.
- SQLite comes pre-installed on macOS and most Linux distros.
- **Windows (Git Bash or WSL2):** the easiest path is to use **WSL2** (from the Linux
  topic) — Ubuntu has `sqlite3` pre-installed or one command away (`sudo apt install sqlite3`).
  If you must use Git Bash: download the SQLite binary from
  <https://www.sqlite.org/download.html> (the "precompiled binaries for Windows" →
  `sqlite-tools-*.zip`), extract `sqlite3.exe` to a folder, and **add that folder to your
  PATH** (search "edit environment variables Windows" → edit PATH → add the folder →
  restart your terminal). If PATH setup is too much hassle, you can also run SQLite via
  Python's built-in module: `python3 -c "import sqlite3; print(sqlite3.sqlite_version)"` —
  but the assignment uses the `sqlite3` CLI directly, so getting the CLI working is
  worth it. **Recommendation: just use WSL2.**
- **All OSes:** if `sqlite3` is not available, Python's `sqlite3` module works:
  `python3 -c "import sqlite3; conn=sqlite3.connect(':memory:'); conn.execute('SELECT 1'); print('OK')"`

### Terminal

- **Windows:** Git Bash. **macOS:** Terminal.app. **Linux:** your default terminal.

### Get this repo

```bash
git clone <this-repo-url>   # the repo's web URL — see LEARNING_PATH.md if unclear
cd intern-onboarding/topics/databases
```

If any check fails, follow [SELF_HELP.md](../../SELF_HELP.md) before spending an hour on it — most issues solve fast with AI or a web search.

## How the levels relate

Level 2 **builds on Level 1's schema**. If you skip Level 1, you'll write the schema as
part of Level 2's work. The skills are progressive but you can enter at either level.

Open the README inside your chosen level's folder to begin.

## Resources (shared)

[resources.md](resources.md) covers databases **from absolute zero through advanced
SQL**, in one progressive list. Find your starting point there.

## How you'll be checked

Each level has its own [constraints.md](levels/level-1-sql-fundamentals/constraints.md)
with manual, observable pass/fail criteria, and its own `RESULTS.md` to self-report into.
See [../../HOW_IT_WORKS.md](../../HOW_IT_WORKS.md) for the overall workflow.
