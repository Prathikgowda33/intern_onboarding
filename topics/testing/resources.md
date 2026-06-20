# Resources — Testing

Shared across both Testing levels. This is a **progressive** resource list: it starts from
"why test at all?" and goes up through mocking and integration testing. **You don't read all
of it.** Find the level you're working on, read only what your failed constraints point to.

This list focuses on testing with Python/pytest specifically. The master cross-topic list is at
[../../resources.md](../../resources.md).

---

## From absolute zero (why test?)

If you've never written a test and aren't sure why you should, start here.

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Python Testing with pytest — Introduction](https://testdriven.io/blog/python-testing-with-pytest/) | Reading | C1, C2 — what testing is, why it matters, and how pytest works. Start here. |
| [Real Python — Effective Python Testing With pytest](https://realpython.com/pytest-python-testing/) | Reading | C1 — what pytest is, how to write your first test, running tests. |
| [The Pragmatic Programmer — "Test Your Software" chapter](https://www.amazon.com/Pragmatic-Programmers-Your-Journey-Anniversary/dp/0135957052) | Reading (book) | C1 — the "why" of testing from a philosophy perspective. |

**The mental model you need first:** A test is code that checks if other code works. You write
a test that calls a function with a known input, then **asserts** the output is what you expect.
If the function changes and the output becomes wrong, the test fails — catching the bug before
your users do. **pytest** is the Python framework that runs tests and reports results.

## pytest basics (Level 1)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [pytest documentation — Getting Started](https://docs.pytest.org/en/stable/gettingstarted.html) | Reading | C1, C2 — how to install pytest, write a test, and run it. |
| [pytest documentation — Assertions](https://docs.pytest.org/en/stable/how-to/assert.html) | Reading | C2 — how `assert` works in pytest, and why you don't need `self.assertEqual`. |
| [Real Python — Parametrize Your Tests](https://realpython.com/pytest-parametrize/) | Reading | C3 — `@pytest.mark.parametrize` — run the same test logic with multiple inputs. |
| [pytest documentation — Fixtures](https://docs.pytest.org/en/stable/explanation/fixtures.html) | Reading | C4 — what fixtures are and how to use `@pytest.fixture`. |

## Test design and edge cases (Level 1)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Martin Fowler — TestDouble](https://martinfowler.com/bliki/TestDouble.html) | Reading | C5 — the vocabulary of test doubles (stubs, mocks, fakes, spies). |
| [Real Python — Advanced pytest: Fixtures and Coverage](https://realpython.com/advanced-python-testing-with-pytest/) | Reading | C3, C4 — edge cases, fixtures, and test organization. |

## Mocking and integration testing (Level 2)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Real Python — Mocking in Python with unittest.mock](https://realpython.com/python-mock-library/) | Reading | C1, C2 — `patch`, `MagicMock`, return_value, side_effect. The core mocking guide. |
| [Python docs — unittest.mock](https://docs.python.org/3/library/unittest.mock.html) | Reference | C1, C2 — the official documentation for `unittest.mock`. Use this as a reference once you've read the Real Python guide. |
| [Martin Fowler — Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html) | Reading | C3, C4 — the difference between mocks and stubs, and when to use each. Important for writing meaningful tests. |
| [Testdriven.io — Integration Testing](https://testdriven.io/courses/tdd-flask/integration-testing/) | Reading | C5 — what integration tests are, how they differ from unit tests, and when to write them. |

## Test-driven thinking (Level 2)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Kent Beck — Test-Driven Development: By Example](https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530) | Reading (book) | C6, C7 — the definitive book on TDD. Read the first 3 chapters. |
| [Real Python — Test-Driven Development With Python](https://realpython.com/test-driven-development-with-python/) | Reading | C6, C7 — practical TDD workflow: write the test first, watch it fail, write the code, watch it pass. |

---

## How to use these

1. Open the `RESULTS.md` of the level you're working on and find which constraints failed.
2. Read the resource(s) next to those constraints above.
3. Fix your solution.
4. Re-run the checks in the level's `constraints.md`.
5. Update `RESULTS.md` with the new evidence.

Don't read everything top to bottom — target the gap.
