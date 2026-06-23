# Results — Level 2 (CSV Data Analyzer)

## Constraint results

| Constraint | Result | Evidence (command + what you saw) |
|------------|--------|-----------------------------------|
| C1 | PASS | python3 analyze.py starter/employees.csv created report.json |
| C2 | PASS | Valid JSON with 3 top-level keys |
| C3 | PASS | Departments present: Engineering, Marketing, Sales, HR, Finance with avg_salary and count |
| C4 | PASS | total_employees = 20 |
| C5 | PASS | Department averages matched independent calculation |
| C6 | PASS | highest_paid = Carol Williams 112000 |
| C7 | PASS | Malformed rows skipped and total_employees = 2 |

## Overall

✅ CLEARED — all constraints pass. Python Level 2 complete.

## Notes

Implemented CSV analyzer and generated valid report.json output.
