# URL Shortener — System Design Document

<!--
  Use this template to write your design document.
  Fill in each section with your own thinking.
  Delete this comment block when you're done.
-->

## 1. Problem Statement & Requirements

### What is a URL shortener?

<!-- Describe what a URL shortener does in 2-3 sentences -->

### Functional Requirements

<!-- List the core features: create short URL, redirect, etc. -->
<!-- - FR1: ... -->
<!-- - FR2: ... -->

### Non-Functional Requirements

<!-- List NFRs: scale, latency, availability, etc. -->
<!-- - NFR1: ... -->

### Out of Scope

<!-- What won't you handle? (Analytics dashboard, custom domains, user accounts, etc.) -->

---

## 2. API Design

### Create Short URL

```
POST /shorten
Request:
Response:
```

### Redirect

```
GET /:short_code
Request:
Response:
```

<!-- Add any additional endpoints you think are needed -->

---

## 3. Data Model

### Entities

<!-- Describe the main data entities and their fields -->

### Database Choice

<!-- Which database(s) and why? SQL? NoSQL? Cache? -->

### Schema

<!-- Show the schema / table structure -->

---

## 4. High-Level Architecture

```
<!-- Draw an ASCII diagram or describe the architecture -->
<!-- Example: -->

Client → [Load Balancer] → [API Server] → [Cache (Redis)]
                                  ↓
                            [Database]
```

---

## 5. Core Flow

### Write Path: Shortening a URL

<!-- Step by step: what happens when a user submits a URL to shorten? -->
<!-- 1. Client sends POST /shorten with long_url -->
<!-- 2. ... -->

### Read Path: Redirecting a Short URL

<!-- Step by step: what happens when someone visits a short URL? -->
<!-- 1. Client sends GET /:short_code -->
<!-- 2. ... -->

---

## 6. Scalability Considerations

<!-- What happens at scale? -->
<!-- - Caching strategy -->
<!-- - Database scaling (sharding, replication) -->
<!-- - Rate limiting -->
<!-- - CDN for redirects -->

---

## 7. Tradeoffs & Alternatives

### Key Design Decisions

<!-- For each decision, explain what you chose and why -->

| Decision | Choice | Why | Alternative | Tradeoff |
|----------|--------|-----|-------------|----------|
| <!-- e.g., Short code generation --> | <!-- e.g., Base62 --> | <!-- ... --> | <!-- e.g., UUID --> | <!-- ... --> |
| | | | | |

### Weaknesses of This Design

<!-- Be honest: what are the limitations? What would you change at 10x scale? -->
