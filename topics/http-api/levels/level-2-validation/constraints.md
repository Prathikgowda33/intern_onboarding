# Constraints — Level 2 (Validation & Error Handling)

The acceptance checklist. Verify each constraint **manually** by running a `curl` command against
your running server and observing the response. Then record Pass/Fail + evidence in
[RESULTS.md](RESULTS.md).

**Important:** Start your Flask app first (`python3 app.py` in this folder), then run these
commands in a **second terminal** from this folder. Create some test bookmarks first if needed.

## How to check each constraint

1. Start the server: `python3 app.py`
2. Open a second terminal in this folder.
3. Run the **How to verify** step exactly.
4. Decide **Pass** or **Fail** using the explicit **Pass if** / **Fails if** lines.
5. Write down what you observed as evidence in [RESULTS.md](RESULTS.md).

---

## Constraints

- [ ] **C1: Validation rejects missing required fields**
  - How to verify: run `curl -s -w "\nHTTP_CODE:%{http_code}" -X POST http://localhost:5000/bookmarks -H "Content-Type: application/json" -d '{"title": "Only title"}'`.
  - Pass if: HTTP_CODE is 400. The response body is JSON containing `"error"` key with a
    message about the missing `url` field.
  - Fails if: HTTP_CODE is 201 (accepted without url), or not a JSON error response.

- [ ] **C2: Validation rejects invalid URL format**
  - How to verify: run `curl -s -w "\nHTTP_CODE:%{http_code}" -X POST http://localhost:5000/bookmarks -H "Content-Type: application/json" -d '{"title": "Test", "url": "not-a-url"}'`.
  - Pass if: HTTP_CODE is 400. The response body contains an error message about URL format.
  - Fails if: HTTP_CODE is 201 (accepted invalid URL).

- [ ] **C3: Valid bookmark still creates successfully**
  - How to verify: run `curl -s -w "\nHTTP_CODE:%{http_code}" -X POST http://localhost:5000/bookmarks -H "Content-Type: application/json" -d '{"title": "Python Docs", "url": "https://docs.python.org", "tags": ["docs", "python"]}'`.
  - Pass if: HTTP_CODE is 201. The response body contains the title "Python Docs" and url
    "https://docs.python.org".
  - Fails if: HTTP_CODE is not 201, or the bookmark wasn't created.

- [ ] **C4: Search endpoint works**
  - How to verify: first ensure bookmarks exist, then run `curl -s -w "\nHTTP_CODE:%{http_code}" "http://localhost:5000/bookmarks/search?q=python"`.
  - Pass if: HTTP_CODE is 200. The response is a JSON array containing the Python Docs bookmark.
    The search is case-insensitive (matches "Python" with "python").
  - Fails if: no results, or wrong HTTP status code.

- [ ] **C5: Tag filter works**
  - How to verify: run `curl -s -w "\nHTTP_CODE:%{http_code}" "http://localhost:5000/bookmarks?tag=python"`.
  - Pass if: HTTP_CODE is 200. The response is a JSON array containing only bookmarks with
    the tag "python". Bookmarks without this tag are excluded.
  - Fails if: wrong bookmarks returned, or wrong HTTP status code.

- [ ] **C6: Error responses follow consistent format**
  - How to verify: run `curl -s -X POST http://localhost:5000/bookmarks -H "Content-Type: application/json" -d '{}'` and `curl -s http://localhost:5000/bookmarks/999`.
  - Pass if: both responses are JSON with an `"error"` key. The error message describes what
    went wrong. Both have appropriate status codes (400 and 404).
  - Fails if: error responses are plain text, or missing the "error" key, or wrong status codes.

- [ ] **C7: Logging visible in server output**
  - How to verify: make a few requests (a POST, a GET, and a deliberate 400 request). Look at
    the server terminal where `python3 app.py` is running.
  - Pass if: each request appears in the server log with at least the method, path, and
    status code. Validation failures appear with WARNING or higher severity. The log includes
    readable timestamps.
  - Fails if: no log output, or only Flask's default output without timestamps.

---

## Summary

7 constraints. C1/C2 check input validation rejects bad data. C3 checks valid data still works.
C4/C5 check search and filter. C6 checks consistent error format. C7 checks logging. If any
fail, see [../../../resources.md](../../../resources.md) — especially "Validation and error handling".
