# Resources — Linux

Shared across all Linux levels. This is a **progressive** resource list: it starts from
"what is a terminal" and goes up through live-container log analysis. **You don't read
all of it.** Find the level you're working on, read only what your failed constraints
point to.

This list focuses on Linux specifically. The master cross-topic list is at
[../../resources.md](../../resources.md).

---

## From absolute zero (Level 1 prerequisites)

If you've never used a command line, start here.

| Resource | Type | What it gives you |
|----------|------|-------------------|
| [What is the terminal / command line? (Codecademy)](https://www.codecademy.com/article/command-line-setup) | Reading | What the terminal is, why it exists, how to open one on your OS |
| [Linux Tutorial — Basic commands (GeeksforGeeks)](https://www.geeksforgeeks.org/linux-unix/linux-tutorial/) | Reading | `ls`, `cd`, `pwd`, `cat`, `cp`, `mv`, `rm`, `mkdir` — the survival set |
| [Learn the Command Line (Codecademy, free tier)](https://www.codecademy.com/learn/learn-the-command-line) | Interactive | Practice navigating and manipulating files with feedback |
| [Linux 101 Crash Course (YouTube)](https://www.youtube.com/watch?v=w9Zz_myULjc) | Video | Watch someone do real terminal workflows end-to-end |

**The mental model you need before anything else:** the terminal is just a way to do
what you do with a file explorer — go into folders, look at files, move them — by typing
commands instead of clicking. `pwd` = "where am I", `ls` = "what's here", `cd` =
"go there". Get those three comfortable first.

## File permissions (Level 1)

| Resource | Type | What it gives you |
|----------|------|-------------------|
| [Linux File Permissions explained (GeeksforGeeks)](https://www.geeksforgeeks.org/ls-command-in-linux/) | Reading | What `rwx` means, owner/group/others, reading `ls -l` output |
| [chmod tutorial](https://www.geeksforgeeks.org/chmod-command-linux/) | Reading | Changing permissions; why a script needs the executable bit |

## Shell scripting basics (Level 2)

| Resource | Type | What it gives you |
|----------|------|-------------------|
| [Bash scripting for beginners](https://linuxconfig.org/bash-scripting-tutorial-for-beginners) | Reading | First script, the shebang `#!/usr/bin/env bash`, running a `.sh` file |
| [Bash scripting cheatsheet (devhints)](https://devhints.io/bash) | Reading | Positional args `$1 $2`, variables, conditionals — quick lookup |
| [Positional parameters (GNU Bash manual)](https://www.gnu.org/software/bash/manual/html_node/Positional-Parameters.html) | Reading | Reading arguments passed to a script (the `$1`/`$2`/`$@` thing) |

## Text processing: grep, sort, uniq, awk (Level 2)

| Resource | Type | What it gives you |
|----------|------|-------------------|
| [grep basics (GNU manual)](https://www.gnu.org/software/grep/manual/grep.html) | Reading | Searching lines that match a pattern |
| [The `sort \| uniq -c \| sort -rn` pattern](https://stackoverflow.com/questions/6712437/find-and-count-duplicate-lines) | Reading | The classic "count and rank repeated lines" pipeline |
| [AWK tutorial (Grymoire)](https://www.grymoire.com/Unix/Awk.html) | Reading | Extracting fields by column number, e.g. `$1` for the first field |

## Robustness: exit codes, error messages (Level 2)

| Resource | Type | What it gives you |
|----------|------|-------------------|
| [Exit status & `set -e` (GNU Bash manual)](https://www.gnu.org/software/bash/manual/html_node/Exit-Status.html) | Reading | Returning non-zero on failure so callers know something went wrong |
| [Defensive Bash scripting (bash-hackers wiki)](https://wiki.bash-hackers.net/scripting/obsolete) | Reading | Validating inputs, clear error messages instead of raw stack traces |

## Running services in containers (Level 3)

Level 3 uses Docker as a **black-box tool** here — you don't need to understand containers
yet (that's a Month 2 topic). You just need to run the provided command and read the
container's logs. These cover exactly that.

| Resource | Type | What it gives you |
|----------|------|-------------------|
| [Docker — Run a container (basics)](https://docs.docker.com/get-started/) | Reading | `docker run`, what a container is at a glance, enough to use it |
| [docker logs reference](https://docs.docker.com/reference/cli/docker/container/logs/) | Reading | Streaming a container's stdout, `--follow`, `--tail` |
| [Linux Tutorial — I/O redirection & pipes (GeeksforGeeks)](https://www.geeksforgeeks.org/piping-in-unix-or-linux/) | Reading | `|`, `>`, `>>` — feeding one command's output into the next |

---

## How to use these

1. Open the `RESULTS.md` of the level you're working on and find which constraints failed.
2. Use the tables above — each row maps to specific constraints.
3. Fix your solution.
4. Re-run that level's `constraints.md`.
5. Update `RESULTS.md` with the new evidence.

Don't read everything top to bottom — target the gap.
