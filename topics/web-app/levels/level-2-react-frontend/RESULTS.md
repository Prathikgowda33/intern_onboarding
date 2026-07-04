# Results — Level 2 (React Frontend)

| Constraint | Result | Evidence (command + what you observed) |
|------------|--------|--------------------------------------|
| C1: API returns JSON | PASS | POST created Alice entry and GET /api/entries returned JSON containing Alice and Hello from API |
| C2: React app loads | PASS | React app loaded successfully on localhost:5173 |
| C3: React displays API entries | PASS | React displayed Alice entry fetched from the Flask API |
| C4: Can add entries from React | PASS | Added Bob with React test from the form; React updated immediately and Flask API contained Bob |
| C5: CORS configured | PASS | OPTIONS request returned HTTP 200 with Access-Control-Allow-Origin for localhost:5173 |
| C6: Multiple components | PASS | App.jsx, Guestbook.jsx, and EntryForm.jsx exist with distinct responsibilities |
| C7: Both servers run | PASS | Flask API and React server simultaneously returned HTTP 200 |

## Overall

- [x] **CLEARED** — all constraints pass. Web App topic complete.
- [ ] **Not cleared** — constraints above marked FAIL.

## Notes (optional)

Completed Web App Level 2 with Flask JSON API, CORS, Vite React frontend, fetch API integration, multiple React components, and simultaneous backend/frontend servers.
