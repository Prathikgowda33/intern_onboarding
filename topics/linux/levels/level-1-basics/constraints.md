# Constraints — Linux Level 1 (Command-Line Basics)

The acceptance checklist. Verify each constraint **manually** by running the inspection
command and looking at the output. Then record Pass/Fail + evidence in
[RESULTS.md](RESULTS.md).

All paths below are **relative to this level's folder** (`topics/linux/levels/level-1-basics/`).

## How to check each constraint

1. Run the **How to verify** command.
2. Decide **Pass** or **Fail** using the explicit **Pass if** / **Fails if** lines.
3. Write down what you observed as evidence in [RESULTS.md](RESULTS.md).

---

## Constraints

- [ ] **C1: Directory structure exists**
  - How to verify: run `ls -R workspace`.
  - Pass if: output shows `workspace/` containing `notes.txt`, `notes-backup.txt`,
    `secrets/`, and `scripts/`, and `secrets/` contains `api-key.txt` and `scripts/`
    contains `hello.sh`.
  - Fails if: any of those files/dirs are missing, or the names are wrong.

- [ ] **C2: notes.txt has the correct content**
  - How to verify: run `cat workspace/notes.txt`.
  - Pass if: output is `my first file` (a single trailing newline is acceptable).
  - Fails if: the content differs (typos, extra text, empty file).

- [ ] **C3: notes-backup.txt is a real copy**
  - How to verify: run `diff workspace/notes.txt workspace/notes-backup.txt`.
  - Pass if: `diff` produces **no output** (the files are identical) and exits 0.
  - Fails if: `diff` shows differences, or `notes-backup.txt` doesn't exist.

- [ ] **C4: api-key.txt is owner-only (permissions 600)**
  - How to verify: run `ls -l workspace/secrets/api-key.txt`.
  - Pass if: the permissions string begins with `-rw-------` (equivalent to `600`) —
    i.e. read+write for the owner, nothing for group or others.
  - Fails if: any `r`/`w` bit is set for group or others (e.g. `-rw-r--r--` / `644`).
  - Note: this constraint only behaves correctly on **real Linux/Unix** (WSL2 on
    Windows, macOS, or native Linux). On Git Bash for Windows, `chmod` is effectively a
    no-op because NTFS doesn't model Unix permissions — so a "pass" there proves nothing.
    That's why this level requires WSL2 on Windows (see the prerequisites). If you're
    somehow running on Git Bash and this "passes" trivially, switch to WSL2.

- [ ] **C5: hello.sh is executable**
  - How to verify: run `ls -l workspace/scripts/hello.sh` and look at the permissions.
  - Pass if: the permissions string has an `x` for the owner (e.g. `-rwx--xr-x` or
    `-rwx------` — the key is owner-execute).
  - Fails if: there is no execute bit for the owner (e.g. `-rw-r--r--` / `644`).

- [ ] **C6: hello.sh runs and prints "hello"**
  - How to verify: run `./workspace/scripts/hello.sh`.
  - Pass if: output is `hello` (a single trailing newline is acceptable) and exit code
    is 0.
  - Fails if: "permission denied", prints something other than `hello`, or errors out.

- [ ] **C7: You can navigate with relative paths**
  - How to verify: run `cd workspace/secrets && pwd && cat api-key.txt`.
  - Pass if: `pwd` shows you're inside `.../workspace/secrets` AND `cat api-key.txt`
    prints the file's content — proving you used a relative path to move and to read.
  - Fails if: either step fails (you couldn't `cd` relatively, or couldn't read the file
    by relative path from inside the dir).

---

## Summary

7 constraints. C1 checks the overall structure. C2/C3 check file content and copying.
C4/C5 check permissions (the central Linux concept at this level). C6 checks the
executable script. C7 confirms you can navigate with relative paths, not just absolute
ones. If any fail, see [../../resources.md](../../resources.md) sections "From absolute
zero" and "File permissions".
