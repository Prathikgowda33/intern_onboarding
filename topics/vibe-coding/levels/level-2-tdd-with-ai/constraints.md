# Constraints — Level 2 (TDD with AI)

The acceptance checklist. Verify each constraint **manually** by running commands and observing
the result. Then record Pass/Fail + evidence in [RESULTS.md](RESULTS.md).

All commands below assume your terminal is in this folder
(`topics/vibe-coding/levels/level-2-tdd-with-ai/`).

## How to check each constraint

1. Run the **How to verify** step exactly.
2. Decide **Pass** or **Fail** using the explicit **Pass if** / **Fails if** lines.
3. Write down what you observed as evidence in [RESULTS.md](RESULTS.md).

---

## Constraints

- [ ] **C1: All tests pass**
  - How to verify: run `pytest test_md2html.py -v`.
  - Pass if: all tests PASSED, zero failed, zero errors. Exit code is 0.
  - Fails if: any test is FAILED, ERROR, or exit code is non-zero.

- [ ] **C2: At least 10 tests exist**
  - How to verify: run `pytest test_md2html.py --collect-only`.
  - Pass if: collected tests count ≥ 10. The tests cover at least 4 different Markdown
    features (headings, formatting, lists, links, etc.).
  - Fails if: fewer than 10 tests, or tests only cover 1-2 features.

- [ ] **C3: Tests cover each major feature**
  - How to verify: run `grep -n "def test_" test_md2html.py` and review test names.
  - Pass if: test names or comments indicate coverage of at least 5 features:
    headings, bold/italic, code, lists, links, paragraphs, code blocks, or edge cases.
  - Fails if: fewer than 5 distinct features covered by tests.

- [ ] **C4: PROMPT_LOG.md documents TDD process**
  - How to verify: open `PROMPT_LOG.md`.
  - Pass if: the file exists. It documents at least 4 feature cycles, each showing:
    what test you wrote, the AI prompt for implementation, and the result (pass/fail/iterate).
    The log shows a clear test→prompt→verify→iterate pattern.
  - Fails if: file doesn't exist, or doesn't document the TDD cycle, or fewer than 4
    feature cycles.

- [ ] **C5: Tool works as a CLI [ARTIFACT]**
  - How to verify: run `python3 md2html.py --help` and `python3 md2html.py test.md -o test.html`.
  - Pass if: `--help` shows usage. The tool can convert a `.md` file to `.html` without
    errors. The output HTML is valid.
  - Fails if: tool doesn't exist, crashes, or produces invalid output.

- [ ] **C6: HTML output is correct for headings and formatting**
  - How to verify: create a test file with `# Title\n**bold**\n*italic*\n- item` and run
    the tool. Inspect the output.
  - Pass if: the HTML contains `<h1>Title</h1>`, `<strong>bold</strong>`, `<em>italic</em>`,
    and `<li>item</li>` (or equivalent valid HTML for lists).
  - Fails if: any of these features produce incorrect or missing HTML.

- [ ] **C7: Tests were written before implementation (process check)**
  - How to verify: open `PROMPT_LOG.md` and review the order of operations.
  - Pass if: the log clearly shows that for at least 3 features, the test was written BEFORE
    prompting AI for implementation. The test was run and failed BEFORE the implementation
    was added.
  - Fails if: all features were implemented before tests (Level 1 approach), or the log
    doesn't show the test-first order.

---

## Summary

7 constraints. C1 checks all tests pass. C2/C3 check test count and coverage. C4 checks
the TDD process is documented. C5/C6 check the tool works and produces correct output.
C7 checks that tests were written before implementation. If any fail, see
[../../../resources.md](../../../resources.md) — especially "Test-Driven Development with AI".
