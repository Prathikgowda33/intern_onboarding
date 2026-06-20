# Constraints — System Design (URL Shortener)

The acceptance checklist. Some constraints are **structural** (you verify them yourself). Others
are **AI-judged** (you use an AI to review your document). Self-report in [RESULTS.md](RESULTS.md).

## How to check each constraint

**Structural constraints (C1, C2):** Open your design document and verify by reading.

**AI-judged constraints (C3-C8):** These require an AI review (there's no human mentor in
this program). Paste your design doc into Claude/ChatGPT with a review prompt — for example:
> "Review this system design doc critically. For each section, tell me: is it clear, complete,
> and specific? What's missing or vague? Score each of these dimensions 1-5: requirements,
> API design, data model, architecture, scalability, tradeoffs. Be harsh."
Capture the AI's verdict + feedback in RESULTS.md. If it scores anything ≤3, revise and
re-review.

---

## Constraints

- [ ] **C1: All 7 required sections present**
  - How to verify: open your design document (the file you wrote, not the template).
  - Pass if: all 7 required section headings are present:
    1. Problem statement & requirements
    2. API design
    3. Data model
    4. High-level architecture
    5. Core flow
    6. Scalability considerations
    7. Tradeoffs & alternatives
  - Fails if: any section heading is missing or renamed beyond recognition.

- [ ] **C2: Document has sufficient depth**
  - How to verify: run `wc -l` on your design document and open it to review.
  - Pass if: the document is at least 200 lines long. Each section has at least 2-3
    substantial paragraphs (not just a single sentence). The document includes specifics
    (e.g., specific endpoints, specific database schema, specific numbers for scale estimates).
  - Fails if: under 200 lines, or any section is a single sentence, or the document is
    entirely vague (no specifics).

- [ ] **C3: Requirements are clear and complete [AI-JUDGED]**
  - How to verify: paste your design doc into Claude/ChatGPT with the review prompt from [../../SELF_HELP.md](../../SELF_HELP.md) and capture its verdict + feedback.
  - Pass if: functional requirements cover the core features (create short URL, redirect).
    Non-functional requirements mention scale (reads >> writes), latency (redirect must be
    fast), and availability. Edge cases are considered (expired links, custom aliases).
  - Fails if: requirements are vague, missing non-functional requirements, or unrealistic.

- [ ] **C4: API design is practical [AI-JUDGED]**
  - How to verify: paste your design doc into Claude/ChatGPT with the review prompt from [../../SELF_HELP.md](../../SELF_HELP.md) and capture its verdict + feedback.
  - Pass if: endpoints are well-defined with request/response format. HTTP methods are
    appropriate (POST for create, GET for redirect). Status codes are correct.
  - Fails if: endpoints are missing, wrong HTTP methods, or no response format specified.

- [ ] **C5: Data model makes sense [AI-JUDGED]**
  - How to verify: paste your design doc into Claude/ChatGPT with the review prompt from [../../SELF_HELP.md](../../SELF_HELP.md) and capture its verdict + feedback.
  - Pass if: the data model covers what's needed (original URL, short code, creation date,
    optionally click count, user, expiration). The choice of database(s) is justified.
    Indexes or keys are mentioned.
  - Fails if: data model is missing key fields, no database choice justified, or unrealistic.

- [ ] **C6: Architecture is clearly communicated [AI-JUDGED]**
  - How to verify: paste your design doc into Claude/ChatGPT with the review prompt from [../../SELF_HELP.md](../../SELF_HELP.md) and capture its verdict + feedback.
  - Pass if: the architecture diagram (ASCII or described) shows the main components and how
    they connect. It's clear what happens when a request arrives. The architecture matches
    the stated requirements.
  - Fails if: architecture is unclear, missing components, or doesn't match the requirements.

- [ ] **C7: Scalability is addressed [AI-JUDGED]**
  - How to verify: paste your design doc into Claude/ChatGPT with the review prompt from [../../SELF_HELP.md](../../SELF_HELP.md) and capture its verdict + feedback.
  - Pass if: the document discusses what happens at higher scale. At least 2 scalability
    techniques are mentioned (caching, sharding, rate limiting, CDNs, read replicas, etc.).
    The discussion is specific to a URL shortener (not generic advice).
  - Fails if: no scalability section, or only generic advice without URL-shortener specifics.

- [ ] **C8: Tradeoffs are identified [AI-JUDGED]**
  - How to verify: paste your design doc into Claude/ChatGPT with the review prompt from [../../SELF_HELP.md](../../SELF_HELP.md) and capture its verdict + feedback.
  - Pass if: at least 2 specific tradeoffs are discussed with reasoning (e.g., "I chose
    base62 encoding for short codes because... but this means..."). Alternatives are
    mentioned with pros/cons.
  - Fails if: no tradeoffs discussed, or only one, or the discussion lacks reasoning.

---

## Summary

8 constraints. C1-C2 are structural (self-verified). C3-C8 are AI-judged (review with
Claude/ChatGPT using the prompt above). If structural constraints fail, fix and re-check.
If AI-judged constraints score low, revise per the AI's feedback and re-review. See
[resources.md](resources.md) for study material.
