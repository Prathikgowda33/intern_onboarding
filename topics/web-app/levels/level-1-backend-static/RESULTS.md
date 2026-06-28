# Results — Level 1 (Backend + Static HTML)

| Constraint | Result | Evidence (command + what you observed) |
|------------|--------|--------------------------------------|
| C1: Home page loads | PASS | GET / returned HTML page with HTTP 200 |
| C2: Can submit entry via POST | PASS | POST request created guestbook entry successfully |
| C3: Multiple entries persist | PASS | Alice, Bob and Carol entries displayed together |
| C4: File structure correct | PASS | app.py, templates/index.html and static/style.css present |
| C5: Jinja2 template syntax | PASS | Template contains {{ }} and {% %} syntax |
| C6: Entries show name + message | PASS | Each guestbook entry displays both the name and message |
| C7: CSS linked and served | PASS | CSS linked in template and served from /static/style.css |

## Overall

- [x] **CLEARED** — all constraints pass. Web App topic complete.

## Notes (optional)

Successfully completed the Flask Guestbook web application with templates, static CSS, GET/POST routes, and in-memory storage.
