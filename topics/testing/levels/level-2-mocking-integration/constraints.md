# Constraints — Level 2 (Mocking & Integration)

The acceptance checklist. Verify each constraint **manually** by running a command and observing
the result. Then record Pass/Fail + evidence in [RESULTS.md](RESULTS.md).

All commands below assume your terminal is in this folder
(`topics/testing/levels/level-2-mocking-integration/`).

## How to check each constraint

1. Run the **How to verify** step exactly.
2. Decide **Pass** or **Fail** using the explicit **Pass if** / **Fails if** lines.
3. Write down what you observed as evidence in [RESULTS.md](RESULTS.md).

---

## Constraints

- [ ] **C1: All tests pass**
  - How to verify: run `pytest test_weather_reporter.py -v`.
  - Pass if: all tests PASSED, zero failed, zero errors. Exit code is 0.
  - Fails if: any test is FAILED, ERROR, or exit code is non-zero.

- [ ] **C2: At least 7 tests written**
  - How to verify: run `pytest test_weather_reporter.py --collect-only`.
  - Pass if: collected tests count ≥ 7.
  - Fails if: fewer than 7 tests collected.

- [ ] **C3: unittest.mock.patch is used**
  - How to verify: run `grep -n "patch" test_weather_reporter.py`.
  - Pass if: `patch` appears at least once, used as a decorator or context manager on
    `requests.get` (or equivalent). The mock replaces the HTTP call.
  - Fails if: no `patch` found, or patch is used on something other than the HTTP layer.

- [ ] **C4: Error handling is tested**
  - How to verify: run `grep -n "side_effect\|raise\|Exception\|status" test_weather_reporter.py`.
  - Pass if: at least one test checks error handling — either a mock that raises an exception
    via `side_effect`, or a mock that returns an error status code. The test verifies the
    function handles the error gracefully (doesn't crash).
  - Fails if: no tests check error scenarios.

- [ ] **C5: side_effect is used for multiple returns**
  - How to verify: run `grep -n "side_effect" test_weather_reporter.py`.
  - Pass if: `side_effect` is used at least once to simulate multiple different responses
    (e.g., a list of return values, or an exception for one call and a success for another).
  - Fails if: no `side_effect` usage, or only used for a single exception (not multiple
    return values).

- [ ] **C6: Integration test exists**
  - How to verify: open `test_weather_reporter.py` and look for a test that calls multiple
    functions together (e.g., `get_current_weather` then `format_weather_report`).
  - Pass if: at least one test calls 2+ functions from `weather_reporter.py` in sequence,
    mocking only the HTTP layer. The test verifies the end-to-end result (not just a single
    function in isolation).
  - Fails if: no test calls more than one function from the module.

- [ ] **C7: No real HTTP calls in tests**
  - How to verify: run `pytest test_weather_reporter.py -v --tb=short` with no network.
    Optionally, verify by searching: `grep -n "requests.get" test_weather_reporter.py` should
    return zero results (only patched references, not direct calls).
  - Pass if: all tests pass regardless of network connectivity. No test calls `requests.get`
    directly — all calls go through mocked `patch`.
  - Fails if: any test makes a real HTTP call (would fail without internet or be flaky).

---

## Summary

7 constraints. C1 checks all tests pass. C2 checks minimum test count. C3 checks mocking is
used. C4/C5 check error handling and `side_effect` usage. C6 checks integration testing. C7
checks no real network calls. If any fail, see [../../../resources.md](../../../resources.md)
— especially "Mocking and integration testing".
