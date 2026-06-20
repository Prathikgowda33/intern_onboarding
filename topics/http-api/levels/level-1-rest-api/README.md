# Level 1 — REST API

<!--
  Level metadata:
    slug: http-api/level-1-rest-api
    skills: REST, HTTP methods (GET/POST/PUT/DELETE), JSON, status codes, Flask routes
    difficulty: Medium
    estimated_time: 2-3h
    starter_mode: scratch
-->

## Prerequisites

You need **Python 3**, **Flask**, and **curl**. See the [topic README](../../../README.md)
for installation instructions.

### Verify

```bash
python3 --version && python3 -c "import flask; print('Flask OK')" && curl --version | head -1
```

All three should succeed without error.

## What to build

Build a **Bookmark Manager REST API** using Flask. The API manages bookmarks (URLs with titles
and optional tags). All data is stored **in memory** (a Python list or dict — no database needed).

### The API endpoints

| Method | Path | Description | Request body | Response |
|--------|------|-------------|--------------|----------|
| GET | `/bookmarks` | List all bookmarks | None | 200 + JSON array |
| GET | `/bookmarks/<id>` | Get one bookmark | None | 200 + JSON object, or 404 |
| POST | `/bookmarks` | Create a bookmark | JSON: `{title, url, tags?}` | 201 + JSON object |
| PUT | `/bookmarks/<id>` | Update a bookmark | JSON: `{title?, url?, tags?}` | 200 + JSON object, or 404 |
| DELETE | `/bookmarks/<id>` | Delete a bookmark | None | 204 (no body), or 404 |

### Data model

Each bookmark has:
- `id` (integer, auto-increment)
- `title` (string, required)
- `url` (string, required)
- `tags` (list of strings, optional, defaults to empty list)
- `created_at` (string, auto-set to creation time)

### Step-by-step

1. Create `app.py` in this folder.
2. Set up Flask app and an in-memory store. If you've never written Flask, here's the
   minimal starting boilerplate (this is a Hello-World, NOT the solution — replace the
   single route with your 5 bookmark endpoints):
   ```python
   from flask import Flask, jsonify, request
   app = Flask(__name__)
   bookmarks = []        # your in-memory store
   next_id = 1           # auto-increment counter

   @app.route("/")
   def index():
       return jsonify({"hello": "world"})

   if __name__ == "__main__":
       app.run(host="0.0.0.0", port=5000)
   ```
   Test this boots: `python3 app.py`, then in another terminal `curl http://localhost:5000/`
   should return `{"hello":"world"}`. Once that works, delete the `/` route and build the
   5 bookmark endpoints.
3. Implement all 5 endpoints with proper HTTP methods and status codes. Use
   `request.json` to read the POST/PUT body, `jsonify(...)` to return JSON, and pass the
   status code as a second return value: `return jsonify(bookmark), 201`.
4. Start the server: `python3 app.py` (it should listen on `http://localhost:5000`).
   **Keep this terminal open** — you'll test from a second terminal.
5. Test each endpoint with `curl` (see constraints.md for exact commands).

### How to run

**You need TWO terminals for this topic** — one to run the server (it must stay running),
one to send `curl` requests. Open a second terminal tab/window in the same folder.

```bash
# Terminal 1 — start the server (leave it running)
python3 app.py

# In another terminal, test with curl:
curl http://localhost:5000/bookmarks
curl -X POST http://localhost:5000/bookmarks -H "Content-Type: application/json" -d '{"title": "Google", "url": "https://google.com"}'
curl http://localhost:5000/bookmarks/1
```

### Error handling

Return proper status codes:
- 200 for successful GET/PUT
- 201 for successful POST (Created)
- 204 for successful DELETE (No Content)
- 404 when a bookmark doesn't exist
- 400 for malformed requests (optional for Level 1, required in Level 2)

## Why this matters

REST APIs are the backbone of web services. Every frontend app, mobile app, and microservice
talks to other services over HTTP. Understanding HTTP methods, status codes, and JSON is a
skill you'll use daily at any startup.

## Deliverables

- `app.py` — a Flask app with 5 working endpoints
- All endpoints responding to `curl` commands as described

## Starter mode: `scratch`

No starter code. Build everything from the assignment above.

## How you'll be checked

Open [constraints.md](constraints.md). Each constraint is verified by running a `curl` command
against your running server and observing the response. Self-report in [RESULTS.md](RESULTS.md).
See [../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the full workflow.

- All constraints pass → Level 1 cleared (and the whole HTTP-API topic is cleared).
- Any constraint fails → study [../../../resources.md](../../../resources.md), fix, re-check.
