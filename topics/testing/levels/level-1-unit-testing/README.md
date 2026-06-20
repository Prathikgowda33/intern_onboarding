# Level 1 — Unit Testing

<!--
  Level metadata:
    slug: testing/level-1-unit-testing
    skills: pytest, assertions, parametrize, fixtures, edge cases, reading test failures
    difficulty: Medium
    estimated_time: 2-3h
    starter_mode: fix-this
-->

## Prerequisites

You need **Python 3** and **pytest**. See the [topic README](../../../README.md) for
installation instructions.

### Verify

```bash
python3 --version && pytest --version
```

Both should print version numbers.

## What to build

The starter code contains a `calculator.py` module with **deliberate bugs** and a
`test_calculator.py` file with **incomplete and failing tests**. Your job:

1. **Read** the existing code in `starter/calculator.py` and `starter/test_calculator.py`.
2. **Run** the tests from the starter (before copying): `pytest starter/test_calculator.py -v`
   — they will fail. (This is just to see the starting state. After step 1 below you'll
   copy the files to your level folder and run `pytest test_calculator.py -v` instead.)
3. **Analyze** each failure. For each failing test, determine: is the bug in the code, in
   the test, or is a test missing entirely?
4. **Fix** the tests so they correctly test the expected behavior (some tests check the wrong
   thing).
5. **Fix** the bugs in `calculator.py` so all tests pass.
6. **Add** at least 3 additional tests covering edge cases that the existing suite misses
   (e.g., division by zero, empty strings, negative numbers, large numbers).

### The starter files

- **`starter/calculator.py`** — a module with 6 functions: `add`, `subtract`, `multiply`,
  `divide`, `percentage`, `format_result`. Several have real bugs.
- **`starter/test_calculator.py`** — 15 tests. Some are correct, some test the wrong thing,
  some are missing. Your job is to figure out which is which.

### Step-by-step

1. Copy the starter files to this level's folder:
   ```bash
   cp starter/calculator.py .
   cp starter/test_calculator.py .
   ```
2. Run `pytest test_calculator.py -v` and note which tests fail.
3. For each failure, read the error message carefully. Decide: bug in code, or bug in test?
4. Fix issues one at a time. After each fix, re-run `pytest` to see progress.
5. When all existing tests pass, identify edge cases not covered and write at least 3 more tests.
6. Run the full suite again: `pytest test_calculator.py -v`. All tests should pass.

## How to read a pytest failure (for first-timers)

When a test fails, pytest prints something like:
```
FAILED test_calculator.py::test_subtract_basic - assert 7 == -7
```
Read it as: the test `test_subtract_basic` ran an `assert` that failed — it got `-7` where
it expected `7`. The two numbers tell you what the code returned vs. what the test wanted.
**That gap is the bug** (in the code, the test, or your understanding). Look just above the
`FAILED` line for the file + line number where the assert is. Use `pytest -v` (verbose) and
`pytest --tb=short` (shorter tracebacks) to make failures readable.

## Why this matters

At a startup, you ship code fast — but if it breaks in production, you lose users. Tests are
your safety net. The hardest skill isn't writing tests — it's **knowing what to test**: edge
cases, error paths, boundary values. This level teaches you that skill by making you debug
both the code *and* the tests.

## Deliverables

- `calculator.py` — the fixed module (bugs removed, original API preserved)
- `test_calculator.py` — the fixed test suite + at least 3 new tests
- All tests passing when you run `pytest test_calculator.py -v`

## Starter mode: `fix-this`

The starter code in `starter/` has deliberate bugs in both the module and the tests. Your job
is to read the code, understand the intended behavior, fix the tests so they check the right
thing, and fix the code so the tests pass. Do **not** rewrite the module from scratch — fix
the existing code.

## How you'll be checked

Open [constraints.md](constraints.md). Each constraint is verified by running a command and
observing the output. Self-report in [RESULTS.md](RESULTS.md). See
[../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the full workflow.

- All constraints pass → Level 1 cleared (and the whole Testing topic is cleared).
- Any constraint fails → study [../../../resources.md](../../../resources.md), fix, re-check.
