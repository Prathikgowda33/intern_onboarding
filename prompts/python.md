# Prompts — Python

For the [Python topic](../topics/python/). Common situations: logic bugs (code runs but
output is wrong), CLI/argparse issues, file I/O, CSV/JSON parsing, scary tracebacks.

---

## Code runs but output is wrong (logic bug)

**When:** no error, but the result isn't what you expected.

```
[CONTEXT] I'm writing a Python script to <goal — e.g., "categorize files by extension
into folders"> for the Python <level> assignment.
[GOAL] For input <X>, I expected output <Y>.
[ACTUAL] I got <Z>.

[WHAT'S HAPPENING — my understanding]
Here's what I think my code does, line by line:
1. <e.g., "parse the --directory arg">
2. <e.g., "walk the directory, for each file get its extension">
3. <e.g., "look up the extension in EXTENSION_MAP to get a category">
4. <e.g., "move the file to <category>/ folder">
If any step is wrong, correct me.

[WHAT'S WRONG — my hypothesis]
I think the bug is in <step> because <e.g., "EXTENSION_MAP uses '.txt' as key but
path.suffix returns '.txt' with the dot, so the lookup should work... but maybe my map
has 'txt' without the dot">.

[CODE]
```python
<paste the function or full script>```
[SAMPLE INPUT / OUTPUT]
Input: <e.g., "a folder with a.txt, b.jpg, c.pdf">
Expected: <a.txt → Documents/, b.jpg → Images/, c.pdf → Documents/>
Actual: <e.g., "all files stay in place, no folders created">

[ASK] Trace my code with the sample input — show me the value of each variable at each
step. Pinpoint where my mental model diverges from reality. Give me the fix and explain
why my version was wrong (don't just correct it).
```

---

## Scary traceback I don't understand

**When:** a wall of red text and you don't know what it means.

```
[CONTEXT] I ran `<command>` and Python crashed.
[ACTUAL] Full traceback:
```<paste the ENTIRE traceback, from "Traceback (most recent call last):" to the end>```

[WHAT'S HAPPENING — my understanding]
I read a traceback <bottom-up / top-down — state which>. The LAST line
("`<ExceptionType>: <message>`") is <your interpretation — e.g., "the type of error and
what Python was trying to do when it failed">. The lines above show <your interpretation —
"the call stack, most recent call last">.

[WHAT'S WRONG — my hypothesis]
The error is `<ExceptionType>` which I think means <e.g., "KeyError means I tried to
access a dict key that doesn't exist">. I think it's failing because <your guess — e.g.,
"the CSV row doesn't have a 'salary' column, or it's empty">.

[CODE] The relevant code (the file/line from the traceback):
```python
<paste the function mentioned in the traceback's last frame>```
[INPUT] What I fed it: <e.g., "this CSV row: ...">

[ASK] First, confirm I'm reading the traceback correctly. Then explain THIS specific error
in plain English — what Python was doing, what value tripped it up. Then show me the fix
and how I could have caught this earlier (a guard, a test, a print statement).
```

---

## argparse / CLI not working

**When:** `--help` is wrong, args aren't parsed, or the script errors on missing args.

```
[CONTEXT] I'm building a CLI tool with argparse for the Python <level> assignment.
[GOAL] I want `python script.py --directory /path --dry-run` to <do X>, and
`python script.py` (no args) to <show help / error>.
[ACTUAL] <What's happening instead — e.g., "no args runs the script with None as directory
and crashes" / "--help doesn't list --dry-run">.

[WHAT'S HAPPENING — my understanding]
I think argparse works by <your mental model — e.g., "you add arguments, it parses
sys.argv, required args error if missing">. I declared <X> as <required/optional>.

[WHAT'S WRONG — my hypothesis]
I think the issue is <e.g., "I didn't set required=True on --directory" / "my add_argument
name has a typo" / "I'm calling parse_args() at the wrong scope">.

[CODE]
```python
<paste your argparse setup + main()>```
[OUTPUT] `python script.py --help` prints:
```<paste>```

[ASK] Confirm my understanding of argparse. Diagnose why my CLI isn't behaving. Show me
the corrected argparse setup and explain each part (required, type, default, help text).
Also: show me the idiomatic way to structure a Python CLI (argparse in main(), if __name__
guard, etc.).
```

---

## File I/O or path issue

**When:** FileNotFoundError, permission errors, or "it works in IDE but not terminal."

```
[CONTEXT] My script tries to <read/write> a file at <path>.
[ACTUAL] I get:
```<paste error>```

[WHAT'S HAPPENING — my understanding]
I think the path resolves to <your interpretation — e.g., "I used 'data/input.csv' as a
relative path, so Python looks relative to the current working directory, which is...">.
My CWD when I run it is <run `pwd` and state it>.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "relative vs absolute path mismatch — my IDE runs from project root but my
terminal runs from the script's folder" / "the file genuinely isn't there">.

[INFO I GATHERED]
- `pwd`: <paste>
- `ls <directory>`: <paste>
- In Python, `import os; print(os.getcwd())`: <paste>
- The path string in my code: `<paste>`

[ASK] Explain how Python resolves relative paths (relative to CWD, not the script file —
confirm this). Diagnose my specific issue. Then show me the robust fix — should I use
`pathlib.Path(__file__).parent`, absolute paths, or pass paths as CLI args? Explain the
tradeoff and the idiomatic approach.
```

---

## CSV / JSON parsing confusion

**When:** data loads but the structure isn't what you expect, or a field is missing.

```
[CONTEXT] I'm reading a <CSV/JSON> file to <goal>.
[ACTUAL] The parsed data <is empty / has wrong shape / missing a field / values are
strings not numbers>.

[WHAT'S HAPPENING — my understanding]
For <CSV/JSON>, I think the parsed result is <a list of dicts / a dict / a list of lists>.
My code:
```python
<paste parsing code>```

[WHAT'S WRONG — my hypothesis]
I think <e.g., "CSV gives me all values as strings, so my `salary > 50000` comparison is
comparing strings and behaving wrong" / "my JSON is a dict at the top level, not a list,
so my `for row in data` iterates keys not rows">.

[SAMPLE INPUT] First few lines of my file:
```<paste>```
[WHAT `type(data)` and `data[:2]` SHOW]
```<paste the actual structure>```

[ASK] Confirm what structure `<csv.DictReader / json.load>` produces. Show me what my data
actually looks like after parsing (print statements to inspect). Pinpoint my
misunderstanding and give me the corrected code — plus how I should debug data-shape
issues like this in the future.
```

---

## Don't understand a Python concept (decorators, generators, comprehensions, etc.)

**When:** you've seen a feature but can't read or write it confidently.

```
[CONTEXT] I'm learning Python. I keep seeing <concept — e.g., "list comprehensions" /
"@decorator" / "yield" / "with statement"> and I don't really get it.
[GOAL] Understand it well enough to read it in others' code and write it myself.

[WHAT'S HAPPENING — my current understanding]
Here's what I think `<concept>` does: <your best guess>. I'm confused specifically about
<e.g., "what gets passed to the decorator" / "when the generator actually executes" /
"the difference between [x for x in y] and (x for x in y)">.

[ASK] Explain `<concept>` like I'm new to Python. Give me: (1) the plain-English "what
problem does this solve," (2) the simplest possible example — show the verbose equivalent
(the loop / the function call) next to the concise version so I see they're the same,
(3) one realistic use case from the kind of scripts I'm writing (CLI tools, file
processing). Avoid jargon. Don't show off — teach.
```

---

## Function returns None / wrong type unexpectedly

**When:** a function "doesn't return anything" or returns the wrong type.

```
[CONTEXT] I have a function `<name>(<args>)` that should return <type/value>.
[ACTUAL] It returns <None / wrong thing>.

[WHAT'S HAPPENING — my understanding]
In Python, a function with no `return` (or `return` with no value) returns `None`. I think
my function <does/doesn't> have a return in the path that's executing. Here it is:
```python
<paste function>```

[WHAT'S WRONG — my hypothesis]
I think <e.g., "my return is inside an if-block, and the condition isn't met, so it falls
through to implicit None" / "I'm mutating a list instead of returning it" / "I assigned
the result but forgot to return">.

[ASK] Trace my function with input <X> — show me which path executes and what gets
returned (or not). Pinpoint the bug. Then teach me the general principle (every code path
must return, mutation vs return, etc.) so I stop making this mistake.
```

---

## Code review before I submit

**When:** your code works but you want it checked for quality.

```
[CONTEXT] I finished the Python <level> assignment. My code works (all constraints pass)
but I want a quality review before I move on.

[WHAT'S HAPPENING — my understanding]
The code does <summary of what it does>. I structured it as <describe: functions, main(),
argparse, etc.>. I think it's <clean / a bit messy> because <reasons>.

[CODE]
```python
<paste full script>```

[ASK] Review this as a senior Python dev would. Be critical — I'd rather hear it now.
Look for: (1) bugs or edge cases I missed, (2) Pythonic-ness (am I using the language
well, or writing Java/C in Python?), (3) readability and naming, (4) error handling,
(5) anything that would embarrass me in a real PR. For each issue, show the problem and
the fix, and explain WHY it matters. Don't rewrite the whole thing — point out the top
3-5 things worth fixing.
```
