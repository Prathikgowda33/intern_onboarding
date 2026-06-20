# Prompts — Docker

For the [Docker topic](../topics/docker/). Common situations: Dockerfile build failures,
compose networking, container crashes, "works on my machine" mysteries.

---

## Dockerfile build fails

**When:** `docker build` errors out at some step.

```
[CONTEXT] I'm building a Docker image for <a Flask app / Python script> for the Docker
<level> assignment.
[ACTUAL] `docker build -t <name> .` fails at this step:
```<paste the FULL build output, especially the failing step and error>```

[WHAT'S HAPPENING — my understanding]
A Dockerfile builds <your interpretation — "top to bottom, each instruction creates a
layer; COPY/RUN/etc. execute in order; a failure stops the build">. The error happened at
<COPY / RUN / etc.> which means <your interpretation of what that step tried to do>.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "COPY requirements.txt . fails because the file is in a subfolder, not the
build context root" / "RUN pip install fails because the base image is wrong / no network
in build" / "WORKDIR doesn't exist so COPY target is wrong">.

[MY DOCKERFILE]
```dockerfile
<paste>```
[MY PROJECT STRUCTURE]
```<paste `ls -R` or tree, excluding node_modules/.git>```

[ASK] Walk through my Dockerfile layer by layer — what each instruction does and what
filesystem state it produces. Pinpoint the failing step and explain WHY it fails (wrong
path? missing file? wrong base image? command syntax?). Show the fix. Teach me how to read
Docker build output (the `=> [stage x/y] ...` lines) and how to debug a failing RUN
(interactive `docker run` the partial image).
```

---

## Container starts then immediately exits

**When:** `docker run` exits right away — nothing stays up.

```
[CONTEXT] I run my container and it exits immediately instead of serving my app.
[ACTUAL]
```<paste: the docker run command + what it prints before exiting>```
`docker ps -a` shows it as <Exited (0) / Exited (1) / etc.>.

[WHAT'S HAPPENING — my understanding]
A container runs <your interpretation — "as long as its main process (PID 1) is alive;
when the main process exits, the container exits">. My CMD/entrypoint is <your command>.
I think the process <your interpretation of why it exits — "the command ran and finished"
/ "the command errored and crashed">.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "CMD ['python', 'app.py'] — but app.py has a syntax error so Python exits"
/ "I used CMD in shell form and the process detached" / "the app binds to 127.0.0.1 not
0.0.0.0 so... no that's about reachability not exit" / "I need to see the logs">.

[MY DOCKERFILE (CMD line)]
```dockerfile
CMD [...]
```
[THE LOGS]
```<paste `docker logs <container>` output>```

[ASK] Explain why a container exits (main process lifecycle). Help me read the exit code
(0 = clean exit, 1+ = error) and the logs. Pinpoint why my container exits — is the app
crashing, or is the command wrong (e.g., app ran and finished)? Show the fix. Common
gotchas: CMD form (shell vs exec), the app must stay in foreground.
```

---

## App runs in container but can't reach it from host

**When:** container is up but `curl localhost:PORT` fails.

```
[CONTEXT] My container is running (shows in `docker ps`). But `curl http://localhost:5000`
from my host fails.
[ACTUAL] <Connection refused / timeout / wrong response>.

[WHAT'S HAPPENING — my understanding]
Containers have <your interpretation — "their own network namespace; to reach a container
port from the host, you publish it with -p host:container">. My run command uses
<`-p 5000:5000` / no -p / something else>. Inside the container, my app binds to
<127.0.0.1 / 0.0.0.0>.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "I forgot -p so the port isn't published" / "my app binds to 127.0.0.1
which inside the container means 'container's loopback only' — I need 0.0.0.0 to be
reachable from outside" / "the host port 5000 is already in use">.

[INFO I GATHERED]
- `docker ps`: <paste — does it show 0.0.0.0:5000->5000?>
- `docker exec <c> curl localhost:5000` from INSIDE: <works/fails?>
- `curl localhost:5000` from host: <error?>
- My app's bind line: `app.run(host=<?>...)`

[ASK] Explain container networking (the critical 0.0.0.0 vs 127.0.0.1 distinction — this
is the #1 Docker gotcha). Help me triangulate using the two curl tests (inside vs outside
the container). Pinpoint the cause and show the fix.
```

---

## Two containers can't talk to each other (compose networking)

**When:** web container can't reach redis/db container.

```
[CONTEXT] I have a docker-compose with `web` and `redis` services. My web app connects to
redis but fails.
[ACTUAL] Web logs show: `Redis connection refused` / `<paste>`.

[WHAT'S HAPPENING — my understanding]
In docker-compose, containers <your interpretation — "can reach each other by service name
as hostname, because compose creates a network and DNS for each service">. So my web app
should connect to host `redis` (not `localhost`) at port <6379>. My app's connection string
is `<redis://localhost:6379 / redis://redis:6379 / etc.>`.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "my app connects to 'localhost' but redis is in a different container — I
need 'redis'" / "the services aren't on the same network" / "redis isn't actually running
— check docker compose ps">.

[MY COMPOSE FILE]
```yaml
<paste>```
[MY APP'S CONNECTION CODE]
```python
<paste — e.g., redis.Redis(host=?, port=?)>```
[WHAT I TRIED]
- `docker compose exec web ping redis`: <works/fails — output>
- `docker compose ps`: <both running? / redis exited?>
- `docker compose exec web curl redis:6379` or equivalent: <result>

[ASK] Explain compose networking (the DNS-by-service-name magic, why localhost doesn't
work across containers). Help me triangulate with the ping test. Pinpoint whether this is
a hostname issue, a network issue, or redis-not-running. Show the fix.
```

---

## Data doesn't persist after container restart

**When:** your database/redis data disappears when the container restarts.

```
[CONTEXT] My redis/db container loses data when I `docker compose down` and `up` again.
[GOAL] Data should persist across restarts.
[ACTUAL] After restart, the data is gone.

[WHAT'S HAPPENING — my understanding]
Containers are <your interpretation — "ephemeral by default; the writable layer is
destroyed when the container is removed; to persist data, you mount a volume to a path">.
My compose file <has/doesn't have> a volumes section.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "I have no volume, so data lives in the container's writable layer which is
deleted on `down`" / "I have a volume but it's mounted to the wrong path (redis stores in
/data, I mounted /var/lib/redis)" / "`down` removes volumes; `stop` doesn't">.

[MY COMPOSE FILE]
```yaml
<paste the redis/db service + volumes>```
[WHAT I TRIED]
- `docker compose down && docker compose up` → data <gone/present>
- `docker volume ls`: <paste>
- `docker compose down -v` vs `docker compose down`: <did I run -v?>

[ASK] Explain container storage (writable layer vs volumes vs bind mounts). Diagnose why
my data doesn't persist. Show the correct volume config for <redis (which stores in /data)
/ postgres (which stores in /var/lib/postgresql/data)>. Warn me about `down -v` deleting
volumes.
```

---

## "Works on my machine" — works locally, breaks in container (or vice versa)

**When:** code runs fine locally but the container version behaves differently.

```
[CONTEXT] My Flask app works when I run `python app.py` locally. But in the Docker
container it <errors / can't find a file / different output>.
[ACTUAL] <describe the difference>.

[WHAT'S HAPPENING — my understanding]
The container environment differs from my local env in <your understanding — "different
OS (linux), different Python version, different working directory, files copied not
mounted, no access to my host filesystem">. So things like <relative paths / env vars /
host services> behave differently.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "my app reads a file with a relative path 'data/x.csv', which resolves to
CWD; in the container CWD is /app but I COPY'd files to /app/src so the path is wrong" /
"the base image has Python 3.9, my local has 3.11, a feature differs" / "the container
can't reach my host's localhost:5432 postgres">.

[INFO I GATHERED]
- `docker exec <c> python --version`: <paste>
- `docker exec <c> pwd`: <paste>
- `docker exec <c> ls`: <paste>
- Local: <what works, with the same checks>

[ASK] Help me diff the two environments systematically. Pinpoint the env difference
causing the bug. Show the fix (often: absolute paths, COPY to the right place, env vars,
or use host.docker.internal to reach host services). Teach me the general principle:
"treat the container as a different machine and debug it directly with docker exec."
```

---

## Don't understand a Docker concept (layers, images, volumes, networks)

**When:** you're fuzzy on Docker fundamentals.

```
[CONTEXT] I'm learning Docker. I keep getting confused about <concept — e.g., "the
difference between an image and a container" / "what a layer is" / "bind mount vs volume"
/ "what docker compose actually does vs docker run">.
[GOAL] A clear mental model.

[WHAT'S HAPPENING — my current understanding]
Here's what I think `<concept>` is: <your best guess>. I'm specifically confused about
<the sticking point — e.g., "if images are immutable, how does my container save files?">.

[ASK] Explain `<concept>` like I'm new to Docker. Give me: (1) the problem it solves, (2)
a tiny concrete example (e.g., "an image is a recipe + ingredients; a container is the
cake you bake from it"), (3) the commands that map to it, (4) the common misconception.
Avoid jargon or define it inline.
```

---

## Review my Dockerfile / compose before submitting

**When:** it works but you want best-practices review.

```
[CONTEXT] I finished the Docker <level> assignment. Image builds and runs. I want a
senior review of the Dockerfile / compose.

[WHAT'S HAPPENING — my understanding]
My Dockerfile: <base image, layers, CMD>. My compose: <services, networks, volumes>. I
think it's <decent / probably not following best practices> because <reasons>.

[MY DOCKERFILE]
```dockerfile
<paste>```
[MY COMPOSE]
```yaml
<paste>```

[ASK] Review as a senior would. Look for: (1) image size (slim/alpine base, multi-stage,
layer caching — copy requirements before code), (2) security (running as root?, secrets
in image?), (3) correctness (EXPOSE, CMD form, HEALTHCHECK), (4) compose best practices
(depends_on, named volumes, restart policy). Top 3-5 issues with fixes. Explain WHY each
matters (e.g., "copy requirements.txt before COPY . so you don't reinstall pip packages
every time code changes").
```
