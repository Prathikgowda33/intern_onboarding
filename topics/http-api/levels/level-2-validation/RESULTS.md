# Results — Level 2 (Validation & Error Handling)

| Constraint | Result | Evidence (command + what you observed) |
|------------|--------|--------------------------------------|
| C1: Validation rejects missing fields | PASS | POST without url returned HTTP 400 with JSON error |
| C2: Validation rejects invalid URL | PASS | POST with invalid URL returned HTTP 400 with JSON error |
| C3: Valid bookmark creates | PASS | POST with valid bookmark returned HTTP 201 and created bookmark |
| C4: Search works | PASS | GET /bookmarks/search?q=python returned the Python Docs bookmark with HTTP 200 |
| C5: Tag filter works | PASS | GET /bookmarks?tag=python returned the matching bookmark with HTTP 200 |
| C6: Consistent error format | PASS | GET /bookmarks/999 returned HTTP 404 with {"error":"Bookmark not found"} |
| C7: Logging visible | PASS | Server logs showed timestamps, INFO logs, and WARNING logs for validation failures |

## Overall

- [x] **CLEARED** — all constraints pass. HTTP-API topic complete.

## Notes (optional)

Completed all Level 2 validation, search, filtering, error handling, and logging requirements successfully.
