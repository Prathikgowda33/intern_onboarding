# Linux Level 3 — Live Web Server Logs

<!--
  Level metadata:
    slug: linux/level-3-webserver-logs
    skills: containers (black-box), live logs, log capture, text processing, scripting
    difficulty: Medium
    estimated_time: 2-3h
    starter_mode: scratch
-->

## Prerequisites

Level 3 needs a **real Linux (or Unix-like) shell**, **curl**, and **Docker**. Docker is
the new piece — you'll use it as a black box here (one command to start a web server).
It's taught properly in the Month 2 Docker topic; for now you just need it installed and
running.

> **If you set up WSL2/Ubuntu for Levels 1–2**, you already have the shell + curl. You
> just need Docker on top — see "Docker" below.

### bash + curl

- **Verify:** `bash --version` and `curl --version` both print versions.
- **Windows (REQUIRED):** use your **WSL2/Ubuntu** shell from Levels 1–2 (not Git Bash).
  curl is pre-installed in Ubuntu. If you haven't set up WSL2 yet, follow the Level 1
  prerequisites first.
- **macOS:** Terminal.app — bash and curl are pre-installed.
- **Linux:** pre-installed. (Debian/Ubuntu: `sudo apt install -y curl` if missing.)

### Docker

- **Verify:** run `docker --version` (prints `Docker version ...`) **and**
  `docker run --rm hello-world`. The second command downloads a tiny test image and
  prints a "Hello from Docker!" message. If both work, Docker is installed **and
  running**. **Run this verify command from inside your Linux shell** (WSL2/Ubuntu on
  Windows) — that's where you'll do the whole level.
- **Windows:** install **Docker Desktop** (<https://www.docker.com/products/docker-desktop/>).
  It uses your existing WSL2 as its engine. After installing and starting Docker Desktop:
  1. Open Docker Desktop → **Settings (⚙️)** → **General** → confirm
     ✅ "Use the WSL 2 based engine" is on.
  2. Go to **Resources → WSL Integration** → enable ✅ "Enable integration with my
     default WSL distro", then toggle your **Ubuntu** distro on. Click **Apply & Restart**.
  3. Wait for the whale icon to say "running". Then, **inside your Ubuntu shell**, run
     `docker run --rm hello-world` to confirm Docker is reachable from WSL2.
  (Official guide: <https://docs.docker.com/desktop/wsl/>)
- **macOS:** install **Docker Desktop** for Mac from the same link above. Open it, wait
  for the whale icon to say "running". Apple Silicon (M1/M2/M3): pick the "Apple Chip"
  build — it runs x86 images like `nginx` fine via emulation. Verify with
  `docker run --rm hello-world`.
- **Linux (Debian/Ubuntu):** follow the official
  [Docker Engine install](https://docs.docker.com/engine/install/). After install, add
  yourself to the docker group so you don't need `sudo` every time:
  `sudo usermod -aG docker $USER`, then log out and back in (or reboot). Verify with
  `docker run --rm hello-world`.

> **Docker not reachable from WSL2?** The #1 Windows gotcha is forgetting to enable
> Ubuntu under Docker Desktop's **Resources → WSL Integration**. If `docker` works in
> PowerShell but "command not found" inside Ubuntu, that's the toggle you missed. Other
> common snag: virtualization disabled in BIOS/UEFI (whale icon stays red). Ask in the
> [SELF_HELP.md](../../../../SELF_HELP.md) if stuck — this is a common day-one snag.

### Get this repo

Inside your Linux shell (WSL2/Ubuntu on Windows, Terminal on Mac, your terminal on Linux):

```bash
git clone <this-repo-url>   # the repo's web URL — see LEARNING_PATH.md if unclear
cd intern-onboarding/topics/linux/levels/level-3-webserver-logs
```

If you did Level 1 or 2 here, you already have the repo — just `cd` to this level.

If any check fails and you can't resolve it from the steps above, follow [SELF_HELP.md](../../../../SELF_HELP.md)
before spending an hour — Docker setup issues are common and quick to unblock together.

## What to build

Run a real **nginx** web server inside a Docker container, generate traffic against it,
capture its **live** access logs to a file, then write a script that analyzes those logs.

This is the realistic version of Level 2's exercise: instead of being handed a static
log file, you produce the log yourself by hitting a running server, then analyze what you
collected.

### Steps

1. **Start an nginx container** on port 8080:

   ```bash
   docker run -d --name nginx-logs -p 8080:80 nginx
   ```

   (You don't need to understand Docker here — it's a Month 2 topic. This one command
   starts a web server. That's all you need from Docker for this level.)

2. **Generate traffic** by hitting the server repeatedly with different paths and the
   occasional bad URL (so you get some 404s). For example:

   ```bash
   for i in $(seq 1 50); do curl -s http://localhost:8080/ > /dev/null; done
   for i in $(seq 1 10); do curl -s http://localhost:8080/missing-page-$i > /dev/null; done
   ```

   Feel free to vary IPs by adding headers or just accept that all requests look like
   they come from `127.0.0.1` — that's fine, the analysis still works.

3. **Capture the logs**. nginx writes its access log to the container's stdout, so
   capture it with `docker logs`:

   ```bash
   docker logs nginx-logs > ./captured-access.log 2>&1
   ```

   ⚠️ **Gotcha:** this also captures nginx's startup lines (lines starting with
   `/docker-entrypoint.sh:` or similar). Those are NOT access-log entries and will
   inflate your "total" count. Filter them out so only real access-log lines remain:

   ```bash
   # Keep only lines that look like access logs (start with an IP address)
   grep -E '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' captured-access.log > access-only.log
   mv access-only.log captured-access.log
   ```

   Inspect the result with `head captured-access.log` — every line should start with an
   IP address. If it doesn't, adjust your filter. Your analysis script will run on this
   cleaned file.

   (Note: do NOT use `docker cp nginx-logs:/var/log/nginx/access.log` — in the official
   nginx image that path is a symlink to `/dev/stdout`, so it captures nothing useful.
   `docker logs` is the correct method.)

4. **Write `analyze-live.sh`** — a script with the same interface as Level 2's analyzer:

   ```
   ./analyze-live.sh <logfile> [N]
   ```

   It must print the same four sections (Top N IPs, 4xx/5xx counts, busiest hour, total).
   You may reuse your Level 2 logic if you did Level 2 — this is the same analysis, just
   on a log you produced yourself.

5. **Clean up** when done:

   ```bash
   docker stop nginx-logs && docker rm nginx-logs
   ```

## Why this matters

This is the actual loop of web-ops work: *something is running, it's producing logs,
figure out what those logs say*. Almost no debugging starts from a tidy static file —
you're always pulling logs off a live system and making sense of them under time
pressure. Doing this once, end to end, is the difference between "I've read about logs"
and "I can debug an incident."

## Deliverables

- A script `analyze-live.sh` in this folder, executable, with the interface above.
- A captured log file `captured-access.log` in this folder (the actual logs you
  produced — not edited, not faked).
- Your script's output on that log, pasted into [RESULTS.md](RESULTS.md) as evidence.

## Starter mode: `scratch`

No starter code. Docker is used as a black box here (the one `docker run` command is
given above). You're not expected to understand containers — that's the Month 2 Docker
topic. This level is about *logs and analysis*, with a real server as the log source.

## How you'll be checked

Open [constraints.md](constraints.md). Constraints check that you actually ran a
container, captured real logs from it, and that your analysis script works on those logs.
Self-report in [RESULTS.md](RESULTS.md). See [../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md).

- All constraints pass → Level 3 cleared → Linux topic cleared.
- Any constraint fails → study [../../resources.md](../../resources.md), section
  "Running services in containers", fix, re-check.

## Notes & hints

- The nginx default access log format is slightly different from Level 2's combined
  format — the first field is the client IP and the status is still a fixed field, but
  **inspect the actual log with `head` before scripting** so your field numbers are
  right. Don't assume; look.
- To produce a variety of status codes, request pages that don't exist (404s). Generating
  5xx is harder with plain nginx — if you can't get any, that's fine; your script should
  just report `5xx errors: 0` for that section. The constraint only checks the count
  matches reality, not that it's non-zero.
- `docker logs nginx-logs` vs `docker cp ...access.log` may give you slightly different
  formats (one may include the request line quoted differently). Pick one source and
  stick with it.
