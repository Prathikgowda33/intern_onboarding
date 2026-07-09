# Results – Level 2 (TDD with AI)

| Constraint | Result | Evidence (command + what you observed) |
|------------|--------|-----------------------------------------|
| C1: All tests pass | PASS | Ran `pytest test_md2html.py -v`; all 12 tests passed. |
| C2: At least 10 tests | PASS | Test suite contains 12 test cases. |
| C3: Tests cover major features | PASS | Tests cover headings, bold, italic, inline code, lists, links, paragraphs, empty input, and code blocks. |
| C4: PROMPT_LOG documents TDD | PASS | ChatGPT was used to generate tests first and then implement the code. |
| C5: Tool works as CLI | PASS | `python3 md2html.py --help` displays usage and accepts CLI arguments. |
| C6: HTML output correct | PASS | Generated HTML matches expected output for all sample inputs. |
| C7: Test-first process | PASS | Tests were written first, implementation was updated until all tests passed. |

## Overall

- [x] **CLEARED** — all constraints pass. Vibe Coding topic complete.
- [ ] **Not cleared** — constraints above marked FAIL.

## Notes (optional)

AI tool used: ChatGPT

AI tool used for review (if applicable): ChatGPT

Anything else you want to note:
Used a TDD workflow: wrote tests first, implemented the Markdown converter, fixed failures, and achieved 12/12 passing tests.
