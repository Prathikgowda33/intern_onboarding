# Level 1 — Local Git Fundamentals

<!--
  Level metadata:
    slug: git/level-1-local-fundamentals
    skills: git init, commit, branch, merge, meaningful commit messages
    difficulty: Easy
    estimated_time: 1-2h
    starter_mode: scratch
-->

## Prerequisites

You need **Git** installed and a **terminal**. This topic only uses Git commands — no real
Linux behavior is required — so **Git Bash is fine on Windows** (no need for WSL2 here,
though WSL2 also works if you already have it from the Linux topic).

### Git

- **Verify:** `git --version` (prints `git version 2.x.x`).
- **Windows:** install [Git for Windows](https://git-scm.com/download/win). This also
  gives you **Git Bash**, the terminal to use for this topic.
- **macOS:** `git --version` usually works; if not, `xcode-select --install`, or
  [Git for Mac](https://git-scm.com/download/mac).
- **Linux (Debian/Ubuntu):** `sudo apt update && sudo apt install -y git`.

### Terminal

- **Verify:** open your terminal and run `git --version` from it (proves both work).
- **Windows:** **Git Bash** (from Git for Windows) — do not use CMD/PowerShell.
- **macOS:** Terminal.app (Cmd+Space, type "terminal").
- **Linux:** your default terminal.

### Get this repo

```bash
git clone <this-repo-url>   # the repo's web URL — see LEARNING_PATH.md if unclear   # see note below for what URL to use
cd intern-onboarding/topics/git/levels/level-1-local-fundamentals
```

> **What's `<this-repo-url>`?** It's the web address of this repository. On GitHub, click
> the green **"<> Code"** button on the repo page and copy the URL (looks like
> `https://github.com/<user>/intern-onboarding.git`).

If any check fails, follow [SELF_HELP.md](../../../../SELF_HELP.md) before spending an hour on it — most issues solve fast with AI or a web search.

## What to build

Build a small **project workspace** inside this folder using Git. You'll create a
"notes" project — a few markdown files and a simple Python script — and practice the
core Git workflow: initialize, commit, branch, merge.

### Step-by-step

> **Where to do this work:** Because you cloned the repo, this folder is *already* inside
> a Git repository — so `git init` here would create a confusing nested repo. **Do this
> assignment in a SEPARATE folder outside the cloned repo** (e.g., `~/my-git-practice/`),
> OR if you want to use this exact folder, you can skip `git init` and just use the
> existing repo (your history will be part of the bigger repo — that's fine for practice).

1. **Initialize** a Git repository in your chosen folder (`git init`) — only if you're
   using a separate folder. (Skips if you're inside the existing repo.)
2. **Create** at least 3 files:
   - `notes.md` — a markdown file with a few notes about what you're learning.
   - `scripts/hello.sh` — a bash script that prints "Hello from Level 1". Make it
     executable with `chmod +x scripts/hello.sh` (the `+x` sets the executable bit so
     the script can be run directly — covered in Linux L1 if you haven't done it).
   - `README.md` — a brief description of the project.
3. **Commit** all files to the `main` branch with at least 3 meaningful commits. Use
   good commit messages (e.g., "add initial project structure with notes and script",
   not "update" or "fix"). The pattern for each commit:
   ```bash
   git add <file>           # stage the file
   git commit -m "<message>"  # record a snapshot with a message
   ```
4. **Create a feature branch** from main:
   ```bash
   git checkout -b add-summary
   ```
   The `-b` flag means "create the branch AND switch to it in one command." Branching
   lets you work on a feature without touching main.
5. **Add** at least 2 commits on the feature branch — e.g., add a `summary.md` file
   with a summary of your notes, and update `README.md` to reference it. (Use the same
   `git add` + `git commit` pattern as step 3.)
6. **Merge** the feature branch back into main:
   ```bash
   git checkout main            # switch back to main
   git merge --no-ff add-summary  # join the branch's work into main
   ```
   The `--no-ff` flag forces a merge commit even when a fast-forward is possible — this
   makes the branch history visible in the graph (constraint C5 checks for this).

When you're done, you should have a Git history that shows: work on main, a branch,
work on the branch, and a merge commit.

## Why this matters

Every line of code you ship at a startup goes through Git. Branching lets you work on
features without breaking main. Merge commits show the history of how a feature came
together. Meaningful commit messages let anyone (including your future self) understand
*why* a change was made. These are daily skills, not interview trivia.

## Deliverables

- A Git repository initialized in this folder.
- At least 3 files with real content.
- A commit history showing at least 3 commits on main and 2 on a feature branch.
- A merge commit joining the feature branch into main.

## Starter mode: `scratch`

No starter code. You build everything from the assignment above. The constraints check
Git state (history, branches, messages) — not the content of your files.

## How you'll be checked

Open [constraints.md](constraints.md). Each constraint is verified by running a Git
command and observing the output. Self-report in [RESULTS.md](RESULTS.md). See
[../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the full workflow.

- All constraints pass → Level 1 cleared (and the whole Git topic is cleared).
- Any constraint fails → study [../../../resources.md](../../../resources.md), fix, re-check.
