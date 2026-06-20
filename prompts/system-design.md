# Prompts — System Design

For the [System design topic](../topics/system-design/). System design is a *thinking*
skill, so most prompts here are about **getting feedback on your reasoning** and
**deepening sections that feel shallow**. Plus the AI-review prompts for the AI-judged
constraints.

---

## I don't know how to start a design doc

**When:** you're staring at the template and don't know where to begin.

```
[CONTEXT] I need to write a system design doc for <a URL shortener>. I have the template
with 7 sections but I'm overwhelmed — I don't know how to approach it.
[GOAL] A concrete starting point and a method for working through the sections.

[WHAT'S HAPPENING — my understanding]
I think system design means <your interpretation — "describing how a system would be
built: components, data, scale, tradeoffs">. The 7 sections are <list them>. I don't know
<which to write first / how detailed to go / what counts as "good enough">.

[ASK] DON'T write the doc for me. Instead, teach me the METHOD: (1) which section should I
write first and why (hint: requirements), (2) for each section, the 2-3 questions I should
answer, (3) how to know when a section is "good enough" vs needs more depth, (4) the order
to tackle them. Give me a concrete first step I can take in the next 10 minutes on my URL
shortener. I want to learn the skill of designing, not get a finished doc.
```

---

## Stuck on a specific section (requirements / API / data model / etc.)

**When:** you're writing one section and it feels shallow or you're blocked.

```
[CONTEXT] I'm writing the <SECTION NAME — e.g., "Scalability considerations"> section of
my URL shortener design doc. Here's my draft:
```<paste your draft for this section>```

[WHAT'S HAPPENING — my understanding]
I think this section should cover <your interpretation of the section's purpose — e.g.,
"what happens to my system as load grows, and what techniques handle it">. I've written
<what you wrote>. I think it's <too shallow / missing something / maybe wrong>.

[WHAT'S WRONG — my hypothesis / what feels weak>
I'm worried <e.g., "I just listed 'caching' and 'sharding' generically without tying them
to a URL shortener's specific bottlenecks" / "I don't have actual numbers — how many QPS?
how much storage?">.

[ASK] DON'T rewrite it for me. Instead: (1) tell me what's specifically weak about my
draft, (2) ask me 3-4 probing questions that would force me to deepen it (e.g., "at 100M
short URLs, how much storage? at 10k QPS reads, where's the bottleneck?"), (3) point me at
the specific technique that applies to a URL shortener at scale (read-heavy → caching,
short code generation → hash vs counter tradeoff). Make me think, then I'll revise and
show you again.
```

---

## Don't know how to estimate scale / capacity

**When:** the doc asks for numbers (QPS, storage, bandwidth) and you don't know how.

```
[CONTEXT] My design doc should include scale estimates for a URL shortener, but I don't
know how to come up with the numbers.
[GOAL] Learn the back-of-the-envelope estimation method.

[WHAT'S HAPPENING — my understanding]
I think estimates are <your interpretation — "rough order-of-magnitude calculations based
on assumptions like user count and usage patterns">. I have no idea what assumptions to
start from.

[ASK] Teach me the estimation method for a URL shortener. Walk me through: (1) what
assumptions do I state (users, URLs per user, reads per URL, retention)? Give me
reasonable starter numbers and justify them. (2) How do I compute QPS, storage, bandwidth
from those — show the arithmetic. (3) The point isn't precision — it's order of magnitude.
Show me how a senior thinks: "is this 1k QPS or 100k QPS? that changes the design." Then
have ME redo the estimate with different assumptions so I learn the skill.
```

---

## Help me identify tradeoffs in my design

**When:** you're at the tradeoffs section and can only think of generic ones.

```
[CONTEXT] I'm at the tradeoffs section of my URL shortener doc. I wrote:
```<paste>```
[GOAL] Find REAL, specific tradeoffs — not generic platitudes.

[WHAT'S HAPPENING — my understanding]
A tradeoff is <your interpretation — "a design decision where choosing A gains X but
loses Y">. I listed <your tradeoffs>. I suspect they're <too vague / not actually
tradeoffs / missing the real ones>.

[WHAT'S WRONG — my hypothesis>
I think the real tradeoffs in a URL shortener are about <short code generation (hash vs
counter), storage (SQL vs NoSQL), caching (consistency vs speed)> but I don't know how to
articulate the pros/cons concretely.

[ASK] For my design, identify the 3-4 GENUINE decision points where I made (or should
make) a tradeoff. For each: what were the options, what did I pick, what did I gain, what
did I give up, and what would change my mind at 10x scale? Don't list generic "ACID vs
BASE" — make them specific to MY design. Push back if a tradeoff I listed isn't really a
tradeoff.
```

---

## Architecture diagram feedback

**When:** you drew the architecture (ASCII or described) and want it critiqued.

```
[CONTEXT] Here's my high-level architecture for a URL shortener:
```<paste your ASCII diagram or detailed text description>```

[WHAT'S HAPPENING — my understanding]
The components are: <list them and what each does>. Request flow for "shorten a URL":
<your description>. Request flow for "redirect": <your description>. I think this handles
<requirements> because <reasoning>.

[WHAT'S WRONG — my hypothesis / what I'm unsure about>
I'm unsure whether <e.g., "I need a load balancer" / "where the cache sits" / "is one DB
enough" / "should the redirect be synchronous or async">.

[ASK] Critique my architecture: (1) Is the request flow correct and complete? (2) What
components am I missing (load balancer? cache? CDN? queue?)? (3) Are there single points
of failure? (4) Does it actually satisfy my stated requirements? Be specific — point at
parts of my diagram. Don't redraw it; tell me what to fix and why, then I'll revise.
```

---

## The AI-review prompts (for AI-judged constraints C3-C8)

These are the prompts to run when you hit the AI-judged constraints in the system-design
topic. Paste your whole design doc with each.

**Comprehensive review (run this first):**
```
You are a senior engineer reviewing a system design document for a URL shortener, written
by someone learning system design. Here's the doc:
```<paste your full design doc>```

Score each dimension 1-5 and explain the score. Be critical — I want honest feedback, not
flattery. For anything ≤3, give specific, actionable suggestions.

Dimensions:
- Requirements (functional + non-functional complete? edge cases? realistic?)
- API design (endpoints well-defined? methods/status correct? request/response shapes?)
- Data model (covers needed fields? DB choice justified? keys/indexes?)
- Architecture (components clear? request flow correct? matches requirements?)
- Scalability (addresses growth? specific techniques for a URL shortener? not generic?)
- Tradeoffs (specific decisions with reasoning? alternatives with pros/cons?)

Then: what are the TOP 3 things I should improve to make this doc stronger?
```

**Deep-dive on a weak section (after the comprehensive review):**
```
In your review, you scored my <SECTION> a <N>/5. Here's that section:
```<paste>```
You said it was weak because: <quote the AI's feedback>.

I want to improve it. DON'T rewrite it for me. Instead: (1) give me 3 probing questions
that will force me to think harder, (2) point me at the specific concept/technique I'm
missing, (3) show me one tiny example of what a strong version of this section looks like
(for a DIFFERENT system, so I can't copy it). Then I'll revise and show you again for a
re-score.
```

**Re-review after revision:**
```
I revised my <SECTION> based on your feedback. Here's the new version:
```<paste>```
Re-score it 1-5 using the same criteria. Did I address your feedback? What's still weak?
Is it good enough now (4-5) or should I iterate again?
```
