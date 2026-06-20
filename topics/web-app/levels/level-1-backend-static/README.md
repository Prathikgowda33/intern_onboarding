# Level 1 — Backend + Static HTML

<!--
  Level metadata:
    slug: web-app/level-1-backend-static
    skills: Flask, Jinja2 templates, HTML forms, GET/POST, static files
    difficulty: Medium
    estimated_time: 2-3h
    starter_mode: scratch
-->

## Prerequisites

You need **Python 3** and **Flask**. See the [topic README](../../../README.md) for installation.

### Verify

```bash
python3 --version && python3 -c "import flask; print('Flask OK')"
```

## What to build

Build a **Guestbook** web app with Flask. The app serves an HTML page where visitors can leave
their name and a message, and view all previous messages. Data is stored **in memory** (a Python
list).

### The app

- **Home page** (`GET /`): displays all guestbook entries (name, message, timestamp) in a
  styled HTML page, and a form at the bottom to add a new entry.
- **Submit** (`POST /`): accepts form data (name + message), stores the entry, and redirects
  back to the home page.

### Step-by-step

1. Create `app.py` with a Flask app and a list to store entries. If you've never written
   Flask with templates, here's the minimal shape (NOT the solution — fill in the logic):
   ```python
   from flask import Flask, render_template, request, redirect, url_for
   import datetime
   app = Flask(__name__)
   entries = []  # in-memory store; each entry: {"name":..., "message":..., "time":...}

   @app.route("/", methods=["GET", "POST"])
   def index():
       if request.method == "POST":
           # TODO: read name + message from request.form, append to entries, redirect
           pass
       # GET: render the template, passing entries
       return render_template("index.html", entries=entries)

   if __name__ == "__main__":
       app.run(host="0.0.0.0", port=5000)
   ```
2. Create a `templates/` folder (must be exactly named `templates/` — Flask looks there by
   default) with `index.html` — the guestbook page using Jinja2 templates. Minimal Jinja2
   pattern for looping over entries:
   ```html
   {% for entry in entries %}
     <div>{{ entry.name }} said: {{ entry.message }}</div>
   {% endfor %}
   ```
3. Create a `static/` folder (must be exactly named `static/`) with `style.css` — basic
   styling (not required to be fancy, but should be readable). Link it in your HTML:
   `<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">`.
4. Implement `GET /` — passes entries to the template, renders the page (done in the
   boilerplate above).
5. Implement `POST /` — reads `name` and `message` from `request.form`, appends to the
   list (with a timestamp), then `return redirect(url_for("index"))`.
6. Start the server: `python3 app.py` (listens on `http://localhost:5000`).
7. Open `http://localhost:5000` in a browser and test.

### How to run

```bash
python3 app.py
# Open http://localhost:5000 in your browser
```

## Why this matters

This is the simplest possible full web app: a backend that serves HTML and handles form
submissions. Every complex web app starts here — Flask routes, templates, and request/response.
Understanding this pattern is the foundation for everything else in web development.

## Deliverables

- `app.py` — Flask app with GET/POST routes
- `templates/index.html` — Jinja2 template with the guestbook page
- `static/style.css` — basic styling
- App running and testable in a browser

## Starter mode: `scratch`

No starter code. Build everything from the assignment above.

## How you'll be checked

Open [constraints.md](constraints.md). Each constraint is verified by running a `curl` command
or checking the file structure. Self-report in [RESULTS.md](RESULTS.md). See
[../../../../HOW_IT_WORKS.md](../../../../HOW_IT_WORKS.md) for the full workflow.

- All constraints pass → Level 1 cleared (and the whole Web App topic is cleared).
- Any constraint fails → study [../../../resources.md](../../../resources.md), fix, re-check.
