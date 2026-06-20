# Vibe Coding

<!--
  Topic metadata:
    slug: vibe-coding
    month: 3
    skills: AI-assisted development, prompting, code review, verification, TDD with AI
    difficulty: Medium (L1) → Medium-Hard (L2)
    estimated_time: 2-4h per level
    levels: 1,2
-->

This topic is **tiered**. Vibe coding skills span from "never used AI to help me code" to
"test-first development with AI" — so pick the level that matches where you are. You only
need to clear **one** level to clear the topic.

## What is vibe coding?

**Vibe coding** is using AI coding assistants (like GitHub Copilot, Cursor, or chat-based
AI tools) to help you build software. The key skill isn't the tool — it's **knowing how to
direct AI effectively**: writing good prompts, verifying generated code, iterating, and
maintaining code quality when AI is part of your workflow.

## Pick your level

Self-assess honestly. Choose the **highest** level you think you can clear. Fail it →
drop to the level below and try again. Pass it → topic cleared, you don't need the lower
level.

| Level | For whom | What you do | Est. time |
|-------|----------|-------------|-----------|
| [1 — AI-assisted build](levels/level-1-ai-assisted-build/README.md) | Hasn't used AI to help code, or has but without structure | Build an md2html converter with AI, keeping a prompt log and verification doc | 2–3h |
| [2 — TDD with AI](levels/level-2-tdd-with-ai/README.md) | Has used AI for coding, hasn't done test-first development with AI | Build an md2html converter test-first: write tests, then have AI implement | 3–4h |

### How to decide

- **Never used an AI tool to help you write code, or just pasted AI output without reviewing it?** → Level 1.
- **You've used AI for coding but haven't tried writing tests first, then having AI implement the feature?** → Level 2.

## Prerequisites (all levels)

This topic needs a **terminal** and an **AI coding tool** (GitHub Copilot, Cursor, Claude,
ChatGPT, or any AI chat with code generation). Language runtime only — **Git Bash is fine on
Windows**.

### AI tool

- **Verify:** you have access to an AI coding tool and have used it at least once.
- Options: GitHub Copilot (VS Code extension), Cursor (AI-native editor), Claude, ChatGPT.

### Python 3

- **Verify:** `python3 --version` prints `Python 3.x.x`.
- Your md2html tool will be written in Python.

### Terminal

- **Verify:** `python3 --version` from your terminal.
- **Windows:** Git Bash. **macOS/Linux:** default terminal.

### Get this repo

```bash
git clone <this-repo-url>   # the repo's web URL — see LEARNING_PATH.md if unclear
cd intern-onboarding/topics/vibe-coding
```

## How the levels relate

Level 1 focuses on the AI coding workflow: prompting, verifying, and documenting. Level 2
adds test-first development discipline on top of AI assistance. The skills are progressive
but you can enter at either level.

Open the README inside your chosen level's folder to begin.

## Resources (shared)

[resources.md](resources.md) covers vibe coding **from absolute zero through TDD with AI**,
in one progressive list. Find your starting point there.

## How you'll be checked

Each level has its own [constraints.md](levels/level-1-ai-assisted-build/constraints.md)
with a mix of structural, behavioral, artifact, and AI-judged constraints. Self-report in
[RESULTS.md](RESULTS.md). See [../../HOW_IT_WORKS.md](../../HOW_IT_WORKS.md) for the overall workflow.
