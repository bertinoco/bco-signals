// Data path for GitHub Pages with `docs/` at repo root
const DATA_PATH = 'data/jobs.json';
const SIGNAL_THRESHOLD = 2;
const TITLES_LIMIT = 12;
let showAllTitles = false;
let globalData = null;

async function loadData() {
  try {
    const res = await fetch(DATA_PATH);
    if (!res.ok) throw new Error('Failed to load data');
    return await res.json();
  } catch (err) {
    console.error(err);
    return null;
  }
}

function renderMeta(data) {
  const dateEl = document.getElementById('footer-date');
  dateEl.textContent = data.meta.lastUpdated;
}

function renderClusters(data) {
  const grid = document.getElementById('cluster-grid');
  const clusterKeys = Object.keys(data.clusters);

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
    const count = [...new Set(clusterMap[key])].length;
    return `
      <div class="cluster-card">
        <h3>${cluster.label}</h3>
        <p class="cluster-desc">${cluster.description}</p>
      </div>
    `;
  }).join('');
}

function formatDate(iso) {
  const [y, m, d] = iso.split('-').map(Number);
  return new Date(y, m - 1, d).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
}

function renderTitles(data) {
  const list = document.getElementById('title-list');
  const showMore = document.getElementById('titles-show-more');
  const showMoreBtn = showMore ? showMore.querySelector('.show-more-btn') : null;
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
    const compHtml = entry.compRange
      ? `<div class="title-comp">${fmt(entry.compRange.min)}–${fmt(entry.compRange.max)} ${entry.compRange.currency}${entry.compRange.note ? ' ' + entry.compRange.note : ''}</div>`
      : '';
    const noteHtml = '';
    const hasQuote = !!entry.quote;
    const quoteHtml = hasQuote
      ? `<div class="title-quote"><blockquote>${entry.quote}</blockquote></div>`
      : '';
    const expandBtn = hasQuote
      ? `<button class="title-expand" aria-expanded="false" aria-label="Show quote">+</button>`
      : '';
    const dateHtml = entry.dateAdded
      ? `<div class="title-domain">${formatDate(entry.dateAdded)}</div>`
      : '';

    return `
      <div class="title-entry${hasQuote ? ' has-quote' : ''}">
        <div class="title-meta">
          <div class="title-company">${entry.company}</div>
          <div class="title-domain">${entry.domain}</div>
          ${dateHtml}
        </div>
        <div class="title-body">
          <div class="title-header">
            <div class="title-name">${entry.title}</div>
            ${expandBtn}
          </div>
          ${compHtml}
          ${noteHtml}
          ${quoteHtml}
        </div>
      </div>
    `;
  }).join('');

  // Expand/collapse on click
  list.querySelectorAll('.title-expand').forEach(btn => {
    btn.addEventListener('click', () => {
      const entry = btn.closest('.title-entry');
      const isOpen = entry.classList.toggle('is-expanded');
      btn.setAttribute('aria-expanded', String(isOpen));
      btn.textContent = isOpen ? '×' : '+';
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

  list.innerHTML = relevantSignals.map(key => {
    const signal = data.signals[key];
    const count = [...new Set(signalMap[key])].length;
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

// Init
loadData().then(data => {
  if (!data) {
    const ids = ['cluster-grid', 'title-list', 'signal-list'];
    ids.forEach(id => {
      const el = document.getElementById(id);
      if (el) el.innerHTML = `<p class="loading">Failed to load data. Confirm <code>data/jobs.json</code> exists and you're serving the site from a local or remote HTTP server.</p>`;
    });
    return;
  }
  globalData = data;
  renderMeta(data);
  renderNavCounts(data);
  renderClusters(data);
  renderTitles(data);
  renderSignals(data);
});

// end scripts
