# Resources — Web App

Shared across all three Web App levels. This is a **progressive** resource list: it starts from
"what is a web app?" and goes up through Dockerized full-stack apps. **You don't read all of it.**
Find the level you're working on, read only what your failed constraints point to.

This list focuses on web development specifically. The master cross-topic list is at
[../../resources.md](../../resources.md).

---

## From absolute zero (what is a web app?)

If you've never built a web page or don't know what a backend is, start here.

| Resource | Type | Why it's here |
|----------|------|---------------|
| [MDN — How the Web Works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works) | Reading | C1 — clients, servers, HTTP, DNS — the full picture in plain English. |
| [MDN — Introduction to HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML) | Reading | C1 — what HTML is, elements, tags, and page structure. |
| [Flask Quickstart](https://flask.palletsprojects.com/en/latest/quickstart/) | Reading | C1 — how to create a Flask app, routes, templates, serving static files. |

**The mental model you need first:** A web app has a **backend** (a server running Python/Flask)
that handles requests and a **frontend** (HTML/CSS/JS in the browser) that the user sees. The
frontend sends HTTP requests to the backend, the backend processes them and sends back responses.
Level 1 has both in one Flask app. Level 2 separates them.

## Flask backend and HTML (Level 1)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Flask — Rendering Templates](https://flask.palletsprojects.com/en/latest/quickstart/#rendering-templates) | Reading | C1 — how to use Jinja2 templates and `render_template()`. |
| [Flask — Static Files](https://flask.palletsprojects.com/en/latest/quickstart/#static-files) | Reading | C1 — how to serve CSS, JS, and image files. |
| [Jinja2 Template Designer Docs](https://jinja.palletsprojects.com/en/latest/templates/) | Reference | C1 — template syntax: `{{ variable }}`, `{% for %}`, `{% if %}`. |
| [MDN — HTML Forms](https://developer.mozilla.org/en-US/docs/Learn/Forms) | Reading | C1, C3 — how to create forms that POST data to a server. |

## React and frontend frameworks (Level 2)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [React — Quick Start](https://react.dev/learn) | Reading | C1, C2 — what React is, components, state, props. Start with "Thinking in React". |
| [Vite — Getting Started](https://vitejs.dev/guide/) | Reading | C1 — how to create a Vite + React project. |
| [MDN — Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) | Reading | C3 — how to make HTTP requests from JavaScript using `fetch()`. |
| [MDN — CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) | Reading | C2 — what CORS is, why it exists, and how to configure it in Flask. |
| [Flask-CORS](https://flask-cors.readthedocs.io/) | Reference | C2 — how to enable CORS in Flask with `flask-cors`. |

## Production features (Level 3)

| Resource | Type | Why it's here |
|----------|------|---------------|
| [Docker — Get Started](https://docs.docker.com/get-started/) | Reading | C4 — Docker basics: images, containers, Dockerfile. |
| [Flask — Error Handling](https://flask.palletsprojects.com/en/latest/errorhandling/) | Reading | C1 — custom error pages and error handlers. |
| [React — Error Boundaries](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary) | Reference | C2 — how to catch errors in React UI. |
| [MDN — Loading States](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Fetching_data) | Reading | C3 — how to show loading spinners while data is being fetched. |

---

## How to use these

1. Open the `RESULTS.md` of the level you're working on and find which constraints failed.
2. Read the resource(s) next to those constraints above.
3. Fix your solution.
4. Re-run the checks in the level's `constraints.md`.
5. Update `RESULTS.md` with the new evidence.

Don't read everything top to bottom — target the gap.
