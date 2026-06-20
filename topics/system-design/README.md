# System Design

<!--
  Topic metadata:
    slug: system-design
    month: 3
    skills: system design, architecture, scalability, tradeoffs, API design, data modeling
    difficulty: Hard
    estimated_time: 4-6h
    levels: single
-->

This topic is **single-level** (no tiered levels). System design is a thinking skill, not a
coding skill — the assignment is to write a **design document**, and the constraints check
its structure and quality. Some constraints are **AI-judged** (you have an AI review the
quality of your thinking, since there's no human mentor in this program).

## What is system design (and why is this a doc, not code)?

System design is the skill of **answering "how would you build X?"** where X is a whole
product (a URL shortener, a chat app, a rideshare backend). You do not write code. You write
a **design document** that describes the architecture: what components exist, how they
connect, what data you store, how it scales to many users, and what tradeoffs you made.

It is a doc (not code) because the hard part is the *thinking*, not the typing: which
database? how do you generate short codes? what breaks at 100M users? Code cannot answer
those; reasoning can. The doc is where that reasoning lives. (Real engineers write design
docs before big features; this mirrors that.)

**Do not aim for "the one correct answer."** There is not one. Aim for a defensible design
where you can explain *why* you chose each piece. That is what the AI-judged constraints
(C3-C8) check.

## What to build

Write a **system design document** for a **URL shortener** (like bit.ly). The document should
demonstrate that you can think about scalability, data modeling, API design, and tradeoffs
at a level appropriate for a startup engineer.

### The 7 required sections

Your design document must include these sections (in order):

1. **Problem statement & requirements** — What does a URL shortener do? What are the
   functional requirements? What are non-functional requirements (scale, latency,
   availability)?
2. **API design** — What endpoints does the service expose? Request/response format for each.
3. **Data model** — What data do you store? What database(s) do you use? What indexes?
4. **High-level architecture** — Draw (ASCII art or describe) the components: client, API
   server, database, cache, etc. How do they connect?
5. **Core flow** — Walk through the two main flows: shortening a URL (write path) and
   redirecting a short URL (read path). Step by step.
6. **Scalability considerations** — What happens at 1M users? 100M short URLs? How do you
   handle cache, sharding, or rate limiting?
7. **Tradeoffs & alternatives** — What design decisions did you make and why? What would
   you change at different scales? What are the weaknesses of your design?

### How to approach this

1. Read the [resources](resources.md) first. The ByteByteGo URL shortener walkthrough is the
   single best starting point. Read it before you write anything.
2. **Copy** the starter template to your own design doc: `cp starter/DESIGN_TEMPLATE.md MY_DESIGN.md`.
   **Write in `MY_DESIGN.md`**, not the template itself (leave the template clean for reference).
3. Write each section thoughtfully. This is not a coding exercise. Depth of thinking matters
   more than perfect answers. A short, specific paragraph beats a long vague one.
4. Self-check using [constraints.md](constraints.md).
5. For the AI-judged constraints (C3-C8), paste your design doc into Claude/ChatGPT with
   a review prompt (see [../../SELF_HELP.md](../../SELF_HELP.md) — "Review code/design
   critically" template) and use its feedback to revise. Optionally post to
   r/learnprogramming or a Discord for a second opinion.

## Prerequisites

No tools beyond a **terminal** and a **text editor**. A **terminal** is all that's needed — no
special software, no real Linux behavior. **Git Bash is fine on Windows.**

### Get this repo

```bash
git clone <this-repo-url>   # the repo's web URL — see LEARNING_PATH.md if unclear
cd intern-onboarding/topics/system-design
```

## Resources

[resources.md](resources.md) covers system design **from absolute zero through tradeoffs**, in
one progressive list. Find your starting point there.

## How you'll be checked

Open [constraints.md](constraints.md). Some constraints are **structural** (checkable by you —
sections exist, document has enough content). Other constraints are **AI-judged** (you have
an AI review the quality of your thinking, since there's no human mentor in this program).
Self-report in [RESULTS.md](RESULTS.md) for the structural constraints; for AI-judged ones,
run the review prompt, capture the AI's verdict + feedback, and record it. See
[../../HOW_IT_WORKS.md](../../HOW_IT_WORKS.md) for the overall workflow.

- All constraints pass → System design topic cleared.
- Any structural constraint fails → fix and re-check.
- AI-judged constraints marked "Needs revision" → revise per the AI's feedback and re-review.
