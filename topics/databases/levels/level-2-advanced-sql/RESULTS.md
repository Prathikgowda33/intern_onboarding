# Results — Level 2 (Advanced SQL)

| Constraint | Result | Evidence (command + what you observed) |
|------------|--------|--------------------------------------|
| C1: Two views exist and return data | PASS | sqlite_master showed v_task_summary and v_project_stats; both COUNT queries returned rows |
| C2: v_task_summary filters correctly | PASS | SELECT DISTINCT status returned only pending and in_progress |
| C3: At least 2 indexes exist | PASS | idx_tasks_project_id and idx_tasks_status listed in sqlite_master |
| C4: Indexes are used by queries | PASS | EXPLAIN QUERY PLAN showed USING INDEX idx_tasks_project_id and idx_tasks_status |
| C5: Three-table join correctness | PASS | Join returned project name, task title and tag from all three tables |
| C6: Window function ranks correctly | PASS | ROW_NUMBER ranking restarted at 1 for each project and highest priority task had rank 1 |
| C7: Transaction is atomic | PASS | Failed transaction produced an error and Rollback Test project was not present afterward |

## Overall

- [x] CLEARED — all constraints pass. Databases topic complete.

## Notes (optional)

Completed views, indexes, multi-table joins, window functions and transaction testing.
