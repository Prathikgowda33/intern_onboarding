# Intern Onboarding

A placement-test style onboarding repo for startup interns. Interns prove they can
already do something — if they can, they skip the learning material. If they can't,
they study the curated resources and try again.

## 👋 First time here?

- **If you're an intern** → start with [LEARNING_PATH.md](LEARNING_PATH.md). It tells you
  where to start, where to end, and what to do when stuck.
- **If you're stuck on something** → read [SELF_HELP.md](SELF_HELP.md) (self-debug, AI
  prompting with many examples, web search, forums). For ready-made prompts by topic, see
  [prompts/](prompts/).
- **If you're authoring or maintaining topics** → start with [AUTHORING.md](AUTHORING.md).

## The idea

Hiring interns to work on a full-stack web + Python stack means a wide skill surface:
Linux, Docker, Python, JavaScript, databases, APIs, web apps, system design, and
AI-assisted "vibe coding." Rather than making everyone sit through the same material
regardless of what they already know, this repo lets them **test out** of each topic:

- Each topic is a small project to build.
- Each project has a **constraints checklist** — high-level acceptance criteria checked
  by running the solution and observing the result.
- Pass all constraints → the topic is **cleared**, skip the resources.
- Fail any constraint → study the topic's **resources**, fix the solution, re-check.

The constraints check *behavior*, not whether the intern followed a specific recipe —
so they're higher-level than the original project requirement. If the app starts with
one command and returns the right responses, that's what matters.

## Who this is for

- **Interns** — work through topics, self-report results in each topic's `RESULTS.md`.
- **Reviewers** — spot-check borderline or failing submissions. See
  [HOW_IT_WORKS.md](HOW_IT_WORKS.md) for the workflow.

## 3-month program structure

Eleven topics, grouped into three monthly clusters:

| Month | Theme | Topics |
|-------|-------|--------|
| 1 | Foundations | Linux · Git · Python · Databases · Testing |
| 2 | Web & Infra | HTTP/API · Web app (full-stack) · Docker · Deployment |
| 3 | Real work | System design · Vibe coding |

Mindset and how we work day-to-day is covered separately in
[How-we-work.md](How-we-work.md) — it's reinforced through culture, not a checked topic.

## How to navigate

| File | Purpose |
|------|---------|
| [LEARNING_PATH.md](LEARNING_PATH.md) | **Start here (interns)** — where to start, where to end, what to do when stuck |
| [PROGRAM_CHECKLIST.md](PROGRAM_CHECKLIST.md) | The high-level checkbox view of the whole program — copy to `MY_CHECKLIST.md` |
| [PROGRESS_TEMPLATE.md](PROGRESS_TEMPLATE.md) | Personal progress journal template — copy to `MY_PROGRESS.md` |
| [SELF_HELP.md](SELF_HELP.md) | How to get unstuck: self-debug, AI prompting (many examples), web search, forums |
| [prompts/](prompts/) | **Prompt library** — copy-paste prompts for every topic (debugging, concepts, review). Start at [prompts/README.md](prompts/README.md) |
| [HOW_IT_WORKS.md](HOW_IT_WORKS.md) | The 6-step per-topic workflow (incl. setup) |
| [How-we-work.md](How-we-work.md) | Startup mindset and expectations |
| [resources.md](resources.md) | Master list of learning resources, by skill area |
| [topics/](topics/) | One folder per topic; start at [topics/README.md](topics/README.md) for the index |
| [TEMPLATE/](TEMPLATE/) | Copy this folder to add a new topic |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to add a new topic (mechanical steps) |
| [AUTHORING.md](AUTHORING.md) | Quality rules + lessons learned for authoring a topic |
| [IMPROVEMENTS.md](IMPROVEMENTS.md) | Proposed improvements to this repo (living list) |

## Status

This repo currently contains the **template** — the folder structure, workflow docs,
resource list, mindset doc, and a copy-to-create topic template. Topic content (Linux,
Git, Python, etc.) is added one-by-one from the template. See
[topics/README.md](topics/README.md) for what's planned and what's ready.
