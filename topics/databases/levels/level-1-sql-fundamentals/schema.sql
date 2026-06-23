PRAGMA foreign_keys = ON;

CREATE TABLE projects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    created_at TEXT
);

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    project_id INTEGER,
    title TEXT NOT NULL,
    status TEXT NOT NULL,
    priority INTEGER,
    due_date TEXT,
    created_at TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(id)
);

CREATE TABLE task_tags (
    id INTEGER PRIMARY KEY,
    task_id INTEGER,
    tag TEXT NOT NULL,
    FOREIGN KEY (task_id) REFERENCES tasks(id)
);
