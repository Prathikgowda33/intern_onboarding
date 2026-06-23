# Results — Level 1 (File Organizer)

## Constraint results

| Constraint | Result | Evidence |
|------------|--------|----------|
| C1 | PASS | python3 organize.py --help showed required --directory and optional --dry-run |
| C2 | PASS | python3 organize.py without arguments produced argparse error requiring --directory |
| C3 | PASS | Category folders images, docs, data, archives, code were created |
| C4 | PASS | Files moved into correct category folders based on extension |
| C5 | PASS | Empty directory handled successfully with no crash |
| C6 | PASS | categorize, create_category_dirs, organize_files and main implemented with real logic |
| C7 | PASS | End-to-end test organized files correctly and left unknown.xyz in root |

## Overall

✅ CLEARED — all constraints pass. Python Level 1 complete.

## Notes

Implemented file organizer using argparse, os and shutil.
