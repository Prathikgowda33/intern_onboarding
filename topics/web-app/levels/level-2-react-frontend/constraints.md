# Constraints — Level 2 (React Frontend)

The acceptance checklist. Verify each constraint **manually** by running commands and observing
the result. Then record Pass/Fail + evidence in [RESULTS.md](RESULTS.md).

**Important:** Start both servers first (Flask API and React dev server), then run these
commands.

## How to check each constraint

1. Start Flask API: `cd backend && python3 app.py` (Terminal 1)
2. Start React: `cd frontend && npm run dev` (Terminal 2)
3. Open a third terminal in this folder.
4. Run the **How to verify** step exactly.
5. Decide **Pass** or **Fail** using the explicit **Pass if** / **Fails if** lines.
6. Write down what you observed as evidence in [RESULTS.md](RESULTS.md).

---

## Constraints

- [ ] **C1: Flask API returns entries as JSON**
  - How to verify: first add an entry: `curl -s -X POST http://localhost:5000/api/entries -H "Content-Type: application/json" -d '{"name": "Alice", "message": "Hello from API"}'`. Then run `curl -s http://localhost:5000/api/entries`.
  - Pass if: both commands succeed. The GET response is a JSON array containing at least one
    entry with `"name": "Alice"` and `"message": "Hello from API"`.
  - Fails if: API returns HTML instead of JSON, or any error status code.

- [ ] **C2: React app loads in browser**
  - How to verify: run `curl -s -w "\nHTTP_CODE:%{http_code}" http://localhost:5173/`.
  - Pass if: HTTP_CODE is 200. The response contains HTML with React-related content
    (look for `<div id="root">` or React script tags).
  - Fails if: HTTP_CODE is not 200, or the page doesn't load.

- [ ] **C3: React frontend displays entries from API**
  - How to verify: ensure the Flask API has entries (use C1's POST if needed). Open
    `http://localhost:5173` in a browser, or run `curl -s http://localhost:5173/` and check
    for entry text.
  - Pass if: the React app displays guestbook entries (Alice's message or equivalent).
    The entries are loaded from the Flask API (not hardcoded in React).
  - Fails if: no entries appear, or entries are hardcoded (still show after deleting all
    API entries).

- [ ] **C4: Can add entries from React frontend**
  - How to verify: using the React app's form, add a new entry with name "Bob" and message
    "React test". Then check the API: `curl -s http://localhost:5000/api/entries`.
  - Pass if: the API returns an entry with `"name": "Bob"` and `"message": "React test"`.
    The React app updates to show the new entry without a full page reload.
  - Fails if: the entry doesn't appear in the API, or the page requires a full reload.

- [ ] **C5: CORS is properly configured**
  - How to verify: run `curl -s -I -X OPTIONS http://localhost:5000/api/entries -H "Origin: http://localhost:5173" -H "Access-Control-Request-Method: POST"`.
  - Pass if: the response headers include `Access-Control-Allow-Origin` (allowing
    `http://localhost:5173`). The OPTIONS request returns 200 or 204.
  - Fails if: no CORS headers present, or the OPTIONS request fails.

- [ ] **C6: React app has multiple components**
  - How to verify: run `find frontend/src -name "*.jsx" -o -name "*.tsx" -o -name "*.js"` (excluding `node_modules` and `dist`).
  - Pass if: at least 3 component files exist in `frontend/src/` (e.g., `App.jsx`,
    `Guestbook.jsx`, `EntryForm.jsx`). Each component handles a distinct responsibility.
  - Fails if: all code is in a single file (`App.jsx` only).

- [ ] **C7: Both servers can run simultaneously**
  - How to verify: with Flask on port 5000 and React on port 5173, run `curl -s http://localhost:5000/api/entries` and `curl -s http://localhost:5173/`.
  - Pass if: both return successful responses (HTTP 200). Neither server crashes or shows
    errors when the other is running.
  - Fails if: one server fails when the other starts, or port conflicts.

---

## Summary

7 constraints. C1 checks the API works. C2 checks React loads. C3/C4 check frontend-backend
communication. C5 checks CORS. C6 checks component structure. C7 checks both servers coexist.
If any fail, see [../../../resources.md](../../../resources.md) — especially "React and frontend
frameworks".
