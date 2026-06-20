# How We Work

This isn't a topic you "pass." It's how we operate day-to-day, and it applies to
everything — the onboarding topics, real work after onboarding, and how we treat each
other. Read this once. It gets reinforced through practice: shipping cadence,
retrospectives, 1:1s, and real incidents.

## Why this matters more than any single topic

You can learn Docker in a week. You can't learn "how to behave when prod is down" from
a checklist. Startups live or die on a handful of habits. These are ours.

## Ownership

- **You own outcomes, not tasks.** "I did the ticket" is not the bar. The bar is "the
  thing works for users."
- If something you depend on is broken, fix it or escalate loudly — don't wait for
  someone to notice.
- When you finish something, ask: *is it actually done, or did I just stop working on it?*

## Ship fast, then fix

- **Small, shippable increments beat big bangs.** A tiny PR merged today beats a perfect
  PR next week.
- Bias toward getting something working end-to-end (ugly) before polishing any one piece.
- "Done" means: it works, it's tested enough to trust, someone else can run it, and the
  next person knows what it does. Not "I wrote the code."

## Work with ambiguity

- Real requirements are rarely fully specified. You will get "build a thing that does X."
- When something is unclear, **write down your assumptions** and proceed on them. Don't
  stall waiting for perfect spec.
- Asking one good clarifying question is great. Asking ten before starting is not.

## Written communication is default

- We over-index on writing: PR descriptions, design notes, commit messages, status
  updates. If it isn't written down, it didn't happen.
- A short doc beats a long meeting. A one-line Slack beats a 30-minute call — usually.
- Write for the next person who will read it cold in three months. That person is often you.

## How to use AI well ("vibe coding" without losing control)

- AI is a force multiplier, not a replacement for understanding. **You are responsible
  for every line** it generates.
- Break work into the smallest possible pieces. One feature, one function, one test.
- Keep prompts specific. Vague prompts → vague code → hours of debugging.
- **Verify each step before moving on.** "It compiled" is not verification.
- Keep a rough prompt log for non-trivial work. If something breaks later, you can trace
  why you wrote it that way.
- If you can't explain what the AI wrote, don't ship it.

## Make reversible vs. irreversible decisions

- **Reversible** (feature flag off, a new endpoint not wired up): move fast, decide alone.
- **Irreversible** (deleting prod data, a public API contract, a schema migration): slow
  down, get a second opinion, write it down.

## Feedback and growth

- Expect direct feedback. Give it directly too — kindly, but without burying the point.
- In code review: argue the idea, not the person. Cite the code.
- When you don't know something, say so early. "I don't know yet, here's how I'll find
  out" is a senior answer.

## What failure looks like here

- Hiding a mistake until it blows up.
- Saying "done" when it isn't.
- Building for two weeks without showing anyone.
- Copy-pasting AI output you don't understand into something users touch.

## What success looks like here

- Shipping small things often.
- Writing down what you did and why.
- Catching your own mistakes early and saying so.
- Making the next person's job easier.
