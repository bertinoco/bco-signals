// Site-wide hamburger menu. Loaded on every page (home and findings), so it
// touches nothing but the menu's own markup -- scripts.js holds everything
// that only exists on the home page.
(function () {
  const toggle = document.getElementById('menu-toggle');
  const menu = document.getElementById('site-menu');
  const backdrop = document.getElementById('site-menu-backdrop');
  const closeBtn = document.getElementById('site-menu-close');
  if (!toggle || !menu || !backdrop || !closeBtn) return;

  // Everything outside the drawer. Both attributes, same reasoning as the
  // flip-card overlay in scripts.js: aria-hidden alone leaves focusable
  // descendants reachable by Tab.
  const BACKGROUND_SELECTOR = '.site-header, .post-header, .hero-quote, main, .site-footer';
  let lastFocused = null;

  function reducedMotion() {
    return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  function setBackgroundInert(inert) {
    document.querySelectorAll(BACKGROUND_SELECTOR).forEach(el => {
      if (inert) el.setAttribute('aria-hidden', 'true');
      else el.removeAttribute('aria-hidden');
      el.inert = inert;
    });
  }

  function openMenu() {
    lastFocused = document.activeElement;
    menu.hidden = false;
    backdrop.hidden = false;
    // Force layout with the drawer still off-canvas, so adding .is-open
    // animates the slide instead of jumping straight to the end state.
    void menu.offsetWidth;
    menu.classList.add('is-open');
    backdrop.classList.add('is-open');
    toggle.setAttribute('aria-expanded', 'true');
    setBackgroundInert(true);
    document.body.style.overflow = 'hidden';
    document.addEventListener('keydown', onKeydown);
    closeBtn.focus();
  }

  function closeMenu() {
    if (menu.hidden) return;
    menu.classList.remove('is-open');
    backdrop.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
    setBackgroundInert(false);
    document.body.style.overflow = '';
    document.removeEventListener('keydown', onKeydown);

    const finish = () => {
      // Reopened before the slide-out finished: leave it showing.
      if (menu.classList.contains('is-open')) return;
      menu.hidden = true;
      backdrop.hidden = true;
    };
    if (reducedMotion()) finish();
    else menu.addEventListener('transitionend', finish, { once: true });

    if (lastFocused && typeof lastFocused.focus === 'function') lastFocused.focus();
  }

  function onKeydown(e) {
    if (e.key === 'Escape') closeMenu();
  }

  toggle.addEventListener('click', () => {
    if (menu.hidden) openMenu();
    else closeMenu();
  });
  closeBtn.addEventListener('click', closeMenu);
  backdrop.addEventListener('click', closeMenu);

  // A same-page link (/#signals while already on /) doesn't reload, so the
  // drawer has to close itself or it would sit open over the section it
  // just switched to.
  menu.addEventListener('click', (e) => {
    if (e.target.closest('a')) closeMenu();
  });
})();
