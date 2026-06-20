# Level 2 — Collaboration & Merge Conflicts

<!--
  Level metadata:
    slug: git/level-2-collaboration
    skills: merge conflicts, conflict resolution, collaboration simulation, meaningful commits
    difficulty: Medium
    estimated_time: 2-3h
    starter_mode: scratch (starter code provided for the conflict scenario)
-->

## Prerequisites

You need **Git** and a **terminal** — same as Level 1. **Git Bash is fine on Windows.**

### Git

- **Verify:** `git --version` (prints `git version 2.x.x`).
- **Windows:** [Git for Windows](https://git-scm.com/download/win) — use Git Bash.
- **macOS:** `xcode-select --install` or [Git for Mac](https://git-scm.com/download/mac).
- **Linux:** `sudo apt update && sudo apt install -y git`.

### Terminal

- **Windows:** Git Bash. **macOS:** Terminal.app. **Linux:** your default terminal.

### Get this repo

```bash
git clone <this-repo-url>   # the repo's web URL — see LEARNING_PATH.md if unclear
cd intern-onboarding/topics/git/levels/level-2-collaboration
```

If any check fails, follow [SELF_HELP.md](../../../../SELF_HELP.md) before spending an hour on it — most issues solve fast with AI or a web search.

## What to build

**Simulate a real collaboration conflict.** You'll work in a single repo, playing two
roles: "you" (working on a feature branch) and a "teammate" (making changes on main).
The twist: both of you edit the same lines in the same file, causing a **real merge
conflict** that you must resolve.

### The setup (starter code)

The `starter/` folder contains:
- `app.py` — a Python script with a `GREETING` variable.
- `notes/shared.md` — a shared notes file.

### Step-by-step

1. **Initialize** a Git repo in this folder (`git init`).
2. **Copy** the starter files into the repo root (this folder) and commit them on `main`:
   ```bash
   cp starter/app.py starter/notes/shared.md .
   git add .
   git commit -m "add starter project with greeting app and shared notes"
   ```
3. **Create a feature branch** from main:
   ```bash
   git checkout -b feature/improve-greeting
   ```
4. **Edit `app.py` on your feature branch:**
   Change the `GREETING` variable to something different, e.g., `"Hello from feature branch!"`.
   Add a comment explaining the change.
   Commit: `git commit -am "update greeting to feature branch version"`
5. **Simulate the teammate** — switch back to main and edit the same line:
   ```bash
   git checkout main
   ```
   Edit `app.py`: change the `GREETING` variable to something different from both the
   original and your feature branch, e.g., `"Hello from the team!"`.
   Also edit `notes/shared.md`: add a note like "Team member updated this file."
   Commit: `git commit -am "update greeting and notes as teammate"`
6. **Merge main into your feature branch** (this will cause the conflict):
   ```bash
   git checkout feature/improve-greeting
   git merge main
   ```
7. **Resolve the conflict** — Git will mark the conflicted file with `<<<<<<<`, `=======`,
   and `>>>>>>>` markers. Open the file and edit it to keep both changes (or choose one
   — the constraint just requires that conflict markers are gone and the file works).
8. **Commit the resolution:**
   ```bash
   git add .
   git commit -m "resolve merge conflict: combine greeting changes from both branches"
   ```
9. **Merge the feature branch into main:**
   ```bash
   git checkout main
   git merge --no-ff feature/improve-greeting -m "merge feature/improve-greeting into main"
   ```
10. **Verify the app still works:**
    ```bash
    python3 app.py
    ```

## Why this matters

Merge conflicts are inevitable in real teams. Everyone edits the same files eventually.
Knowing how to read the conflict markers, understand what happened, and resolve the
conflict without losing anyone's work is a skill you'll use weekly. The key insight:
conflicts aren't scary — they're Git telling you "two people changed the same thing,
please decide what the right answer is."

## Deliverables

- A Git repo in this folder with the full workflow above.
- At least one resolved merge conflict (conflict markers removed, file works).
- The `app.py` script runs without errors after resolution.
- Meaningful commit messages throughout.

## Starter mode: `scratch` (starter code provided)

The `starter/` folder provides the initial files (`app.py` and `notes/shared.md`). You
initialize the repo, copy them in, and drive the entire workflow yourself. The starter
exists only to give you a concrete file to create conflicts in.

## How you'll be checked

Open [constraints.md](constraints.md). Each constraint is verified by running a Git
command or a Python command. Self-report in [RESULTS.md](RESULTS.md). See
[../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the full workflow.

- All constraints pass → Level 2 cleared (and the whole Git topic is cleared).
- Any constraint fails → study [../../../resources.md](../../../resources.md), fix, re-check.
