# <Topic Name>

<!--
  This is a TEMPLATE. To create a real topic, see ../CONTRIBUTING.md.

  TWO SHAPES ARE SUPPORTED:

  ── Single-level topic (simplest) ──
    topics/<slug>/
      ├── README.md            ← this file, the assignment
      ├── constraints.md
      ├── resources.md
      ├── RESULTS.md
      └── starter/             (optional: skeleton/fix-this only)

  ── Tiered topic (multi-level, for topics that naturally have
     beginner / intermediate / advanced flavors) ──
    topics/<slug>/
      ├── README.md            ← "pick your level" guidance (NOT an assignment)
      ├── resources.md         ← shared, covers all levels from scratch
      └── levels/
          ├── level-1-<name>/  ← each level is a full single-level topic
          │   ├── README.md       (README + constraints + resources + RESULTS + starter/)
          │   ├── constraints.md
          │   ├── resources.md    (optional — can just link to ../resources.md)
          │   ├── RESULTS.md
          │   └── starter/
          ├── level-2-<name>/
          └── level-3-<name>/

  WHICH TO USE:
    - Single-level when the topic is one coherent skill. Don't manufacture levels.
    - Tiered only when the topic genuinely has beginner vs advanced flavors AND the
      startup would realistically hire people at different points on that curve.

  This README file is written for the SINGLE-LEVEL shape. For a tiered topic, the
  top-level README becomes a level-selection guide (see topics/linux/README.md for an
  example), and each level folder is itself a single-level topic.
-->

<!--
  Front-matter (metadata). Keep this block at the top.
-->
<!--
slug: <topic-slug>
month: <1 | 2 | 3>
skills: <comma-separated, e.g. "shell, filesystem, permissions">
difficulty: <Easy | Medium | Hard>
estimated_time: <e.g. "2-3h">
starter_mode: <scratch | skeleton | fix-this>
levels: <omit for single-level | "1,2,3" for tiered>
-->

## Prerequisites

Before starting this topic, install/verify the tools below. Each has a one-line check —
run it; if it prints a version, you're ready. If it says "command not found", follow the
install steps for your OS.

<Remove the tools this topic doesn't need. Add any topic-specific ones. The format is:
what + install (Windows/macOS/Linux) + verify command.>

### <Tool 1, e.g. Git>

You'll use this to <one-line why>.

- **Verify:** `git --version` (should print `git version 2.x.x`)
- **Windows:** install [Git for Windows](https://git-scm.com/download/win) — this also
  gives you Git Bash, the terminal you'll use throughout.
- **macOS:** `git --version` usually works out of the box; if not, install Command Line
  Tools with `xcode-select --install`, or [Git for Mac](https://git-scm.com/download/mac).
- **Linux (Debian/Ubuntu):** `sudo apt update && sudo apt install -y git`

### <Tool 2, e.g. Python 3>

<...same format...>

### Terminal / shell

<Almost every topic needs a terminal. Include this block when the topic uses shell
commands. IMPORTANT — choose the Windows recommendation based on what the topic checks:
- If the topic checks REAL LINUX behavior (file permissions, chown, /var paths, GNU tools)
  → require WSL2 for Windows. Git Bash does NOT provide real Linux semantics.
- If the topic only runs a language runtime (Python/Node) or git → Git Bash is fine.
State which case applies for THIS topic.>

- **Verify:** open your terminal and run `ls -l /` — you should see a Unix filesystem
  (`bin`, `etc`, `usr`, ...) with permission strings like `drwxr-xr-x`.
- **Windows:** use **Git Bash** (installs with [Git for Windows](https://git-scm.com/download/win))
  for topics that just need a bash-like shell + a runtime. For topics that need **real
  Linux** (permissions, GNU tools, containers), use **WSL2** instead: open PowerShell as
  Administrator, run `wsl --install`, restart, launch Ubuntu
  (<https://learn.microsoft.com/en-us/windows/wsl/install>). Pick the one this topic needs.
- **macOS:** Terminal.app (Cmd+Space, type "terminal") or iTerm2. macOS is Unix, so it
  works for shell topics. (Note: some tools like `sed`/`awk` are BSD-flavored, not GNU.)
- **Linux:** your default terminal (Ctrl+Alt+T on most distros).

If any check fails and you can't resolve it from the steps above, ask in the team channel
before burning an hour — setup issues are common and quick to unblock together.



## What to build

<In 2–4 sentences, describe the project the intern will build. One small, scoped project.
Example: "Build a small issue tracker with login, CRUD on issues, and a database. Run it
locally with Docker."> 

## Why this matters

<1–2 sentences on how this skill shows up in real startup work. Example: "Every feature
we ship touches the filesystem, permissions, and the shell. Being fast here is
table stakes.">

## Deliverables

List the exact outputs the intern must produce. Be concrete — constraints reference these.

- <e.g. "A runnable app invokable with a single command from this folder.">
- <e.g. "A `README.md` at the topic root with run steps.">
- <e.g. "The solution committed in this folder (do not modify files outside it).">

## Starter mode: `<scratch | skeleton | fix-this>`

- If **scratch**: build everything from the prompt above. No starter code is provided.
- If **skeleton**: the `starter/` folder contains stub files. Fill them in. Do not
  rename or move them unless a constraint allows it.
- If **fix-this**: the `starter/` folder contains a broken/incomplete solution. Make it
  pass the constraints. You may change anything inside `starter/`.

## How you'll be checked

Open [constraints.md](constraints.md). It lists the high-level acceptance criteria.
You verify each one manually by running your solution and observing the result, then
self-report in [RESULTS.md](RESULTS.md). See [../HOW_IT_WORKS.md](../HOW_IT_WORKS.md)
for the full workflow.

- **All constraints pass** → topic cleared, skip [resources.md](resources.md).
- **Any constraint fails** → study [resources.md](resources.md), fix, re-check.

<!-- FOR TIERED TOPICS, replace the section above with level-selection guidance:

## Pick your level

This topic is tiered. Choose the highest level you think you can clear. Fail it →
drop to the level below. Pass it → topic cleared, you don't need the lower levels.

| Level | For whom | What |
|-------|----------|------|
| 1     | <never done X>  | <one-line description> |
| 2     | <used X before> | <one-line description> |
| 3     | <comfortable>   | <one-line description> |

Open the README inside your chosen level's folder.

## Resources (shared)

[resources.md](resources.md) covers the topic from absolute basics through advanced.
Start at the section matching your level and work outward as needed.
-->
