# Deployment

<!--
  Topic metadata:
    slug: deployment
    month: 3
    skills: Railway.app, environment variables, Docker deployment, GitHub Actions, CI/CD
    difficulty: Medium (L1) → Hard (L2)
    estimated_time: 2-4h per level
    levels: 1,2
-->

This topic is **tiered**. Deployment skills span from "never deployed anything" to "automated
CI/CD pipeline" — so pick the level that matches where you are. You only need to clear **one**
level to clear the topic.

## Pick your level

Self-assess honestly. Choose the **highest** level you think you can clear. Fail it →
drop to the level below and try again. Pass it → topic cleared, you don't need the lower
level.

| Level | For whom | What you do | Est. time |
|-------|----------|-------------|-----------|
| [1 — First deploy](levels/level-1-first-deploy/README.md) | Never deployed an app to the internet | Deploy a provided Flask app to Railway.app | 2–3h |
| [2 — CI/CD](levels/level-2-ci-cd/README.md) | Has deployed manually, hasn't set up automated pipelines | Set up GitHub Actions to auto-build and deploy on push | 3–4h |

### How to decide

- **Never deployed an app that's accessible via a public URL?** → Level 1.
- **You've deployed with `git push` or a platform UI, but haven't written a CI/CD pipeline?** → Level 2.

If you start at Level 2 and get stuck on something Level 1 would have taught you, that's
fine — go read that section in [resources.md](resources.md), then come back.

## Prerequisites (all levels)

This topic needs a **GitHub account**, **Railway.app account** (free tier), **Git**, and a
**terminal**. Level 2 additionally requires your code to be in a GitHub repo.

### GitHub account

- **Verify:** you can log in to <https://github.com>.
- Create one at <https://github.com/signup> if needed.

### Railway.app account

- **Verify:** you can log in to <https://railway.app>.
- Sign up with your GitHub account at <https://railway.app/login>.

### Git

- **Verify:** `git --version` prints a version.
- See the Git topic for installation instructions.

### Terminal

- **Verify:** `git --version` from your terminal.
- **Windows:** Git Bash. **macOS/Linux:** default terminal.

### Get this repo

```bash
git clone <this-repo-url>   # the repo's web URL — see LEARNING_PATH.md if unclear
cd intern-onboarding/topics/deployment
```

If any check fails, follow [SELF_HELP.md](../../SELF_HELP.md) before spending an hour on it — most issues solve fast with AI or a web search.

## How the levels relate

Level 1 teaches manual deployment (push code, platform builds and runs). Level 2 automates
that with GitHub Actions (CI/CD). Level 2 assumes you understand what deployment is and how
Railway works.

Open the README inside your chosen level's folder to begin.

## Resources (shared)

[resources.md](resources.md) covers deployment **from absolute zero through CI/CD**, in one
progressive list. Find your starting point there.

## How you'll be checked

Each level has its own [constraints.md](levels/level-1-first-deploy/constraints.md)
with manual, observable pass/fail criteria, and its own `RESULTS.md` to self-report into.
See [../../HOW_IT_WORKS.md](../../HOW_IT_WORKS.md) for the overall workflow.
