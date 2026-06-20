# Linux — Shell Log Analyzer

<!--
  Topic metadata:
    slug: linux
    month: 1
    skills: shell, filesystem, permissions, text processing, scripting
    difficulty: Easy
    estimated_time: 2-3h
    starter_mode: scratch
-->

## Prerequisites

Level 2 needs a **real Linux (or Unix-like) shell** with bash and the standard
text-processing tools (`awk`, `grep`, `sort`, `uniq`, `wc`).

> **If you already set up WSL2/Ubuntu for Level 1, you're done** — all these tools are
> pre-installed. Skip to "Get this repo" below.

### bash + text tools

- **Verify:** run `bash --version` (prints `GNU bash, version ...`) and `awk --version`
  (prints a version). Both should succeed.
- **Windows (REQUIRED):** use **WSL2/Ubuntu** (not Git Bash). If you haven't set it up,
  follow the Level 1 prerequisites — the short version: open **PowerShell as Admin**,
  run `wsl --install`, restart, launch Ubuntu. bash, awk, grep, sort, uniq, wc are all
  pre-installed in Ubuntu. (Official WSL guide:
  <https://learn.microsoft.com/en-us/windows/wsl/install>)
- **macOS:** Terminal.app. Everything is pre-installed (BSD-flavored, but fine here).
- **Linux:** your default terminal. Everything is pre-installed.
  If somehow missing on Debian/Ubuntu: `sudo apt install -y gawk coreutils`.

### Get this repo

Inside your Linux shell:

```bash
git clone <this-repo-url>   # the repo's web URL — see LEARNING_PATH.md if unclear
cd intern-onboarding/topics/linux/levels/level-2-log-analyzer
```

If you did Level 1 here, you already have the repo — just `cd` to this level's folder.

If any check fails, follow [SELF_HELP.md](../../../../SELF_HELP.md) before spending an hour on it — most issues solve fast with AI or a web search.

## What to build

Write a **bash script** that analyzes a web server access log and prints a human-readable
summary. You are given a sample log file ([sample-access.log](sample-access.log)) in this
folder; your script must work on it.

When run, your script must output four sections:

1. **Top N IPs** — the top N most frequent client IPs, with their request counts.
2. **Error breakdown** — total count of `4xx` responses and total count of `5xx`
   responses.
3. **Busiest hour** — the single hour (00–23) with the most requests, and that count.
4. **Total requests** — total number of log lines processed.

The script's interface:

```
./analyze.sh <logfile> [N]
```

- `<logfile>` — path to the access log (required).
- `[N]` — number of top IPs to show. Optional. Defaults to `5`.

### Example

```
$ ./analyze.sh sample-access.log 3
=== Top 3 IPs ===
203.0.113.7     142
198.51.100.23   98
192.0.2.88      71

=== Errors ===
4xx errors: 85
5xx errors: 36

=== Busiest hour ===
14:00 (count: 137)

=== Total ===
Total requests processed: 526
```

These are the real values for the provided `sample-access.log`, so you can use them as a
sanity check. (The exact formatting/spacing of your output is up to you — the constraints
check the values, not the whitespace.)

## Why this matters

In a web startup you constantly look at logs — "who's hitting us?", "are there 5xx
spikes?", "when's our peak hour?". Doing this from the shell with standard tools
(grep/awk/sort/uniq) is faster than spinning up a dashboard for one-off questions. If you
can parse text and write a small script here, you can debug real incidents.

## Deliverables

- A script named `analyze.sh` in this folder.
- It must be **executable** (`chmod +x`).
- It must accept the arguments above and produce the four sections in the order shown.
- It must run on a clean Linux shell with no special setup beyond standard coreutils.

## Starter mode: `scratch`

Build everything from the prompt above. No starter code is provided. You choose the
tools (awk? grep+sort+uniq? a mix?) — the constraints only check behavior, not how you
write it.

## How you'll be checked

Open [constraints.md](constraints.md). Each constraint is a manual check — run the script,
look at the output. Self-report pass/fail in [RESULTS.md](RESULTS.md). See
[../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the workflow.

- All constraints pass → topic cleared, skip [resources.md](../../resources.md).
- Any constraint fails → study [../../resources.md](../../resources.md) (the shared Linux
  resources, "Text processing" section), fix, re-check.

## Notes & hints

- The sample log uses the common "combined log format" with a leading timestamp field
  (see the file). Inspect it with `head`/`less` before scripting.
- `awk` is your friend for field extraction; `sort | uniq -c | sort -rn` is the classic
  counting pattern.
- Decide on a quoting/error-handling stance up front (what if the file is missing? what
  if N is not a number?). Constraint C7 covers the error case.
