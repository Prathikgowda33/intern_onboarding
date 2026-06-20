# Prompts — Linux

For the [Linux topic](../topics/linux/). Common situations: permission errors, "command
not found", scripting bugs, text-processing confusion (`grep`/`awk`/`sed`).

---

## Permission denied

**When:** a command fails with `Permission denied` or a script won't run.

```
[CONTEXT] I'm on <Ubuntu/WSL2/macOS>. I'm trying to <run a script / write a file / access
a directory>.
[ACTUAL] I get:
```<paste exact error, including the command you ran>```

[WHAT'S HAPPENING — my understanding]
I ran `<command>`. The shell tried to <what you think it tried — e.g., "execute hello.sh
as a program">. Permissions are checked <when? — e.g., "before the script runs">.

[WHAT'S WRONG — my hypothesis]
I think the problem is <e.g., "the file isn't marked executable, so the shell refuses to
run it">. I'm <confident/unsure> because <e.g., "I recall chmod +x is needed but I'm not
sure if that's the issue here">.

[WHAT I TRIED]
- `ls -l <file>` shows: <paste output>
- I tried `<command>` and got <result>

[ASK] First, confirm or correct my understanding of how permissions work here. Then tell
me the exact fix (the command to run) and explain what each part of it does.
```

---

## Command not found / not on PATH

**When:** `bash: <tool>: command not found` even though you installed it.

```
[CONTEXT] I installed <tool> on <OS>. I'm in <terminal: Git Bash / WSL2 Ubuntu / Terminal.app>.
[ACTUAL] `<command>` returns: `bash: <tool>: command not found`.

[WHAT'S HAPPENING — my understanding]
When I type a command, the shell searches directories listed in `$PATH` for an executable
with that name. If it's not found, I get "command not found."

[WHAT'S WRONG — my hypothesis]
I think <e.g., "the tool installed to a directory not on my PATH, like /usr/local/bin or
~/.local/bin">. I'm <confident/unsure>.

[INFO I GATHERED]
- `echo $PATH` shows: <paste>
- `which <tool>` returns: <nothing / a path>
- `ls <install location>` shows: <paste>
- How I installed it: <apt / brew / download / pip>

[ASK] Confirm my understanding of PATH. Then tell me exactly how to make `<tool>` findable
— do I need to add to PATH, symlink it, or reinstall? Give me the exact commands for my OS.
```

---

## Script doesn't do what I expect (logic bug)

**When:** your bash script runs without errors but the output is wrong.

```
[CONTEXT] I wrote a bash script to <goal — e.g., "count HTTP 404s in an access log">.
[GOAL] I expected <e.g., "a single number: the count of 404 lines">.
[ACTUAL] I got <e.g., "every line of the file printed, no count">.

[WHAT'S HAPPENING — my understanding]
Here's what I think my pipeline does, step by step:
1. <e.g., "cat access.log pipes the file content">
2. <e.g., "grep '404' filters to lines containing 404">
3. <e.g., "wc -l counts them">
If any step is wrong, correct me.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "grep isn't matching because the 404 is in a different column than I
assumed, or my regex is too loose and matches '4004' too">.

[CODE]
```bash
<paste your script or one-liner>```
[SAMPLE INPUT] First 3 lines of my input:
```<paste>```
[ACTUAL OUTPUT]
```<paste>```

[ASK] Walk through my pipeline line by line with the sample input. Show me what each stage
produces. Then pinpoint where my mental model is wrong and give me the corrected command.
Explain the fix, don't just hand it to me.
```

---

## Confused about grep / awk / sed /管道

**When:** you're not sure which text-processing tool to use or how to combine them.

```
[CONTEXT] I have a file that looks like this:
```<paste 5 sample lines>```
[GOAL] I want to extract/transform <exactly what — e.g., "the IP address from lines
containing '404', one per line, deduplicated">.

[WHAT'S HAPPENING — my understanding]
I think I need <grep for X / awk to print column Y / sed to replace Z>, but I'm fuzzy on
which tool does what. My current understanding:
- grep: <what you think it does>
- awk: <what you think it does>
- sed: <what you think it does>

[ASK] First, correct any misunderstanding about what each tool does. Then tell me the
simplest pipeline (using the right tool for each job) to achieve my goal. Explain each
stage of the pipeline and why you chose that tool. Don't over-engineer — I want the
simplest thing that works.
```

---

## Don't understand a man page or flag

**When:** the man page is impenetrable and you don't know what a flag does.

```
[CONTEXT] I'm learning the <tool> command. I ran `man <tool>` but the docs are dense.
[GOAL] I want to understand what `<flag>` (e.g., `-v`, `-r`, `--color`) does.

[WHAT'S HAPPENING — my understanding]
From the man page, I read: "<quote the relevant line>". I interpret this as <your
interpretation>. I'm <confident/confused>.

[ASK] Explain `<flag>` for `<tool>` like I'm new to the terminal. Give me: (1) what it
does in plain English, (2) a tiny example with and without the flag showing the
difference, (3) when I'd actually use it. Don't quote the man page back at me — translate it.
```

---

## Cron job / service not running

**When:** a scheduled task or background service isn't firing.

```
[CONTEXT] I set up <cron job / systemd service / background process> to <do X every Y>.
[ACTUAL] It's <not running at all / running but failing / running but wrong output>.

[WHAT'S HAPPENING — my understanding]
I configured it by <how — e.g., "adding a line to crontab">. I expect it to trigger
<when>. When it runs, it should <do what>.

[WHAT'S WRONG — my hypothesis]
I think the issue might be <e.g., "the cron environment doesn't have my PATH, so the
script's commands aren't found" / "absolute vs relative paths" / "permissions">.

[INFO I GATHERED]
- My config: <paste crontab line / service file>
- Logs: <check `journalctl` / `/var/log/syslog` / wherever — paste what you see>
- Does it work when I run it manually? <yes/no>

[ASK] Confirm or correct my hypothesis. Walk me through how to debug a <cron/systemd>
issue step by step — what logs to check, what env differences to test. Then give me the
fix and explain why it broke.
```

---

## File permissions / ownership confusion (chmod/chown)

**When:** you don't understand why you can't read/write/execute something.

```
[CONTEXT] There's a file/dir at <path>. I want to <read/write/execute> it.
[ACTUAL] I get <Permission denied / operation not permitted / ownership error>.

[WHAT'S HAPPENING — my understanding]
Here's what `ls -l <path>` shows:
```<paste — e.g., "-rw-r--r-- 1 root root ...">```
I read this as: <your interpretation of owner/group/other permissions>. I am logged in as
<user>, in group <group>.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "the file is owned by root and I'm not root, so I can't write to it even
though 'other' has read">. I'm <confident/unsure>.

[ASK] Decode the permission string for me and explain why my action fails. Then tell me
the safest fix (chmod vs chown vs sudo) for my situation — and warn me if there's a
dangerous option I should avoid (like chmod 777).
```

---

## "This works on my Mac but not on Linux" (or vice versa)

**When:** a command behaves differently across systems.

```
[CONTEXT] I have a one-liner that works on <macOS / my Linux box>:
```<paste command>```
[ACTUAL] On <the other OS>, it <errors / gives different output / isn't found>.

[WHAT'S HAPPENING — my understanding]
I think the difference is <e.g., "macOS ships BSD grep/sed, Linux ships GNU versions, and
they have different flags" / "different default shell">.

[ASK] Confirm whether this is a BSD-vs-GNU difference (or whatever). Then give me a
version of the command that works on BOTH, or tell me how to detect which version is
available and adapt. Explain the root cause so I recognize it next time.
```
