# Level 2 — CSV Data Analyzer

<!--
  Level metadata:
    slug: python/level-2-csv-analyzer
    skills: csv, json, data processing, aggregation, error handling
    difficulty: Medium
    estimated_time: 2-3h
    starter_mode: scratch
-->

## Prerequisites

**Python 3** and a **terminal**. See the topic [README.md](../../../README.md) for install
steps. No extra packages needed — this level uses only the standard library (`csv`,
`json`, `sys`).

- **Verify:** `python3 --version` prints `Python 3.x.x`.

## What to build

Build a **CSV data analyzer** that reads employee data and produces a JSON report with
statistics. The script reads a CSV file and writes a JSON file — no web server, no
database, just file-in, file-out.

### Input

A CSV file (`employees.csv`) with columns: `name`, `department`, `salary`, `years_at_company`.
A sample file is provided in `starter/employees.csv` with 20 rows of realistic data.

### Output

A JSON file (`report.json`) with this structure:

```json
{
  "departments": {
    "Engineering": {
      "avg_salary": 95000.0,
      "count": 5
    },
    "Marketing": {
      "avg_salary": 66000.0,
      "count": 4
    }
  },
  "highest_paid": {
    "name": "Carol Williams",
    "salary": 112000
  },
  "total_employees": 20
}
```

### How to run

```bash
python3 analyze.py starter/employees.csv
```

This reads `starter/employees.csv` and produces `report.json` in the current directory.

### Error handling

- If the file doesn't exist: print a clear error message and exit (no traceback).
- If a row is malformed (wrong number of columns, non-numeric salary): skip the row
  and print a warning. Don't crash.
- If the CSV has no data rows: produce a valid JSON report with zero counts.

## Why this matters

Processing data files is a daily engineering task — parsing CSVs, computing aggregates,
writing results. This level teaches you the `csv` and `json` standard library modules,
which are the tools you'll use for config files, data exports, and API payloads.

## Deliverables

- A working `analyze.py` script in this folder.
- A `report.json` produced by running the script on the sample data.

## Starter mode: `scratch`

No starter code for the script. The `starter/employees.csv` file is provided with known
data so you can verify your results. You write `analyze.py` from scratch.

## How you'll be checked

Open [constraints.md](constraints.md). Each constraint is verified by running the
script and inspecting the output. Self-report in [RESULTS.md](RESULTS.md). See
[../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the workflow.

- All constraints pass → Level 2 cleared (and the whole Python topic is cleared).
- Any constraint fails → study [../../../resources.md](../../../resources.md), fix, re-check.
