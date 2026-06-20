# Prompts — Web App (Full-Stack)

For the [Web app topic](../topics/web-app/). Common situations: Flask templates, React
state/effects, CORS, frontend-backend integration, the "full stack is broken" tangle.

---

## Frontend can't reach backend / fetch fails

**When:** your React app's `fetch()` errors out.

```
[CONTEXT] My React app calls my Flask API. The fetch fails in the browser.
[ACTUAL] Browser console / Network tab shows:
```<paste exact error — TypeError: Failed to fetch / CORS error / 404 / network error>```

[WHAT'S HAPPENING — my understanding]
My fetch:
```js
<paste>```
I think fetch works by <your interpretation — "the browser makes an HTTP request to the
URL, returns a promise that resolves with the Response">. The error "Failed to fetch"
usually means <your interpretation — "network-level failure: wrong URL, server not
running, or CORS blocked">.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "the URL is wrong — I'm fetching /api/entries but my Flask route is
/entries" / "CORS is blocking it" / "my Flask server isn't running" / "I'm calling fetch
inside the component body instead of useEffect, causing an infinite loop that crashes">.

[INFO I GATHERED]
- Does `curl <same URL>` from terminal work? <yes/no>
- Network tab: status is <200/404/CORS/pending>
- Browser console: <paste exact message>
- Flask console: <did it log the request? yes/no>

[ASK] Help me triangulate: is this a CORS issue, a URL issue, a server-not-running issue,
or a React issue? Walk me through the diagnostic (curl test → Network tab → Flask logs →
browser console). Pinpoint the cause and give me the fix on whichever side is broken.
```

---

## React state isn't updating / component doesn't re-render

**When:** you call setState but the UI doesn't change.

```
[CONTEXT] My React component should <show updated data after I add an entry / re-render
when state changes>.
[ACTUAL] <The UI stays the same / shows old data / re-renders but wrong>.

[WHAT'S HAPPENING — my understanding]
React re-renders a component when <your interpretation — "its state or props change">. I
call `setEntries(...)` and expect React to <your expectation>. My current understanding of
state: <it's a JS variable React watches / async / batched — state what you know>.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "I mutated the array directly (entries.push(x)) instead of creating a new
array, so React didn't detect the change" / "I'm reading state right after setState and
it's still the old value (setState is async)" / "my state is in a parent but the child
isn't getting the new prop">.

[MY COMPONENT]
```jsx
<paste>```
[WHAT I EXPECT vs WHAT I SEE]
- I click "Add", expect: <list updates with new entry>
- Actually: <nothing changes / old list / error>

[ASK] Explain React's re-render model (when and why it re-renders, immutability of state).
Trace my component: when I call setState, what does React do? Pinpoint why my UI isn't
updating. Show the fix and explain the immutability rule (why `setArr([...arr, newItem])`
not `arr.push`). Teach me how to debug React state (React DevTools, logging in render).
```

---

## useEffect is misbehaving (infinite loop / doesn't run / runs too often)

**When:** your effect runs forever, never runs, or runs at the wrong time.

```
[CONTEXT] I have a useEffect that should <fetch data once on mount / run when X changes>.
[ACTUAL] <It runs in an infinite loop / doesn't run at all / runs on every render>.

[WHAT'S HAPPENING — my understanding]
useEffect works by <your interpretation — "runs after render; the dependency array
controls when it re-runs; empty array = once on mount; array with values = when those
change; no array = every render">.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "my dependency array has an object/array that's recreated each render, so
React sees a 'new' reference every time and re-runs" / "I put a function in deps that
changes identity each render" / "I forgot the dependency array entirely">.

[MY EFFECT]
```jsx
<paste the useEffect + surrounding component>```
[SYMTOM]
- <Infinite requests in Network tab / effect never fires / fires on every keystroke>

[ASK] Explain useEffect's dependency array in detail (referential equality, why objects/
arrays/functions in deps are dangerous). Pinpoint why my effect misbehaves. Show the fix
and teach me the rules: when to use empty array, when to list deps, how to handle objects
(useMemo/useCallback or move out). Show me how to read React's warning about missing deps.
```

---

## Flask template (Jinja2) not rendering / wrong output

**When:** your HTML template shows raw `{{ variable }}` or doesn't show the data.

```
[CONTEXT] My Flask route renders a Jinja2 template. The variables <aren't showing / show
as None / show the literal {{ }}>.
[ACTUAL] <describe>.

[WHAT'S HAPPENING — my understanding]
`render_template('index.html', entries=entries)` <your interpretation — "loads the
template, replaces {{ entries }} with the value, sends HTML to browser">. In the template,
`{{ x }}` <prints x> and `{% for x in entries %}` <loops>.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "I named the template var 'entries' but in the template I wrote
{{ entry }}" / "my template is in the wrong folder (not templates/)" / "I returned the
template string directly instead of using render_template" / "the for-loop syntax is
wrong">.

[MY ROUTE]
```python
<paste>```
[MY TEMPLATE]
```html
<paste the relevant section>```
[WHAT THE BROWSER SHOWS]
```<paste — e.g., "the literal text {{ entries }} shows on the page">```

[ASK] Explain how Flask finds templates (templates/ folder) and how Jinja2 substitutes.
Diagnose why my variables don't render. Show the fix. Teach me the common Jinja2 gotchas
(variable name typos, missing templates/ folder, using render_template_string vs
render_template, for-loop scoping).
```

---

## Form submission doesn't work (Flask POST)

**When:** your HTML form's POST doesn't send data or Flask doesn't receive it.

```
[CONTEXT] I have an HTML form that should POST <name + message> to my Flask route.
[ACTUAL] <Flask gets empty request.form / 400 / form doesn't submit>.

[WHAT'S HAPPENING — my understanding]
A form POST works by <your interpretation — "browser encodes form fields and sends in the
body as application/x-www-form-urlencoded; Flask puts them in request.form">. The form
needs <action + method="post" + named inputs>.

[WHAT'S WRONG — my hypothesis]
I think <e.g., "my inputs have no `name` attribute, only `id`, so they're not sent" /
"the form method is GET not POST" / "I'm reading request.json instead of request.form">.

[MY FORM HTML]
```html
<paste>```
[MY FLASK ROUTE]
```python
<paste>```
[WHAT request.form SHOWS IN FLASK]
- `print(request.form)`: <ImmutableMultiDict([]) / the fields>

[ASK] Explain how HTML forms encode and send data, and how Flask exposes it (request.form
vs request.json vs request.data). Diagnose why my data isn't arriving. Show the fix. Teach
me the #1 gotcha: inputs need `name`, not just `id`/`placeholder`.
```

---

## Full stack is a mess and I don't know where the bug is

**When:** something's broken and you can't tell if it's frontend, backend, or the wire.

```
[CONTEXT] My full-stack app (React frontend, Flask backend) <isn't loading data / can't
submit / shows errors>. I don't know which layer is broken.
[GOAL] A systematic way to isolate the bug to one layer.

[WHAT'S HAPPENING — my understanding]
The data flow is: <React renders → useEffect fetches → Flask route queries store →
returns JSON → React setState → re-render>. The bug could be in <any of these>.

[WHAT I'VE CHECKED]
- Does `curl <backend URL>` return correct JSON? <yes/no — paste output>
- Does the browser Network tab show the request? <yes/no — status?>
- Does Flask log show the request arriving? <yes/no>
- Does the React console have errors? <yes/no — paste>
- Is the server running? <yes/no>

[ASK] DON'T fix it yet — teach me the systematic isolation method. Given my answers above,
which layer is the bug in? Walk me through the "divide and conquer": test backend with
curl first (removes frontend), then check the wire (Network tab), then frontend. Tell me
the next 2 diagnostic steps to nail it down. I want the debugging skill, not just the fix.
```

---

## Don't understand a React/Flask concept

**When:** you're fuzzy on a full-stack fundamental.

```
[CONTEXT] I'm learning <React / Flask / how frontend and backend communicate>. I keep
getting confused about <concept — e.g., "props vs state" / "why we need a build step for
React" / "what a component lifecycle is" / "what render_template actually does">.
[GOAL] A clear mental model.

[WHAT'S HAPPENING — my current understanding]
Here's what I think `<concept>` is/does: <your best guess>. Specifically I'm confused
about <the sticking point>.

[ASK] Explain `<concept>` like I'm new to web dev. Give me: (1) the problem it solves (why
does it exist?), (2) a tiny concrete example, (3) the mental model in one sentence,
(4) the common misconception. Avoid jargon or define it inline. Use my guestbook app as
the running example if it helps.
```

---

## Review my full-stack app

**When:** it works but you want a quality review across the stack.

```
[CONTEXT] I finished the Web App <level> assignment. It works end to end. I want a senior
review across frontend, backend, and integration.

[WHAT'S HAPPENING — my understanding]
Architecture: <Flask serves JSON at /api, React on :5173 fetches and renders, etc.>. I
think the code is <clean / messy in X>. The main risk areas I'm aware of: <CORS, error
handling, loading states>.

[MY BACKEND (app.py)]
```python
<paste>```
[MY FRONTEND (key components)]
```jsx
<paste>```

[ASK] Review across the stack. Look for: (1) backend — REST correctness, validation, error
handling; (2) frontend — component structure, state management, effect correctness; (3)
integration — error handling when API fails, loading states, race conditions; (4) the
"would this survive real users" test. Top 5 issues with fixes. Call out one thing each
layer does well.
```
