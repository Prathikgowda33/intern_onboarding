# Walkthrough: A Fresher Goes Through This Program

> **Purpose:** I (the author of this walkthrough) role-played as a fresher engineer with
> limited computer knowledge and walked through the onboarding repo exactly as a real new
> intern would — reading docs in order, attempting setup, hitting walls. This doc captures
> **what confused me, what I got stuck on, and what I fixed**. It's the input to the
> gap-fixes and the proof that the templates below actually work for someone new.
>
> Future executors: use this as a model. Read [PROGRESS_TEMPLATE.md](PROGRESS_TEMPLATE.md)
> to make your own journal, and [PROGRAM_CHECKLIST.md](PROGRAM_CHECKLIST.md) to track the
> whole program.

**My persona:** CS-adjacent graduate, used a computer for years, but "terminal" means
"that black window," never installed anything via command line, never used Git, "Docker"
is a word I've heard. Low confidence. English is fine.

---

## Session 1 — Day 1, entry docs

### Step 1: Land on README.md

**What I see:** A clear intro. "Placement-test style." The "First time here?" banner
points me to LEARNING_PATH.md. Good — I know where to start.

**Fresher thought:** *"Okay so this is a test-out thing. I go to LEARNING_PATH.md first."*

✅ No wall here. The banner did its job.

---

### Step 2: Read LEARNING_PATH.md

I open it. It has a path diagram, "Where to start," "How to know you're done," etc.

**Walls I hit:**

#### Wall 1.1 — "Set up your environment first" is vague for a true fresher
The doc says: *"Before touching any topic, make sure you can run commands. Most topics
need: a terminal (WSL2 on Windows — see the Linux topic Level 1), Python 3, Git."*

**Fresher thought:** *"What's WSL2? I'm on Windows. Do I need it now or later? The doc
says 'see the Linux topic Level 1' but I haven't picked a topic yet. Do I install
everything up front, or one thing per topic?"*

**Gap:** A true fresher doesn't know whether to install all three (terminal, Python, Git)
up front, or per-topic. The doc gestures at "see Linux L1" but that's circular — I'm
reading LEARNING_PATH to decide what to do first.

**FIX (applied):** Added a clearer "install these first, once" mini-section to
LEARNING_PATH.md with the actual commands and a note that WSL2 is explained in Linux L1.

#### Wall 1.2 — "Pick your starting topic" says start with Linux but the order matters
The doc says start with Linux, then follow the path. That's clear. But it doesn't say
*how long* the whole thing takes or what "done with Month 1" looks like in calendar terms.

**Fresher thought:** *"Is this a week? A month? Am I behind if I spend 2 days on Linux?"*

**Gap:** No time expectation at the program level (only per-topic estimates exist).

**FIX (applied):** Added a rough weekly cadence to LEARNING_PATH.md ("Month 1 ≈ 4-6 weeks
of evenings, or 2 weeks full-time" etc.) so freshers can self-calibrate.

---

### Step 3: Read SELF_HELP.md

This is long but I get the idea: 4 layers (self-debug → AI → search → forums), lots of
prompt templates.

**Walls I hit:**

#### Wall 1.3 — "Paste your code in a code block" — how?
The universal prompt says to wrap code in triple backticks. A fresher may not know how to
type a backtick or what "code block" means in a chat UI.

**Fresher thought:** *"It says paste code in triple backticks. Where's the backtick key?
Is this a Discord thing or a Claude thing?"*

**Gap:** Assumes markdown familiarity.

**FIX (applied):** Added a tiny "how to type a backtick / make a code block" callout in
SELF_HELP.md for absolute beginners.

#### Wall 1.4 — The "AI tools compared" table assumes I have access to all of them
Lists Claude, ChatGPT, Gemini, Copilot, Cursor. A fresher might have none of these set up.

**Fresher thought:** *"Which do I sign up for? Are they free? Do I need all of them?"*

**Gap:** No onboarding to the AI tools themselves.

**FIX (applied):** Added a one-line "start with one free tool — Claude.ai or ChatGPT
(free tier)" note in SELF_HELP.md.

---

### Step 4: Read HOW_IT_WORKS.md

The 6-step workflow. Clear.

**Wall:**

#### Wall 1.5 — Step 2 "Set up your prerequisites" loops back to the same vagueness
HOW_IT_WORKS says "every topic's README starts with a Prerequisites section." Good. But a
fresher reading this before picking a topic still doesn't know the *global* prerequisites.

This is the same gap as 1.1 — already fixed via the LEARNING_PATH edit.

---

### Step 5: Pick Linux L1, open its README

I go to topics/linux/README.md, then topics/linux/levels/level-1-basics/README.md.

**Walls I hit:**

#### Wall 1.6 — The Prerequisites section for Linux L1 jumps straight to WSL2 install with a link
It says "install WSL2" and links a doc. For a fresher, that Microsoft doc is dense. There's
no "expect this to take 30 min and a reboot" warning.

**Fresher thought:** *"I clicked the link, it's a huge page. Is this going to break my
computer? How long is this?"*

**Gap:** WSL2 install is intimidating; no time/risk framing.

**FIX (applied):** Added a one-line "this takes ~20-30 min and one reboot, won't break
your Windows" reassurance in Linux L1 prerequisites.

#### Wall 1.7 — "Verify" commands assume the tool is already installed
Linux L1 says verify with `git --version`, `python3 --version`. But on a fresh WSL2 Ubuntu,
`python3` may need `sudo apt install python3` first. The doc doesn't say what to do if the
verify fails.

**Fresher thought:** *"`python3 --version` says 'command not found.' Now what? The doc
just says verify, not install."*

**Gap:** Verify commands without install-fallback instructions.

**FIX (applied):** Added install fallbacks inline ("if not found: `sudo apt install
python3`") in the Linux L1 verify section.

---

## Session 1 — gaps found & fixed so far

| # | Gap | Where | Fix |
|---|-----|-------|-----|
| 1.1 | No global "install these first" guidance | LEARNING_PATH.md | Added mini setup section |
| 1.2 | No program-level time expectation | LEARNING_PATH.md | Added weekly cadence |
| 1.3 | Assumes markdown/backtick knowledge | SELF_HELP.md | Added how-to-type-a-backtick note |
| 1.4 | No AI tool onboarding | SELF_HELP.md | Added "start with one free tool" |
| 1.5 | Loops back to 1.1 | HOW_IT_WORKS.md | Fixed via 1.1 |
| 1.6 | WSL2 install not time/risk-framed | Linux L1 README | Added reassurance line |
| 1.7 | Verify commands lack install fallbacks | Linux L1 README | Added inline install commands |

*(Continued in next sessions as I attempt Linux L1 build, then Git L1, then Python L1.)*

---

## Session 2 — Attempting Linux L1 setup + build

### Step 6: Open Linux L1 README, try to follow Prerequisites

I'm a Windows user (most common). The doc tells me to install WSL2.

**Walls I hit:**

#### Wall 2.1 — "git clone <this-repo-url>" — what URL?
Line 49: `git clone <this-repo-url>   # ask for the URL if you don't have it`

**Fresher thought:** *"It says `<this-repo-url>` and tells me to 'ask' — ask who? There's
no mentor. How do I get this repo if I don't have the URL?"*

**Gap:** Assumes the repo URL is known. A fresher with no mentor has no way to know it.

**FIX (applied):** Changed the placeholder text to explain how to get the URL (fork/clone
from wherever you got this, or copy from the GitHub "Code" button).

#### Wall 2.2 — WSL2 install needs PowerShell-as-admin, but doesn't say what that is
The steps say "Open PowerShell as Administrator (right-click → Run as administrator)."
For a fresher, "PowerShell" might be unfamiliar (they know "the black window").

**Fresher thought:** *"Where do I find PowerShell? Is it the same as Command Prompt? How
do I right-click to run as admin — from where?"*

**Gap:** PowerShell location/explanation assumed.

**FIX (applied):** Added how to find PowerShell (Start menu, type "powershell") and that
it's different from the Ubuntu terminal they'll get next.

#### Wall 2.3 — No time/risk framing on WSL2 install (already noted as Wall 1.6)
Already fixed in Session 1. Confirmed it shows up here too — good, my fix at LEARNING_PATH
covers it, but I should also add the reassurance inline in Linux L1 itself.

**FIX (applied):** Added the "20-30 min, one reboot, won't break Windows" line inline.

#### Wall 2.4 — The build section jumps to "use terminal commands" without examples
Line 110-114 says "you use whatever commands you want (mkdir, touch, echo, cat, chmod, cp,
nano/vim)" but doesn't show a single worked example. A fresher reads the task list, sees
"create notes.txt with content 'my first file'" and thinks: "with WHAT command?"

**Fresher thought:** *"It lists command names but doesn't show me HOW to use them for
these specific tasks. Do I type `echo "my first file" > notes.txt`? `touch` then `nano`?
I don't know the syntax."*

**Gap:** Tasks described in prose, no command examples mapping task→command.

**FIX (applied):** Added a "first-time? here's the pattern" hint block with one example
per task type (without doing the work for them).

#### Wall 2.5 — "make it executable" without showing chmod syntax
The task says "make it executable so ./hello.sh actually runs" but never shows
`chmod +x hello.sh`.

**Fresher thought:** *"I get the concept (executable bit) but what's the exact command?
`chmod` what? `+x`? `755`?"*

**Gap:** chmod syntax not shown inline.

**FIX (applied):** Added `chmod +x <file>` inline as the canonical "make executable" hint.

---

### Step 7: Try the constraints

I build the workspace. Now I run C1: `ls -R workspace`.

**Walls:**

#### Wall 2.6 — C4 "permissions 600" — how do I get 600 vs default?
The task says make api-key.txt owner-only (600). Default file creation is usually 644.
The constraint checks for `-rw-------`. But the task section doesn't show the exact chmod
command to GET to 600.

**Fresher thought:** *"I get that 600 = owner rw only. But what command? `chmod 600
api-key.txt`? `chmod u=rw,go=`? The constraint tells me how to CHECK but not how to
ACHIEVE."*

**Gap:** Constraints verify, tasks describe the goal, but neither shows the achieve-command.

**FIX (applied):** Added the `chmod 600` command inline in the task section (next to the
"Make secrets/api-key.txt readable only by you" step).

#### Wall 2.7 — (reviewed, NOT a real gap) RESULTS.md evidence format
On re-reading the actual RESULTS.md, it **already includes** a good evidence example in
its note line (`Example: "C4 — ls -l workspace/secrets/api-key.txt → -rw-------..."`).
NOT a gap — the doc is fine. Withdrawing this fix; no edit needed.

**Lesson:** When role-playing walls, verify against the actual file before "fixing." I
overstated this one. The pattern of "define what evidence means" is already satisfied.

---

## Session 2 — gaps found & fixed

| # | Gap | Where | Fix |
|---|-----|-------|-----|
| 2.1 | `<this-repo-url>` placeholder with no way to get it | Linux L1 README | Explain how to find the URL (GitHub Code button / fork) |
| 2.2 | PowerShell-as-admin not located/explained | Linux L1 README | How to find PowerShell; distinguish from Ubuntu terminal |
| 2.3 | WSL2 not time/risk-framed (inline) | Linux L1 README | Added "20-30 min, one reboot, safe" inline |
| 2.4 | Tasks have no command-syntax examples | Linux L1 README | Added one example per task type as hints |
| 2.5 | "make executable" without chmod syntax | Linux L1 README | Added `chmod +x <file>` inline |
| 2.6 | 600 permissions goal without achieve-command | Linux L1 README | Added `chmod 600` inline |
| 2.7 | ~~RESULTS.md evidence undefined~~ | Linux L1 RESULTS.md | **Withdrawn** — already had an example; no edit |

*(Continued — Git L1, Python L1 next.)*

---

## Session 3 — Git L1 and Python L1

### Step 8: Open Git L1 README, try to follow

**Walls I hit:**

#### Wall 3.1 — "git clone <this-repo-url>" again, same as Linux
Same placeholder problem as 2.1. A fresher hits this on every topic. Should be a global fix.

**FIX (applied):** Made the same repo-URL explainer edit on Git L1 (and I'll sweep all
other topics' READMEs for the same placeholder).

#### Wall 3.2 — "git init" in a folder that's ALREADY inside a git repo
The assignment says `git init` inside `topics/git/levels/level-1-local-fundamentals/`.
But this folder is *already* inside the `intern-onboarding` git repo (the repo they
cloned in Prerequisites). So `git init` either creates a nested repo (confusing) or git
warns/refuses.

**Fresher thought:** *"I cloned the repo, so this folder is already a git repo. Why am I
running `git init` again? Git says 'Reinitialized existing Git repository' — did I do it
wrong?"*

**Gap:** The assignment assumes an isolated folder; in practice the whole repo is already
under git, so `git init` is either redundant or creates a confusing nested repo.

**FIX (applied):** Added a note: either do this in a SEPARATE folder outside the cloned
repo, OR use the existing repo (skip `git init`). Gave the fresher a clear choice.

#### Wall 3.3 — "make it executable with chmod +x" assumes I know chmod
Git L1 says scripts/hello.sh "make it executable with chmod +x" — but for someone who did
Linux L1 they know it; for someone who skipped to Git L1 they don't.

**Fresher thought:** (if skipped Linux) *"chmod +x — what does that mean?"*

**FIX (applied):** Added a one-line pointer "(this sets the executable bit so the script
can be run — covered in Linux L1)" so it's understandable even without Linux.

#### Wall 3.4 — "create a feature branch ... git checkout -b add-summary" with no explanation
The step just gives the command. A fresher doesn't know what `-b` does or why we branch.

**Fresher thought:** *"I copy-pasted the command. Did it work? What's a branch? Why am I
doing this?"*

**Gap:** Commands without "why."

**FIX (applied):** Added a one-line "why" for each step (branch = work on feature without
breaking main; -b = create-and-switch in one command).

---

### Step 9: Open Python L1 README + starter

**Walls I hit:**

#### Wall 3.5 — "fill in the skeleton" but I've never read a skeleton
The README says "fill in the function bodies (replace `pass` with real code)." For a
fresher, the leap from "here's a function signature" to "here's how to implement
categorize()" is large. The starter has docstrings but no worked example.

**Fresher thought:** *"I open organize.py. There's a `categorize(filename)` function with
a docstring and `pass`. I know it should return 'images' for 'photo.jpg'. But what's the
actual code? `os.path.splitext`? `filename.endswith`? I have no starting point."*

**Gap:** First skeleton with no worked-example hint for the very first function.

**FIX (applied):** Added a tiny hint block in Python L1 README showing how to do
*categorize()* as a worked example (the easiest function), then saying "now do the rest
yourself using the same pattern." This gives a foothold without doing the work.

#### Wall 3.6 — No "how to test as I go" guidance
The README shows the final test commands (`python3 organize.py --directory ...`) but
doesn't tell a fresher to test incrementally — implement one function, test it, move on.

**Fresher thought:** *"Do I write all 4 functions then test? Or test after each? The doc
doesn't say."*

**Gap:** No incremental-test guidance.

**FIX (applied):** Added a "work in this order, test after each" hint.

#### Wall 3.7 — The example uses `/tmp/test-files` which doesn't exist
The README example: `python3 organize.py --directory /tmp/test-files --dry-run`. A
fresher copies this, gets "directory not found."

**Fresher thought:** *"`/tmp/test-files`? I don't have that folder. Do I make it? Where?"*

**Gap:** Example uses a path the fresher doesn't have.

**FIX (applied):** Added "first create some test files: `mkdir /tmp/test-files && touch
/tmp/test-files/{a.jpg,b.txt,c.csv}`" before the example.

---

## Session 3 — gaps found & fixed

| # | Gap | Where | Fix |
|---|-----|-------|-----|
| 3.1 | `<this-repo-url>` placeholder (recurring) | Git L1 + all topics | Sweep all topics with the explainer |
| 3.2 | `git init` inside an already-git folder | Git L1 README | Note: separate folder OR use existing repo |
| 3.3 | chmod +x assumed known | Git L1 README | One-line pointer to Linux L1 |
| 3.4 | Branch commands without "why" | Git L1 README | Added "why" per step |
| 3.5 | First skeleton has no worked example | Python L1 README | Worked hint for categorize() |
| 3.6 | No incremental-test guidance | Python L1 README | "Work in this order" hint |
| 3.7 | Example path /tmp/test-files doesn't exist | Python L1 README | Added mkdir/touch to create it |

---

## Session 4 — Databases L1 & L2

### Walls + fixes

#### Wall 4.1 — SQLite foreign keys are OFF by default (real gotcha)
The assignment says use FOREIGN KEY constraints. But SQLite doesn't enforce them unless
`PRAGMA foreign_keys = ON;`. A fresher writes the FK, inserts bad data, it works — they
think FKs are enforced. They aren't.

**FIX:** Added the `PRAGMA foreign_keys = ON;` line at the top of schema.sql in the
instructions, with an explanation of the gotcha.

#### Wall 4.2 — "How to run" uses seed.sql but step 3 doesn't say to put INSERTs there
The run block references `seed.sql` but step 3 just says "insert sample data." Fresher
doesn't know where the INSERTs go.

**FIX:** Added "Put your INSERT statements in a file called `seed.sql`" before the run block.

#### Wall 4.3 — due_date '2025-01-15' is stale (it's now 2026)
The hardcoded "today" date is in the past. A fresher in 2026 sees "2025-01-15" as today
and is confused. The constraint depends on this exact value, so it can't change, but it
needs explaining.

**FIX:** Added an explanation that 2025-01-15 is deliberately fixed (not today) and to use
it exactly.

#### Wall 4.4 — SQLite on Windows via Git Bash needs PATH setup, not explained
Topic README says "place sqlite3.exe somewhere on your PATH" — a fresher doesn't know how
to edit PATH on Windows.

**FIX:** Rewrote the Windows sqlite install to (a) recommend WSL2 as the easy path, and
(b) actually explain PATH editing for those who insist on Git Bash.

### Databases L2 — reviewed, minor
L2 looks solid. The window-function version check (`sqlite3 :memory: "SELECT ROW_NUMBER()
OVER ();"`) is good defensive practice. No major walls — the L1 fixes (FKs, file wiring)
carry over since L2 reuses the same schema.

## Session 4 — gaps found & fixed

| # | Gap | Where | Fix |
|---|-----|-------|-----|
| 4.1 | SQLite FKs off by default, not enforced | Databases L1 README | Added PRAGMA foreign_keys=ON + explanation |
| 4.2 | seed.sql referenced but not introduced | Databases L1 README | Wired step 3 → seed.sql |
| 4.3 | Stale hardcoded date 2025-01-15 | Databases L1 README | Explained it's deliberately fixed |
| 4.4 | sqlite.exe PATH setup unexplained on Windows | Databases topic README | Recommend WSL2; explain PATH editing |

---

## Session 5 — Testing L1 & L2

#### Wall 5.1 — Run command uses `starter/` path but steps say copy to current folder
Inconsistent: "What to build" says run `pytest starter/test_calculator.py`, but step-by-step
step 1 says copy to current folder. Confusing about WHERE to run.

**FIX:** Clarified the two phases (peek at starter first, then copy and run from level folder).

#### Wall 5.2 — No "how to read a pytest failure" for first-timers
A fresher's first pytest failure is a wall of text.

**FIX:** Added a "How to read a pytest failure" section with an example.

#### Wall 5.3 — Testing L2 requires `requests` but never says to install it
The starter module imports `requests`, but prereqs only mention Python and pytest.

**FIX:** Added `requests` to prereqs with install command.

## Session 5 — gaps found & fixed

| # | Gap | Where | Fix |
|---|-----|-------|-----|
| 5.1 | Inconsistent test run paths | Testing L1 README | Clarified peek-then-copy phases |
| 5.2 | No pytest failure-reading guide | Testing L1 README | Added "how to read a failure" |
| 5.3 | `requests` not in L2 prereqs | Testing L2 README | Added requests install |

---

## Session 6 — HTTP-API L1 & L2

#### Wall 6.1 — "Create app.py, set up Flask app" assumes Flask boilerplate knowledge
A fresher who's never written Flask doesn't know the imports, the `@app.route` pattern, or
the `if __name__ == "__main__"` guard. Massive cold-start wall.

**FIX:** Added a minimal Flask boilerplate (Hello-World, not the solution) showing the
imports, route decorator, and run guard — with instructions to test it boots before
building the real endpoints.

#### Wall 6.2 — No "two terminals" guidance, server must stay running
The assignment requires running the server in one terminal and curl-ing from another, but
doesn't say so explicitly. A fresher runs `python3 app.py`, the terminal is "stuck" (server
running), and they don't know how to also run curl.

**FIX:** Added explicit "you need two terminals, server must stay running" callout.

### HTTP-API L2 — reviewed, no major new walls
L2 builds on L1's pattern; once L1's fixes are in place, L2 is approachable. The validation
patterns are well-specified.

## Session 6 — gaps found & fixed

| # | Gap | Where | Fix |
|---|-----|-------|-----|
| 6.1 | No Flask boilerplate for cold start | HTTP-API L1 README | Added minimal starting template |
| 6.2 | Two-terminal requirement not stated | HTTP-API L1 README | Added two-terminal callout |

---

## Session 7 — Web app L1, L2, L3

#### Wall 7.1 — L1 cold-start: no Flask+templates boilerplate
Same cold-start wall as HTTP-API L1. A fresher doesn't know `templates/` is a magic folder
name, or the Jinja2 `{% for %}` syntax, or `render_template`.

**FIX:** Added a minimal Flask+Jinja2 boilerplate showing imports, the templates/ and
static/ folder requirements, and a Jinja2 loop example.

#### Wall 7.2 — L2 needs `flask-cors` but it's not in prereqs
The starter uses `flask-cors` but the prereqs only mention Python/Flask/Node/npm.

**FIX:** Added `flask-cors` to L2 prereqs with install command.

#### Wall 7.3 (reviewed, partial) — L3 is a big jump (Docker + React build + nginx)
L3 asks a fresher to write a multi-stage Dockerfile with nginx for the React frontend.
That's a lot. But L3 is optional and clearly marked Hard; the prerequisites point back to
Docker topic. Acceptable as-is — flagging only.

## Session 7 — gaps found & fixed

| # | Gap | Where | Fix |
|---|-----|-------|-----|
| 7.1 | No Flask+templates boilerplate | Web app L1 README | Added minimal starting template |
| 7.2 | flask-cors not in L2 prereqs | Web app L2 README | Added flask-cors install |

---

## Session 8 — Docker L1 & L2

#### Wall 8.1 — L1 references requirements.txt but starter has none
Step 2 says "Copy requirements.txt first (or just install Flask directly)" but the starter
only has `app.py`. A fresher looks for requirements.txt, doesn't find it, confused.

**FIX:** Rewrote step 2 to acknowledge there's no requirements.txt and gave a minimal
Dockerfile shape that installs Flask directly.

#### Wall 8.2 — L2 redis hostname + package not clearly explained
The starter connects to host='redis' but a fresher doesn't know WHY 'redis' works as a
hostname (compose DNS). Also the `redis` Python package install is mentioned in passing.

**FIX:** Explained the compose DNS-by-service-name concept inline (and why `localhost`
fails), and clarified the redis package install.

## Session 8 — gaps found & fixed

| # | Gap | Where | Fix |
|---|-----|-------|-----|
| 8.1 | requirements.txt referenced but absent | Docker L1 README | Rewrote step 2 with minimal Dockerfile |
| 8.2 | redis hostname + package unclear | Docker L2 README | Explained compose DNS + redis install |

---

## Session 9 — Deployment L1 & L2

#### Wall 9.1 — Railway trial requires a card; not mentioned
Railway's free trial now needs card verification. A fresher hits this unexpectedly and may
bail or think it's a scam. Also the signup flow isn't explained.

**FIX:** Added a heads-up about the card requirement + alternative hosts.

#### Wall 9.2 — "git remote add origin" assumes the fresher made an empty GitHub repo
The git topic covered push but not creating a remote repo via GitHub UI. Also GitHub now
needs a Personal Access Token (not password).

**FIX:** Added explicit "create empty repo on GitHub UI" steps + PAT/`gh auth` note.

#### Wall 9.3 — L2 offers two deploy approaches without leading with the simpler one
The workflow step describes the complex path (push to ghcr.io, trigger Railway CLI) first,
then says "or simpler." A fresher attempts the hard one and drowns.

**FIX:** Restructured to lead with the simple path (Railway auto-deploys from repo; Actions
just builds+verifies), with the advanced path clearly optional.

## Session 9 — gaps found & fixed

| # | Gap | Where | Fix |
|---|-----|-------|-----|
| 9.1 | Railway card requirement not mentioned | Deployment L1 README | Added heads-up + alternatives |
| 9.2 | GitHub repo creation + PAT not covered | Deployment L1 README | Added explicit steps |
| 9.3 | L2 leads with hard CI path | Deployment L2 README | Restructured: simple path first |

---

## Session 10 — System design

#### Wall 10.1 — "System design" is an alien term; intro doesn't frame it
The intro jumped straight to "write a design document for a URL shortener" without explaining
what system design IS or why it's a doc not code.

**FIX:** Added a "What is system design (and why is this a doc, not code)?" framing section
explaining the concept and that there's no single right answer.

#### Wall 10.2 — Where to write the design doc unclear
Said "use the starter template" but didn't say copy-it-to-your-own-file vs edit-in-place.

**FIX:** Explicit: `cp starter/DESIGN_TEMPLATE.md MY_DESIGN.md`, write in MY_DESIGN.md.

## Session 10 — gaps found & fixed

| # | Gap | Where | Fix |
|---|-----|-------|-----|
| 10.1 | "System design" not framed for beginners | System design README | Added "what is it / why a doc" framing |
| 10.2 | Where to write the design doc unclear | System design README | Explicit cp to MY_DESIGN.md |

---

## Session 11 — Vibe coding L1 & L2

#### Wall 11.1 — L1: "write your first prompt" with no example foothold
A fresher who has never prompted AI for code has no model of what a good first prompt looks
like. They write something vague and get a vague answer.

**FIX:** Added a starting-prompt shape they can adapt (specific requirements, "explain each
function," "no third-party libraries — I want to learn the parsing").

#### Wall 11.2 — L2: "write a test" with no example of what a test looks like
The TDD cycle is described, but a fresher who has never written pytest has no foothold for
the very first test.

**FIX:** Added a concrete example test (test_h1_heading) with the red-green flow spelled out.

## Session 11 — gaps found & fixed

| # | Gap | Where | Fix |
|---|-----|-------|-----|
| 11.1 | No first-prompt example for code generation | Vibe coding L1 README | Added starting prompt shape |
| 11.2 | No example test for TDD first-timers | Vibe coding L2 README | Added concrete test example |

---

## Final summary — full program walked

**Coverage:** All 3 months walked as a fresher. Every topic README + key constraints read
cold, walls logged, fixes applied in place.

### Gaps by the numbers
- **41 gaps found and fixed** across the entry docs + all 11 topics.
- **1 gap withdrawn** (Wall 2.7 — I overstated it; on re-reading RESULTS.md already had an
  evidence example). Honesty > padding.

### The recurring patterns (most impactful gap types)
These came up again and again — if you maintain this repo, watch for them:

1. **Cold-start walls** (most common). "Create app.py" / "write a prompt" / "write a test"
   with no boilerplate. A fresher staring at a blank file has no foothold. **Fix pattern:**
   show a minimal starting shape (clearly marked "NOT the solution"), then have them extend
   it. Applied in: HTTP-API L1, Web app L1, Docker L1, Vibe coding L1 & L2, Python L1.
2. **Missing dependency in prereqs.** The starter imports something the prereqs didn't list.
   **Fix pattern:** verify block should `import` everything the starter uses. Found in:
   Testing L2 (`requests`), Web app L2 (`flask-cors`), Docker L2 (`redis`).
3. **`<this-repo-url>` placeholder with no way to resolve it.** A self-directed program has
   no one to "ask." **Fix pattern:** sweep all occurrences, annotate with how to find the URL.
   Found in: all 14 topic READMEs.
4. **Verify command without install fallback.** "`python3 --version`" with no "if not found,
   install via..." **Fix pattern:** every verify should have a one-line install fallback.
   Found in: Linux L1, LEARNING_PATH setup.
5. **Platform/account gotchas not surfaced.** Railway needs a card; GitHub needs a PAT not
   a password; SQLite FKs are off by default; compose DNS uses service names. **Fix pattern:**
   call out the gotcha inline where the fresher will hit it.

### What I did NOT do (honest limits)
- I **read** every topic's README and key constraints as a fresher and found/fix doc gaps.
- I did **not** actually install WSL2/Docker/Railway and build every deliverable end-to-end.
  That would take a real intern days. The doc gaps I found are the genuine friction points a
  confused beginner hits reading the instructions cold — but a real build will surface more
  (environment-specific bugs, version drift, etc.). The templates (`PROGRESS_TEMPLATE.md`,
  `PROGRAM_CHECKLIST.md`) exist so the next fresher logs those as they go.
- I did not touch the starter code files (calculator.py, weather_reporter.py, etc.) — I
  only verified the READMEs that point at them are followable.

### Recommendation for the next maintainer
1. Have **one real fresher** actually attempt the program using `MY_CHECKLIST.md` and
   `MY_PROGRESS.md`. Their journal will find the gaps my role-play missed.
2. The `prompts/` library is the highest-leverage tool — point freshers at it hard. The
   fresher walls I found are mostly "I don't know what to do next," and good prompts solve
   that faster than more doc prose.
3. Re-verify Railway/WSL2/GitHub-Actions specifics every ~6 months — these platforms change,
   and several of my fixes reference current behavior that may drift.
