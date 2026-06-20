# Resources

Master list of learning resources, organized by skill area. Each topic also has its own
`resources.md` with a **focused subset** of these — you only read the full list below if
you want breadth across the whole program.

**How to use this:** Don't read everything. The intended workflow (see
[HOW_IT_WORKS.md](HOW_IT_WORKS.md)) is:

1. Attempt the topic's project.
2. Check the constraints.
3. Only if a constraint **fails**, open that topic's `resources.md` (a focused subset)
   and study the specific gap.

The resources below are the full pool each topic draws from.

---

## Learning path (suggested order)

```
Linux → Git → Python → Databases → Testing → HTTP/API → Web app → Docker → Deployment → System design → Vibe coding
```

Foundations first, then web & infra, then real-world integration. This mirrors the
3-month structure in [README.md](README.md).

---

## Linux basics

| Resource | Type | Covers |
|----------|------|--------|
| [Linux Tutorial (GeeksforGeeks)](https://www.geeksforgeeks.org/linux-unix/linux-tutorial/) | Reading | Filesystem, commands, permissions, scripting |
| [Linux 101 Crash Course (YouTube)](https://www.youtube.com/watch?v=w9Zz_myULjc) | Video | Practical terminal workflows for beginners |

## Git & collaboration

| Resource | Type | Covers |
|----------|------|--------|
| [Pro Git book (ch. 1–3)](https://git-scm.com/book/en/v2) | Reading | Commits, branches, merging, remotes |
| [Learn Git Branching](https://learngitbranching.js.org) | Interactive | Branching/merging visually |
| [GitHub's PR guide](https://docs.github.com/en/pull-requests) | Reading | Pull requests, review, conflicts |

## Python

| Resource | Type | Covers |
|----------|------|--------|
| [Python Tutorial (official)](https://docs.python.org/3/tutorial/) | Reading | Core language, stdlib, idioms |
| [Real Python — start here](https://realpython.com/learning-paths/python-basics/) | Reading | Beginner-to-intermediate path |
| [Flask quickstart](https://flask.palletsprojects.com/en/latest/quickstart/) or [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) | Reading | Building a small web service |

## JavaScript

| Resource | Type | Covers |
|----------|------|--------|
| [JavaScript.info (part 1)](https://javascript.info) | Reading | Modern JS fundamentals |
| [MDN — Getting started with the web](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web) | Reading | JS + HTML + CSS together |
| [Eloquent JavaScript (ch. 1–5)](https://eloquentjavascript.net) | Reading | Deeper language understanding |

## Databases

| Resource | Type | Covers |
|----------|------|--------|
| [SQLBolt](https://sqlbolt.com) | Interactive | SQL basics, joins, aggregates |
| [PostgreSQL Tutorial](https://www.postgresqltutorial.com) | Reading | Real-world SQL on Postgres |
| [Use The Index, Luke!](https://use-the-index-luke.com) | Reading | How indexes actually work |

## Testing

| Resource | Type | Covers |
|----------|------|--------|
| [pytest — Getting started](https://docs.pytest.org/en/stable/getting-started.html) | Reading | Writing and running tests |
| [Testing Your Code (Real Python)](https://realpython.com/learning-paths/python-testing/) | Reading | What to test, unit vs integration |
| [Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) | Reading | Test strategy at scale |

## HTTP & API design

| Resource | Type | Covers |
|----------|------|--------|
| [Mozilla — HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview) | Reading | Requests, responses, methods, status codes |
| [REST API Tutorial](https://www.restapitutorial.com) | Reading | REST conventions and status codes |
| [Google API Design Guide](https://cloud.google.com/apis/design) | Reading | Naming, versioning, resources |

## Web app (full-stack)

| Resource | Type | Covers |
|----------|------|--------|
| [MDN — Web Forms](https://developer.mozilla.org/en-US/docs/Learn/Forms) | Reading | Forms, validation, submission |
| [React quick start](https://react.dev/learn) | Reading | Component-based frontend |
| [Intern onboarding list (datawadi)](https://github.com/datawadi/intern-onboarding) | Reading | Curated list touching the whole stack |

## Docker

| Resource | Type | Covers |
|----------|------|--------|
| [Docker — Get started](https://docs.docker.com/get-started/) | Reading | Official fundamentals + CLI cheat sheet |
| [Docker Curriculum](https://docker-curriculum.com) | Reading | Building and deploying web apps with Docker |
| [Compose quickstart](https://docs.docker.com/compose/gettingstarted/) | Reading | Multi-container apps locally |

## Deployment

| Resource | Type | Covers |
|----------|------|--------|
| [Deploy with Docker + a VPS (basic)](https://docs.docker.com/get-started/deploy/) | Reading | Getting a container live |
| [GitHub Actions quickstart](https://docs.github.com/en/actions/quickstart) | Reading | Basic CI/CD pipelines |
| [Let's Encrypt / HTTPS basics](https://letsencrypt.org/getting-started/) | Reading | Free TLS for a live domain |

## System design

| Resource | Type | Covers |
|----------|------|--------|
| [System Design Primer](https://github.com/donnemartin/system-design-primer) | Reading | The canonical intro |
| [System Design 101](https://github.com/zaamad/system-design-101) | Reading | Visual explanations of common patterns |
| [System Design for Web-Apps](https://github.com/PawanRamaMali/System-Design) | Reading | Requirements → API → data model → bottlenecks |

The system-design framework used across these: **requirements → interface/API → data
model → high-level design → detailed design → bottlenecks**. The design-note headings in
the System Design topic follow this.

## Vibe coding (AI-assisted development)

| Resource | Type | Covers |
|----------|------|--------|
| [Introduction to Vibe Coding (Microsoft Learn)](https://learn.microsoft.com/en-us/training/modules/introduction-vibe-coding/) | Reading | Workflow and mindset |
| [Intro to Vibe Coding (Codecademy)](https://www.codecademy.com/learn/intro-to-vibe-coding) | Reading | Tools and app-building process |
| [Cursor beginner tutorial (YouTube)](https://www.youtube.com/watch?v=8AWEPx5cHWQ) | Video | Cursor workflow, small steps |
| [Cursor + Claude starter (YouTube)](https://www.youtube.com/watch?v=PuNkNClfOUM) | Video | Prompts, focus, testing each step |

The common thread across all four: **small steps, specific prompts, one feature at a
time, verify before moving on.** See also [How-we-work.md](How-we-work.md) — "How to use
AI well."
