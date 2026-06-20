# Resources — Docker

Shared across both Docker levels. This is a **progressive** resource list: it starts from
"what is Docker?" and goes up through compose. **You don't read all of it.** Find the level
you're working on, read only what your failed constraints point to.

This list focuses on Docker specifically. The master cross-topic list is at
[../../resources.md](../../resources.md).

---

## From absolute zero (what is Docker?)

If you've never used Docker and don't know what a container is, start here.

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Docker — Get Started](https://docs.docker.com/get-started/) | Reading | C1 — what Docker is, what containers are, why they matter. The official tutorial. |
| [Docker Overview](https://docs.docker.com/get-started/overview/) | Reading | C1 — Docker architecture: images, containers, registries, Dockerfile. |
| [Docker — What is a Container?](https://www.docker.com/resources/what-container/) | Reading | C1 — containers vs VMs vs bare metal. The 2-minute explanation. |

**The mental model you need first:** A **container** is a lightweight, isolated environment that
packages your app and all its dependencies together. A **Dockerfile** is a recipe that says "start
from this base image, copy my code in, install these dependencies, run this command." You **build**
a Dockerfile into an **image**, then **run** the image as a container. The same image runs
identically on every machine — that's the point.

## Dockerfile basics (Level 1)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Docker — Dockerfile Reference](https://docs.docker.com/engine/reference/builder/) | Reference | C1, C2 — the definitive guide to Dockerfile instructions: FROM, COPY, RUN, EXPOSE, CMD, WORKDIR, ENTRYPOINT. |
| [Docker Best Practices for Python](https://docs.docker.com/develop/language-best-practices/python/) | Reading | C1, C2 — how to write a good Dockerfile for a Python Flask app: multi-stage builds, .dockerignore, virtual envs. |
| [Docker — .dockerignore](https://docs.docker.com/engine/reference/builder/#dockerignore-file) | Reading | C2 — what to exclude from your build context. |
| [Real Python — Dockerize a Flask App](https://realpython.com/docker-python/) | Reading | C1 — step-by-step: write Dockerfile, build, run a Flask app in Docker. |

## Docker Compose (Level 2)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Docker — Compose Overview](https://docs.docker.com/compose/) | Reading | C1, C2 — what compose is, why you need it, the `docker-compose.yml` format. |
| [Docker — Compose Getting Started](https://docs.docker.com/compose/gettingstarted/) | Reading | C1, C2, C3 — step-by-step: define services, build, run with compose. |
| [Docker — Networking in Compose](https://docs.docker.com/compose/networking/) | Reading | C4 — how containers communicate in compose (DNS-based service discovery). |
| [Docker — Volumes in Compose](https://docs.docker.com/compose/manage-volumes/) | Reading | C5 — persistent data with volumes. |

---

## How to use these

1. Open the `RESULTS.md` of the level you're working on and find which constraints failed.
2. Read the resource(s) next to those constraints above.
3. Fix your solution.
4. Re-run the checks in the level's `constraints.md`.
5. Update `RESULTS.md` with the new evidence.

Don't read everything top to bottom — target the gap.
