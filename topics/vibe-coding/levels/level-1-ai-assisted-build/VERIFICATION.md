# Verification

## Test 1
Input: sample1.md
Output: sample1.html
Result: PASS

## Test 2
Input: sample2.md
Output: sample2.html
Result: PASS

## Help Command
Command:
python3 md2html.py --help

Result:
PASS

## Missing File Test
Command:
python3 md2html.py missing.md -o out.html

Expected:
Shows an error message and exits gracefully.

Result:
PASS
