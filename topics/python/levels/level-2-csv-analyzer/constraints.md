# Constraints — Level 2 (CSV Data Analyzer)

The acceptance checklist. Verify each constraint **manually** by running your script
and inspecting the output. Then record Pass/Fail + evidence in [RESULTS.md](RESULTS.md).

All commands below assume your terminal is in this folder
(`topics/python/levels/level-2-csv-analyzer/`).

## How to check each constraint

1. Run the **How to verify** step exactly.
2. Decide **Pass** or **Fail** using the explicit **Pass if** / **Fails if** lines.
3. Write down what you observed as evidence in [RESULTS.md](RESULTS.md).

**Sample data reference (starter/employees.csv):** 20 employees across 5 departments
(Engineering, Marketing, Sales, HR, Finance). Known values for verification are provided
in each constraint.

---

## Constraints

- [ ] **C1: Script runs with CSV argument and produces report.json**
  - How to verify: run `python3 analyze.py starter/employees.csv`, then `ls report.json`.
  - Pass if: the command exits with code 0 and a file `report.json` is created.
  - Fails if: the command crashes with a traceback, or no `report.json` is produced.

- [ ] **C2: report.json is valid JSON**
  - How to verify: run `python3 -c "import json; data=json.load(open('report.json')); print('Valid JSON with', len(data), 'top-level keys')"`.
  - Pass if: the command prints "Valid JSON" with the key count, no error.
  - Fails if: a `json.JSONDecodeError` is raised, or the command crashes.

- [ ] **C3: JSON structure has departments with avg_salary and count, all 5 departments present**
  - How to verify: run `python3 -c "
import json
data = json.load(open('report.json'))
depts = data.get('departments', {})
print('Departments:', sorted(depts.keys()))
for name, info in depts.items():
    print(f'  {name}: avg={info.get(\"avg_salary\")}, count={info.get(\"count\")}')
"`.
  - Pass if: all 5 departments are present (Engineering, Marketing, Sales, HR, Finance),
    and each has `avg_salary` (a number) and `count` (an integer) keys.
  - Fails if: any department is missing, or the structure is wrong.

- [ ] **C4: Total employee count is 20**
  - How to verify: run `python3 -c "import json; print(json.load(open('report.json'))['total_employees'])"`.
    Also verify independently: `wc -l < starter/employees.csv` (should be 21: 20 data + 1 header).
  - Pass if: the JSON shows `total_employees` = 20.
  - Fails if: the count is not 20.

- [ ] **C5: Average salary is correct for all departments**
  - How to verify: run the following independent check and compare to your report:
    ```bash
    python3 -c "
import csv
from collections import defaultdict
with open('starter/employees.csv') as f:
    reader = csv.DictReader(f)
    depts = defaultdict(list)
    for row in reader:
        depts[row['department']].append(int(row['salary']))
for dept, salaries in sorted(depts.items()):
    avg = sum(salaries) / len(salaries)
    print(f'{dept}: avg={avg}, count={len(salaries)}')
"
    ```
  - Pass if: every department's `avg_salary` in `report.json` matches the independent
    check above (exact match, not rounded differently).
  - Fails if: any department's average is wrong.
  - **Expected values:** Engineering=95000.0, Marketing=66000.0, Sales=69500.0, HR=70000.0, Finance=88333.33 (5 departments).

- [ ] **C6: Highest-paid employee is Carol Williams at 112000**
  - How to verify: run `python3 -c "import json; h=json.load(open('report.json'))['highest_paid']; print(h['name'], h['salary'])"`.
    Independent check: `sort -t, -k3 -rn starter/employees.csv | head -2`.
  - Pass if: the JSON shows `name` = "Carol Williams" and `salary` = 112000.
  - Fails if: a different employee is listed, or the salary is wrong.

- [ ] **C7: Handles malformed rows gracefully**
  - How to verify: create a CSV with bad rows and test:
    ```bash
    cat > /tmp/bad-employees.csv << 'CSVEOF'
    name,department,salary,years_at_company
    Good User,Engineering,80000,3
    Bad Row No Salary,Engineering,
    Another Bad,Marketing,not_a_number,2
    Good User 2,Sales,70000,1
    CSVEOF
    python3 analyze.py /tmp/bad-employees.csv
    python3 -c "import json; print(json.load(open('report.json'))['total_employees'])"
    ```
  - Pass if: the script does not crash (exit code 0), produces valid `report.json`, and
    `total_employees` is 2 (only the two good rows were counted). A warning may be printed
    about the malformed rows.
  - Fails if: the script crashes with a traceback, or all 4 rows are counted.

---

## Summary

7 constraints. C1/C2 check the script runs and produces valid JSON. C3/C4 check structure
and counts. C5/C6 check correctness with independent verification. C7 checks error handling.
If any fail, see [../../../resources.md](../../../resources.md).
