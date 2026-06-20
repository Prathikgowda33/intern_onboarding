# Constraints — Level 1 (REST API)

The acceptance checklist. Verify each constraint **manually** by running a `curl` command against
your running server and observing the response. Then record Pass/Fail + evidence in
[RESULTS.md](RESULTS.md).

**Important:** Start your Flask app first (`python3 app.py` in this folder), then run these
commands in a **second terminal** from this folder.

## How to check each constraint

1. Start the server: `python3 app.py`
2. Open a second terminal in this folder.
3. Run the **How to verify** step exactly.
4. Decide **Pass** or **Fail** using the explicit **Pass if** / **Fails if** lines.
5. Write down what you observed as evidence in [RESULTS.md](RESULTS.md).

---

## Constraints

- [ ] **C1: POST creates a bookmark**
  - How to verify: run `curl -s -w "\nHTTP_CODE:%{http_code}" -X POST http://localhost:5000/bookmarks -H "Content-Type: application/json" -d '{"title": "Google", "url": "https://google.com", "tags": ["search"]}'`.
  - Pass if: the response body contains `"Google"` and `"https://google.com"`. The HTTP_CODE is 201.
  - Fails if: HTTP_CODE is not 201, or the response body doesn't contain the title and url.

- [ ] **C2: GET all bookmarks returns a list**
  - How to verify: run `curl -s -w "\nHTTP_CODE:%{http_code}" http://localhost:5000/bookmarks`.
  - Pass if: the response is a JSON array (starts with `[`). The array contains at least one
    bookmark (the one created in C1). HTTP_CODE is 200.
  - Fails if: not a JSON array, or empty, or HTTP_CODE is not 200.

- [ ] **C3: GET single bookmark by ID**
  - How to verify: run `curl -s -w "\nHTTP_CODE:%{http_code}" http://localhost:5000/bookmarks/1`.
  - Pass if: the response body is a JSON object with `"id": 1` (or equivalent). Contains the
    title "Google". HTTP_CODE is 200.
  - **Independent check:** the title and url match what you POSTed in C1.
  - Fails if: HTTP_CODE is not 200, or the bookmark doesn't match what was created.

- [ ] **C4: GET nonexistent bookmark returns 404**
  - How to verify: run `curl -s -w "\nHTTP_CODE:%{http_code}" http://localhost:5000/bookmarks/999`.
  - Pass if: HTTP_CODE is 404. The response body contains an error message (not empty).
  - Fails if: HTTP_CODE is not 404 (e.g., 200 with null, or 500).

- [ ] **C5: PUT updates a bookmark**
  - How to verify: first create a second bookmark: `curl -s -X POST http://localhost:5000/bookmarks -H "Content-Type: application/json" -d '{"title": "GitHub", "url": "https://github.com"}'`. Then update it: `curl -s -w "\nHTTP_CODE:%{http_code}" -X PUT http://localhost:5000/bookmarks/2 -H "Content-Type: application/json" -d '{"title": "GitHub Updated", "tags": ["code", "git"]}'`. Then verify: `curl -s http://localhost:5000/bookmarks/2`.
  - Pass if: the PUT response HTTP_CODE is 200. The final GET shows `"title": "GitHub Updated"`
    (or equivalent). The tags include `"code"` and `"git"`.
  - Fails if: PUT returns wrong status code, or the GET still shows the old title.

- [ ] **C6: DELETE removes a bookmark**
  - How to verify: run `curl -s -w "\nHTTP_CODE:%{http_code}" -X DELETE http://localhost:5000/bookmarks/2`. Then verify: `curl -s -w "\nHTTP_CODE:%{http_code}" http://localhost:5000/bookmarks/2`.
  - Pass if: the DELETE returns HTTP_CODE 204 (no body) or 200. The subsequent GET returns 404.
  - Fails if: the bookmark still exists after deletion, or DELETE returns wrong status code.

- [ ] **C7: GET all bookmarks reflects changes**
  - How to verify: run `curl -s http://localhost:5000/bookmarks`.
  - Pass if: the JSON array has length 1 (only the Google bookmark from C1 remains; the GitHub
    one was deleted in C6). The array contains the Google bookmark with id=1.
  - **Independent check:** `curl -s http://localhost:5000/bookmarks | python3 -c "import sys,json; data=json.load(sys.stdin); print(len(data))"` should print `1`.
  - Fails if: the array length is not 1, or the deleted bookmark still appears.

- [ ] **C8: Response bodies are valid JSON**
  - How to verify: run `curl -s http://localhost:5000/bookmarks | python3 -c "import sys,json; json.load(sys.stdin); print('Valid JSON')"` and `curl -s http://localhost:5000/bookmarks/1 | python3 -c "import sys,json; json.load(sys.stdin); print('Valid JSON')"`.
  - Pass if: both commands print `Valid JSON` without error.
  - Fails if: either produces a JSON parse error.

---

## Summary

8 constraints. C1 checks POST (create). C2 checks GET all (list). C3/C4 check GET single
(success and 404). C5 checks PUT (update). C6 checks DELETE. C7 checks state consistency.
C8 checks JSON validity. If any fail, see [../../../resources.md](../../../resources.md)
— especially "REST basics" or "Building with Flask".
