# Copy patterns

Reference for the copy that appears when the page has nothing to show: loading,
empty, and error states. It records decisions we've already made so the next
state doesn't get written from scratch in a different voice.

Voice rules live in `CLAUDE.md` under "Voice & copy decisions" and apply here
too. This document covers what's specific to failed states.

## Where the strings live

All three families live in one `COPY` object at the top of `docs/js/scripts.js`.
Nothing is written inline in a render function, and nothing is duplicated
between the JS and `docs/index.html` except the loading string, which appears in
the HTML so the first paint isn't blank.

Change copy in `COPY`. If a string needs a number in it (the signal threshold,
an entry count), interpolate the constant rather than typing the number — copy
that hardcodes a threshold goes stale the moment the threshold moves.

## Shape of a state

Every state is the same three parts, in the same order:

| Part | Required | What it does |
|---|---|---|
| `title` | Yes | Names what happened, in one sentence. |
| `body` | Empty states and errors | Says what it means for the reader, and what happens next. |
| action | Only when it resolves the state | One button. Never two. |

Loading uses `title` alone. Errors that a retry can't fix carry no action — see
below.

## Loading

One string, everywhere: **Loading the dataset…**

Decisions:

- **One string, not three.** The three panels load from one file in one request.
  Writing "Loading responsibilities…" in one panel and "Loading roles…" in
  another implies three independent fetches and three ways to fail. There is one.
- **Held back 400ms.** The dataset is a single small JSON file and usually
  arrives before the reader's eye settles. The loading text fades in on a delay
  so a fast load never flashes a message and then yanks it away. Under
  `prefers-reduced-motion`, it appears immediately with no fade.
- **No "Please wait."** The reader can see that.
- **No progress language.** We don't know the percentage and won't invent one.
- **No skeleton screens.** A skeleton promises a layout. The three panels render
  different shapes, and a wrong-shaped skeleton is worse than a line of text.

## Empty

Two situations that look identical on screen and read differently:

**Nothing here yet.** The dataset genuinely has no rows of this kind. State that,
then say what would put something here.

> No roles yet.
> Roles appear here as job descriptions are audited into the dataset.

**Nothing cleared the bar.** Rows exist, but a rule filtered them all out. State
that, then explain the rule — otherwise the reader assumes the page is broken.

> No skills have crossed the threshold yet.
> Skills appear here once 2 or more postings ask for them. One posting is an anecdote.

Decisions:

- **Name the rule when a rule is doing the filtering.** The signals panel hides
  anything below the threshold. A reader who can't see the rule can't tell the
  difference between an empty dataset and a strict filter.
- **No exhortation.** We don't tell the reader to check back soon or follow
  along. The site doesn't have a subscribe button and shouldn't imply one.
- **Empty is not an error.** No alarm styling, no `role="alert"`, no retry
  button. Nothing failed.

## Errors

Four kinds, because they need four different things from the reader.

| Kind | When | Copy | Action |
|---|---|---|---|
| `offline` | `navigator.onLine` is false, or the request fails while offline | **You're offline.** / Reconnect and try again. | Try again |
| `network` | Non-2xx response, or the request throws | **The dataset didn't load.** / This is on our end. Try again, or come back in a few minutes. | Try again |
| `timeout` | No response within 10s | **The dataset is taking too long.** / The request timed out before the file came back. Try again. | Try again |
| `malformed` | The response isn't valid JSON, or is missing `entries`, `clusters`, or `signals` | **The dataset loaded, but we couldn't read it.** / Retrying won't fix this one. Email joe@bertino.co and we'll take a look. | None — email link in the body |

Decisions:

- **Only offer an action that can resolve the state.** A retry button on a
  malformed file is a button that fails every time it's pressed. When we can't
  fix it from the browser, we say so and give the reader the one thing that
  works, which is telling us.
- **Say whose problem it is.** "This is on our end" answers the question the
  reader is actually asking, which is whether they did something wrong. Offline
  is the one case where the answer is on their side, and the copy says so without
  making it a scolding.
- **No apologies.** "Sorry" doesn't load the file. One sentence on what happened,
  one on what to do.
- **No error codes, no stack traces, no file paths.** The previous error state
  told readers to confirm `data/jobs.json` exists and to serve the site over
  HTTP. That's a note to the developer, printed on a page for content designers.
  Diagnostic detail belongs in `console.error`, and that's where it goes now.
- **No blame-shifting to the reader's setup.** We don't suggest clearing the
  cache, disabling extensions, or trying another browser unless we know that's
  the cause. We don't.
- **The error replaces the panel, not the page.** The header, nav, and footer
  stay. The footer's last-updated date falls back to the value in the HTML rather
  than going blank.

## Accessibility

- A visually hidden live region (`#a11y-status`) carries every state change:
  the error text on failure, `Dataset loaded. N roles.` on success. Screen
  readers announce a change to a region that already exists; they're unreliable
  about a region that gets injected, which is why it's in the HTML from the start.
- Error blocks also carry `role="alert"`. Empty and loading blocks carry no role —
  the live region already handles them, and a second announcement is noise.
- Retry destroys the button that had focus. Focus moves to the active panel
  (`tabindex="-1"`) so a keyboard reader lands where they were, not at the top of
  the document.
- The retry button is a real `<button>` with a visible focus ring. Every state
  action must be reachable by keyboard.

## Words we don't use

| Not this | This |
|---|---|
| Oops! / Uh oh / Something went wrong | Name what didn't load |
| Please try again later | Try again, or come back in a few minutes |
| An error occurred (code 500) | The dataset didn't load |
| No data available | No roles yet |
| We're working on it | (Only if we are) |
| Check back soon! | (Say what would put content here instead) |

## Adding a state

1. Write it into `COPY` in `docs/js/scripts.js`. Don't inline it.
2. Pick the variant: `loading`, `empty`, or `error`. The variant sets the styling
   and the ARIA role.
3. Title names what happened. Body says what it means and what's next. Skip the
   action unless it can actually resolve the state.
4. Read it aloud against `CLAUDE.md` — em dashes sparingly, colons only for
   lists, no hedging, no consulting tone.
5. Verify it renders. Every state in this document was checked in a browser by
   intercepting the request: 404 for `network`, a hung request for `timeout`,
   truncated JSON for `malformed`, and an empty dataset for the empty states.
