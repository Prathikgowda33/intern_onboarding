# Level 2 — Mocking & Integration

<!--
  Level metadata:
    slug: testing/level-2-mocking-integration
    skills: unittest.mock, patch, MagicMock, side_effect, integration testing
    difficulty: Medium-Hard
    estimated_time: 2-3h
    starter_mode: scratch
-->

## Prerequisites

You need **Python 3**, **pytest**, and the **`requests`** library (the starter module uses it).
You should be comfortable with basic pytest (assertions, test functions, running `pytest`).
If not, do Level 1 first.

### Verify

```bash
python3 --version && pytest --version && python3 -c "import requests; print('requests OK')"
```

If `import requests` fails, install it: `python3 -m pip install requests` (use a venv if your
system complains — see the topic README).

## What to build

Write tests for a module that calls **external HTTP APIs**. You'll use `unittest.mock` to
replace real HTTP calls with controlled fakes, then write one small integration test.

### The starter

`starter/weather_reporter.py` contains 3 functions that call external APIs via `requests.get()`:
- `get_current_weather(city)` — calls OpenWeatherMap API
- `get_weather_summary(cities)` — calls the above for multiple cities
- `format_weather_report(city, data)` — formats a weather dict into a readable string

You write the tests. You do NOT modify `weather_reporter.py`.

### Step-by-step

1. Copy the starter: `cp starter/weather_reporter.py .`
2. Create `test_weather_reporter.py` in this folder.
3. **Write unit tests using `unittest.mock.patch`:**
   - Mock `requests.get` so it returns fake weather data without making real HTTP calls.
   - Test that `get_current_weather` correctly parses the API response.
   - Test that `get_current_weather` handles API errors (status code ≠ 200).
   - Test that `get_weather_summary` calls the API once per city.
   - Test that `format_weather_report` produces the correct string format.
4. **Write at least 2 tests using `side_effect`:**
   - Test that `get_weather_summary` handles a mix of successful and failed city lookups.
   - Test that a network timeout is handled gracefully.
5. **Write 1 integration test:**
   - Test that `get_current_weather` + `format_weather_report` work together correctly
     (call the real function, mock only the HTTP layer, verify the full pipeline).

### How to run

```bash
# Run all tests
pytest test_weather_reporter.py -v

# Run with output shown
pytest test_weather_reporter.py -v -s
```

## Why this matters

In real codebases, functions call databases, external APIs, file systems, and other services.
You can't test those functions by making real HTTP calls to real servers — it's slow, flaky,
and expensive. **Mocking** lets you replace those dependencies with controlled fakes. It's the
difference between "I tested my code" and "I tested my code in a way I can run 100 times
without it ever breaking for external reasons."

## Deliverables

- `test_weather_reporter.py` — complete test suite with mocked HTTP calls
- `weather_reporter.py` — copied from starter (unmodified)
- All tests passing when you run `pytest test_weather_reporter.py -v`

## Starter mode: `scratch` (tests only)

The `starter/weather_reporter.py` file is provided as the module under test. You write the
entire test suite from scratch. You do NOT modify the starter module — your tests must work
with the provided code.

## How you'll be checked

Open [constraints.md](constraints.md). Each constraint is verified by running a command and
observing the output. Self-report in [RESULTS.md](RESULTS.md). See
[../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the full workflow.

- All constraints pass → Level 2 cleared (and the whole Testing topic is cleared).
- Any constraint fails → study [../../../resources.md](../../../resources.md), fix, re-check.
