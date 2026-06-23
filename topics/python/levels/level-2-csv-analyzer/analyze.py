#!/usr/bin/env python3

import csv
import json
import sys
from collections import defaultdict

if len(sys.argv) != 2:
    print("Usage: python3 analyze.py <csv_file>")
    sys.exit(1)

csv_file = sys.argv[1]

try:
    departments = defaultdict(list)
    highest_paid = None
    total_employees = 0

    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)

        for row in reader:
            try:
                name = row["name"]
                department = row["department"]
                salary = int(row["salary"])

                departments[department].append(salary)

                if highest_paid is None or salary > highest_paid["salary"]:
                    highest_paid = {
                        "name": name,
                        "salary": salary
                    }

                total_employees += 1

            except Exception:
                print(f"Warning: skipping malformed row: {row}")

    report = {
        "departments": {},
        "highest_paid": highest_paid if highest_paid else {"name": "", "salary": 0},
        "total_employees": total_employees
    }

    for dept, salaries in departments.items():
        report["departments"][dept] = {
            "avg_salary": sum(salaries) / len(salaries),
            "count": len(salaries)
        }

    with open("report.json", "w") as f:
        json.dump(report, f, indent=2)

    print("report.json created")

except FileNotFoundError:
    print(f"Error: file '{csv_file}' not found")
    sys.exit(1)
