# Resources — System Design

This topic has a single level. The resource list covers system design **from absolute zero
through tradeoffs**. Find your starting point and read only what your failed constraints
point to.

The master cross-topic list is at [../../resources.md](../../resources.md).

---

## From absolute zero (what is system design?)

If you've never heard of system design or don't know what it means to "design a system," start here.

| Resource | Type | Why it's here |
|----------|------|---------------|
| [ByteByteGo — System Design Primer](https://bytebytego.com/) | Reading | C1, C2, C3 — the best system design resource for beginners. Covers the full mental model. |
| [System Design Interview — Alex Xu (Book)](https://www.amazon.com/System-Design-Interview-insiders-Second/dp/B08CMF2CQF) | Reading (book) | C1-C8 — the definitive book. Read chapters 1-3 for the methodology, then the URL shortener chapter. |
| [Grokking the System Design Interview](https://www.educative.io/courses/grokking-modern-system-design-interview-for-engineers-managers) | Course | C1-C8 — structured course covering common system design patterns. |

**The mental model you need first:** System design is about answering: "How would you build X?"
where X is a product (URL shortener, chat app, etc.). You don't write code — you write a
document describing the architecture: what components exist, how they connect, what data
you store, how it scales, and what tradeoffs you made. Good system design is about **making
explicit tradeoffs**, not finding the "perfect" solution.

## Components and patterns

| Resource | Type | Why it's here |
|----------|------|---------------|
| [ByteByteGo — Database Scaling](https://bytebytego.com/) | Reading | C5, C7 — sharding, replication, when to use SQL vs NoSQL. |
| [High Scalability — Real Architectures](https://highscalability.com/) | Reading | C4, C6, C7 — real-world architecture stories from companies like YouTube, WhatsApp, Twitter. |
| [Martin Fowler — Patterns of Enterprise Application Architecture](https://martinfowler.com/eaaCatalog/) | Reference | C4, C5 — common architecture patterns: caching, CQRS, event sourcing. |

## URL shortener specifically

| Resource | Type | Why it's here |
|----------|------|---------------|
| [ByteByteGo — URL Shortener](https://bytebytego.com/) | Reading | C1-C8 — the canonical URL shortener system design walkthrough. Use this as your primary reference. |
| [System Design — URL Shortener (educative.io)](https://www.educative.io/answers/how-to-design-a-url-shortening-service) | Reading | C3, C4, C5 — focused walkthrough of the URL shortener problem. |
| [Base62 Encoding](https://en.wikipedia.org/wiki/Base62) | Reference | C5 — the encoding scheme most URL shorteners use for short codes. |

## Writing design documents

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Google — Design Docs](https://www.google.com/design-docs/) | Reading | C1, C2, C8 — how Google structures design documents. A model for clarity. |
| [How to Write a Technical Design Document](https://www.notion.so/How-to-Write-a-Technical-Design-Document-cc1a3a3b3f0d4e0ea4a5b3c0d1e2f3a4) | Reading | C2 — practical advice on writing clear design documents. |

---

## How to use these

1. Open [RESULTS.md](RESULTS.md) and find which constraints failed or need AI review.
2. Read the resource(s) next to those constraints above.
3. Fix your design document.
4. Re-check the structural constraints.
5. For AI-judged constraints, re-run the review prompt in Claude/ChatGPT and capture the
   new verdict + feedback.

Don't read everything top to bottom — target the gap.
