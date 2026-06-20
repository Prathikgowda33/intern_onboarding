# Constraints — Level 1 (Backend + Static HTML)

The acceptance checklist. Verify each constraint **manually** by running a command and observing
the result. Then record Pass/Fail + evidence in [RESULTS.md](RESULTS.md).

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

- [ ] **C1: Home page loads**
  - How to verify: run `curl -s -w "\nHTTP_CODE:%{http_code}" http://localhost:5000/`.
  - Pass if: HTTP_CODE is 200. The response body contains HTML (look for `<html>` or `<div>`
    or `<h1>` tags). The response includes the guestbook form or entry list.
  - Fails if: HTTP_CODE is not 200, or no HTML content.

- [ ] **C2: Can submit a guestbook entry via POST**
  - How to verify: run `curl -s -w "\nHTTP_CODE:%{http_code}" -X POST http://localhost:5000/ -d "name=Alice&message=Hello+world"`.
  - Pass if: HTTP_CODE is 200 or 302 (redirect after POST is fine). After this POST, a
    GET to `/` shows "Alice" and "Hello world" somewhere in the HTML.
  - Fails if: HTTP_CODE is 400 or 500, or the entry doesn't appear on the page.

- [ ] **C3: Multiple entries persist and display**
  - How to verify: submit two more entries: `curl -s -X POST http://localhost:5000/ -d "name=Bob&message=Second+entry"` and `curl -s -X POST http://localhost:5000/ -d "name=Carol&message=Third+entry"`. Then run `curl -s http://localhost:5000/`.
  - Pass if: the HTML output contains "Alice", "Bob", and "Carol". All three entries are
    visible on the same page. The entries appear in the order they were added (newest last or
    newest first — either is fine).
  - Fails if: not all three names appear, or only one entry is shown.

- [ ] **C4: File structure is correct**
  - How to verify: run `ls -R` from this folder.
  - Pass if: `app.py` exists. A `templates/` directory exists containing at least one `.html`
    file. A `static/` directory exists containing at least one `.css` file.
  - Fails if: missing any of the three required files/directories.

- [ ] **C5: Template uses Jinja2 syntax**
  - How to verify: run `grep -n "{{ \|{% " templates/index.html`.
  - Pass if: at least one Jinja2 template variable (`{{ ... }}`) or control structure (`{% ... %}`)
    is found in the template. The template dynamically renders entries from the backend.
  - Fails if: no Jinja2 syntax found (template is pure static HTML with no dynamic content).

- [ ] **C6: Each entry has a name and message**
  - How to verify: run `curl -s http://localhost:5000/` and look at the entries.
  - Pass if: each entry on the page displays both a name and a message. Entries are visually
    distinguishable from each other (not all crammed into one line).
  - Fails if: entries show only one field, or entries are not visually separated.

- [ ] **C7: CSS file is linked and affects the page**
  - How to verify: run `grep -i "stylesheet\|style.css\|link.*css" templates/index.html`.
  - Pass if: the HTML contains a link to a CSS file (typically `<link rel="stylesheet" href="/static/style.css">`).
  - Fails if: no CSS link found, or CSS is inline in the HTML only.
  - **Independent check:** run `curl -s http://localhost:5000/static/style.css` — should
    return CSS content (HTTP 200).

---

## Summary

7 constraints. C1 checks the page loads. C2 checks form submission. C3 checks data persistence.
C4 checks file structure. C5 checks template rendering. C6 checks data display. C7 checks CSS.
If any fail, see [../../../resources.md](../../../resources.md) — especially "Flask backend and HTML".
