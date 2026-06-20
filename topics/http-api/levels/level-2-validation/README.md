# Level 2 — Validation & Error Handling

<!--
  Level metadata:
    slug: http-api/level-2-validation
    skills: input validation, error handling, search/filter, logging, proper status codes
    difficulty: Medium-Hard
    estimated_time: 2-3h
    starter_mode: scratch
-->

## Prerequisites

You need **Python 3**, **Flask**, and **curl**. You should be comfortable building basic REST
endpoints (Level 1 skills). See the [topic README](../../../README.md) for installation.

### Verify

```bash
python3 --version && python3 -c "import flask; print('Flask OK')" && curl --version | head -1
```

## What to build

Extend the Bookmark Manager API from Level 1 with **input validation**, **proper error handling**,
**search/filter functionality**, and **logging**. Build on your Level 1 code or start fresh.

### New requirements

1. **Input validation** on POST and PUT:
   - `title` is required and must be a non-empty string
   - `url` is required and must look like a URL (starts with `http://` or `https://`)
   - `tags` must be a list of strings (if provided)
   - Return 400 with a descriptive JSON error message for validation failures

2. **Search endpoint:**
   - `GET /bookmarks/search?q=<query>` — search bookmarks by title (case-insensitive partial match)
   - `GET /bookmarks?tag=<tag>` — filter bookmarks by tag
   - Both return 200 with a JSON array (empty if no matches)

3. **Error responses** all follow a consistent format:
   ```json
   {"error": "description of what went wrong"}
   ```

4. **Logging:**
   - Log every request to the console (method, path, status code)
   - Log errors (5xx status codes) at ERROR level
   - Log validation failures at WARNING level

### Step-by-step

1. Create `app.py` in this folder (or copy from Level 1 and extend).
2. Add a `validate_bookmark(data)` function that checks required fields and URL format.
3. Use this validator in POST and PUT endpoints. Return 400 with error JSON on failure.
4. Add the search endpoint (`GET /bookmarks/search?q=...`) and filter parameter (`GET /bookmarks?tag=...`).
5. Add Flask logging: configure the app logger to output to console with timestamps.
6. Create 2-3 bookmarks with different tags for testing.
7. Test all scenarios with `curl`.

### How to run

```bash
# Start the server (logging will appear in the server terminal)
python3 app.py

# Test validation:
curl -s -w "\nHTTP_CODE:%{http_code}" -X POST http://localhost:5000/bookmarks -H "Content-Type: application/json" -d '{"title": ""}'
# Should return 400

# Test search:
curl -s "http://localhost:5000/bookmarks/search?q=google"

# Test tag filter:
curl -s "http://localhost:5000/bookmarks?tag=search"
```

## Why this matters

A REST API without validation is a security hole. Missing required fields, malformed URLs, and
wrong data types will crash your app or corrupt your database. Proper error responses help
frontend developers debug issues quickly. Logging is how you diagnose production problems at 3 AM.
These are production skills, not nice-to-haves.

## Deliverables

- `app.py` — Flask app with validation, search, filter, and logging
- All endpoints responding correctly to `curl` commands

## Starter mode: `scratch`

No starter code. Build on your Level 1 code or start fresh from the requirements above.

## How you'll be checked

Open [constraints.md](constraints.md). Each constraint is verified by running a `curl` command
and observing the response. Self-report in [RESULTS.md](RESULTS.md). See
[../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the full workflow.

- All constraints pass → Level 2 cleared (and the whole HTTP-API topic is cleared).
- Any constraint fails → study [../../../resources.md](../../../resources.md), fix, re-check.
