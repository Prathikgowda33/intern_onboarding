# Resources — Vibe Coding

Shared across both Vibe Coding levels. This is a **progressive** resource list: it starts from
"what is vibe coding?" and goes up through TDD with AI. **You don't read all of it.** Find
the level you're working on, read only what your failed constraints point to.

This list focuses on AI-assisted development specifically. The master cross-topic list is at
[../../resources.md](../../resources.md).

---

## From absolute zero (what is vibe coding?)

If you've never used AI to help you write code, start here.

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Andrej Karpathy — Vibe Coding blog post](https://x.com/Andrej_Karpathy/status/1893482229184008657) | Reading | C1 — the origin of the term "vibe coding". The mindset in one post. |
| [GitHub Copilot Docs — Getting Started](https://docs.github.com/en/copilot/getting-started) | Reading | C1, C2 — how to set up and use GitHub Copilot in your editor. |
| [Cursor Documentation](https://docs.cursor.com/) | Reading | C1, C2 — if using Cursor (AI-native editor), start here. |

**The mental model you need first:** Vibe coding means you describe what you want in natural
language, AI generates code, and **you verify it works**. You're the architect and reviewer —
AI is the drafter. The key skills are: writing clear prompts, reading and understanding the
generated code, testing it, and iterating when it doesn't do what you want. You never blindly
accept AI output.

## Effective prompting (Level 1)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [OpenAI — Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) | Reading | C1, C2 — strategies for writing better prompts: be specific, provide context, give examples. |
| [Google — Prompt Engineering for Developers](https://ai.google.dev/gemini-api/docs/prompting-intro) | Reading | C1 — practical prompting techniques for code generation. |
| [How to Review AI-Generated Code](https://github.blog/developer-skills/github-copilot/how-to-effectively-review-code-from-github-copilot/) | Reading | C3, C5 — what to look for when reviewing AI output: correctness, security, style, edge cases. |

## Verification and quality (Level 1)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Testing Python — pytest Quickstart](https://docs.pytest.org/en/stable/gettingstarted.html) | Reading | C5, C6 — how to run tests to verify your AI-generated code works. |
| [Python — argparse](https://docs.python.org/3/library/argparse.html) | Reference | C5, C6 — the `argparse` module for building CLI tools (your md2html tool will use it). |

## Test-Driven Development with AI (Level 2)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Real Python — Test-Driven Development with Python](https://realpython.com/test-driven-development-with-python/) | Reading | C1, C2 — the TDD workflow: write the test first, watch it fail, write the code, watch it pass. |
| [Kent Beck — Test-Driven Development](https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530) | Reading (book) | C1 — the definitive book on TDD philosophy. Read the first 2 chapters. |
| [Using AI for TDD](https://martinfowler.com/articles/ai-tdd.html) | Reading | C1, C3, C4 — how to combine TDD with AI: you write tests, AI implements the feature to pass them. |

---

## How to use these

1. Open the `RESULTS.md` of the level you're working on and find which constraints failed.
2. Read the resource(s) next to those constraints above.
3. Fix your approach or solution.
4. Re-run the checks in the level's `constraints.md`.
5. Update `RESULTS.md` with the new evidence.

Don't read everything top to bottom — target the gap.
