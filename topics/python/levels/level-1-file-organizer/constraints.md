# Constraints — Level 1 (File Organizer CLI)

The acceptance checklist. Verify each constraint **manually** by running your script and
observing the result. Then record Pass/Fail + evidence in [RESULTS.md](RESULTS.md).

All commands below assume your terminal is in the `starter/` folder inside this level.

## How to check each constraint

1. Set up a test directory with files (see specific commands below).
2. Run the **How to verify** step exactly.
3. Decide **Pass** or **Fail** using the explicit **Pass if** / **Fails if** lines.
4. Write down what you observed as evidence in [RESULTS.md](RESULTS.md).

---

## Constraints

- [ ] **C1: Script shows --help with required arguments**
  - How to verify: run `python3 organize.py --help`.
  - Pass if: the output shows `--directory` as a required argument and `--dry-run`
    as an optional flag. No errors.
  - Fails if: the command errors out, or the arguments are missing from the help text.

- [ ] **C2: Fails gracefully without --directory argument**
  - How to verify: run `python3 organize.py` (with no arguments).
  - Pass if: the script exits with a non-zero code and prints a usage/error message
    mentioning that `--directory` is required. No Python traceback.
  - Fails if: a Python traceback is printed, or the script exits silently with code 0.

- [ ] **C3: Creates at least 4 subdirectories by category**
  - How to verify: create a test directory and run the script:
    ```bash
    mkdir -p /tmp/test-organize
    touch /tmp/test-organize/photo.jpg /tmp/test-organize/report.pdf
    touch /tmp/test-organize/data.csv /tmp/test-organize/backup.zip
    python3 organize.py --directory /tmp/test-organize
    ls /tmp/test-organize/
    ```
  - Pass if: at least 4 subdirectories exist (e.g., `images/`, `docs/`, `data/`,
    `archives/`). Files have been moved into the correct ones.
  - Fails if: fewer than 4 subdirectories, or files remain in the root directory.

- [ ] **C4: Moves files into correct subdirectories**
  - How to verify: after running C3's setup, check each target:
    ```bash
    ls /tmp/test-organize/images/photo.jpg
    ls /tmp/test-organize/docs/report.pdf
    ls /tmp/test-organize/data/data.csv
    ls /tmp/test-organize/archives/backup.zip
    ```
  - Pass if: all four files exist in their correct category subdirectories.
  - Fails if: any file is in the wrong subdirectory, or still in the root.

- [ ] **C5: Handles empty directory without crashing**
  - How to verify:
    ```bash
    mkdir -p /tmp/test-empty
    python3 organize.py --directory /tmp/test-empty
    ```
  - Pass if: the script exits with code 0 and no traceback. It may print nothing,
    or a message like "No files to organize."
  - Fails if: a Python traceback or crash occurs.

- [ ] **C6: Uses at least 2 custom functions with real logic**
  - How to verify: open `organize.py` and count the functions (excluding `main` if it
    just calls other functions). Look for functions that do real work (not just `pass`).
  - Pass if: at least 2 functions contain real logic — they have at least one
    non-trivial line of code (not just `pass`, `return None`, or a bare `print`).
  - Fails if: fewer than 2 functions have real logic, or the functions are just stubs.

- [ ] **C7: End-to-end test with 10+ files across multiple categories**
  - How to verify: create a comprehensive test:
    ```bash
    mkdir -p /tmp/test-full
    # Images (3)
    touch /tmp/test-full/a.jpg /tmp/test-full/b.png /tmp/test-full/c.gif
    # Docs (3)
    touch /tmp/test-full/x.pdf /tmp/test-full/y.txt /tmp/test-full/z.md
    # Data (2)
    touch /tmp/test-full/p.csv /tmp/test-full/q.json
    # Archives (2)
    touch /tmp/test-full/r.zip /tmp/test-full/s.tar
    # Unknown extension (1)
    touch /tmp/test-full/unknown.xyz

    python3 organize.py --directory /tmp/test-full

    # Verify counts
    echo "Images:"; ls /tmp/test-full/images/ 2>/dev/null | wc -l
    echo "Docs:"; ls /tmp/test-full/docs/ 2>/dev/null | wc -l
    echo "Data:"; ls /tmp/test-full/data/ 2>/dev/null | wc -l
    echo "Archives:"; ls /tmp/test-full/archives/ 2>/dev/null | wc -l
    echo "Root remaining:"; ls /tmp/test-full/*.* 2>/dev/null | wc -l
    ```
  - Pass if: images=3, docs=3, data=2, archives=2. The unknown.xyz file may be
    in an "other/" folder or skipped (either is acceptable). No traceback.
  - Fails if: any category has the wrong count, or the script crashes.

---

## Summary

7 constraints. C1/C2 check argparse. C3/C4 check organization correctness. C5 checks
edge case handling. C6 checks code structure. C7 is a full end-to-end test. If any
fail, see [../../../resources.md](../../../resources.md).
