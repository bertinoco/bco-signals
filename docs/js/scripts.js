// Data path for GitHub Pages with `docs/` at repo root
const DATA_PATH = 'data/jobs.json';
const SIGNAL_THRESHOLD = 2; // show signals with at least this many entries

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
  const el = document.getElementById('meta-line');
  const dateEl = document.getElementById('footer-date');
  const clusterCount = Object.keys(data.clusters).length;
  const signalCount = Object.keys(data.signals).length;
  el.innerHTML = `<span>${data.meta.totalEntries} roles</span><span>${clusterCount} responsibilities</span><span>${signalCount} skills</span>`;
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

function renderTitles(data) {
  const list = document.getElementById('title-list');

  list.innerHTML = data.entries.map(entry => {
    const fmt = (n) => '$' + n.toLocaleString('en-US');
    const compHtml = entry.compRange
      ? `<div class="title-comp">${fmt(entry.compRange.min)}–${fmt(entry.compRange.max)} ${entry.compRange.currency}${entry.compRange.note ? ' ' + entry.compRange.note : ''}</div>`
      : '';
    const noteHtml = entry.note ? `<div class="title-note">${entry.note}</div>` : '';
    const hasQuote = !!entry.quote;
    const quoteHtml = hasQuote
      ? `<div class="title-quote"><blockquote>${entry.quote}</blockquote></div>`
      : '';
    const expandBtn = hasQuote
      ? `<button class="title-expand" aria-expanded="false" aria-label="Show quote">+</button>`
      : '';

    return `
      <div class="title-entry${hasQuote ? ' has-quote' : ''}">
        <div class="title-meta">
          <div class="title-company">${entry.company}</div>
          <div class="title-domain">${entry.domain}</div>
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

// Accessible tab behavior (click + arrow keys)
const tabs = Array.from(document.querySelectorAll('.tab'));
const tablist = document.querySelector('.tabs');

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    tabs.forEach(t => {
      t.classList.remove('active');
      t.setAttribute('aria-selected', 'false');
    });
    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));

    tab.classList.add('active');
    tab.setAttribute('aria-selected', 'true');
    document.getElementById(tab.dataset.section).classList.add('active');
  });
});

tablist.addEventListener('keydown', (e) => {
  if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
  e.preventDefault();
  const idx = tabs.indexOf(document.activeElement);
  let next = idx;
  if (e.key === 'ArrowRight') next = (idx + 1) % tabs.length;
  if (e.key === 'ArrowLeft') next = (idx - 1 + tabs.length) % tabs.length;
  tabs[next].focus();
  tabs[next].click();
});

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
  renderMeta(data);
  renderClusters(data);
  renderTitles(data);
  renderSignals(data);
});

// end scripts
