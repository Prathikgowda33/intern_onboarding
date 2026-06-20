# Prompts — Vibe Coding (AI-Assisted Development)

For the [Vibe coding topic](../topics/vibe-coding/). This topic is *meta* — it's about
using AI well. So these prompts include **meta-prompts** (prompts about prompting),
verification prompts, and TDD-with-AI prompts.

---

## Meta-prompt: help me write a better prompt

**When:** you're stuck and want to ask an AI for help, but you don't know how to phrase it.

```
[CONTEXT] I'm stuck on <problem>. I want to ask <Claude/ChatGPT> for help but I'm not sure
how to phrase the prompt to get a good answer.
[GOAL] A well-structured prompt I can paste into an AI.

[WHAT'S HAPPENING — my situation]
Here's what I'm working on: <describe>. Here's what's wrong: <describe>. Here's what I've
tried: <list>. I have this code/error/context available: <paste if relevant>.

[ASK] Don't solve my problem yet. Help me CRAFT the prompt. (1) What context should I
include that I haven't? (2) What's the single most important question to ask? (3) Write me
a draft prompt using the [CONTEXT]/[WHAT'S HAPPENING]/[WHAT'S WRONG]/[ASK] structure from
SELF_HELP.md. (4) Tell me what makes a good vs bad prompt for this kind of problem. Then
I'll use your draft (possibly edited) to ask the other AI.
```

---

## AI generated code I don't understand — make it explain before I use it

**When:** AI gave you working code but you can't explain why it works.

```
[CONTEXT] I asked an AI for <code to do X>. It gave me this:
```<paste the AI's code>```
It <works / seems to work>, but I can't fully explain it.

[WHAT'S HAPPENING — my current understanding]
Here's what I THINK it does, line by line:
1. <your interpretation of line 1>
2. <your interpretation of line 2>
...
I'm specifically confused about <the part that mystifies you>.

[ASK] DON'T just say "looks good." Go line by line and: (1) confirm or correct my
interpretation of each line, (2) explain the part I'm confused about like I'm new to this,
(3) tell me if there's anything subtle, brittle, or non-obvious that would bite me later,
(4) tell me if there's a simpler/clearer way to write it that I'd understand better. My
goal is to UNDERSTAND it, not just ship it. If I can't explain it after this, I shouldn't
use it.
```

---

## Review AI-generated code critically before I ship it

**When:** you want a second opinion on AI code before using it.

```
[CONTEXT] I'm using AI to build <project>. An AI gave me this code for <feature>:
```<paste>```
[GOAL] A critical review before I ship it.

[WHAT'S HAPPENING — my understanding]
The code is supposed to <do X>. I've tested it and it <works for the happy path / has
issues>. I'm worried about <edge cases / security / it being non-idiomatic / subtle bugs>.

[ASK] Review this as a skeptical senior engineer. Specifically check: (1) correctness — are
there inputs that break it? edge cases? (2) security — injection, validation, secrets?
(3) idiomatic-ness — is this how an experienced dev would write it, or is it awkward/
verbose/wrong-style? (4) hidden coupling or assumptions that'll break later. For each
issue: show the problem, show the fix, explain why it matters. If parts are genuinely good,
say so. Don't rubber-stamp it.
```

---

## My AI assistant is stuck in a loop / keeps giving wrong answers

**When:** you've asked the AI 3+ times and it keeps giving broken solutions.

```
[CONTEXT] I've been trying to get an AI to help me <do X>. I've tried <N> prompts and it
keeps giving me solutions that <don't compile / have the same bug / miss the point>.
[GOAL] Break out of the loop.

[WHAT'S HAPPENING — my understanding>
My recent prompts: <summarize the last 3 prompts and what the AI gave back>. I think the
AI <misunderstands my goal / is hallucinating an API / is confidently wrong about the
domain / is missing context>.

[WHAT'S WRONG — my hypothesis>
I suspect <e.g., "my prompt is too vague so it guesses wrong" / "it's training data is
stale on this library" / "I keep accepting its framing instead of stepping back">.

[ASK] Help me reset. (1) What's likely going wrong — is it my prompt, the AI's limits, or
my approach? (2) Give me a strategy to break the loop: should I ask a different AI, reframe
the problem, simplify, or step back to basics? (3) Rewrite my prompt from scratch using
the [CONTEXT]/[WHAT'S HAPPENING]/[WHAT'S WRONG]/[ASK] structure, focused on getting UNSTUCK
rather than getting the fix. Teach me the meta-skill of recovering from a bad AI loop.
```

---

## TDD with AI: I have a test, make the AI implement to pass it

**When:** you wrote a test first (Level 2 vibe coding) and want AI to implement the feature.

```
[CONTEXT] I'm doing TDD with AI. I wrote this test FIRST (it currently fails):
```python
<paste your test>```
[GOAL] Have you implement the MINIMUM code to make this test pass.

[WHAT'S HAPPENING — my understanding>
TDD cycle: red (write failing test) → green (write minimum code to pass) → refactor. I'm
at the green step. The function under test is <name>, in module <file>. It should <behavior
described by the test>.

[ASK] Implement the minimum code to make my test pass. Constraints: (1) Don't over-engineer
— the SIMPLEST thing that passes the test, not the "proper" general solution. (2) After
implementing, explain WHY your code passes the test and walk through the execution. (3)
Tell me what additional tests I should write next to force the design to evolve (the TDD
way) — don't implement those, just name them. (4) If my test itself is wrong or incomplete,
say so before implementing.
```

---

## Verification: how do I actually confirm this AI code works?

**When:** AI gave you code and you need to verify it rigorously (for VERIFICATION.md).

```
[CONTEXT] I have this code (from an AI or myself) that's supposed to <do X>:
```<paste>```
[GOAL] A verification plan — concrete tests/inputs to PROVE it works, not just "looks ok."

[WHAT'S HAPPENING — my understanding>
I ran it once on a happy-path input and it worked. But "it ran once" isn't verification.
I need to find the cases where it would BREAK.

[ASK] Don't just say "write more tests." Give me: (1) a checklist of edge-case CATEGORIES
that apply to THIS function (empty input, None, wrong type, boundary values, very large,
unicode, concurrency, etc. — only the ones relevant here), (2) for each category, the
SPECIFIC input to try and what I should see if the code is correct, (3) one input you
predict will actually break it (and why), (4) a minimal test I can run to confirm. I'll
run these, record results in VERIFICATION.md, and fix any bugs found.
```

---

## Build a feature end-to-end with AI (scaffolding prompt)

**When:** you're starting a new feature and want AI to scaffold it, but you stay in control.

```
[CONTEXT] I'm building <feature — e.g., "a markdown to HTML converter CLI"> for the Vibe
Coding <level> assignment. I'll use AI to help, but I want to stay in control and verify
everything.
[GOAL] A plan for how to build this WITH AI, step by step, with verification at each step.

[WHAT'S HAPPENING — my understanding>
I want to break this into small pieces, have AI generate each, and verify each before
moving on. The features are: <list — e.g., "headings, bold, lists, links, code blocks">.

[ASK] DON'T write the code yet. Give me: (1) a breakdown of the feature into small,
independently-verifiable chunks (one per Markdown feature), (2) for each chunk, the order
to build it and a one-line test I can use to verify it, (3) the exact prompt I should send
to an AI for each chunk (using the good-prompt structure), (4) what to watch for at each
step (common bugs, how to verify). This is my build plan — once I approve it, I'll execute
it chunk by chunk, logging prompts in PROMPT_LOG.md.
```

---

## Review my PROMPT_LOG.md (AI judges my prompting)

**When:** you've finished a vibe-coding build and want feedback on your prompting (the AI-judged constraint).

```
[CONTEXT] I'm on the Vibe Coding <level> assignment. I built <md2html tool> with AI help
and logged every meaningful prompt in PROMPT_LOG.md. Here it is:
```<paste your PROMPT_LOG.md>```

[WHAT'S HAPPENING — my understanding>
A good prompt log shows iteration (I refined based on testing), understanding (I read and
modified AI output, didn't blindly accept), and learning (later prompts are better than
early ones). I think my log <does/doesn't> show this because <reasons>.

[ASK] You are judging the quality of my AI-assisted workflow. Score my prompting 1-5 on:
(1) Iteration — did I refine prompts based on test results, or repeat the same request?
(2) Understanding — did I read and modify AI output, or blindly accept?
(3) Specificity — were my prompts well-contextualized or vague?
(4) Learning — do the prompts improve over time?
For each dimension: cite specific entries from my log as evidence. Be critical. For
anything ≤3, tell me what a stronger version would look like. End with: did I demonstrate
the discipline of AI-assisted coding (verify, understand, iterate) or did I let the AI do
my thinking for me?
```

---

## Don't understand a vibe-coding concept

**When:** you're fuzzy on the meta-skill itself.

```
[CONTEXT] I'm learning "vibe coding" / AI-assisted development. I keep getting confused
about <concept — e.g., "when to trust AI vs verify" / "how to break work into
AI-sized pieces" / "what a 'prompt log' is really for" / "context window limits">.
[GOAL] A clear mental model.

[WHAT'S HAPPENING — my current understanding>
Here's what I think: <your best guess>. I'm confused about <the sticking point>.

[ASK] Explain `<concept>` like I'm new to using AI for coding. Give me: (1) the principle,
(2) a concrete example (good vs bad practice), (3) the failure mode if I get it wrong,
(4) a simple rule I can follow. Don't just say "verify everything" — show me what
verification actually looks like for a specific case.
```
