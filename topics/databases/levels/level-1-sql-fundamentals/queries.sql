-- All tasks in project 1
SELECT * FROM tasks WHERE project_id = 1;

-- Pending tasks sorted by highest priority
SELECT title, priority
FROM tasks
WHERE status='pending'
ORDER BY priority DESC;

-- Count tasks per project
SELECT p.name, COUNT(t.id)
FROM projects p
JOIN tasks t ON p.id=t.project_id
GROUP BY p.id;

-- Overdue tasks
SELECT title, due_date, status
FROM tasks
WHERE status='pending'
AND due_date < '2025-01-15';

-- Project with most tasks
SELECT p.name, COUNT(t.id) AS task_count
FROM projects p
JOIN tasks t ON p.id=t.project_id
GROUP BY p.id
ORDER BY task_count DESC
LIMIT 1;
