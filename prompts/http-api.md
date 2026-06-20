# Prompts — HTTP & APIs

For the [HTTP-API topic](../topics/http-api/). Common situations: wrong status codes,
validation, routing, curl debugging, request/response shape issues.

---

## Endpoint returns the wrong status code (400/404/500)

**When:** your Flask route returns an error code when you expected 200/201.

```
[CONTEXT] I'm building a Flask bookmark API (HTTP-API <level>). My `<METHOD> /<path>`
endpoint should return <200/201>.
[ACTUAL] It returns <400/404/500>.

[WHAT'S HAPPENING — my understanding]
When I send this request, Flask <your understanding of the flow — e.g., "matches the URL
to a route, calls my view function, my function returns a Response, Flask sends it back">.
A 500 usually means <your interpretation — "my code raised an exception">. A 404 means
<your interpretation>. A 400 means <your interpretation>.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "my function is throwing a KeyError because request.json is None (the
Content-Type header wasn't set), and Flask returns 500" / "I returned a tuple wrong:
`(body, 201)` vs `201, body`" / "the route decorator is missing the right methods=">。

[MY ROUTE]
```python
<paste>```
[THE CURL I TEST WITH]
```<paste exact command>```
[THE FLASK CONSOLE OUTPUT (the traceback or log)]
```<paste>```
[THE HTTP RESPONSE]
```<status code + body>```

[ASK] First, decode the status code for me (what <400/404/500> specifically means in this
context). Then walk through what happens when my curl hits Flask — where does it break?
Pinpoint the bug, show the fix, and explain how I should read Flask's console output to
diagnose this myself next time.
```

---

## request.json is None / not getting the body

**When:** your POST/PUT handler can't read the JSON body the client sent.

```
[CONTEXT] My POST endpoint should read JSON from the request body. But `request.json` is
None (or raises).
[ACTUAL] <None / BadRequest / 415 Unsupported Media Type>.

[WHAT'S HAPPENING — my understanding]
`request.json` parses the body as JSON. It's None when <your understanding — "the body
isn't valid JSON OR the Content-Type header isn't application/json">. My client is sending
<what you think you're sending>.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "my curl is missing -H 'Content-Type: application/json'" / "I'm using
request.form instead of request.json" / "the body is form-encoded, not JSON">.

[MY HANDLER]
```python
<paste>```
[MY CURL]
```<paste>```
[WHAT `request.data` and `request.headers.get('Content-Type')` SHOW]
- request.data: `<paste>`
- Content-Type: `<paste>`

[ASK] Explain how Flask decides to populate request.json vs request.form vs request.data.
Show me what my request actually looks like to Flask. Pinpoint why request.json is None
and give me the fix (on the client side, server side, or both). Teach me the 3 debug
prints I should always check (request.method, request.headers, request.data).
```

---

## Validation isn't catching bad input

**When:** your validation lets through empty/invalid data, or rejects valid data.

```
[CONTEXT] I'm adding input validation to my API. My `validate_<thing>` function should
reject <empty strings / invalid URLs / missing fields>.
[ACTUAL] <Bad input gets through / valid input gets rejected>.

[WHAT'S HAPPENING — my understanding]
My validation: <describe the logic — e.g., "checks if title is truthy, checks if url
starts with http">. I return <400 with an error> when validation fails.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "my URL check is too loose — `url.startswith('http')` passes for
'httpgarbage'" / "I'm checking `if title` but '' is falsy so empty string is caught, but
'   ' (whitespace) isn't" / "I return the error but forget to also return, so execution
continues and creates the bad record">.

[MY VALIDATION CODE]
```python
<paste>```
[TEST CASES — what should pass vs fail]
- Input <X> → should <pass/fail>, my code <passes/fails> ❌
- Input <Y> → should <pass/fail>, my code <passes/fails> ✅

[ASK] Audit my validation for gaps. For each bug, show me the input that slips through and
the fix. Teach me the categories of validation I should always consider (presence, type,
format, length, range, security). Give me a stronger version of my validator and explain
the regex/logic for URL validation specifically.
```

---

## curl isn't doing what I expect

**When:** your curl command sends the wrong thing or you can't tell what it sent.

```
[CONTEXT] I'm testing my API with curl. I want to <send a POST with JSON / see the status
code / send a header>.
[ACTUAL] <The server gets the wrong data / I can't see the status / weird behavior>.

[WHAT'S HAPPENING — my understanding]
My curl command:
```<paste>```
I think this sends <your interpretation — e.g., "a POST with a JSON body and the right
Content-Type">. I'm unsure about <the flags — -X, -d, -H, -w>.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "-d without -H sends form-encoded, not JSON" / "I need -w '%{http_code}' to
see the status" / "single quotes vs double quotes in the JSON are messing up shell
escaping">.

[ASK] Decode my curl command flag by flag — what does each part actually send to the
server? Show me the corrected command for my goal (<post JSON + see status + see headers>).
Give me a "curl cheat sheet" for the 5 things I'll do most: GET, POST JSON, see status
code, see response headers, send an auth header.
```

---

## CORS error in the browser

**When:** your frontend can't call your API because of CORS.

```
[CONTEXT] My React app (port 5173) fetches from my Flask API (port 5000). The browser
blocks it.
[ACTUAL] Browser console shows:
```<paste the exact CORS error — usually "blocked by CORS policy: No 'Access-Control-
Allow-Origin' header">```

[WHAT'S HAPPENING — my understanding]
CORS (Cross-Origin Resource Sharing) is <your interpretation — "a browser security
mechanism where the server must explicitly allow requests from other origins via response
headers">. "Origin" means <scheme + host + port>. My frontend origin is
<http://localhost:5173>, my API is <http://localhost:5000> — these are <same/different
origins> because <ports differ>.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "I haven't configured flask-cors" / "I configured it but only for GET, and
my POST triggers a preflight OPTIONS that's failing" / "CORS(app, origins='*') should work
but maybe I'm missing something">.

[MY FLASK CORS SETUP]
```python
<paste — including how you initialized flask-cors>```
[EXACT FETCH IN REACT]
```js
<paste>```

[ASK] First, confirm my CORS mental model (especially why ports matter and what a
"preflight" OPTIONS request is). Then diagnose my specific error. Show me the correct
flask-cors setup and explain what headers the browser needs. Teach me how to debug CORS
in the browser Network tab (look for the OPTIONS request, check response headers).
```

---

## Don't understand a REST concept (methods, status codes, idempotency)

**When:** you're fuzzy on HTTP fundamentals.

```
[CONTEXT] I'm learning REST. I keep getting confused about <GET vs POST / when to use PUT
vs PATCH / what status code to return / what "idempotent" means>.
[GOAL] A clear mental model I can apply.

[WHAT'S HAPPENING — my current understanding]
Here's what I think:
- GET: <your interpretation>
- POST: <your interpretation>
- PUT vs PATCH: <your interpretation — or "no idea">
- "Idempotent" means <your best guess>
- 200 vs 201 vs 204: <your interpretation>

[ASK] Correct me where I'm wrong. Give me a clean reference for HTTP methods (what each
is FOR, not just "GET reads, POST writes" — explain the semantics), the status code
families (2xx/3xx/4xx/5xx) with the ones I'll actually use, and idempotency with a
concrete example (why GET and PUT are idempotent but POST isn't). Tie it to my bookmark
API: for each endpoint, which method and status should I use and why?
```

---

## Route / URL pattern not matching

**When:** your `@app.route` isn't catching the request, or the URL param is wrong.

```
[CONTEXT] I have a route `@app.route('/bookmarks/<int:id>')` (or similar). Requests to it
<404 / get the wrong id / hit the wrong route>.
[ACTUAL] <404 / ValueError / id is None / matched the wrong handler>.

[WHAT'S HAPPENING — my understanding]
Flask routing works by <your interpretation — "matching the URL path against route
patterns, <id> captures a path segment, <int:id> converts it to int">. I think my pattern
should match <URL>.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "I used <id> (string) but my URL has /bookmarks/123 and it should work...
or maybe the issue is trailing slash" / "two routes conflict and the wrong one wins" /
"the converter type is wrong — <int:id> won't match 'abc'">.

[MY ROUTES]
```python
<paste all relevant @app.route decorators + functions>```
[THE URL I REQUEST]
```<e.g., "GET /bookmarks/5">```
[WHAT HAPPENS]
```<404 / matched the list route / ValueError>```

[ASK] Explain Flask URL routing and converters (<int:>, <string:>, <path:>, trailing
slash behavior). Diagnose why my URL doesn't match (or matches wrong). Show the fix. Teach
me how to debug routing (list all rules with `app.url_map`).
```

---

## Review my API design before I submit

**When:** your API works but you want the design reviewed.

```
[CONTEXT] I finished the HTTP-API <level> assignment. Endpoints work and return right
status codes. I want a design review.

[WHAT'S HAPPENING — my understanding]
My API has these endpoints: <list METHOD + path + purpose>. I return <status codes>. I
handle errors by <approach>. I think the design is <RESTful / a bit inconsistent> because
<reasons>.

[MY APP]
```python
<paste app.py>```

[ASK] Review my API as a senior backend dev. Look for: (1) REST correctness (right methods,
right status codes, right URL patterns — plural nouns, nested vs flat), (2) error handling
consistency (do all errors follow the same JSON shape?), (3) missing endpoints or edge
cases (what about DELETE of nonexistent resource? bulk operations?), (4) security basics
(no SQL injection, input validation). Top 3-5 issues with fixes. Don't rewrite — point out
what matters.
```
