// Data path for GitHub Pages with `docs/` at repo root
const DATA_PATH = 'data/jobs.json';
const SIGNAL_THRESHOLD = 2;
const TITLES_LIMIT = 12;
const FETCH_TIMEOUT_MS = 10000;
// Currency the dataset's ranges are read against. Scope qualifiers are only
// shown for ranges in it — see renderTitles.
const BASELINE_CURRENCY = 'USD';
const SECTION_CONTAINERS = ['cluster-grid', 'signal-list', 'title-list'];
let showAllTitles = false;
let globalData = null;

// ── Copy ────────────────────────────────────────────────────
// All loading, empty, and error copy lives here. See copy-patterns.md
// for the rules these strings follow and why each one is worded this way.
const COPY = {
  loading: {
    title: 'Loading the dataset…',
  },
  empty: {
    clusters: {
      title: 'No responsibilities yet.',
      body: 'Responsibilities appear here once the first job description is audited into the dataset.',
    },
    signals: {
      title: 'No skills have crossed the threshold yet.',
      body: `Skills appear here once ${SIGNAL_THRESHOLD} or more postings ask for them. One posting is an anecdote.`,
    },
    titles: {
      title: 'No roles yet.',
      body: 'Roles appear here as job descriptions are audited into the dataset.',
    },
  },
  error: {
    offline: {
      title: "You're offline.",
      body: 'Reconnect and try again.',
      retry: true,
    },
    network: {
      title: "The dataset didn't load.",
      body: 'This is on our end. Try again, or come back in a few minutes.',
      retry: true,
    },
    timeout: {
      title: 'The dataset is taking too long.',
      body: 'The request timed out before the file came back. Try again.',
      retry: true,
    },
    malformed: {
      title: "The dataset loaded, but we couldn't read it.",
      body: 'Retrying won\'t fix this one. Email <a href="mailto:joe@bertino.co">joe@bertino.co</a> and we\'ll take a look.',
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
  if (!dateEl) return;
  const iso = data.meta && data.meta.lastUpdated;
  // No date in the payload: keep the value rendered in the HTML rather than
  // replacing it with a blank.
  if (!iso) return;
  // ISO, matching the dateAdded format on role cards.
  dateEl.innerHTML = `<time datetime="${iso}">${iso}</time>`;
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

  grid.innerHTML = clusterKeys.map(key => {
    const cluster = data.clusters[key];
    return `
      <div class="cluster-card">
        <h3>${cluster.label}</h3>
        <p class="cluster-desc">${cluster.description}</p>
      </div>
    `;
  }).join('');
}

function formatDate(iso) {
  return iso;
}

// Titles are stored verbatim, so they arrive with whatever separator the
// employer used — em dash, pipe or slash all appear in the dataset. Displaying
// them as-is makes the list look inconsistent rather than faithful, so the
// separator is normalised to a comma at render time. Only spaced separators
// match; hyphenated compounds like "AI-Powered" are left alone. jobs.json keeps
// the verbatim title, which is what ties an entry to its jd-source archive.
function formatTitle(title) {
  return title.replace(/\s+[-—–|/]\s+/g, ', ');
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
      showMoreBtn.textContent = `View all ${data.entries.length} job descriptions`;
    } else {
      showMore.style.display = 'none';
    }
  }

  list.innerHTML = entries.map(entry => {
    const fmt = (n) => '$' + n.toLocaleString('en-US');

    // Qualifiers are read from structured fields, never parsed out of prose.
    //
    // `covers: "total"` is shown because a total-comp figure is not comparable
    // to the base ranges around it. `covers: "base"` and `covers: null` show
    // nothing, since neither can claim more than the bare number does.
    //
    // `scope` is a comparability caveat — it explains why a range differs from
    // the others around it — so it only helps when the range is comparable in
    // the first place. Outside the baseline currency it is suppressed: CAD
    // already tells the reader this is a different market, and naming the city
    // adds nothing on top.
    //
    // `extras`, what sits on top of the range, is never rendered. All three
    // fields stay in jobs.json regardless of what displays.
    const c = entry.compRange;
    const showScope = !!c && c.currency === BASELINE_CURRENCY;
    const qualifiers = c
      ? [c.covers === 'total' ? 'total comp' : null, showScope ? c.scope : null].filter(Boolean)
      : [];
    const compHtml = c
      ? `<span class="title-comp">${fmt(c.min)}–${fmt(c.max)} ${c.currency}`
        + qualifiers.map(q => ` · ${q}`).join('')
        + `</span>`
      : '';
    const hasQuote = !!entry.quote;
    const quoteHtml = hasQuote
      ? `<div class="title-quote"><blockquote>${entry.quote}</blockquote></div>`
      : '';
    const expandBtn = hasQuote
      ? `<button class="title-expand" aria-expanded="false" aria-label="Show quote">+</button>`
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
      <div class="title-entry${hasQuote ? ' has-quote' : ''}">
        <div class="title-header">
          <div class="title-name">${formatTitle(entry.title)}</div>
          ${expandBtn}
        </div>
        ${attribHtml}
        ${dateHtml}
        ${quoteHtml}
      </div>
    `;
  }).join('');

  // Expand/collapse on click
  list.querySelectorAll('.title-expand').forEach(btn => {
    btn.addEventListener('click', () => {
      const entry = btn.closest('.title-entry');
      const isOpen = entry.classList.toggle('is-expanded');
      btn.setAttribute('aria-expanded', String(isOpen));
      btn.textContent = isOpen ? '−' : '+';
      btn.blur();
    });
  });
}

function renderSignals(data) {
  const list = document.getElementById('signal-list');
  const signalKeys = Object.keys(data.signals);

  const signalMap = {};
  signalKeys.forEach(key => { signalMap[key] = []; });

  data.entries.forEach(entry => {
    entry.signals.forEach(s => {
      if (signalMap[s]) signalMap[s].push(entry.company);
      else console.warn('Unknown signal key in entry:', s);
    });
  });

  // Sort by number of companies, descending. Filter to signals with SIGNAL_THRESHOLD+ entries.
  const relevantSignals = signalKeys
    .filter(key => signalMap[key].length >= SIGNAL_THRESHOLD)
    .sort((a, b) => signalMap[b].length - signalMap[a].length);

  if (relevantSignals.length === 0) {
    renderState('signal-list', { variant: 'empty', ...COPY.empty.signals });
    return;
  }

  list.innerHTML = relevantSignals.map(key => {
    const signal = data.signals[key];
    return `
      <div class="signal-card">
        <div class="signal-label">${signal.label}</div>
        <p class="signal-desc">${signal.description}</p>
      </div>
    `;
  }).join('');
}

function renderNavCounts(data) {
  const signalCount = Object.keys(data.signals).filter(key => {
    return data.entries.filter(e => e.signals.includes(key)).length >= SIGNAL_THRESHOLD;
  }).length;

  const counts = {
    clusters: Object.keys(data.clusters).length,
    signals: signalCount,
    titles: data.entries.length,
  };

  document.querySelectorAll('.badge-btn').forEach(btn => {
    // Retry re-renders the nav; clear any count from the previous pass.
    const existing = btn.querySelector('.badge-count');
    if (existing) existing.remove();

    const count = counts[btn.dataset.section];
    if (count === undefined) return;
    const span = document.createElement('span');
    span.className = 'badge-count';
    span.textContent = count;
    btn.insertBefore(span, btn.firstChild);
  });
}

// ── Badge nav (click + arrow keys) ──────────────────────────
const badges = Array.from(document.querySelectorAll('.badge-btn'));
const badgeNav = document.querySelector('.badge-nav');

function activateBadge(badge) {
  badges.forEach(b => {
    b.classList.remove('active');
    b.setAttribute('aria-selected', 'false');
  });
  document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
  badge.classList.add('active');
  badge.setAttribute('aria-selected', 'true');
  document.getElementById(badge.dataset.section).classList.add('active');
  badge.blur();
}

badges.forEach(badge => {
  badge.addEventListener('click', () => activateBadge(badge));
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

// Show more
const showMoreEl = document.getElementById('titles-show-more');
if (showMoreEl) {
  showMoreEl.querySelector('.show-more-btn').addEventListener('click', () => {
    showAllTitles = true;
    if (globalData) renderTitles(globalData);
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
  renderNavCounts(globalData);
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
