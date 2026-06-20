# Level 2 — TDD with AI

<!--
  Level metadata:
    slug: vibe-coding/level-2-tdd-with-ai
    skills: test-driven development, AI implementation, pytest, test-first workflow
    difficulty: Medium-Hard
    estimated_time: 3-4h
    starter_mode: scratch
-->

## Prerequisites

You need **Python 3**, **pytest**, and an **AI coding tool**. You should have completed Level 1
(or equivalent) and understand AI-assisted coding workflow. See the [topic README](../../../README.md)
for setup.

### Verify

```bash
python3 --version && pytest --version
```

## What to build

Build the same **Markdown to HTML converter** as Level 1, but using a **test-first** approach:
you write the tests, then have AI implement the feature to pass them.

### The TDD cycle with AI

1. **Write a test** that describes the behavior you want.
2. **Run the test** — it should fail (red).
3. **Prompt AI** to implement the feature that makes the test pass.
4. **Review** the AI's code. Accept or modify.
5. **Run the test** — it should pass (green).
6. **Refactor** — clean up both test and implementation.
7. Repeat for the next feature.

### The key difference from Level 1

In Level 1, you asked AI to build the whole thing, then tested. In Level 2, **you define the
requirements as tests first**, then AI fills in the implementation. You're the architect;
AI is the implementor.

### Features to implement (test-first)

Write tests for each feature, then have AI implement. **If you have never written a pytest
test, here is what your first one (for headings) should look like:**

```python
# test_md2html.py
from md2html import convert   # the function you will have AI write

def test_h1_heading():
    assert convert("# Hello") == "<h1>Hello</h1>"

def test_h2_heading():
    assert convert("## Sub") == "<h2>Sub</h2>"
```

Run it before writing any implementation: `pytest test_md2html.py -v`. It will FAIL (the
`convert` function does not exist yet). That failure is the "red" step — now prompt the AI
to implement `convert` so the tests pass.

1. **Headings:** `# H1`, `## H2`, `### H3` → `<h1>`, `<h2>`, `<h3>`
2. **Inline formatting:** `**bold**`, `*italic*`, `` `code` ``
3. **Lists:** `- unordered`, `1. ordered` → `<ul><li>`, `<ol><li>`
4. **Links:** `[text](url)` → `<a href="url">text</a>`
5. **Paragraphs:** blank lines separate paragraphs → `<p>` tags
6. **Code blocks:** fenced with ``` → `<pre><code>`
7. **Edge cases:** empty input, only whitespace, nested formatting (optional)

### Step-by-step

1. Create `test_md2html.py` and `md2html.py` in this folder.
2. Start with feature 1 (headings): write a failing test, prompt AI to implement, verify it
   passes.
3. Move to feature 2 (inline formatting): write the test, prompt AI, verify.
4. Continue through all features.
5. Log your process in `PROMPT_LOG.md` (prompts and AI responses for each feature).
6. After all tests pass, create sample `.md` files and generate `.html` outputs.

### How to run

```bash
# Run tests
pytest test_md2html.py -v

# Run the tool
python3 md2html.py input.md -o output.html
```

## Why this matters

Test-first development ensures every feature has test coverage by design. When combined with
AI, you get the best of both worlds: you define what "correct" means (tests), and AI does
the implementation work. If AI's implementation is wrong, the tests catch it immediately.
This is how many professional developers use AI — they write tests, AI writes code.

## Deliverables

- `test_md2html.py` — the test suite (written by you, possibly with AI help)
- `md2html.py` — the implementation (written mostly by AI, reviewed by you)
- `PROMPT_LOG.md` — log of prompts and responses for each feature
- All tests passing: `pytest test_md2html.py -v`

## Starter mode: `scratch`

No starter code. You write the tests; AI writes the implementation.

## How you'll be checked

Open [constraints.md](constraints.md). Constraints check both your testing discipline and the
tool's correctness. Self-report in [RESULTS.md](RESULTS.md). See
[../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the full workflow.

- All constraints pass → Level 2 cleared (and the whole Vibe Coding topic is cleared).
- Any constraint fails → study [../../../resources.md](../../../resources.md), fix, re-check.
