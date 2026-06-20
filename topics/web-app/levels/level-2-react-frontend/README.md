# Level 2 — React Frontend

<!--
  Level metadata:
    slug: web-app/level-2-react-frontend
    skills: React, Vite, fetch API, CORS, frontend-backend separation
    difficulty: Medium-Hard
    estimated_time: 3-4h
    starter_mode: scratch
-->

## Prerequisites

You need **Python 3**, **Flask**, **Node.js**, and **npm**. You should be comfortable with
Flask basics (Level 1 skills) and understand HTTP. See the [topic README](../../../README.md)
for installation.

### Verify

```bash
python3 --version && node --version && npm --version
```

You'll also need `flask-cors` for the backend: `python3 -m pip install flask-cors`.

## What to build

Replace the static HTML from Level 1 with a **React frontend** that communicates with the
same Flask guestbook API. You'll build two separate processes: a Flask API backend and a React
frontend, connected by HTTP.

### Architecture

- **Flask API** (`backend/`): serves JSON endpoints only (no HTML templates):
  - `GET /api/entries` — returns all entries as JSON
  - `POST /api/entries` — accepts `{"name": "...", "message": "..."}` as JSON
- **React app** (`frontend/`): built with Vite, displays entries and has a form to add new ones

### Step-by-step

1. Create a `backend/` folder with `app.py` (Flask API with the two endpoints above).
2. Enable CORS on the Flask app (`flask-cors`).
3. Create the React app: `npm create vite@latest frontend -- --template react` (from this level's folder).
4. `cd frontend && npm install && npm run dev` — React dev server on `http://localhost:5173`.
5. Build components:
   - `App` — main layout
   - `Guestbook` — fetches and displays entries
   - `EntryForm` — form with name and message inputs
6. Use `fetch()` to call the Flask API from React.
7. Run both servers: Flask on port 5000, React on port 5173.

### How to run

```bash
# Terminal 1: Start Flask API
cd backend && python3 app.py

# Terminal 2: Start React dev server
cd frontend && npm install && npm run dev

# Open http://localhost:5173 in your browser
```

## Why this matters

Modern web apps separate frontend and backend. The frontend (React) runs in the browser, the
backend (Flask) serves JSON APIs. CORS is the security mechanism that allows them to talk
to each other. This architecture is the standard at every startup.

## Deliverables

- `backend/app.py` — Flask API with CORS, serving JSON
- `frontend/` — Vite + React app with components and fetch calls
- Both servers running and communicating

## Starter mode: `scratch`

No starter code. Build both the Flask API and React frontend from scratch.

## How you'll be checked

Open [constraints.md](constraints.md). Each constraint is verified by running commands and
observing output. Self-report in [RESULTS.md](RESULTS.md). See
[../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the full workflow.

- All constraints pass → Level 2 cleared (and the whole Web App topic is cleared).
- Any constraint fails → study [../../../resources.md](../../../resources.md), fix, re-check.
