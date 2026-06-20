# Level 1 — File Organizer CLI

<!--
  Level metadata:
    slug: python/level-1-file-organizer
    skills: Python basics, argparse, os, shutil, file I/O, error handling
    difficulty: Easy–Medium
    estimated_time: 2-3h
    starter_mode: skeleton
-->

## Prerequisites

Same as the topic-level prerequisites: **Python 3** and a **terminal**. See the topic
[README.md](../../../README.md) for install steps.

- **Verify:** `python3 --version` prints `Python 3.x.x`.

## What to build

Build a **file organizer CLI tool** called `organize.py`. Given a directory, it sorts
files into subdirectories based on their file extension.

### Behavior

- Takes a required `--directory` argument (the folder to organize).
- Takes an optional `--dry-run` flag (prints what it *would* do, without moving files).
- Creates subdirectories based on file extension categories:
  - **images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`, `.webp`
  - **docs**: `.pdf`, `.doc`, `.docx`, `.txt`, `.md`, `.rtf`
  - **data**: `.csv`, `.json`, `.xml`, `.xlsx`, `.xls`
  - **archives**: `.zip`, `.tar`, `.gz`, `.rar`, `.7z`
  - **code**: `.py`, `.js`, `.html`, `.css`, `.java`
- Moves each file into the correct subdirectory.
- Skips directories (only moves files).
- Handles edge cases: empty directory, files with unknown extensions (skip or move to
  an "other/" folder), files that already exist in the target directory.

### Example

```bash
# Dry run first (see what would happen)
python3 organize.py --directory /tmp/test-files --dry-run

# Actually organize
python3 organize.py --directory /tmp/test-files
```

## First time filling in a skeleton? Here's a foothold

The starter has 4 functions to implement (`categorize`, `create_category_dirs`,
`organize_files`, `main`) plus `parse_args` (already done). If you've never done this,
work in this order and **test after each function** rather than writing all 4 then testing:

1. **`categorize(filename)`** (easiest — start here). It takes a filename like
   `"photo.jpg"` and returns the category `"images"`. The trick: get the file extension
   and look it up in `EXTENSION_MAP`. Worked example for the first function:
   ```python
   import os
   def categorize(filename):
       _, ext = os.path.splitext(filename)   # ("photo", ".jpg") — note the dot
       return EXTENSION_MAP.get(ext.lower())  # returns "images", or None if unknown
   ```
   Test it in your terminal before moving on:
   ```bash
   python3 -c "from organize import categorize; print(categorize('photo.jpg'))"
   # should print: images
   ```
2. **`create_category_dirs(base_dir, categories)`** — for each category in the set, make
   `base_dir/<category>/` if it doesn't exist. Look up `os.makedirs(..., exist_ok=True)`.
3. **`organize_files(directory, dry_run=False)`** — the main logic: list files, categorize
   each, create dirs, move files (look up `shutil.move`). Use the `dry_run` flag to print
   instead of moving.
4. **`main()`** — parse args, call `organize_files(args.directory, args.dry_run)`.

**Make some test files first** (the example below uses `/tmp/test-files`, which doesn't
exist until you create it):

```bash
mkdir -p /tmp/test-files
touch /tmp/test-files/{photo.jpg,notes.txt,data.csv,script.py}
```

Now the example commands will work:

```bash
# Dry run first (see what would happen)
python3 organize.py --directory /tmp/test-files --dry-run

# Actually organize
python3 organize.py --directory /tmp/test-files
```

## Why this matters

File organization, CLI argument handling, and filesystem operations are core Python skills.
Every backend engineer writes scripts that move files, parse arguments, and handle edge cases.
This level also teaches you to read and fill in a skeleton — a common onboarding task.

## Deliverables

- A working `organize.py` in the `starter/` folder (fill in the skeleton).
- The script passes all constraints in [constraints.md](constraints.md).

## Starter mode: `skeleton`

The `starter/organize.py` file has the structure already set up — function signatures,
argparse configuration, and the extension map. Your job is to implement the function
bodies (replace `pass` with real code). Do not rename the functions or change the
signatures unless a constraint explicitly allows it.

## How you'll be checked

Open [constraints.md](constraints.md). Each constraint is verified by running a command
and observing the output. Self-report in [RESULTS.md](RESULTS.md). See
[../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the workflow.

- All constraints pass → Level 1 cleared (and the whole Python topic is cleared).
- Any constraint fails → study [../../../resources.md](../../../resources.md), fix, re-check.
