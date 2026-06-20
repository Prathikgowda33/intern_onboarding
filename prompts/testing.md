# Prompts — Testing

For the [Testing topic](../topics/testing/). Common situations: test failures, "is the bug
in my test or my code?", mocking confusion, fixtures, coverage gaps.

---

## Test fails and I can't tell if it's the test or the code

**When:** a test is red and you're not sure whether your test is wrong or your code is.

```
[CONTEXT] I'm on the Testing <level> assignment. My pytest test `<test_name>` is failing.
[GOAL] Figure out whether the bug is in my test (wrong expectation) or my code (wrong
behavior).

[WHAT'S HAPPENING — my understanding]
The test calls `<function>(<args>)` and asserts the result equals `<expected>`. I think
the function should return `<expected>` because <reasoning — e.g., "5 + 3 is 8">.

[WHAT'S WRONG — my hypothesis]
I think the bug is in <the code / the test> because <e.g., "the assertion expects 7 but
subtract(10,3) returning 7 would mean a-b, but maybe the intended behavior is b-a and the
test is right">. Honestly I'm <confident/unsure> which side is wrong.

[THE TEST]
```python
<paste the test function>```
[THE CODE UNDER TEST]
```python
<paste the function>```
[PYTEST OUTPUT]
```<paste the full failure output: the assertion line, expected vs actual>```

[ASK] Don't just tell me the answer — teach me how to decide. Walk me through: (1) what
the function actually returns for this input, (2) what the "correct" behavior should be
based on the function's name/docstring, (3) therefore whether the test or the code is
wrong. Then show me the fix on whichever side is broken.
```

---

## My tests pass but I'm not sure they actually test anything

**When:** tests are green but you suspect they're trivial or wouldn't catch real bugs.

```
[CONTEXT] All my tests pass, but I want to verify they're meaningful (not tautologies
that would pass even if the code were broken).
[GOAL] Confirm my tests would actually FAIL if my code had a bug.

[WHAT'S HAPPENING — my understanding]
A good test fails when the code is wrong and passes when the code is right. I think my
tests do this, but I'm not sure. I've heard of "mutation testing" / "deliberately breaking
the code to see if tests catch it."

[WHAT I'M WORRIED ABOUT]
- Some of my tests might be testing the wrong thing (e.g., asserting a value exists rather
  than the right value).
- Some might be so loose they'd pass with any output.

[MY TESTS]
```python
<paste your test file>```
[THE CODE]
```python
<paste the module under test>```

[ASK] Audit my test suite for "weak" tests — ones that would pass even if the code were
wrong. For each weak test, show me: why it's weak, and how to make it stronger (more
specific assertions, edge cases). ALSO: teach me the technique of deliberately breaking
the code to verify tests catch it — show me one example with my code where you'd introduce
a bug and which test should catch it.
```

---

## Don't know what to test (coverage gaps)

**When:** you've tested the happy path but don't know what edge cases to add.

```
[CONTEXT] I have tests for <function> covering <the cases I already wrote>. I need to find
edge cases I'm missing.
[GOAL] A list of test cases that would catch real bugs — not pointless ones.

[WHAT'S HAPPENING — my understanding]
I've covered: <list your existing tests — e.g., "add positive numbers, add with zero">.
I know I should test "edge cases" but I'm not sure what counts as an edge case for this
kind of function.

[THE FUNCTION]
```python
<paste>```
[MY EXISTING TESTS]
```python
<paste>```

[ASK] Give me a checklist of edge-case categories that apply to THIS function (not generic
advice). For a function like this, I should test: <have the AI enumerate — empty input,
None, negative numbers, zero, very large numbers, wrong types, boundary values, off-by-one,
etc. — and explain WHY each matters for this specific function>. Then suggest 5 concrete
test cases (with the assertion) that would meaningfully improve my coverage. Don't give me
trivial tests like "add(1,1)==2" if I already have similar.
```

---

## Mocking confusion (patch, MagicMock, what to mock)

**When:** you're testing code that calls an external service and the mock isn't working.

```
[CONTEXT] I'm testing `<function>` which calls <requests.get / an API / a database>. I'm
using unittest.mock to replace the external call, but my mock isn't being used or my test
is still making real calls.
[ACTUAL] <The test makes a real HTTP call / errors with "MagicMock has no attribute X" /
the mock's return_value isn't what my code receives>.

[WHAT'S HAPPENING — my understanding]
My understanding of mocking:
- `@patch('module.function')` <your interpretation — "replaces the function with a mock
  during the test">
- `mock.return_value` <your interpretation>
- `mock.json()` or chained attrs <your confusion>
The key gotcha I've heard: you must patch "<where it's looked up, not where it's defined>".
I'm <confident/confused> about what that means.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "I'm patching 'requests.get' but my code imported 'from requests import
get', so the name in my module's namespace is 'get' not 'requests.get'" / "my mock returns
a plain dict but my code calls .json() on the response object">.

[THE CODE UNDER TEST]
```python
<paste — including the imports>```
[THE TEST]
```python
<paste>```
[THE ERROR / BEHAVIOR]
```<paste>```

[ASK] First, explain the "patch where it's looked up" rule concretely with my code. Then
diagnose why my mock isn't intercepting the call (or is returning the wrong shape). Show
me the corrected test. Teach me the mental model: what object does my code actually see
when the mock is active, and how do I shape return_value / side_effect to match what my
code expects?
```

---

## side_effect vs return_value confusion

**When:** you're not sure which to use, or side_effect isn't doing what you want.

```
[CONTEXT] I'm mocking a function. I need it to <return a fixed value / return different
values each call / raise an exception / return success then failure>.
[ACTUAL] <Wrong behavior — e.g., "it returns the same thing every time" / "it raises
immediately instead of on the second call">.

[WHAT'S HAPPENING — my understanding]
My understanding:
- `return_value`: <your interpretation — "always returns this">
- `side_effect` with a list: <your interpretation — "returns each item in sequence?">
- `side_effect` with a function: <your interpretation>
- `side_effect` with an exception class: <your interpretation — "raises it?">

[WHAT'S WRONG — my hypothesis]
I think I'm using the wrong one, OR I misunderstand how side_effect iterates a list.

[MY MOCK SETUP]
```python
<paste — e.g., "mock.side_effect = [resp1, resp2]" or "mock.side_effect = Exception()">```

[ASK] Definitively explain return_value vs side_effect with a tiny table: "to achieve X,
use Y." For my specific goal (<return different values per call / raise on the second
call>), show me the exact mock setup and walk through what each call to the mock returns.
Clear up the common confusion (side_effect with a list returns elements one per call;
side_effect with a callable calls it).
```

---

## Fixture confusion (scope, dependencies, when they run)

**When:** your fixture runs at the wrong time, or you don't understand fixture wiring.

```
[CONTEXT] I'm using pytest fixtures and <my fixture runs once when I want per-test / my
fixture isn't being injected / I get a scope error>.
[ACTUAL] <describe the problem>.

[WHAT'S HAPPENING — my understanding]
My understanding of fixtures:
- A `@pytest.fixture` function <your interpretation — "sets up data, returns it, pytest
  injects the return value into tests that name it as a param">
- `scope="function"` vs `"session"` <your interpretation>
- Fixtures can depend on other fixtures by <naming them as params?>

[WHAT'S WRONG — my hypothesis]
I think <e.g., "my fixture has session scope so the list persists across tests and they
interfere" / "I named the fixture wrong so it's not being injected">.

[MY FIXTURE + TEST]
```python
<paste>```

[ASK] Explain fixture scope and injection with my code. Diagnose my issue. Show me the
corrected fixture and explain the lifecycle (when does setup run, when teardown, how does
pytest know to inject it). Teach me when to use a fixture vs plain setup in the test body.
```

---

## parametrize isn't doing what I expect

**When:** `@pytest.mark.parametrize` runs the wrong cases or the args don't map right.

```
[CONTEXT] I'm trying to run the same test logic over multiple inputs with parametrize.
[ACTUAL] <Wrong number of test cases / args in wrong order / unpacking error>.

[WHAT'S HAPPENING — my understanding]
My understanding of parametrize:
- `@pytest.mark.parametrize("argnames", argvalues)` <your interpretation>
- The first string lists <param names, comma-separated>
- The second arg is <a list of tuples? single values? how do they map?>

[WHAT'S WRONG — my hypothesis]
I think <e.g., "my tuples have 3 values but I only named 2 params" / "I passed a list of
lists instead of list of tuples">.

[MY CODE]
```python
<paste the parametrize decorator + test function>```
[PYTEST OUTPUT]
```<paste — collection error or wrong case count>```

[ASK] Explain parametrize with a clear example: for this decorator, exactly which test
cases get generated and what values each param gets. Fix mine and show me the pattern for
1-param vs multi-param parametrize, and how to add test IDs for readable output.
```

---

## Review my test suite for quality

**When:** tests pass but you want a quality review.

```
[CONTEXT] I finished the Testing <level> assignment. All tests pass. I want a senior review
of the test suite quality.

[WHAT'S HAPPENING — my understanding]
My suite has <N> tests covering <what>. I used <parametrize / fixtures / mocks> in these
places. I think the suite is <thorough / missing X> because <reasons>.

[THE TESTS]
```python
<paste>```
[THE CODE UNDER TEST]
```python
<paste>```

[ASK] Review as a senior would. Look for: (1) tests that are weak/tautological, (2)
missing edge cases, (3) brittle tests (would break on harmless refactors), (4) tests with
misleading names, (5) over-mocking or under-mocking. For each issue, show the problem and
the fix. Don't rewrite everything — call out the top 3-5 improvements. Also: tell me one
thing my suite does WELL so I know what to keep doing.
```
