-- View 1
CREATE VIEW IF NOT EXISTS v_task_summary AS
SELECT p.name AS project_name,
       t.title,
       t.status,
       t.priority
FROM projects p
JOIN tasks t ON p.id = t.project_id
WHERE t.status IN ('pending','in_progress');

-- View 2
CREATE VIEW IF NOT EXISTS v_project_stats AS
SELECT p.name,
       COUNT(t.id) AS total_tasks,
       SUM(CASE WHEN t.status='completed' THEN 1 ELSE 0 END) AS completed_tasks,
       ROUND(
           100.0 * SUM(CASE WHEN t.status='completed' THEN 1 ELSE 0 END)
           / COUNT(t.id),2
       ) AS completion_percentage
FROM projects p
LEFT JOIN tasks t ON p.id=t.project_id
GROUP BY p.id;

-- Indexes
CREATE INDEX IF NOT EXISTS idx_tasks_project_id ON tasks(project_id);
CREATE INDEX IF NOT EXISTS idx_tasks_status ON tasks(status);

-- Three-table join
SELECT p.name AS project_name,
       t.title,
       tt.tag
FROM projects p
JOIN tasks t ON p.id=t.project_id
JOIN task_tags tt ON t.id=tt.task_id;

-- Window function
SELECT p.name,
       t.title,
       t.priority,
       ROW_NUMBER() OVER(
           PARTITION BY p.id
           ORDER BY t.priority DESC
       ) AS rank_num
FROM projects p
JOIN tasks t ON p.id=t.project_id;

-- Successful transaction
BEGIN;
INSERT INTO projects(name) VALUES('Transaction Success');
INSERT INTO tasks(project_id,title,status,priority)
VALUES((SELECT id FROM projects WHERE name='Transaction Success'),
'Task A','pending',1);
INSERT INTO tasks(project_id,title,status,priority)
VALUES((SELECT id FROM projects WHERE name='Transaction Success'),
'Task B','pending',2);
COMMIT;
