# Level 1 — AI-Assisted Build

<!--
  Level metadata:
    slug: vibe-coding/level-1-ai-assisted-build
    skills: prompting, AI code generation, code review, verification, documentation
    difficulty: Medium
    estimated_time: 2-3h
    starter_mode: scratch
-->

## Prerequisites

You need **Python 3** and an **AI coding tool** (Copilot, Cursor, Claude, ChatGPT, etc.).
See the [topic README](../../../README.md) for details.

### Verify

```bash
python3 --version
```

## What to build

Build a **Markdown to HTML converter CLI tool** using AI assistance. The tool:
- Takes a `.md` file as input
- Converts it to HTML (supporting: headings, paragraphs, bold, italic, code blocks, lists,
  links)
- Writes the HTML to an output file
- Has a `--help` flag and proper CLI argument handling

The twist: **you must use AI to help build it**, and you must document your process.

### The two deliverables beyond code

1. **PROMPT_LOG.md** — a log of every prompt you sent to the AI, the AI's response, and
   what you did with it (accepted, modified, rejected, asked follow-up).
2. **VERIFICATION.md** — a document describing how you verified the tool works: what test
   inputs you used, what outputs you expected, what you actually got, and any bugs you
   found and fixed.

### Step-by-step

1. Create this folder as your working directory.
2. Write your first prompt to the AI describing the md2html tool you want to build. Be
   specific about requirements. If you have never written a prompt for code, here is a
   starting shape you can adapt (do not just copy it verbatim; make it yours):
   > I am building a Python CLI tool called `md2html.py` that converts a Markdown file to
   > HTML. Requirements: takes an input `.md` filename and an `-o output.html` flag;
   > supports headings (#/##/###), bold (**), italic (*), inline code (backtick), unordered
   > and ordered lists, links ([text](url)), and paragraphs (blank-line separated); wraps
   > output in a basic <html><body>...</body></html> skeleton; has a --help flag via argparse.
   > Please write the full file, then explain each function. Do NOT use third-party markdown
   > libraries; I want to learn the parsing myself.
3. Review the AI's response. Copy the code into `md2html.py`. **Do not accept code without
   reading it.** (Ask the AI to explain any line you do not understand before you keep it.)
4. Test the code: `python3 md2html.py input.md -o output.html`. Does it work?
5. If it doesn't work, write a follow-up prompt describing the problem. Log it.
6. Iterate until the tool works for all required Markdown features.
7. Create test Markdown files with various features (headings, bold, lists, etc.) and verify
   the HTML output is correct.
8. Write `PROMPT_LOG.md` and `VERIFICATION.md`.

### Markdown features to support

- `# Heading 1`, `## Heading 2`, `### Heading 3`
- `**bold**` and `*italic*`
- `- item` (unordered lists) and `1. item` (ordered lists)
- `` `inline code` ``
- ` ```code blocks``` ` (fenced)
- `[text](url)` links
- Paragraphs (blank line separation)
- At least one of: blockquotes (`>`), images (`![]()`), horizontal rules (`---`) — your choice

## Why this matters

Using AI to code without reviewing the output is dangerous. This level teaches you the
discipline: prompt clearly, read carefully, verify thoroughly, and document your process. These
are the habits that make AI-assisted development productive instead of reckless.

## Deliverables

- `md2html.py` — the working CLI tool
- `PROMPT_LOG.md` — complete log of AI interactions
- `VERIFICATION.md` — test cases, expected vs actual, bugs found
- At least 2 sample `.md` test files and their corresponding `.html` outputs

## Starter mode: `scratch`

No starter code. Use AI to generate the initial code, then iterate.

## How you'll be checked

Open [constraints.md](constraints.md). Constraints are a mix of behavioral (did you use AI
correctly?), artifact (does the tool work?), and AI-judged (an AI reviews your prompting quality, since there's no human mentor).
Self-report in [RESULTS.md](RESULTS.md). See
[../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the full workflow.

- All constraints pass → Level 1 cleared (and the whole Vibe Coding topic is cleared).
- Any constraint fails → study [../../../resources.md](../../../resources.md), fix, re-check.
