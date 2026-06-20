# Prompts — Deployment

For the [Deployment topic](../topics/deployment/). Common situations: Railway deploy
failures, GitHub Actions, env vars, "it works locally but not deployed."

---

## Railway build fails / deploy won't start

**When:** your deploy to Railway fails or the app won't come up.

```
[CONTEXT] I'm deploying <a Flask app> to Railway for the Deployment <level> assignment.
[ACTUAL] The deploy <fails at build / builds but won't start / starts but URL gives
errors>.

[WHAT'S HAPPENING — my understanding]
Railway deploy works by <your interpretation — "pulls my repo, builds the Dockerfile (or
uses Nixpacks), runs the resulting image, routes traffic to it">. The build logs show
<where it failed>. The deploy logs show <runtime errors>.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "the Dockerfile works locally but Railway can't find requirements.txt
because of a path issue" / "the app binds to 127.0.0.1 so Railway's health check can't
reach it — needs 0.0.0.0" / "the PORT env var — Railway assigns a port and I hardcoded
5000">.

[THE BUILD/DEPLOY LOGS]
```<paste the relevant failing section from Railway dashboard>```
[MY DOCKERFILE]
```dockerfile
<paste>```
[MY APP STARTUP]
```python
<paste the app.run(...) line>```

[ASK] Decode the Railway logs for me (build failure vs runtime failure vs health check
failure). Pinpoint the cause. Common Railway gotchas: must bind to 0.0.0.0, must use
$PORT env var (Railway sets it), Dockerfile must be at repo root, health check path. Show
me the fix and explain the platform's expectations so I can self-debug next time.
```

---

## Deployed but the URL gives 502 / timeout / connection refused

**When:** deploy "succeeded" but the public URL doesn't load.

```
[CONTEXT] Railway says my deploy is "running" / "successful." But `curl https://<my-url>`
gives <502 Bad Gateway / timeout / connection refused>.
[ACTUAL]
```<paste the exact curl output / browser error>```

[WHAT'S HAPPENING — my understanding]
Railway routes traffic from my public URL to my container's port. A 502 means <your
interpretation — "Railway's proxy couldn't get a valid response from my app">. A timeout
means <your interpretation>. This usually means <the app crashed / bound to wrong host /
bound to wrong port / health check failed>.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "my app binds to 127.0.0.1:5000 but Railway routes to 0.0.0.0:$PORT — so
the proxy can't reach it" / "the app started then crashed; check deploy logs" / "I'm not
reading $PORT so I bind to 5000 but Railway expects the app on $PORT">.

[INFO I GATHERED]
- Railway deploy logs (last 20 lines): <paste — did the app print "Running on..."?>
- My app.run line: `app.run(host=<?>, port=<?>)`
- `echo $PORT` equivalent: I <am/am not> reading the PORT env var
- Does it work with `docker run -p 5000:5000 ...` locally and curl localhost:5000? <yes/no>

[ASK] Help me triangulate: is the app even running (check logs), is it listening on the
right host:port (0.0.0.0:$PORT), is Railway's health check passing? Pinpoint the cause
and show the fix. Teach me the Railway/PaaS mental model: the platform assigns a port,
your app must listen on 0.0.0.0 at that port.
```

---

## Environment variables not working in production

**When:** your app works locally with a .env file but the deployed version gets None for
env vars.

```
[CONTEXT] My Flask app reads `APP_ENVIRONMENT` from os.environ. Locally it's set via
<.env / export>. On Railway it's <None / wrong value>.
[ACTUAL] `curl .../health` shows `"environment": null` (or the default fallback).

[WHAT'S HAPPENING — my understanding]
Environment variables are <your interpretation — "set per-process; my local shell/Railway
dashboard sets them; os.environ.get reads them">. Locally I set it via <how>. On Railway,
I <did/didn't> set it in the Variables tab.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "I set the variable in Railway but named it 'APP_ENV' not 'APP_ENVIRONMENT'
so the code reads the wrong key" / "I committed a .env file but Railway doesn't read .env
— I must set vars in the dashboard" / "Python caches os.environ at import and I read it at
module top-level before Railway injects the var">.

[INFO I GATHERED]
- Railway Variables tab shows: <key: value pairs — paste>
- My code: `os.environ.get("<KEY>", "<default>")`
- The health response: <paste>
- Locally: `echo $APP_ENVIRONMENT` = <value>

[ASK] Explain how env vars work across local vs PaaS (shell export vs .env vs dashboard;
the .env file is NOT automatically read in production — you set vars in the platform).
Diagnose the mismatch (wrong key name? not set in dashboard? read too early?). Show the
fix. Teach me: never commit secrets, use the platform's var config, read env vars
defensively with defaults.
```

---

## GitHub Actions workflow doesn't trigger / fails

**When:** your CI workflow doesn't run on push, or runs and fails.

```
[CONTEXT] I have `.github/workflows/deploy.yml`. I push to main. <Nothing happens in the
Actions tab / a run starts but fails>.
[ACTUAL]
- If no run: "I pushed but the Actions tab shows no workflow runs."
- If failed: <paste the failed step's logs>

[WHAT'S HAPPENING — my understanding]
A workflow triggers based on the `on:` section. My `on:` is:
```yaml
<paste the on: block>```
I think this should trigger on <push to main / pull request / etc.>. A workflow fails when
<your interpretation — "any step exits non-zero">.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "my `on:` is misindented so it's not a valid trigger" / "the workflow file
isn't on the default branch, so GitHub doesn't pick it up" / "a step fails — checkout,
build, or deploy">.

[MY WORKFLOW]
```yaml
<paste the full file>```
[ACTIONS TAB STATE]
- <No runs / Run failed at step X — paste the error>

[ASK] First, explain GitHub Actions triggers (the `on:` keys, branch filters, why the
workflow must be on the default branch to trigger). If it's failing, decode the failed
step's logs. Pinpoint the cause (syntax, missing secrets, wrong action version, command
failure). Show the fix. Teach me how to read the Actions UI (the step graph, expandable
logs, re-run failed jobs).
```

---

## Secrets / tokens in GitHub Actions

**When:** you need to use a secret (Railway token, API key) in a workflow.

```
[CONTEXT] My workflow needs <a Railway token / Docker registry password / API key> to
deploy. I don't want to hardcode it.
[GOAL] Use the secret securely via GitHub's secrets mechanism.

[WHAT'S HAPPENING — my understanding]
GitHub Secrets are <your interpretation — "stored encrypted in repo settings, exposed to
workflows as ${{ secrets.NAME }}, not visible in logs">. I added a secret named <NAME> in
Settings → Secrets and variables → Actions.

[WHAT'S WRONG — what I'm unsure about>
I'm unsure <e.g., "do I reference it as ${{ secrets.NAME }} or $NAME or env.NAME?" /
"will it show up in the logs if I print it?" / "can a step in a forked PR access it?">.

[MY WORKFLOW STEP]
```yaml
<paste the step that needs the secret>```

[ASK] Explain GitHub Actions secrets: how to add them, how to reference them
(`${{ secrets.NAME }}` in `env:` then `$NAME` in the script), how GitHub redacts them in
logs, and the security boundaries (secrets aren't exposed to pull requests from forks).
Show me the corrected step. CRITICAL: also tell me what to do if I accidentally committed
a secret (revoke + rotate, don't just delete the commit).
```

---

## Commit hash / version endpoint shows wrong value

**When:** your `/version` endpoint shows "unknown" instead of the Git commit hash.

```
[CONTEXT] My Flask app exposes /version that should return the Git commit hash. The
Dockerfile takes COMMIT_HASH as a build arg. On deployment, /version returns "unknown."
[ACTUAL] `curl .../version` returns `{"version": "unknown"}`.

[WHAT'S HAPPENING — my understanding]
The flow: <CI/Actions passes COMMIT_HASH=${{ github.sha }} to docker build → Dockerfile
ARG COMMIT_HASH → ENV COMMIT_HASH so it's in the container env → app reads
os.environ["COMMIT_HASH"]>. I think the value is getting lost somewhere in this chain.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "my Dockerfile has the ARG but forgot the ENV line, so the var is only
available at build time not runtime" / "the workflow doesn't pass --build-arg" / "the app
reads os.environ at import before the ENV is set">.

[MY DOCKERFILE (ARG/ENV lines)]
```dockerfile
ARG COMMIT_HASH
ENV COMMIT_HASH=${COMMIT_HASH}  # or missing?
```
[MY WORKFLOW BUILD STEP]
```yaml
<paste — does it pass build-args: COMMIT_HASH=${{ github.sha }}?>```
[MY APP CODE]
```python
COMMIT_HASH = os.environ.get("COMMIT_HASH", "unknown")
```

[ASK] Trace the value through the chain: CI → build arg → image env → container env →
Python. Pinpoint where "unknown" appears (the default means os.environ.get returned the
fallback, so the var isn't set in the container). Show the fix. Common bug: ARG without
ENV (ARG is build-time only; ENV persists to runtime). Teach me how to debug env in a
container (`docker exec ... env | grep COMMIT`).
```

---

## Don't understand a deployment concept

**When:** you're fuzzy on CI/CD, deployment, or platform fundamentals.

```
[CONTEXT] I'm learning deployment. I keep getting confused about <concept — e.g., "what
CI vs CD actually mean" / "why we containerize for deploy" / "what a build arg vs env var
is" / "what Railway actually does when I push">.
[GOAL] A clear mental model.

[WHAT'S HAPPENING — my current understanding]
Here's what I think `<concept>` is: <your best guess>. I'm confused about <the sticking
point>.

[ASK] Explain `<concept>` like I'm new to deployment. Give me: (1) the problem it solves,
(2) a concrete walkthrough (e.g., "you push code → CI builds an image → CD deploys it →
users hit the new version"), (3) the tools at each step, (4) the common misconception.
Use my Railway + GitHub Actions setup as the running example.
```

---

## Review my deployment setup

**When:** it deploys but you want a review of the whole pipeline.

```
[CONTEXT] I finished the Deployment <level> assignment. The app is live and the CI/CD
pipeline runs. I want a senior review.

[WHAT'S HAPPENING — my understanding]
My setup: <GitHub repo → GitHub Actions on push to main → builds Docker image with
COMMIT_HASH → deploys to Railway → app live at URL>. I think it's <solid / missing X>.

[MY WORKFLOW]
```yaml
<paste>```
[MY DOCKERFILE]
```dockerfile
<paste>```
[MY APP]
```python
<paste relevant parts — /health, /version, env reading>```

[ASK] Review the whole pipeline. Look for: (1) workflow correctness (triggers, steps,
caching), (2) security (no hardcoded secrets, least-privilege tokens), (3) Dockerfile
correctness (build args, env, health), (4) reliability (what happens on deploy failure?
rollback? health checks?), (5) the "would I trust this in production" test. Top 3-5
issues with fixes. Point out one thing done well.
```
