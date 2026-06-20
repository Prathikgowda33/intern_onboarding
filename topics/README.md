# Topics

One folder per topic. Each topic follows the same structure (see [../TEMPLATE/](../TEMPLATE/)
for the pattern, [../CONTRIBUTING.md](../CONTRIBUTING.md) for how to add one, and
[../AUTHORING.md](../AUTHORING.md) for the quality rules + lessons learned).

## Index

Grouped by the 3-month program structure (see [../README.md](../README.md)).

### Month 1 — Foundations

| Topic | Slug | Skills | Difficulty | Est. time | Status |
|-------|------|--------|------------|-----------|--------|
| Linux | `linux` | shell, filesystem, permissions, scripting, container logs | Easy→Medium (tiered: 3 levels) | 1–4h | ✅ READY |
| Git & collaboration | `git` | version control, branching, merge, conflict resolution | Easy→Medium (tiered: 2 levels) | 1–3h per level | ✅ READY |
| Python | `python` | core language, CLI, file I/O, CSV/JSON, argparse | Easy→Medium (tiered: 2 levels) | 2–3h per level | ✅ READY |
| Databases | `databases` | SQL, schema design, queries, indexes, views, transactions | Medium (tiered: 2 levels) | 2–3h per level | ✅ READY |
| Testing | `testing` | pytest, unit testing, mocking, integration tests, test design | Medium (tiered: 2 levels) | 2–3h per level | ✅ READY |

### Month 2 — Web & Infra

| Topic | Slug | Skills | Difficulty | Est. time | Status |
|-------|------|--------|------------|-----------|--------|
| HTTP & API design | `http-api` | REST, methods, status codes, validation, Flask | Medium (tiered: 2 levels) | 2–3h per level | ✅ READY |
| Web app (full-stack) | `web-app` | Flask, HTML, React, CORS, Docker, error handling | Medium→Hard (tiered: 3 levels) | 2–4h per level | ✅ READY |
| Docker | `docker` | Dockerfile, docker build, compose, multi-container | Medium→Medium-Hard (tiered: 2 levels) | 2–3h per level | ✅ READY |
| Deployment | `deployment` | Railway.app, env vars, GitHub Actions, CI/CD | Medium→Hard (tiered: 2 levels) | 2–4h per level | ✅ READY |

### Month 3 — Real work

| Topic | Slug | Skills | Difficulty | Est. time | Status |
|-------|------|--------|------------|-----------|--------|
| System design | `system-design` | requirements, API design, data model, architecture, scalability, tradeoffs | Hard (single-level) | 4–6h | ✅ READY |
| Vibe coding | `vibe-coding` | AI-assisted dev, prompting, code review, TDD with AI | Medium→Medium-Hard (tiered: 2 levels) | 2–4h per level | ✅ READY |

## Status legend

- 🔲 **TODO** — not started (no folder yet)
- 📝 **SCAFFOLDED** — folder exists with metadata + per-OS prerequisites filled in, but
  assignment/constraints/resources are placeholders. **Do not assign to interns.** The
  structure + prerequisites are ready; the actual topic content is awaiting authoring +
  verification per [../AUTHORING.md](../AUTHORING.md).
- 🚧 **IN PROGRESS** — being authored
- ✅ **READY** — complete AND the author has attempted it and verified every constraint

## How an intern works through a topic

See [../HOW_IT_WORKS.md](../HOW_IT_WORKS.md). In short: set up prerequisites → build it →
check constraints manually → self-report in the topic's `RESULTS.md` → pass all = cleared,
any fail = study `resources.md` and retry. (Only ✅ READY topics are assignable.)

## For authors

To turn a 📝 SCAFFOLDED topic into ✅ READY, follow [../AUTHORING.md](../AUTHORING.md) —
especially the non-negotiable: attempt the topic yourself and verify every constraint
before marking it ready.
