# Resources — Python Core

Shared across both Python levels. This is a **progressive** resource list: it starts from
"what is Python?" and goes up through CSV/JSON data processing. **You don't read all of
it.** Find the level you're at, read only what your failed constraints point to.

This list focuses on Python specifically. The master cross-topic list is at
[../../resources.md](../../resources.md).

---

## From absolute zero (what is Python?)

If you've never written a line of Python, start here.

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Python.org — What is Python?](https://www.python.org/about/gettingstarted/) | Reading | C1 — what Python is, why it's popular, how to run it. 2-minute read. |
| [Python Tutorial — Chapter 1: Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html) | Reading | C1 — the official intro: what Python feels like, a quick example. |
| [Automate the Boring Stuff — Chapter 1](https://automatetheboringstuff.com/2e/chapter1/) | Reading | C1 — absolute beginner: installing Python, writing your first program, what an IDE is. |
| [Real Python — Start Here](https://realpython.com/learning-paths/python-basics/) | Reading | C1, C6 — structured beginner-to-intermediate path. Read the first few sections if you're new. |

**The mental model you need first:** Python is a programming language. You write a `.py`
file with instructions, run it with `python3 filename.py`, and it does what you told it.
The standard library (`import os`, `import json`, etc.) gives you hundreds of tools without
installing anything extra.

## Variables, functions, and control flow (Level 1 prerequisites)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Python Tutorial — Chapter 3: Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) | Reading | C6 — `def`, arguments, return values, docstrings. |
| [Python Tutorial — Chapter 4: Data Structures](https://docs.python.org/3/tutorial/datastructures.html) | Reading | C3 — lists, dicts — used throughout Level 1. |
| [Python Tutorial — Chapter 5: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) | Reading | C5, C7 — `try`/`except`, `FileNotFoundError`, handling edge cases. |

## argparse — command-line arguments (Level 1)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Python docs — argparse tutorial](https://docs.python.org/3/howto/argparse.html) | Reading | C1, C2 — how to make a script accept `--directory` and `--dry-run` flags. |
| [Real Python — Command Line Interfaces](https://realpython.com/command-line-interfaces-python-argparse/) | Reading | C1, C2 — deeper argparse walkthrough with examples. |

## Filesystem operations — os and shutil (Level 1)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Python docs — os — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.path.html) | Reading | C3, C4 — `os.path.splitext()`, `os.listdir()`, path manipulation. |
| [Python docs — shutil — High-level file operations](https://docs.python.org/3/library/shutil.html) | Reading | C4 — `shutil.move()` — how to move files between directories. |

## CSV and JSON modules (Level 2)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Python docs — csv — Reading and Writing CSV Files](https://docs.python.org/3/library/csv.html) | Reading | C1, C4, C7 — `csv.DictReader`, reading rows, handling malformed data. |
| [Python docs — json — JSON encoder and decoder](https://docs.python.org/3/library/json.html) | Reading | C2, C3, C5 — `json.dump()`, writing pretty-printed JSON, data structures. |
| [Real Python — Reading and Writing CSV Files](https://realpython.com/read-write-files-python/) | Reading | C1, C4 — practical guide to reading/writing CSV with Python. |

## Error handling — try/except (Level 1, Level 2)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Python Tutorial — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) | Reading | C5, C7 — `try`/`except`/`else`/`finally`. How to handle bad input gracefully. |

---

## How to use these

1. Open the `RESULTS.md` of the level you're working on and find which constraints failed.
2. Read the resource(s) next to those constraints above.
3. Fix your solution.
4. Re-run the checks in the level's `constraints.md`.
5. Update `RESULTS.md` with the new evidence.

Don't read everything top to bottom — target the gap.
