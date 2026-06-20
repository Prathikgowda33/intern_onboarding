# Prompt Library

Copy-paste prompt templates for every topic in the program. Each file has 8-15 prompts
tuned to the specific situations you'll hit in that topic — debugging, learning concepts,
reviewing your work, recovering from mistakes.

## How to use this

1. **Don't read these top to bottom.** Open the file for the topic you're working on.
2. **Find the prompt that matches your situation** (each is labeled by scenario).
3. **Copy it, fill in the `<brackets>`, paste into Claude/ChatGPT/Gemini.**
4. **Adapt it.** These are starting points — add your specific context, remove parts that
   don't apply, ask follow-up questions.

The prompts follow the pattern from [../SELF_HELP.md](../SELF_HELP.md): always give
context, paste the real error, and (importantly) **state what you think is happening and
what you think is wrong before asking for a fix**. That diagnosis step makes the AI's
answer dramatically better — and often solves the problem before you even send.

## The universal template (start here)

For any debugging situation, this works regardless of topic:

```
[CONTEXT] I'm working on <what you're building> as part of <which topic/level>.
[GOAL] I expected <X> to happen.
[ACTUAL] Instead, <Y> happened.

[WHAT'S HAPPENING — my understanding]
Here's what I think my code does, step by step:
1. <step>
2. <step>
3. <step>
If any of this is wrong, correct me before fixing anything.

[WHAT'S WRONG — my hypothesis]
I think the problem is <your best guess>. I'm <confident / unsure> because <reasoning>.

[CODE]
```<paste code>```
[ERROR] When I run `<exact command>`, I get:
```<paste full error>```
[TRIED] I've already tried: <X, Y, Z>.

[ASK] First, tell me if my understanding and hypothesis are correct. Then explain the
real cause in plain English. Then show me the fix and explain why it works.
```

The topic-specific files below are **variations** on this — tuned to the common failure
modes of each topic. Use the universal template when no specific one fits.

## Index

| Topic | File | What's inside |
|-------|------|---------------|
| Linux | [linux.md](linux.md) | Permissions errors, command not found, scripting bugs, `grep`/`awk`/`sed` confusion |
| Git | [git.md](git.md) | History confusion, merge conflicts, undo mistakes, branch recovery |
| Python | [python.md](python.md) | Logic bugs, CLI/argparse, file I/O, CSV/JSON parsing, tracebacks |
| Databases | [databases.md](databases.md) | Schema design, wrong query results, JOINs, window functions |
| Testing | [testing.md](testing.md) | Test failures, "is it the test or the code?", mocking, fixtures |
| HTTP/API | [http-api.md](http-api.md) | Wrong status codes, validation, routing, curl debugging |
| Web app | [web-app.md](web-app.md) | Flask templates, React state, CORS, frontend-backend integration |
| Docker | [docker.md](docker.md) | Dockerfile build failures, compose networking, container crashes |
| Deployment | [deployment.md](deployment.md) | Railway deploys, GitHub Actions, env vars, 502/errors |
| System design | [system-design.md](system-design.md) | Design doc sections, tradeoffs, scalability, AI review prompts |
| Vibe coding | [vibe-coding.md](vibe-coding.md) | Meta-prompts (prompts about prompting), verification, TDD |

## Conventions

- **`<brackets>`** = fill this in with your specific info
- **` ```code blocks``` `** = paste your actual code/error there
- Every debugging prompt asks the AI to **explain before fixing** — don't skip that
- Every prompt ends with a clear `[ASK]` so the AI knows exactly what you want

## Tips

- **If the first AI's answer is wrong or confusing, ask a different AI.** Claude and
  ChatGPT have different strengths. Don't trust the first answer blindly.
- **Iterate.** "That's closer, but now explain X" / "Make it simpler" / "What about edge
  case Y?" — the conversation is the tool.
- **Save prompts that work.** Build your own personal prompt library over time.
- **Verify everything.** AI hallucinates version numbers and API signatures. If it says
  "call `flask.foo()`", check the Flask docs.

See [../SELF_HELP.md](../SELF_HELP.md) for the full self-help playbook (when to use AI vs
web search vs forums, the 30-minute stuck protocol, etc.).
