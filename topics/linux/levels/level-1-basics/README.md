# Linux Level 1 — Command-Line Basics

<!--
  Level metadata:
    slug: linux/level-1-basics
    skills: navigation, file operations, permissions, reading files
    difficulty: Easy
    estimated_time: 1-2h
    starter_mode: scratch
-->

## Prerequisites

Level 1 needs a **real Linux (or Unix-like) shell** — because the constraints check real
Unix file permissions, which don't behave correctly on Windows' native tools. Set up your
environment once here and it works for all three levels.

### A real Linux shell

You need a terminal running an actual Linux (or Unix) shell where `ls`, `cd`, `mkdir`,
`chmod` all work the Unix way.

- **Verify:** open your terminal and run `ls -l /`. You should see a real Unix filesystem
  listing (`bin`, `etc`, `usr`, `var`, ...) with permission strings like `drwxr-xr-x`. If
  you see Windows drive letters (`C:\`) or "command not found", you're not in a Linux shell.
- **Windows (REQUIRED):** install **WSL2** — it runs a full Ubuntu kernel inside Windows,
  so `chmod`, permissions, and the whole filesystem behave exactly like real Linux (Git
  Bash does *not* — its permissions are a no-op, so it would make this topic's
  permission constraints meaningless). **This takes ~20-30 minutes and one reboot. It
  will not break your Windows — WSL2 runs alongside it.**
  1. Open **PowerShell as Administrator**: press the **Windows key**, type `powershell`,
     right-click "Windows PowerShell" → **"Run as administrator"** → click Yes on the
     prompt. (PowerShell is a Windows terminal, different from the Ubuntu terminal you'll
     get in step 4 — you only use PowerShell once, for the install.)
  2. Run: `wsl --install` — this enables the Linux subsystem, installs **Ubuntu**, and
     sets WSL2 as default. (Official guide:
     <https://learn.microsoft.com/en-us/windows/wsl/install>)
  3. **Restart** your machine.
  4. Launch **Ubuntu** from the Start menu; create a Linux username + password when
     prompted. This Ubuntu terminal is where you'll do all three Linux levels.
  5. Verify inside Ubuntu: `ls -l /` should show the Unix filesystem.
- **macOS:** open **Terminal** (Cmd+Space, type "terminal", Enter). macOS is Unix, so it
  works out of the box. (Minor note: a few tools like `sed`/`awk` are BSD-flavored, not
  GNU — for this level it doesn't matter.)
- **Linux:** your default terminal (Ctrl+Alt+T on Ubuntu/Debian). Works out of the box.

### Get this repo onto your machine

Inside your Linux shell (WSL2/Ubuntu on Windows, Terminal on Mac, your terminal on Linux):

```bash
# In any folder you want to keep work in:
git clone <this-repo-url>   # the repo's web URL — see LEARNING_PATH.md if unclear   # replace with the actual URL — see note below
cd intern-onboarding/topics/linux/levels/level-1-basics
```

> **What's `<this-repo-url>`?** It's the web address of this repository. If you got here
> from GitHub, click the green **"<> Code"** button on the repo page and copy the URL
> (looks like `https://github.com/<user>/intern-onboarding.git`). If someone gave you a
> fork or zip, use that URL. If you truly have no URL, ask whoever pointed you here.

If `git` isn't recognized:
- **Windows/WSL2:** inside Ubuntu, run `sudo apt update && sudo apt install -y git`.
- **macOS:** `xcode-select --install` (or it prompts automatically on first use).
- **Linux:** `sudo apt install -y git` (Debian/Ubuntu).

If any check fails and you can't resolve it, follow [SELF_HELP.md](../../../../SELF_HELP.md) before spending an
hour on it — setup issues are quick to unblock together.

## What to build

This level is **not** a program. It's a set of filesystem tasks you complete by running
individual terminal commands. When you're done, a specific directory structure will exist
with specific contents and permissions — and the constraints check that structure.


Build the following inside **this folder** (`topics/linux/levels/level-1-basics/`):

```
workspace/
├── notes.txt              # contains the text exactly: "my first file" (no trailing newline from echo is fine)
├── secrets/
│   └── api-key.txt        # contains any text you like
└── scripts/
    └── hello.sh           # a shell script that prints "hello", and is executable
```

### The tasks (what you'll actually do)

Use terminal commands to:

1. **Create** the `workspace/` directory and the three subdirectories (`secrets/`,
   `scripts/`).
2. **Create** `notes.txt` with the content `my first file`.
3. **Create** `secrets/api-key.txt` with any content.
4. **Make** `secrets/api-key.txt` readable **only by you** (the owner) — group and others
   get no read, no write, no execute. (Permissions string `rw-------` → `600`.) The
   command is `chmod 600 workspace/secrets/api-key.txt`.
5. **Create** `scripts/hello.sh` that prints `hello` when run, and **make it executable**
   so `./workspace/scripts/hello.sh` actually runs. The command to make it executable is
   `chmod +x workspace/scripts/hello.sh`.
6. **Copy** `notes.txt` to `workspace/notes-backup.txt` using a copy command (not retyping
   it).

### First time with the terminal? Here's the pattern

If you've never done these, here's **one example per task type** so you see the syntax.
(These are examples for *different* files — don't copy them blindly, adapt to your task.)

```bash
# Create a directory:
mkdir -p workspace/secrets      # -p creates parent dirs too

# Create a file with specific text content:
echo "my first file" > notes.txt   # > writes the text into the file

# Create an empty file then edit it:
touch workspace/secrets/api-key.txt
nano workspace/secrets/api-key.txt   # nano is a beginner-friendly editor; Ctrl+O save, Ctrl+X exit
                                  # (vim works too if you know it)

# Create a script file:
nano workspace/scripts/hello.sh
#   inside, type:
#     #!/usr/bin/env bash
#     echo "hello"
#   save (Ctrl+O, Enter) and exit (Ctrl+X)

# Make it executable:
chmod +x workspace/scripts/hello.sh

# Set owner-only permissions (600 = owner read/write, nothing else):
chmod 600 workspace/secrets/api-key.txt

# Copy a file:
cp notes.txt notes-backup.txt
```

After each command, run `ls -l` to see what you created and check the permissions column.

## Why this matters

Every developer at a startup uses the terminal daily — to look at files, fix
permissions, write small scripts, copy things around. If navigating the filesystem,
creating files, and setting permissions feel natural, everything else (Git, Docker,
deploying) gets dramatically easier. This level confirms you have that foundation.

## Deliverables

- The `workspace/` directory tree above, created **inside this folder**.
- `workspace/scripts/hello.sh` is executable and prints `hello`.
- `workspace/secrets/api-key.txt` has permissions `600` (owner read/write only).

That's it. No submission file, no README to write — the filesystem state *is* the
deliverable.

## Starter mode: `scratch`

No starter code. You use whatever terminal commands you want (`mkdir`, `touch`, `echo`,
`cat`, `chmod`, `cp`, `nano`/`vim`/an editor). The constraints only check the resulting
filesystem state, not which commands you used.

## How you'll be checked

Open [constraints.md](constraints.md). Each constraint is verified by running a single
inspection command (`ls -l`, `cat`, executing the script) and looking at the output.
Self-report in [RESULTS.md](RESULTS.md). See [../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md).

- All constraints pass → Level 1 cleared (and since it's the topic you picked, the whole
  Linux topic is cleared).
- Any constraint fails → study [../../resources.md](../../resources.md), sections
  "From absolute zero" and "File permissions", fix, re-check.
