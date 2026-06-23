INSERT INTO projects VALUES
(1,'Website Redesign','Company website refresh','2024-01-01'),
(2,'Mobile App','Android app development','2024-02-01'),
(3,'Database Migration','Move data to new system','2024-03-01');

INSERT INTO tasks VALUES
(1,1,'Design homepage','pending',5,'2025-01-10','2024-01-05'),
(2,1,'Update CSS','completed',3,'2025-02-01','2024-01-06'),
(3,1,'Create wireframes','in_progress',4,'2025-02-15','2024-01-07'),
(4,1,'Accessibility audit','pending',2,'2025-03-01','2024-01-08'),

(5,2,'Setup project','completed',3,'2025-02-01','2024-02-05'),
(6,2,'Login screen','pending',5,'2025-02-10','2024-02-06'),
(7,2,'API integration','in_progress',4,'2025-02-20','2024-02-07'),

(8,3,'Backup database','completed',5,'2025-01-25','2024-03-05'),
(9,3,'Migrate users','pending',4,'2025-02-05','2024-03-06'),
(10,3,'Verify migration','pending',3,'2025-02-15','2024-03-07');

INSERT INTO task_tags VALUES
(1,1,'urgent'),
(2,2,'frontend'),
(3,6,'mobile'),
(4,7,'backend'),
(5,9,'database'),
(6,10,'verification');
