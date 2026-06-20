# Constraints — Level 1 (Unit Testing)

The acceptance checklist. Verify each constraint **manually** by running a command and observing
the result. Then record Pass/Fail + evidence in [RESULTS.md](RESULTS.md).

All commands below assume your terminal is in this folder
(`topics/testing/levels/level-1-unit-testing/`).

## How to check each constraint

1. Run the **How to verify** step exactly.
2. Decide **Pass** or **Fail** using the explicit **Pass if** / **Fails if** lines.
3. Write down what you observed as evidence in [RESULTS.md](RESULTS.md).

---

## Constraints

- [ ] **C1: All tests pass**
  - How to verify: run `pytest test_calculator.py -v`.
  - Pass if: the output shows all tests PASSED. The final summary says something like
    `"X passed"` with zero failed, zero errors. Exit code is 0.
  - Fails if: any test is FAILED, ERROR, or the exit code is non-zero.

- [ ] **C2: Test file has at least 18 tests (15 original + 3 new)**
  - How to verify: run `pytest test_calculator.py --collect-only`.
  - Pass if: the collected tests count is ≥ 18 (the original 15 + at least 3 you added).
    The count is shown in the summary line.
  - Fails if: fewer than 18 tests collected.

- [ ] **C3: At least one parametrized test exists**
  - How to verify: run `grep -n "parametrize" test_calculator.py`.
  - Pass if: at least one line contains `@pytest.mark.parametrize`. The parametrize
    decorator is used on a test function with at least 2 parameter sets.
  - Fails if: no `parametrize` found in the file.

- [ ] **C4: At least one fixture exists**
  - How to verify: run `grep -n "@pytest.fixture" test_calculator.py` or `grep -n "fixture" test_calculator.py`.
  - Pass if: at least one `@pytest.fixture` decorator is found in the file. A fixture
    function is defined and used by at least one test.
  - Fails if: no fixture found.

- [ ] **C5: Edge cases are tested**
  - How to verify: open `test_calculator.py` and search for tests that cover edge cases.
  - Pass if: at least 3 tests exist that cover edge cases such as: zero inputs, negative
    numbers, very large numbers, empty strings, or boundary values. The test names or
    comments indicate what edge case is being tested.
  - Fails if: no edge case tests found, or fewer than 3.

- [ ] **C6: Tests catch the original bugs**
  - How to verify: open `starter/calculator.py` and compare it with your fixed `calculator.py`.
    Identify which bugs existed in the original. Then check that your tests would have caught
    those bugs by reverting one fix at a time and running pytest.
  - Pass if: at least 3 of the original bugs in `calculator.py` are caught by failing tests
    when the fix is reverted. The tests fail for the right reason (e.g., `assert 100 == 50`
    not just a syntax error).
  - Fails if: reverting a bug fix doesn't cause any test to fail (meaning no test covers
    that bug).

- [ ] **C7: Tests are readable and well-named**
  - How to verify: open `test_calculator.py` and review the test function names and structure.
  - Pass if: test function names describe what's being tested (e.g., `test_divide_by_zero_raises_error`,
    not `test_3`). Each test tests one thing. There are comments for non-obvious test logic.
  - Fails if: test names are cryptic, or tests do multiple unrelated assertions without
    a descriptive name.

- [ ] **C8: Original API preserved**
  - How to verify: run `python3 -c "from calculator import add, subtract, multiply, divide, percentage, format_result; print('OK')"` from this folder.
  - Pass if: prints `OK` without error. All 6 original function names are importable.
  - Fails if: any import fails (function was renamed or removed).
  - **Independent check:** run `grep "^def " calculator.py` and verify the same 6 function
    names exist as in `starter/calculator.py`.

---

## Summary

8 constraints. C1 checks all tests pass. C2 checks minimum test count. C3/C4 check pytest
features (parametrize, fixtures). C5 checks edge case coverage. C6 checks that tests are
meaningful (catch real bugs). C7 checks test quality. C8 checks API compatibility. If any
fail, see [../../../resources.md](../../../resources.md) — especially "pytest basics" or
"Test design and edge cases".
