# Self-Help: How to Get Unstuck (AI-First)

This program is **self-directed**: there's no mentor to ping, no senior engineer over your
shoulder. Your help comes from **AI assistants** (Gemini, ChatGPT, Claude, Copilot,
Cursor), **community forums** (Stack Overflow, Reddit, GitHub Issues, Discord), **video
tutorials** (YouTube), and **official docs**. Used well, these are more than enough.

The meta-skill that matters most: **learn to ask well**. A great prompt to Claude beats a
vague question to a human. This doc is the complete playbook.

If you remember one thing: **AI is your default first stop, your own debugging is step
zero, and writing down what you tried is what makes every next step faster.**

## The 4-layer help model

```
┌─────────────────────────────────────────────────────────┐
│  Layer 0: Debug yourself (10 min)                       │ ← always start here
│  Read the error. Reproduce it. Check the topic resources.│
└───────────────────────────┬─────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────┐
│  Layer 1: AI assistants (your main tool)                │ ← 90% of help comes here
│  Gemini · ChatGPT · Claude · Copilot · Cursor           │
└───────────────────────────┬─────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────┐
│  Layer 2: Search & community (when AI is wrong/confused)│
│  Web search · Stack Overflow · Reddit · GitHub Issues   │
└───────────────────────────┬─────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────┐
│  Layer 3: Humans in forums (last resort)                │
│  Discord · Reddit · Stack Overflow (new question)       │
└─────────────────────────────────────────────────────────┘
```

**Climb one layer at a time.** Don't skip to Layer 3 when Layer 0-1 would solve it in
2 minutes. Don't get stuck on Layer 0 for an hour when Layer 1 would unblock you in
30 seconds.

---

## Layer 0: Debug yourself (10 minutes)

Before asking anyone or anything — **10 focused minutes of active debugging**. Not
staring — *acting*.

### Step 1: Read the error out loud

Error messages are written by engineers who want to help you. The answer is often in the
**first line** or the **last line before the stack trace**.

| Error | What it usually means |
|-------|----------------------|
| `ModuleNotFoundError: No module named 'flask'` | Not installed, or wrong virtualenv |
| `Connection refused` | Nothing listening on that port — is your server running? |
| `Permission denied` | Check `ls -l` and `chmod +x` |
| `command not found` | Tool not installed, or not on your PATH |
| `Cannot locate Dockerfile` | Wrong working directory, or file is named wrong |
| `KeyError: 'name'` | Your dict/JSON is missing the `name` key |

**90% of "I'm stuck" is an unread error message.**

### Step 2: Reproduce it reliably

If the error is intermittent, you can't fix it and no one can help you. Get it to happen
**every time**. Note the **exact command** and the **exact output** (copy-paste, don't
paraphrase).

### Step 3: Check the topic's `resources.md`

Every topic has a curated `resources.md` mapped to its constraints. Open it and find the
section that matches what you're stuck on. This is faster than the whole internet because
it's pre-filtered for your exact situation.

If 10 minutes of Layer 0 doesn't solve it → move to Layer 1.

---

## Layer 1: AI assistants (your main tool)

AI is where **90% of your help comes from** in this program. The skill is entirely in
**how you ask**. A bad prompt wastes your time; a good prompt gets you an answer in
seconds.

### The tools — pick by strength

| Tool | Best for | Notes |
|------|----------|-------|
| **Claude** (Anthropic) | Long code, deep reasoning, reviewing your approach, explaining concepts | Strongest at nuanced analysis and reading large codebases |
| **ChatGPT** (OpenAI) | General coding, quick scripts, debugging, Python/data | Fast, broad knowledge |
| **Gemini** (Google) | Quick lookups, current info, Python/JS, integration with Google docs | Good for "what's the current way to..." |
| **GitHub Copilot** | Inline code completion in your editor | Best for "finish this function" not "explain this error" |
| **Cursor** | AI-native editor — chat + code in one place | Combines editing + AI; great for refactors |

**If you have none of these set up yet:** start with **one free tool** — go to
[claude.ai](https://claude.ai) or [chatgpt.com](https://chatgpt.com) and sign up (free
tier is fine). You do NOT need all five — one is enough for the whole program. Copilot and
Cursor are editor integrations you can add later once you're comfortable.

**Pro tip:** If one AI gives a wrong or confusing answer, **ask another**. They have
different strengths and weaknesses. Don't trust the first answer blindly.

### How to format a prompt (for absolute beginners)

The prompts below wrap code and errors in **triple backticks** so they stay readable:

~~~
Here's my code:
```python
print("hello")
```
And the error:
```
NameError: name 'hell' is not defined
```
~~~

**How to type a backtick:** it's the key above **Tab** on most keyboards (next to **1**),
typed as `` ` ``. Three of them ```` ``` ```` open a code block, three more close it. In
Claude/ChatGPT you can also use the `</>` or "code" button in the toolbar, or just paste
your code and press Enter — the AI can usually read unformatted code too, but backticks
make errors much easier to parse.

If this feels fiddly, don't let it stop you — paste your code however you can and ask
"here's my code and error, help me fix it." Formatting is nice-to-have, not required.

### The golden rules of prompting

1. **Give context.** The AI doesn't know your project, your level, or your goal unless
   you tell it. "It doesn't work" → useless. "I'm building a Flask bookmark API and
   `POST /bookmarks` returns 500, here's the code and error" → solvable.
2. **Paste the exact error.** Not a summary — the literal text. Errors contain file
   names, line numbers, and stack traces that pinpoint the problem.
3. **Show your code.** The relevant part, formatted in a code block. If it's long, paste
   the function you're working on.
4. **Say what you tried.** "I already tried X and Y, same error" prevents the AI from
   suggesting X and Y again.
5. **One question at a time.** Don't bundle 5 questions. Solve one, verify, then ask
   the next.
6. **Never ship code you can't explain.** If the AI's fix works but you don't know why,
   ask it to explain. "Explain line by line" is one of the best prompts.
7. **Verify everything against docs.** AI hallucinates version numbers, API signatures,
   and library specifics. If it says "call `flask.foo()`", check the Flask docs.

### The universal good-prompt template

```
[CONTEXT] I'm working on <what you're building> as part of <which topic/level>.
[GOAL] I expected <X> to happen.
[ACTUAL] Instead, <Y> happened.

[WHAT'S HAPPENING — my understanding]
Here's what I think my code does, step by step:
1. <step 1 — e.g., "user POSTs JSON to /bookmarks">
2. <step 2 — e.g., "Flask reads request.json and validates title/url">
3. <step 3 — e.g., "if valid, appends to the bookmarks list and returns 201">
If any of this is wrong, correct me before fixing anything.

[WHAT'S WRONG — my hypothesis]
I think the problem is <your best guess — e.g., "the validation isn't catching empty
strings, so an empty title gets through and crashes jsonify">. I'm <confident / unsure>
about this because <reasoning>.

[CODE] Here's my code so far:
```<paste code>```
[ERROR] When I run `<exact command>`, I get:
```<paste full error>```
[TRIED] I've already tried: <X, Y, Z>.

[ASK] First, tell me if my understanding (WHAT'S HAPPENING) and my hypothesis (WHAT'S
WRONG) are correct. Then explain the real cause in plain English. Then show me the fix
and explain why it works.
```

**Why this works better than "what's wrong?":** The `[WHAT'S HAPPENING]` and
`[WHAT'S WRONG]` sections force you to **articulate your mental model before asking for
a fix**. Two things happen:

1. **You often solve it yourself.** Writing "here's what I think the code does, step by
   step" exposes the gap in your own understanding. ~30% of the time, you'll spot the
   bug while filling in this section and won't even need to send the prompt.
2. **The AI gives a much better answer.** When the AI sees your (possibly wrong)
   mental model, it can correct the *misunderstanding*, not just patch the symptom.
   "Your hypothesis is close, but you're wrong about X — here's what actually happens"
   teaches you something. "Here's the fix" doesn't.

If you genuinely can't form a hypothesis (no idea what's wrong), say so honestly:
`[WHAT'S WRONG] I have no hypothesis — I don't understand this code well enough to guess.
Help me build a mental model first, then we'll diagnose.` That's a valid, good prompt.

### 📚 The prompt library — topic-specific prompts

The universal template above handles ~80% of debugging. For the other 20%, there's a
**per-topic prompt library** at [prompts/](prompts/) — one file per topic (Linux, Git,
Python, Databases, Testing, HTTP-API, Web app, Docker, Deployment, System design, Vibe
coding), each with 8+ ready-to-copy prompts tuned to that topic's common failure modes.

**Use it like this:**

1. Open [prompts/README.md](prompts/README.md) for the index.
2. Click the file for the topic you're working on.
3. Find the prompt that matches your situation (each is labeled: "permission denied,"
   "test fails and I don't know if it's the test or the code," "container starts then
   exits," etc.).
4. Copy, fill in the `<brackets>`, paste into Claude/ChatGPT/Gemini.

The topic prompts follow the same diagnosis-first pattern as the universal template — they
ask you to state what's happening and what you think is wrong before asking for a fix.
This is deliberate: **articulating your mental model is what makes the answer good** (and
often solves the problem before you send).

The 10 general-purpose prompts below are for cross-cutting situations that don't fit a
single topic.

### The 10 most useful prompts (copy-paste these)

**1. Decode a mystery error:**
> I'm getting this error in Python:
> ```
> <paste full traceback>
> ```
> My code is:
> ```python
> <paste>
> ```
> Explain what's causing this in plain English, then show me the fix.

**2. Understand a concept you've never seen:**
> Explain `<concept>` (e.g., "CORS", "window functions in SQL", "Git rebase") like I've
> never heard of it. Use one simple analogy and one tiny code example. Don't assume I
> know related jargon — define every term you use.

**3. Sanity-check your plan before coding:**
> I need to build <X>. Here's my plan:
> 1. <step>
> 2. <step>
> 3. <step>
> What am I missing? What edge cases will trip me up? What's a simpler approach I
> haven't considered?

**4. Make AI explain its own code before you use it:**
> I ran your suggested code and it works, but I don't fully understand it. Explain each
> line, especially `<the confusing part>`. Why did you choose this approach over
> <alternative>?

**5. Review code for bugs before you ship:**
> Review this code critically. Look for: bugs, edge cases I missed, security issues,
> and style problems. Be harsh — I'd rather hear it now than in review.
> ```<paste code>```

**6. Get unstuck when AI's first answer didn't work:**
> I tried your suggestion but I'm still getting the same error. Here's exactly what I
> did: <steps>. Here's the new output: <paste>. The error persists. What else could be
> causing this? What should I check next?

**7. Ask for a worked example, not just an explanation:**
> Show me a complete, runnable example of <X> (e.g., "a Flask route that accepts JSON
> POST and returns 201"). Include the imports, the full file, and a curl command to test
> it. Then explain each part.

**8. When you don't even know what to search for:**
> I'm trying to <high-level goal> but I don't know what this technique is called or what
> to search for. Here's what I want to happen: <describe>. What's this called? What are
> the standard tools/approaches? Point me at the right keywords to research.

**9. Compare two approaches:**
> I'm deciding between <approach A> and <approach B> for <task>. Compare them: what are
> the pros/cons of each? When would you pick one over the other? Which is simpler for a
> beginner?

**10. Get a step-by-step debugging plan (not just an answer):**
> Don't just tell me the fix — teach me how to debug this myself. I have this error:
> `<paste>`. Walk me through the steps to diagnose it: what to check first, what
> commands to run, how to narrow down the cause. I want to learn the process, not just
> get the answer.

### Stage-by-stage prompting guide

Different topics need different prompts. Here's what to ask at each stage of the program.

#### Month 1 — Foundations (Linux, Git, Python, Databases, Testing)

**Linux — when a command fails or behaves weirdly:**
> I ran `<command>` on <Ubuntu/WSL2/macOS> and got:
> ```
> <output or error>
> ```
> I expected <X>. Is this a permissions issue, a path issue, or something else? Show me
> how to diagnose it with commands, not just the fix.

**Git — when history/branches are confusing:**
> Here's my `git log --oneline --graph --all` output:
> ```
> <paste>
> ```
> I'm trying to <merge a branch / resolve a conflict / undo a commit>. Walk me through
> the exact commands. Explain what each one does to my history.

**Git — recovering from a mistake (scary moment):**
> I accidentally ran `<git command>` and now <bad thing happened>. My repo state: I'm on
> branch `<X>`, last good commit was `<hash>`. How do I safely undo this WITHOUT losing
> my uncommitted work in <file>? Go slow — I'm afraid of making it worse.

**Python — when code runs but output is wrong:**
> My script runs without errors but the output is wrong. Input: `<X>`. Expected output:
> `<Y>`. Actual output: `<Z>`. Here's the code:
> ```python
> <paste>
> ```
> Where's the logic bug? Walk me through what each line does with this input.

**Databases — when a query returns wrong results:**
> My SQL query returns <wrong thing>. Here's my schema:
> ```sql
> <paste CREATE TABLE statements>
> ```
> Here's my query:
> ```sql
> <paste>
> ```
> Here's the sample data (first few rows): `<paste>`. I expected <X> rows but got <Y>.
> What's wrong with my JOIN/WHERE/GROUP BY?

**Testing — when a test fails and you don't know why:**
> My pytest test is failing. Here's the test:
> ```python
> <paste>
> ```
> Here's the code under test:
> ```python
> <paste>
> ```
> The failure output:
> ```
> <paste pytest -v output>
> ```
> Is the bug in my test or my code? How do I tell?

#### Month 2 — Web & Infra (HTTP/API, Web app, Docker, Deployment)

**HTTP/API — when an endpoint returns the wrong status:**
> My Flask endpoint returns 500 but I expected 201. Here's my route:
> ```python
> <paste>
> ```
> The curl command I'm testing with:
> ```
> curl -X POST http://localhost:5000/bookmarks -H "Content-Type: application/json" -d '{"title":"test"}'
> ```
> The full error in my Flask console:
> ```
> <paste server output>
> ```
> What's wrong?

**Web app — when frontend can't reach backend (CORS):**
> My React app (port 5173) can't fetch from my Flask API (port 5000). Browser console
> shows:
> ```
> <paste CORS error>
> ```
> I have `<this>` in my Flask app. How do I fix CORS properly? Show me the exact code
> and explain why it works.

**Docker — when a container won't start or build:**
> My Docker build fails at this step:
> ```
> <paste docker build output with the error>
> ```
> My Dockerfile:
> ```dockerfile
> <paste>
> ```
> My project structure: `<paste ls -R>`. What's wrong with the COPY/RUN/PATH?

**Docker — when containers can't talk to each other:**
> I have two containers in docker-compose: `web` and `redis`. The web container logs
> show `Redis connection refused`. My compose file:
> ```yaml
> <paste>
> ```
> I tried `docker compose exec web ping redis` and it <worked/failed>. How do I debug
> the network connection between them?

**Deployment — when the deploy fails or the URL doesn't work:**
> I deployed my Flask app to Railway. The build succeeded but `curl https://<my-url>/`
> returns `<error/timeout/502>`. Here's my Dockerfile:
> ```dockerfile
> <paste>
> ```
> Railway deploy logs:
> ```
> <paste>
> ```
> What could be wrong? (Common suspects: port, host binding, health check.)

#### Month 3 — Real work (System design, Vibe coding)

**System design — when you're stuck on a section:**
> I'm writing the "Scalability considerations" section of a design doc for a URL
> shortener. Here's what I have so far:
> ```
> <paste your draft>
> ```
> This feels shallow. What am I missing? What specific techniques should a URL shortener
> consider at 10M users vs 100M? Push back on anything that's wrong or vague.

**Vibe coding — when AI-generated code is confusing:**
> I asked an AI to generate <X> and it gave me this:
> ```<paste>```
> It works, but I want to understand it before I use it. Explain it to me like I'm a
> junior dev. Then tell me: are there bugs, edge cases, or bad practices I should fix?

**Vibe coding — when you want AI to help you write better prompts:**
> I'm stuck on <problem>. Help me write a really good prompt to ask another AI for help.
> What context should I include? Here's my situation: <describe>.

### Power-user prompting techniques

**Role prompting** — tell the AI who to be:
> You are a senior Python engineer doing a code review. Be direct and critical. Review
> this: `<paste>`.

**Chain-of-thought** — ask the AI to reason before answering:
> Think step by step. First diagnose the likely cause, then propose a fix, then explain
> how to verify the fix worked.

**Constraint setting** — tell the AI what NOT to do:
> Explain this without using the words "asynchronous", "event loop", or "callback" —
> I'm not there yet. Use plain analogies.

**Few-shot** — give examples of what you want:
> Here are two good test names: `test_divide_by_zero_raises_error`,
> `test_add_negative_numbers`. Now suggest 5 more test names for a calculator's
> `percentage()` function in the same style.

**Iterative refinement** — the conversation is the tool:
> "That's closer, but make it simpler." / "Now add error handling." / "Now explain why
> you chose try/except over an if-check." Don't expect perfection in one round.

### What AI is bad at (verify these yourself)

- **Exact version numbers and API signatures** — it will confidently say "use
  `flask.request.json`" when the real API is different. Check official docs.
- **Recent library changes** — if a library had a breaking change in the last 6-12
  months, the AI may give you the old way.
- **Your specific environment** — it doesn't know your OS version, your file paths,
  your installed versions unless you tell it.
- **"Does this work?"** — never trust "yes". **Run it.**
- **Counting and exact math** — if precision matters, verify.

### Keep a prompt log for non-trivial work

When you're building something substantial with AI help, keep a `PROMPT_LOG.md` of the
**meaningful** prompts (not every tiny one). For each entry:

- What you asked (the prompt)
- What the AI gave you (summary or full)
- What you did with it (accepted / modified / rejected — and why)

This is required for the Vibe coding topic and recommended everywhere. It helps you
trace *why your code is the way it is* when something breaks later, and it makes you a
better prompter over time because you can see what worked.

---

## Layer 2: Search & community (when AI is wrong or confused)

AI is wrong sometimes. When it gives you an answer that doesn't work after 2-3 tries, or
you suspect it's hallucinating, **go to the source**.

### Web search

Paste the **exact error message** (in quotes) into a search engine. Someone has hit this
before. Where to look, in priority order:

1. **Official docs** — the canonical answer. Python docs, Flask docs, Docker docs. Often
   the first search result for `<tool> <feature>`.
2. **Stack Overflow** — the largest Q&A archive. Look for answers with high scores and
   recent comments. Beware answers older than ~3 years for fast-moving tools (Docker,
   React).
3. **GitHub Issues** — search the tool's repo for your error. Real bugs and real fixes
   from real maintainers. `site:github.com <error>` works well.
4. **Blog posts & tutorials** — good for "how do I do X end-to-end". Quality varies;
   prefer posts from the last 2 years.

**Filter for recency.** A 2018 Docker answer may be flat-out wrong today. A 2020 React
answer predates hooks maturity. Add `after:2023` to your search or check the date.

### YouTube (when you learn better by watching)

Some people learn faster by watching than by reading. YouTube is excellent for:

- **Setup walkthroughs** — "install WSL2 on Windows 11 step by step", "set up Docker
  Desktop 2024".
- **Visual concepts** — "how Git branching works visually", "Docker containers vs
  VMs explained".
- **End-to-end builds** — "build a Flask REST API from scratch".

**Search tips:**
- Add the year for current info: `"flask rest api 2024"`.
- Sort by upload date for recent content, by rating for classics.
- Prefer videos under 30 minutes for specific tasks; longer courses for deep dives.
- **Cross-check** what the video shows against official docs — YouTubers make mistakes
  and tools change.

**Good channels by topic (verify they're current):**

| Topic | Search for / channels |
|-------|----------------------|
| Linux/bash | "linux command line tutorial", NetworkChuck, Corey Schafer |
| Git | "git branching explained", "learn git branching", Fireship |
| Python | Corey Schafer, Programming with Mosh, Tech With Tim |
| SQL/Databases | "sql tutorial", "sqlite tutorial", Mosh, freeCodeCamp |
| Testing/pytest | "pytest tutorial", "python mocking", Corey Schafer |
| Flask/APIs | "flask rest api", Corey Schafer, Tech With Tim |
| React | "react tutorial 2024", Fireship, Web Dev Simplified |
| Docker | "docker tutorial", NetworkChuck, TechWorld with Nana |
| Deployment | "deploy flask railway", "github actions tutorial" |
| System design | "system design url shortener", ByteByteGo, Gaurav Sen |
| Vibe coding/AI | "cursor tutorial", "github copilot tutorial", Fireship |

### Discord & chat communities

Real-time help from humans (Layer 3) when forums don't have your answer:

- **Python Discord** (discord.gg/python) — huge, active, beginner-friendly
- **r/learnpython**, **r/learnprogramming** (Reddit) — post your question with context
- **Flask Discord**, **Reactiflux** (React) — framework-specific
- **Docker Community Slack** — Docker-specific
- **Stack Overflow** — post a new question only if no existing answer fits (search
  first!)

**How to ask in a forum** — see "How to ask for help (with context)" below. Same rules
apply whether you're asking an AI or a human.

---

## Layer 3: Asking humans in forums (last resort)

When AI, docs, search, and YouTube all fail, post a question to a forum. This is slower
(hours to days for an answer) so use it only when you've genuinely exhausted Layers 0-2.

### Where to post

| Need | Where |
|------|-------|
| Specific tool/language question | Stack Overflow (search first!), the tool's Discord/Slack |
| "Am I doing this right?" (conceptual) | r/learnprogramming, r/cscareerquestions |
| Bug in a specific library | GitHub Issues for that library |
| Setup/environment issue | The tool's Discord, or r/<tool> (e.g., r/docker, r/flask) |
| Career/learning path advice | r/learnprogramming, Hacker News |

### How to ask for help (with context) — the universal template

This works for **AI, forums, Discord, Stack Overflow — everyone**. The more context you
give, the faster and better the answer.

```
WHAT I'M DOING:
I'm working through the <topic> <level> assignment, building <X>.

WHAT I EXPECTED:
When I run <command>, I expected <result>.

WHAT ACTUALLY HAPPENS:
When I run <command>, I get:
<full error/output, copy-pasted>

MY ENVIRONMENT:
- OS: <Ubuntu 22.04 / WSL2 / macOS 14 / Windows 11>
- <Tool> version: <run `tool --version` and paste>
- Relevant code or config:
<code or file contents, in a code block>

WHAT I'VE TRIED:
1. <attempt 1> → <result>
2. <attempt 2> → <result>
3. <read this doc/resource> → <didn't help because...>

WHAT I THINK THE PROBLEM MIGHT BE:
<your hypothesis, even if vague — "I think it's a path issue" or "not sure, maybe
CORS?">

QUESTION:
<your specific question — "How do I fix this?" or "What should I check next?">
```

**Why this works:** It saves the helper from asking "what OS?", "what version?", "what
did you try?" — and it shows you've put in effort, which makes people *want* to help.

### Forum-specific etiquette

**Stack Overflow:**
- Search exhaustively first. Duplicates get downvoted/closed.
- Show your research: "I found [this similar question] but it didn't cover <my case>."
- Include a **minimal reproducible example** — the smallest code that reproduces the
  error. Strip out everything irrelevant.

**Reddit (r/learnpython etc.):**
- Be humble and specific. "I'm a beginner stuck on <X>" gets better responses than
  "Why doesn't this work??"
- Use a clear title: "[Flask] POST endpoint returns 500, can't find the bug" not "HELP".

**Discord:**
- Don't ping individuals unless they've offered help. Post in the right help channel.
- Use code blocks (triple backticks) for code and errors — don't paste raw.

**GitHub Issues:**
- Check existing/closed issues first.
- Use the issue template if the repo has one.
- Include environment info and reproduction steps.

---

## The 30-minute stuck protocol

If you're stuck and losing momentum, run this exactly:

1. **Minute 0-10: Layer 0.** Read the error. Reproduce it. Check the topic's
   `resources.md`. Try one fix.
2. **Minute 10-20: Layer 1.** Open Claude/ChatGPT. Use the **universal good-prompt
   template** above. Paste error + code + what you tried. Try the AI's fix.
3. **Minute 20-25: If AI's fix didn't work.** Paste the exact error in quotes into web
   search. Read the top 2-3 results (docs, Stack Overflow, GitHub Issues).
4. **Minute 25-30: If still stuck.** Try a *different* AI (Claude → ChatGPT or vice
   versa). If that fails, draft a forum post using the **universal template** and post
   it to the relevant community (Stack Overflow/Discord/Reddit). Then **move on to a
   different task** while you wait for an answer — don't lose the whole day.

**Document the whole thing.** Whatever the outcome, write in your RESULTS.md notes:
- What the problem was
- What you tried
- What fixed it (or where you posted for help)

This becomes your personal troubleshooting guide for next time.

---

## Common mistakes (don't do these)

- ❌ **Vague prompts:** "it doesn't work" / "my code is broken" / "help with docker"
- ❌ **Asking before trying:** "How do I do X?" when a 2-minute search would answer it
- ❌ **Blind copy-paste:** Running AI code you don't understand, then being unable to fix
  it when it breaks
- ❌ **All-in on one AI:** Trusting ChatGPT's answer without checking Claude or the docs
- ❌ **Asking 5 questions at once:** You'll get shallow answers to all of them
- ❌ **No context in forum posts:** "Help, Flask error" with no code or error text
- ❌ **Staring instead of acting:** Re-reading the same error for 20 minutes. Try
  something. Anything.
- ❌ **Giving up silently:** If you're truly blocked after the 30-min protocol, note it
  in RESULTS.md and move on — don't disappear for a week.

## Document as you go (the multiplier habit)

This is the habit that separates people who improve fast from people who don't:

- **When you fix a bug**, note the cause + fix in your RESULTS.md notes.
- **When a prompt worked great**, save it for reuse.
- **When you learn a new command**, add it to your own notes.
- **When AI hallucinated**, note what it got wrong so you recognize it next time.

The act of writing it down forces you to understand it. And next time you hit the same
problem, your notes save you an hour.

---

## Related

- [Learning path](LEARNING_PATH.md) — where you are in the program and what to do next.
- [How it works](HOW_IT_WORKS.md) — the per-topic workflow.
- [How we work](How-we-work.md) — the mindset, including the AI discipline principle.
- [Master resources](resources.md) — the full pool of curated links per topic.
