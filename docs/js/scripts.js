// Data path for GitHub Pages with `docs/` at repo root
const DATA_PATH = 'data/jobs.json';
const SIGNAL_THRESHOLD = 2;
const TITLES_LIMIT = 12;
const FETCH_TIMEOUT_MS = 10000;
const SECTION_CONTAINERS = ['cluster-grid', 'signal-list', 'title-list'];
// Symbol only — the ISO code is always shown alongside it (see fmt below),
// since a bare symbol is ambiguous (USD/CAD/AUD/HKD all use "$"). A currency
// missing here still renders correctly: no symbol, just the number and code.
const CURRENCY_SYMBOLS = {
  USD: '$',
  GBP: '£',
  CAD: '$',
  EUR: '€',
};
let showAllTitles = false;
let showAllClusters = false;
let showAllSignals = false;
let globalData = null;

// Full sorted key order for each collection, snapshotted at render time —
// the overlay carousel reads from these, not the grid's DOM, so it can
// always reach every entry regardless of what pagination currently has
// rendered (see openFlipCard/navigateFlipCard).
let clusterOrder = [];
let signalOrder = [];

// Responsibilities/Skills truncate at 3 full rows of whatever column count
// the grid is actually rendering at, not a flat number — read the live
// layout instead of duplicating the grid's own breakpoints as a second,
// driftable source of truth.
function currentColumnCount(gridEl) {
  return getComputedStyle(gridEl).gridTemplateColumns.split(' ').length;
}

// ── Copy ────────────────────────────────────────────────────
// All loading, empty, and error copy lives here. See copy-patterns.md
// for the rules these strings follow and why each one is worded this way.
const COPY = {
  loading: {
    title: 'Loading…',
  },
  empty: {
    clusters: {
      title: 'No responsibilities yet',
      body: 'Responsibilities appear here once the first job description is audited successfully.',
    },
    signals: {
      title: 'No skills yet',
      body: `Skills appear here once ${SIGNAL_THRESHOLD} or more postings ask for them.`,
    },
    titles: {
      title: 'No roles yet',
      body: 'Roles appear here as job descriptions are added to the dataset.',
    },
  },
  error: {
    offline: {
      title: "You're offline",
      body: 'Reconnect and try again.',
      retry: true,
    },
    network: {
      title: "The dataset didn't load",
      body: 'This is on our end. Try again, or come back in a few minutes.',
      retry: true,
    },
    timeout: {
      title: 'The dataset is taking too long',
      body: 'The request timed out before the file came back. Try again.',
      retry: true,
    },
    malformed: {
      title: "The dataset loaded, but we couldn't read it",
      body: 'Retrying won\'t fix this one. Email <a href="mailto:joe@bertino.co">joe@bertino.co</a> to take a look.',
      retry: false,
    },
  },
};

// ── State rendering ─────────────────────────────────────────
function announce(message) {
  const region = document.getElementById('a11y-status');
  if (region) region.textContent = message;
}

function stateMarkup({ variant, title, body, retry }) {
  return `
    <div class="state state--${variant}"${variant === 'error' ? ' role="alert"' : ''}>
      <p class="state-title">${title}</p>
      ${body ? `<p class="state-body">${body}</p>` : ''}
      ${retry ? '<button type="button" class="state-action">Try again</button>' : ''}
    </div>
  `;
}

function renderState(containerId, state) {
  const el = document.getElementById(containerId);
  if (el) el.innerHTML = stateMarkup(state);
}

function renderLoading() {
  SECTION_CONTAINERS.forEach(id => renderState(id, { variant: 'loading', title: COPY.loading.title }));
}

function renderError(kind) {
  const copy = COPY.error[kind] || COPY.error.network;
  SECTION_CONTAINERS.forEach(id => renderState(id, { variant: 'error', ...copy }));

  // The retry affordance appears in all three panels; only one is visible at a
  // time, so wire every instance.
  document.querySelectorAll('.state-action').forEach(btn => {
    btn.addEventListener('click', () => init({ fromRetry: true }));
  });

  announce(`${copy.title} ${copy.body.replace(/<[^>]+>/g, '')}`);
}

// ── Data ────────────────────────────────────────────────────
function isWellFormed(data) {
  return !!data
    && typeof data === 'object'
    && Array.isArray(data.entries)
    && !!data.clusters && typeof data.clusters === 'object'
    && !!data.signals && typeof data.signals === 'object';
}

async function loadData() {
  if (navigator.onLine === false) return { error: 'offline' };

  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), FETCH_TIMEOUT_MS);

  try {
    const res = await fetch(DATA_PATH, { signal: controller.signal });
    if (!res.ok) return { error: 'network' };

    const data = await res.json();
    if (!isWellFormed(data)) return { error: 'malformed' };
    return { data };
  } catch (err) {
    if (err.name === 'AbortError') return { error: 'timeout' };
    // A JSON parse failure means the file came back but isn't readable.
    if (err instanceof SyntaxError) return { error: 'malformed' };
    console.error(err);
    return { error: navigator.onLine === false ? 'offline' : 'network' };
  } finally {
    clearTimeout(timer);
  }
}

// ── Render ──────────────────────────────────────────────────
function renderMeta(data) {
  const dateEl = document.getElementById('footer-date');
  const iso = data.meta && data.meta.lastUpdated;
  // No date in the payload: keep the value rendered in the HTML rather than
  // replacing it with a blank.
  if (dateEl && iso) {
    // ISO, matching the dateAdded format on role cards.
    dateEl.innerHTML = `<time datetime="${iso}">${iso}</time>`;
  }

  // entries.length, not meta.totalEntries: the array actually loaded is the
  // authoritative count, rather than a separately hand-maintained field that
  // could drift from it.
  const countEl = document.getElementById('hero-role-count');
  if (countEl && Array.isArray(data.entries)) {
    countEl.textContent = data.entries.length;
  }
}

// The Skills tab shows a signal only once SIGNAL_THRESHOLD postings ask for it —
// one posting is an anecdote. Nav counts and the per-role chips read the same
// filter from here, so a signal can never appear on a role without also being
// findable in Skills.
function signalEntryCounts(data) {
  const counts = new Map(Object.keys(data.signals).map(k => [k, 0]));
  data.entries.forEach(entry => {
    (entry.signals || []).forEach(s => {
      if (counts.has(s)) counts.set(s, counts.get(s) + 1);
      else console.warn('Unknown signal key in entry:', s);
    });
  });
  return counts;
}

function displayedSignalKeys(data) {
  return new Set(
    [...signalEntryCounts(data)]
      .filter(([, n]) => n >= SIGNAL_THRESHOLD)
      .map(([key]) => key)
  );
}

// Entries that carry a given cluster/signal key, most recent first — backs
// the "appears in N roles" list on the flip-card overlay.
function entriesForKey(data, key, field) {
  return data.entries
    .filter(entry => (entry[field] || []).includes(key))
    .slice()
    .sort((a, b) => new Date(b.dateAdded) - new Date(a.dateAdded));
}

// Single source for the rounded percentage shown both on the card front
// (bare number) and the back (full "Appears in N of M roles" string).
function keyPercentage(data, key, field) {
  const entries = entriesForKey(data, key, field);
  const total = data.entries.length;
  return total ? Math.round((entries.length / total) * 100) : 0;
}

// Title + description + stat line only — the part that swaps when the
// overlay carousel navigates to another key. The close button lives
// outside this wrapper so navigating never has to re-wire its listener.
// Percentage is deliberately not repeated here — the front already shows
// the bare number, and this line's own "N of M roles" count is the same
// conclusion stated a different way; a reader can connect the two without
// the figure appearing twice.
function flipCardContentHtml(key, field, label, description, data) {
  const entries = entriesForKey(data, key, field);
  const total = data.entries.length;
  const rolesHtml = entries.length
    ? `<div class="flip-card-roles">
        <p class="flip-card-roles-label">Appears in ${entries.length} of ${total} roles</p>
      </div>`
    : '';
  return `
    <h3 class="flip-card-back-title">${label}</h3>
    ${rolesHtml}
    <p class="flip-card-back-desc">${description}</p>
  `;
}

function flipCardBackHtml(key, field, label, description, data) {
  return `
    <button type="button" class="flip-card-close" aria-label="Close">
      <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="M1 1L13 13M13 1L1 13" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
      </svg>
    </button>
    <div class="flip-card-back-content">
      ${flipCardContentHtml(key, field, label, description, data)}
    </div>
  `;
}

function renderClusters(data) {
  const grid = document.getElementById('cluster-grid');
  const clusterKeys = Object.keys(data.clusters);

  if (clusterKeys.length === 0) {
    renderState('cluster-grid', { variant: 'empty', ...COPY.empty.clusters });
    return;
  }

  const clusterMap = {};
  clusterKeys.forEach(key => { clusterMap[key] = []; });

  data.entries.forEach(entry => {
    entry.clusters.forEach(c => {
      if (clusterMap[c]) clusterMap[c].push(entry.company);
      else console.warn('Unknown cluster key in entry:', c);
    });
  });

  // Sort by number of companies, descending
  clusterKeys.sort((a, b) => clusterMap[b].length - clusterMap[a].length);
  clusterOrder = clusterKeys.slice();

  const showMore = document.getElementById('clusters-show-more');
  const showMoreBtn = showMore ? showMore.querySelector('.show-more-btn') : null;
  // Single column (mobile) shows everything, no pagination — with a dataset
  // this small, "load more" gates a handful of items, not a real list.
  const isSingleColumn = currentColumnCount(grid) === 1;
  const limit = currentColumnCount(grid) * 3;
  const keysToRender = (isSingleColumn || showAllClusters) ? clusterKeys : clusterKeys.slice(0, limit);

  if (showMore) {
    if (!isSingleColumn && !showAllClusters && clusterKeys.length > limit) {
      showMore.style.display = 'block';
      showMoreBtn.textContent = 'View all';
    } else {
      showMore.style.display = 'none';
    }
  }

  grid.innerHTML = keysToRender.map(key => {
    const cluster = data.clusters[key];
    const pct = keyPercentage(data, key, 'clusters');
    return `
      <div class="flip-card cluster-card" data-key="${key}" role="button" tabindex="0" aria-label="Expand ${cluster.label}, ${pct}% of roles">
        <div class="flip-card-front">
          <h3>${cluster.label}</h3>
          <div class="flip-card-stat">${pct}%</div>
        </div>
        <div class="flip-card-back">
          ${flipCardBackHtml(key, 'clusters', cluster.label, cluster.description, data)}
        </div>
      </div>
    `;
  }).join('');
}

function formatDate(iso) {
  return iso;
}

// Titles are stored verbatim, so they arrive with whatever separator the
// employer used. Em dash and pipe both join a role to its scope — "Annotation
// Manager — Content Platform", "Content Strategist | Agentic Commerce" — which
// is what a comma does, so those are normalised.
//
// A forward slash is left alone. It joins two titles naming one role, as in
// Zoom's "AI Information Architect / Content Strategist", and a comma there
// would read as scope rather than as an alternate title.
//
// Only spaced separators match, so hyphenated compounds like "AI-Powered" are
// untouched. jobs.json keeps the verbatim title either way — that is what ties
// an entry to its jd-source archive.
function formatTitle(title) {
  return title.replace(/\s+[-—–|]\s+/g, ', ');
}

function renderTitles(data) {
  const list = document.getElementById('title-list');
  const showMore = document.getElementById('titles-show-more');
  const showMoreBtn = showMore ? showMore.querySelector('.show-more-btn') : null;

  if (data.entries.length === 0) {
    if (showMore) showMore.style.display = 'none';
    renderState('title-list', { variant: 'empty', ...COPY.empty.titles });
    return;
  }

  const sorted = [...data.entries].sort((a, b) => new Date(b.dateAdded) - new Date(a.dateAdded));
  const entries = showAllTitles ? sorted : sorted.slice(0, TITLES_LIMIT);

  if (showMore) {
    if (!showAllTitles && data.entries.length > TITLES_LIMIT) {
      showMore.style.display = 'block';
      showMoreBtn.textContent = 'View all';
    } else {
      showMore.style.display = 'none';
    }
  }

  const displayed = displayedSignalKeys(data);

  list.innerHTML = entries.map(entry => {
    const fmt = (n, currency) => (CURRENCY_SYMBOLS[currency] || '') + n.toLocaleString('en-US');

    // Qualifiers are read from structured fields, never parsed out of prose.
    //
    // `covers: "total"` is shown because a total-comp figure is not comparable
    // to the base ranges around it. `covers: "base"` and `covers: null` show
    // nothing, since neither can claim more than the bare number does.
    //
    // `scope` and `extras` are never rendered on the card — location strings
    // wrap and extend the card at narrow widths. Both stay in jobs.json.
    const c = entry.compRange;
    const qualifiers = c
      ? [c.covers === 'total' ? 'total comp' : null].filter(Boolean)
      : [];
    const compHtml = c
      ? `<span class="title-comp">${fmt(c.min, c.currency)}–${fmt(c.max, c.currency)} ${c.currency}`
        + qualifiers.map(q => ` · ${q}`).join('')
        + `</span>`
      : '';
    // Chips are filtered to the signals the Skills tab shows, so a reader can
    // always follow one from a role to its definition. Insurify's "Title
    // dilution" and Meta's "Hybrid role" sit below the threshold and are held
    // back here; both remain assigned in jobs.json.
    const shownSignals = (entry.signals || []).filter(s => displayed.has(s));
    const signalsHtml = shownSignals.length
      ? `<ul class="title-signals">`
        + shownSignals.map(s => `<li class="signal-chip">${data.signals[s].label}</li>`).join('')
        + `</ul>`
      : '';

    // The control opens whatever the entry has. Three entries carry signals but
    // no quote, so gating on the quote alone would leave their chips unreachable.
    const hasQuote = !!entry.quote;
    const hasDetail = hasQuote || shownSignals.length > 0;
    // `quoteTranslatedFrom`/`titleTranslatedFrom` mark the quote and/or title as
    // translations rather than verbatim source text — see CLAUDE.md's Quote and
    // Title field sections. One plain note, regardless of which field(s) are
    // actually translated, surfaces only once a reader expands the entry (not
    // as metadata sitting under the title) — so it only ever shows alongside
    // the quote it qualifies. A title-only translation on an entry with no
    // quote and no signals has no detail panel to appear in; no entry has hit
    // that yet, so it's left unhandled rather than solved for a case that
    // doesn't exist.
    const translationLang = entry.quoteTranslatedFrom || entry.titleTranslatedFrom;
    const translationHtml = (hasDetail && translationLang)
      ? `<p class="quote-translation-note">Translated from ${translationLang}</p>`
      : '';
    const detailHtml = hasDetail
      ? `<div class="title-detail"><div class="title-detail-inner">`
        + (hasQuote ? `<blockquote>${entry.quote}</blockquote>` : '')
        + translationHtml
        + signalsHtml
        + `</div></div>`
      : '';
    const expandBtn = hasDetail
      ? `<button class="title-expand" aria-expanded="false" aria-label="Show details">+</button>`
      : '';
    // Company and pay share the attribution line; the date drops to its own
    // line below, being the least useful fact in the entry. `domain` is
    // deliberately not rendered: it largely restates the company beside it. It
    // stays in jobs.json, where the taxonomy keeps the dataset queryable.
    const sep = '<span class="title-sep">·</span>';
    const attribHtml = `<div class="title-attrib">`
      + `<span class="title-company">${entry.company}</span>`
      + (compHtml ? `${sep}${compHtml}` : '')
      + `</div>`;
    const dateHtml = entry.dateAdded
      ? `<div class="title-date">${formatDate(entry.dateAdded)}</div>`
      : '';

    return `
      <div class="title-entry${hasDetail ? ' is-expandable' : ''}">
        <div class="title-header">
          <div class="title-name">${formatTitle(entry.title)}</div>
          ${expandBtn}
        </div>
        ${attribHtml}
        ${dateHtml}
        ${detailHtml}
      </div>
    `;
  }).join('');

  // Expand/collapse: the whole summary row is the hit target, not just the
  // icon, so a reader can click anywhere on a line item to open it. Clicks
  // inside the detail region itself are excluded so selecting the quote text
  // doesn't collapse the row out from under it.
  list.querySelectorAll('.title-entry.is-expandable').forEach(entry => {
    const btn = entry.querySelector('.title-expand');
    entry.addEventListener('click', (e) => {
      if (e.target.closest('.title-detail')) return;
      const isOpen = entry.classList.toggle('is-expanded');
      btn.setAttribute('aria-expanded', String(isOpen));
      btn.textContent = isOpen ? '−' : '+';
      btn.blur();
    });
  });
}

function renderSignals(data) {
  const list = document.getElementById('signal-list');

  // Most-attested first.
  const relevantSignals = [...signalEntryCounts(data)]
    .filter(([, n]) => n >= SIGNAL_THRESHOLD)
    .sort((a, b) => b[1] - a[1])
    .map(([key]) => key);

  if (relevantSignals.length === 0) {
    renderState('signal-list', { variant: 'empty', ...COPY.empty.signals });
    return;
  }

  signalOrder = relevantSignals.slice();

  const showMore = document.getElementById('signals-show-more');
  const showMoreBtn = showMore ? showMore.querySelector('.show-more-btn') : null;
  // Single column (mobile) shows everything, no pagination — with a dataset
  // this small, "load more" gates a handful of items, not a real list.
  const isSingleColumn = currentColumnCount(list) === 1;
  const limit = currentColumnCount(list) * 3;
  const keysToRender = (isSingleColumn || showAllSignals) ? relevantSignals : relevantSignals.slice(0, limit);

  if (showMore) {
    if (!isSingleColumn && !showAllSignals && relevantSignals.length > limit) {
      showMore.style.display = 'block';
      showMoreBtn.textContent = 'View all';
    } else {
      showMore.style.display = 'none';
    }
  }

  list.innerHTML = keysToRender.map(key => {
    const signal = data.signals[key];
    const pct = keyPercentage(data, key, 'signals');
    return `
      <div class="flip-card signal-card" data-key="${key}" role="button" tabindex="0" aria-label="Expand ${signal.label}, ${pct}% of roles">
        <div class="flip-card-front">
          <div class="signal-label">${signal.label}</div>
          <div class="flip-card-stat">${pct}%</div>
        </div>
        <div class="flip-card-back">
          ${flipCardBackHtml(key, 'signals', signal.label, signal.description, data)}
        </div>
      </div>
    `;
  }).join('');
}

// ── Badge nav (click + arrow keys) ──────────────────────────
const badges = Array.from(document.querySelectorAll('.badge-btn'));
const badgeNav = document.querySelector('.badge-nav');

const badgeNavIndicator = document.querySelector('.badge-nav-indicator');

// Slides the shared indicator under whichever tab is active. top is
// included, not just left/width, because the nav wraps to a second row
// at narrow widths (see the <=480px media query) — the active tab isn't
// always on the same row. skipTransition suppresses the CSS transition
// for the very first call, so the indicator doesn't animate in from
// (0,0) on page load — see the "Skip Animation on Page Load" pattern
// used elsewhere on the site.
function positionNavIndicator(skipTransition) {
  const activeBadge = document.querySelector('.badge-btn.active');
  if (!activeBadge || !badgeNavIndicator) return;
  if (skipTransition) badgeNavIndicator.style.transition = 'none';
  badgeNavIndicator.style.top = `${activeBadge.offsetTop + activeBadge.offsetHeight}px`;
  badgeNavIndicator.style.left = `${activeBadge.offsetLeft}px`;
  badgeNavIndicator.style.width = `${activeBadge.offsetWidth}px`;
  if (skipTransition) {
    void badgeNavIndicator.offsetWidth; // force reflow before restoring the transition
    badgeNavIndicator.style.transition = '';
  }
}

function activateBadge(badge) {
  badges.forEach(b => {
    b.classList.remove('active');
    b.setAttribute('aria-selected', 'false');
  });
  document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
  badge.classList.add('active');
  badge.setAttribute('aria-selected', 'true');
  document.getElementById(badge.dataset.section).classList.add('active');
  positionNavIndicator();
}

badges.forEach(badge => {
  badge.addEventListener('click', () => {
    activateBadge(badge);
    // Blur only here, not inside activateBadge: the arrow-key handler below
    // also calls activateBadge after moving focus with .focus(), and a
    // shared blur() there stripped focus again immediately — the keydown
    // listener is on .badge-nav, and relies on a focused descendant for
    // events to bubble through, so after one arrow press focus (and with
    // it, all further arrow presses) went dead.
    badge.blur();
  });
});

badgeNav.addEventListener('keydown', (e) => {
  if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
  e.preventDefault();
  const idx = badges.indexOf(document.activeElement);
  const next = e.key === 'ArrowRight'
    ? (idx + 1) % badges.length
    : (idx - 1 + badges.length) % badges.length;
  badges[next].focus();
  activateBadge(badges[next]);
});

positionNavIndicator(true);
// Column count and text wrapping don't change on resize, but which row a
// tab wraps to (<=480px) or the container's own available width can —
// both shift a button's offsetLeft/offsetTop.
window.addEventListener('resize', () => positionNavIndicator(true));

// ── AI disclosure tooltip ────────────────────────────────────
// Click-to-toggle rather than hover-only: hover doesn't exist on touch, and
// a single trigger mechanism that works everywhere beats hover-plus-a-
// separate-touch-fallback for a control this minor.
const aiInfoBtn = document.getElementById('ai-info-btn');
const aiInfoTooltip = document.getElementById('ai-info-tooltip');

// Below 480px the toggletip spans the full nav-heading-row instead of
// anchoring to the icon (see the CSS comment on that media query), so the
// caret can't just sit at a fixed spot — it has to track wherever the icon
// actually renders, which shifts with the heading text's rendered width.
// Harmless to compute above 480px too: the desktop caret is positioned via
// `right`, not `left`, so --caret-left has no effect there.
function positionAiCaret() {
  const row = aiInfoBtn.closest('.nav-heading-row');
  if (!row) return;
  const rowRect = row.getBoundingClientRect();
  const btnRect = aiInfoBtn.getBoundingClientRect();
  const center = btnRect.left + btnRect.width / 2 - rowRect.left;
  const clamped = Math.max(16, Math.min(center, rowRect.width - 16));
  aiInfoTooltip.style.setProperty('--caret-left', `${clamped}px`);
}

function closeAiInfo() {
  aiInfoTooltip.hidden = true;
  aiInfoBtn.setAttribute('aria-expanded', 'false');
}

function openAiInfo() {
  positionAiCaret();
  aiInfoTooltip.hidden = false;
  aiInfoBtn.setAttribute('aria-expanded', 'true');
}

aiInfoBtn.addEventListener('click', (e) => {
  e.stopPropagation();
  if (aiInfoTooltip.hidden) openAiInfo();
  else closeAiInfo();
});

document.addEventListener('click', (e) => {
  if (!aiInfoTooltip.hidden && e.target !== aiInfoBtn && !aiInfoTooltip.contains(e.target)) {
    closeAiInfo();
  }
});

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && !aiInfoTooltip.hidden) {
    closeAiInfo();
    aiInfoBtn.focus();
  }
});

// Rotating a device or resizing the window while the toggletip is open
// shifts the row's width and the icon's position within it.
window.addEventListener('resize', () => {
  if (!aiInfoTooltip.hidden) positionAiCaret();
});

// ── Flip-card overlay ───────────────────────────────────────
// Clicking a cluster/signal card flips it and grows it to fill the
// viewport. The trigger card stays in the grid (visibility: hidden, so
// layout doesn't reflow) while a clone does the animating: `.flip-card`
// owns position/size via top/left/width/height (real layout, so text
// reflows correctly at every step, not a distorted transform-scale) while
// the front label crossfades to the back content via the `.is-open`
// class. Both run on the same duration so they land together.
const overlayBackdrop = document.getElementById('card-overlay-backdrop');
const overlayPrevBtn = document.getElementById('card-overlay-prev');
const overlayNextBtn = document.getElementById('card-overlay-next');
let activeOverlay = null;

function reducedMotion() {
  return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
}

// The back face fills whatever box it's given (position: absolute; inset: 0),
// so it can't reveal its own natural content height. Render its markup into
// an offscreen probe at the target width to measure the height a centered
// panel should grow to, capped so a long roles list still scrolls internally
// instead of pushing the panel past the viewport.
function measureOverlayHeight(backInnerHTML, width) {
  const probe = document.createElement('div');
  // Padding must match .flip-card--overlay .flip-card-back exactly (see
  // styles.css) — a narrower probe wraps text less than the real render
  // does, so the estimated height comes in short.
  probe.style.cssText = `position:fixed; visibility:hidden; left:-9999px; top:0;
    width:${width}px; box-sizing:border-box; display:flex; flex-direction:column;
    align-items:flex-start; padding: var(--space-8) 88px;`;
  probe.innerHTML = backInnerHTML;
  document.body.appendChild(probe);
  const height = probe.scrollHeight;
  probe.remove();
  return height;
}

// Matches the grid's own single-column breakpoint (see .cluster-grid) —
// below it the overlay switches from a centered panel to a full-screen
// sheet with a fixed footer, driven by the same media query in styles.css.
function isMobileOverlay() {
  return window.matchMedia('(max-width: 599px)').matches;
}

// A centered panel, not an edge-to-edge sheet, so the blurred page stays
// visible around it — except on mobile, where it goes full-screen instead
// (a floating panel has too little margin to work with at that width,
// and the footer nav below needs the full viewport height to anchor to).
function computeOverlayTarget(clone) {
  if (isMobileOverlay()) {
    return { top: 0, left: 0, width: window.innerWidth, height: window.innerHeight };
  }
  const width = Math.min(680, window.innerWidth * 0.9);
  const backHTML = clone.querySelector('.flip-card-back').innerHTML;
  const contentHeight = measureOverlayHeight(backHTML, width);
  const height = Math.min(contentHeight, window.innerHeight * 0.85);
  const left = (window.innerWidth - width) / 2;
  const top = Math.max((window.innerHeight - height) / 2, 24);
  return { top, left, width, height };
}

// The nav buttons sit inset from the PANEL's own edges rather than the
// viewport's — anchoring them to the viewport instead breaks down on
// narrow screens, where the panel (up to 90vw) leaves too little margin
// for viewport-edge buttons to avoid overlapping its content. Vertically
// centered on the panel; the "next" button's column aligns with the close
// button directly above it. `right`/`top` on an absolutely-positioned
// child resolve against the containing block's *padding edge* — the
// containing block's own padding does not add a further offset on top of
// that, so the close button's true center is just 24 (its own `right`) +
// 18 (half its 36px width) in from the panel's actual right edge.
// (Previously double-counted the base card padding here too, which
// silently misaligned the chevron from the close button above it by
// exactly that amount — 24px — and let description text run underneath it.)
function positionNavButtons(target) {
  // Mobile positions them via the fixed-footer CSS instead — clear any
  // inline values a wider viewport may have set.
  if (isMobileOverlay()) {
    overlayPrevBtn.style.top = '';
    overlayPrevBtn.style.left = '';
    overlayNextBtn.style.top = '';
    overlayNextBtn.style.left = '';
    return;
  }
  const midY = target.top + target.height / 2;
  const closeCenterX = target.left + target.width - 24 - 18;
  overlayPrevBtn.style.top = `${midY}px`;
  overlayNextBtn.style.top = `${midY}px`;
  overlayPrevBtn.style.left = `${target.left + 24}px`;
  overlayNextBtn.style.left = `${closeCenterX - 22}px`;
}

function onOverlayKeydown(e) {
  if (e.key === 'Escape') closeFlipCard();
  if (e.key === 'ArrowLeft') navigateFlipCard('prev');
  if (e.key === 'ArrowRight') navigateFlipCard('next');
}

// Full key order for the active collection — clusterOrder/signalOrder are
// snapshotted at render time (see renderClusters/renderSignals), independent
// of how many of those keys the grid currently has rendered. The carousel
// reads from here rather than querying DOM `.flip-card` elements, so it can
// reach every entry even when the grid itself is still paginated ("View
// all" not yet clicked) — previously it stopped at whatever was rendered.
function overlayKeys() {
  return activeOverlay.type === 'clusters' ? clusterOrder : signalOrder;
}

// The grid tile for a key, if the grid currently has one rendered (it may
// not, past a pagination cutoff) — used only to hide/restore the underlying
// tile while its overlay is open, never to drive navigation itself.
function gridTileForKey(key) {
  return activeOverlay.container.querySelector(`.flip-card[data-key="${key}"]`);
}

function updateNavButtons() {
  const keys = overlayKeys();
  const index = keys.indexOf(activeOverlay.currentKey);
  overlayPrevBtn.disabled = index <= 0;
  overlayNextBtn.disabled = index >= keys.length - 1;
}

function openFlipCard(card) {
  if (activeOverlay) return;

  const rect = card.getBoundingClientRect();
  const lastFocused = document.activeElement;
  const container = card.closest('#cluster-grid, #signal-list');
  const type = container.id === 'cluster-grid' ? 'clusters' : 'signals';
  const key = card.dataset.key;
  const item = globalData[type][key];
  const pct = keyPercentage(globalData, key, type);

  const clone = card.cloneNode(true);
  card.style.visibility = 'hidden';
  clone.classList.add('flip-card--overlay');
  clone.removeAttribute('tabindex');
  clone.setAttribute('role', 'dialog');
  clone.setAttribute('aria-modal', 'true');
  clone.setAttribute('aria-label', `${item.label}, ${pct}% of roles`);
  clone.style.position = 'fixed';
  clone.style.margin = '0';
  clone.style.top = `${rect.top}px`;
  clone.style.left = `${rect.left}px`;
  clone.style.width = `${rect.width}px`;
  clone.style.height = `${rect.height}px`;
  document.body.appendChild(clone);

  document.querySelectorAll('.site-header, .nav-bar, main, .site-footer')
    .forEach(el => el.setAttribute('aria-hidden', 'true'));
  overlayBackdrop.hidden = false;
  overlayPrevBtn.hidden = false;
  overlayNextBtn.hidden = false;
  document.body.style.overflow = 'hidden';

  const closeBtn = clone.querySelector('.flip-card-close');
  closeBtn.addEventListener('click', closeFlipCard);

  // triggerCard is fixed for the whole overlay session — the close animation
  // always shrinks back to where it opened, regardless of how far the
  // carousel navigated (its target key may not even have a grid tile if the
  // grid is still paginated). currentKey is what actually drives the
  // carousel and the accessible name as navigation moves it.
  activeOverlay = { clone, triggerCard: card, currentKey: key, container, type, lastFocused, pendingHandler: null, navigating: false };
  updateNavButtons();

  // Force layout with the clone at the card's original rect, so the style
  // change below animates from there instead of jumping straight there.
  void clone.getBoundingClientRect();

  const finishOpen = () => {
    activeOverlay.pendingHandler = null;
    closeBtn.focus();
  };

  const target = computeOverlayTarget(clone);
  positionNavButtons(target);

  if (reducedMotion()) {
    clone.style.top = `${target.top}px`;
    clone.style.left = `${target.left}px`;
    clone.style.width = `${target.width}px`;
    clone.style.height = `${target.height}px`;
    clone.style.borderRadius = '';
    clone.classList.add('is-open');
    overlayBackdrop.classList.add('is-visible');
    finishOpen();
    return;
  }

  requestAnimationFrame(() => {
    overlayBackdrop.classList.add('is-visible');
    clone.style.top = `${target.top}px`;
    clone.style.left = `${target.left}px`;
    clone.style.width = `${target.width}px`;
    clone.style.height = `${target.height}px`;
    clone.style.borderRadius = '';
    clone.classList.add('is-open');
  });

  function onOpenEnd(e) {
    if (e.propertyName !== 'width') return;
    clone.removeEventListener('transitionend', onOpenEnd);
    finishOpen();
  }
  activeOverlay.pendingHandler = onOpenEnd;
  clone.addEventListener('transitionend', onOpenEnd);

  document.addEventListener('keydown', onOverlayKeydown);
}

// Swaps the panel's content in place (slide + fade) instead of closing and
// reopening — the flip/grow animation only ever plays once, on first open.
function navigateFlipCard(direction) {
  if (!activeOverlay || activeOverlay.navigating) return;

  const keys = overlayKeys();
  const index = keys.indexOf(activeOverlay.currentKey);
  const nextIndex = index + (direction === 'next' ? 1 : -1);
  if (nextIndex < 0 || nextIndex >= keys.length) return;

  const nextKey = keys[nextIndex];
  const { clone, type } = activeOverlay;
  const contentEl = clone.querySelector('.flip-card-back-content');
  const outClass = direction === 'next' ? 'is-sliding-out-next' : 'is-sliding-out-prev';
  const inClass = direction === 'next' ? 'is-sliding-in-from-right' : 'is-sliding-in-from-left';

  activeOverlay.navigating = true;

  const swap = () => {
    // Neither tile is guaranteed to exist — the grid may still be paginated
    // past one or both keys. Only hide/restore a tile that's actually there.
    const prevTile = gridTileForKey(activeOverlay.currentKey);
    const nextTile = gridTileForKey(nextKey);
    if (prevTile) prevTile.style.visibility = '';
    if (nextTile) nextTile.style.visibility = 'hidden';
    activeOverlay.currentKey = nextKey;

    const item = globalData[type][nextKey];
    const pct = keyPercentage(globalData, nextKey, type);
    contentEl.innerHTML = flipCardContentHtml(nextKey, type, item.label, item.description, globalData);
    clone.setAttribute('aria-label', `${item.label}, ${pct}% of roles`);

    const target = computeOverlayTarget(clone);
    clone.style.top = `${target.top}px`;
    clone.style.left = `${target.left}px`;
    clone.style.width = `${target.width}px`;
    clone.style.height = `${target.height}px`;
    positionNavButtons(target);

    updateNavButtons();
    activeOverlay.navigating = false;
  };

  if (reducedMotion()) {
    swap();
    return;
  }

  contentEl.classList.add(outClass);
  const onSlideOutEnd = (e) => {
    if (e.propertyName !== 'opacity') return;
    contentEl.removeEventListener('transitionend', onSlideOutEnd);
    swap();
    contentEl.classList.remove(outClass);
    contentEl.classList.add(inClass);
    void contentEl.getBoundingClientRect();
    requestAnimationFrame(() => contentEl.classList.remove(inClass));
  };
  contentEl.addEventListener('transitionend', onSlideOutEnd);
}

function closeFlipCard() {
  if (!activeOverlay) return;
  const { clone, triggerCard, currentKey, lastFocused, pendingHandler } = activeOverlay;
  if (pendingHandler) clone.removeEventListener('transitionend', pendingHandler);

  // Always shrinks back to the tile that opened it, not wherever the
  // carousel ended up — that key may not even have a grid tile right now.
  const rect = triggerCard.getBoundingClientRect();
  overlayBackdrop.classList.remove('is-visible');
  overlayPrevBtn.hidden = true;
  overlayNextBtn.hidden = true;
  document.removeEventListener('keydown', onOverlayKeydown);

  const currentTile = gridTileForKey(currentKey);

  const finishClose = () => {
    clone.remove();
    triggerCard.style.visibility = '';
    if (currentTile && currentTile !== triggerCard) currentTile.style.visibility = '';
    document.querySelectorAll('.site-header, .nav-bar, main, .site-footer')
      .forEach(el => el.removeAttribute('aria-hidden'));
    document.body.style.overflow = '';
    overlayBackdrop.hidden = true;
    activeOverlay = null;
    if (lastFocused && typeof lastFocused.focus === 'function') lastFocused.focus();
  };

  if (reducedMotion()) {
    finishClose();
    return;
  }

  clone.style.top = `${rect.top}px`;
  clone.style.left = `${rect.left}px`;
  clone.style.width = `${rect.width}px`;
  clone.style.height = `${rect.height}px`;
  clone.style.borderRadius = '';
  clone.classList.remove('is-open');

  function onCloseEnd(e) {
    if (e.propertyName !== 'width') return;
    clone.removeEventListener('transitionend', onCloseEnd);
    finishClose();
  }
  clone.addEventListener('transitionend', onCloseEnd);
}

overlayPrevBtn.addEventListener('click', () => navigateFlipCard('prev'));
overlayNextBtn.addEventListener('click', () => navigateFlipCard('next'));

function bindFlipCards(container) {
  container.addEventListener('click', (e) => {
    const card = e.target.closest('.flip-card');
    if (card) openFlipCard(card);
  });
  container.addEventListener('keydown', (e) => {
    if (e.key !== 'Enter' && e.key !== ' ') return;
    const card = e.target.closest('.flip-card');
    if (!card) return;
    e.preventDefault();
    openFlipCard(card);
  });
}

overlayBackdrop.addEventListener('click', closeFlipCard);
bindFlipCards(document.getElementById('cluster-grid'));
bindFlipCards(document.getElementById('signal-list'));

// Show more
const showMoreEl = document.getElementById('titles-show-more');
if (showMoreEl) {
  showMoreEl.querySelector('.show-more-btn').addEventListener('click', () => {
    showAllTitles = true;
    if (globalData) renderTitles(globalData);
  });
}

const clustersShowMoreEl = document.getElementById('clusters-show-more');
if (clustersShowMoreEl) {
  clustersShowMoreEl.querySelector('.show-more-btn').addEventListener('click', () => {
    showAllClusters = true;
    if (globalData) renderClusters(globalData);
  });
}

const signalsShowMoreEl = document.getElementById('signals-show-more');
if (signalsShowMoreEl) {
  signalsShowMoreEl.querySelector('.show-more-btn').addEventListener('click', () => {
    showAllSignals = true;
    if (globalData) renderSignals(globalData);
  });
}

// ── Init ────────────────────────────────────────────────────
async function init({ fromRetry = false } = {}) {
  renderLoading();

  const result = await loadData();

  if (result.error) {
    renderError(result.error);
    return;
  }

  globalData = result.data;
  renderMeta(globalData);
  renderClusters(globalData);
  renderTitles(globalData);
  renderSignals(globalData);
  announce(`Dataset loaded. ${globalData.entries.length} roles.`);

  // Retry destroys the button that had focus. Move focus to the panel the
  // reader was already looking at rather than dropping them back at the top.
  if (fromRetry) {
    const panel = document.querySelector('.section.active');
    if (panel) panel.focus();
  }
}

init();

// end scripts
