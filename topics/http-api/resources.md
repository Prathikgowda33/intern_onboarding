# Resources — HTTP & APIs

Shared across both HTTP-API levels. This is a **progressive** resource list: it starts from
"what is HTTP?" and goes up through validation and logging. **You don't read all of it.** Find
the level you're working on, read only what your failed constraints point to.

This list focuses on HTTP and REST APIs specifically. The master cross-topic list is at
[../../resources.md](../../resources.md).

---

## From absolute zero (what is HTTP?)

If you've never heard of HTTP status codes or REST, start here.

| Resource | Type | Why it's here |
|----------|------|---------------|
| [MDN — What is HTTP?](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview) | Reading | C1 — what HTTP is, how clients and servers communicate, the request/response cycle. |
| [MDN — HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) | Reading | C1, C2 — GET, POST, PUT, DELETE — what each does and when to use it. |
| [MDN — HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) | Reading | C1, C2 — 200, 201, 400, 404, 500 — what each means and when to return it. |

**The mental model you need first:** HTTP is a protocol where a **client** (like `curl` or a browser)
sends a **request** to a **server** (your Flask app), and the server sends back a **response**.
The request has a **method** (GET, POST, PUT, DELETE) and a **path** (`/bookmarks`). The response
has a **status code** (200 = OK, 201 = Created, 400 = Bad Request, 404 = Not Found, 500 = Server Error)
and a **body** (usually JSON).

## REST basics (Level 1)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [RESTful API Design — Best Practices](https://restfulapi.net/) | Reading | C1, C2 — what REST is, resource naming, URL patterns, idempotent methods. |
| [Flask Quickstart](https://flask.palletsprojects.com/en/latest/quickstart/) | Reading | C1 — how to create a Flask app, define routes, handle requests. |
| [Flask — Request Object](https://flask.palletsprojects.com/en/latest/api/#flask.request) | Reference | C1, C2 — how to access request data: `request.json`, `request.args`, `request.method`. |
| [JSON Introduction](https://www.json.org/json-en.html) | Reading | C1, C2 — what JSON is, the syntax, why APIs use it. |

## Building with Flask (Level 1)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Flask — Variable Rules in Routes](https://flask.palletsprojects.com/en/latest/quickstart/#variable-rules) | Reading | C1 — `@app.route('/bookmarks/<int:id>')` — URL parameters. |
| [Flask — Responses](https://flask.palletsprojects.com/en/latest/quickstart/#about-responses) | Reading | C1, C2 — how to return JSON: `jsonify()`, custom status codes. |
| [Real Python — Flask REST API Tutorial](https://realpython.com/flask-rest-api-part-1/) | Reading | C1, C2, C3 — builds a complete REST API with Flask. Follow Parts 1-2. |

## Validation and error handling (Level 2)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Flask — Error Handling](https://flask.palletsprojects.com/en/latest/errorhandling/) | Reading | C1 — how to return custom error responses with proper status codes. |
| [Real Python — Flask REST API Part 2](https://realpython.com/flask-rest-api-part-2/) | Reading | C2, C3 — input validation, error responses, and proper API patterns. |
| [Python Logging HOWTO](https://docs.python.org/3/howto/logging.html) | Reading | C4 — how to use Python's `logging` module in a Flask app. |

---

## How to use these

1. Open the `RESULTS.md` of the level you're working on and find which constraints failed.
2. Read the resource(s) next to those constraints above.
3. Fix your solution.
4. Re-run the checks in the level's `constraints.md`.
5. Update `RESULTS.md` with the new evidence.

Don't read everything top to bottom — target the gap.
