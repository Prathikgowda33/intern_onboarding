# Results – Level 1 (AI-Assisted Build)

| Constraint | Type | Result | Evidence |
|------------|------|--------|----------|
| C1: PROMPT_LOG.md with 3+ prompts | Behavioral | PASS | PROMPT_LOG.md contains multiple prompts showing AI-assisted development. |
| C2: VERIFICATION.md with test cases | Behavioral | PASS | VERIFICATION.md records test cases and expected results. |
| C3: md2html.py --help works | Artifact | PASS | python3 md2html.py --help displays usage information. |
| C4: Tool converts MD to HTML | Artifact | PASS | sample1.md and sample2.md successfully converted to HTML. |
| C5: Tool handles edge cases | Artifact | PASS | Missing file is handled gracefully with an error message. |
| C6: 2+ sample files with output | Artifact | PASS | sample1.md, sample2.md and corresponding HTML outputs created. |
| C7: Prompts show iteration | Human-judged | PASS | Prompt log demonstrates multiple iterations and improvements. |
| C8: Verification is thorough | Human-judged | PASS | Verification covers help command, conversion, and error handling. |

## Overall

- [x] **CLEARED** — all constraints pass. Vibe Coding topic complete.
- [ ] **Not cleared** — constraints above marked FAIL.

## Notes (optional)

AI tool used for build: ChatGPT

AI tool used for review (C7/C8): ChatGPT

Anything else you want to note:
The Markdown converter supports headings, lists, bold, italic, links, blockquotes, code blocks, horizontal rules, and generates valid HTML output.
