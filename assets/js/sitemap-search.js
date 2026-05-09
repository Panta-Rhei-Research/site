// Sitemap v4 — client-side instant search + jump-nav scroll-spy.
// Static-first progressive enhancement: page is fully usable without this script.
(function () {
  'use strict';

  var input = document.getElementById('sitemap-search-input');
  var clearBtn = document.getElementById('sitemap-search-clear');
  var statusEl = document.getElementById('sitemap-search-status');
  var emptyEl = document.getElementById('sitemap-empty');
  var jumpNav = document.querySelector('.sitemap-jump');
  if (!input || !statusEl) return;

  var laneCards = Array.prototype.slice.call(
    document.querySelectorAll('.sitemap-card[data-sitemap-lane]')
  );
  var miniCards = Array.prototype.slice.call(
    document.querySelectorAll('.sitemap-mini-card[data-sitemap-link-title]')
  );
  var totalLinks = miniCards.length;

  // Initialize default status text from data-default-text.
  var defaultStatus = statusEl.getAttribute('data-default-text') || '';

  function setStatus(html) {
    if (!html) {
      statusEl.innerHTML = '';
      // Fallback to default text via :empty::before in CSS
      return;
    }
    statusEl.innerHTML = html;
  }

  function escapeHtml(str) {
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function applyFilter(query) {
    var q = (query || '').trim().toLowerCase();
    var matches = 0;

    if (!q) {
      // Clear filter — show all
      miniCards.forEach(function (card) { card.removeAttribute('hidden'); });
      laneCards.forEach(function (lane) { lane.removeAttribute('hidden'); });
      emptyEl.setAttribute('hidden', '');
      setStatus('');
      clearBtn.setAttribute('hidden', '');
      return;
    }

    // Per-mini-card substring match against data-sitemap-link-title
    miniCards.forEach(function (card) {
      var title = card.getAttribute('data-sitemap-link-title') || '';
      if (title.indexOf(q) !== -1) {
        card.removeAttribute('hidden');
        matches += 1;
      } else {
        card.setAttribute('hidden', '');
      }
    });

    // Hide whole lane cards that have zero visible mini-cards
    laneCards.forEach(function (lane) {
      var anyVisible = lane.querySelector('.sitemap-mini-card:not([hidden])');
      if (anyVisible) {
        lane.removeAttribute('hidden');
      } else {
        lane.setAttribute('hidden', '');
      }
    });

    if (matches === 0) {
      emptyEl.removeAttribute('hidden');
      setStatus('No pages match <strong>' + escapeHtml(q) + '</strong>.');
    } else {
      emptyEl.setAttribute('hidden', '');
      setStatus(
        '<strong>' + matches + '</strong> of ' + totalLinks +
        ' pages match <strong>' + escapeHtml(q) + '</strong>.'
      );
    }
    clearBtn.removeAttribute('hidden');
  }

  // Debounced input handler
  var debounceTimer = null;
  function onInput() {
    if (debounceTimer) clearTimeout(debounceTimer);
    debounceTimer = setTimeout(function () {
      var q = input.value;
      applyFilter(q);
      updateUrlState(q);
    }, 80);
  }

  // URL state — preserve filter via ?q=
  function updateUrlState(q) {
    if (!window.history || !window.history.replaceState) return;
    var url = new URL(window.location.href);
    if (q && q.trim()) {
      url.searchParams.set('q', q.trim());
    } else {
      url.searchParams.delete('q');
    }
    window.history.replaceState({}, '', url.toString());
  }

  // Read initial state from URL
  function readInitialState() {
    var url = new URL(window.location.href);
    var q = url.searchParams.get('q');
    if (q) {
      input.value = q;
      applyFilter(q);
    }
  }

  // Clear button
  clearBtn.addEventListener('click', function () {
    input.value = '';
    applyFilter('');
    updateUrlState('');
    input.focus();
  });

  // Empty-state suggestion buttons
  document.querySelectorAll('.sitemap-empty-suggestion').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var suggestion = btn.getAttribute('data-search-suggestion') || '';
      input.value = suggestion;
      applyFilter(suggestion);
      updateUrlState(suggestion);
      input.focus();
    });
  });

  // Keyboard shortcuts
  document.addEventListener('keydown', function (e) {
    // Don't intercept when user is typing in an input/textarea
    var tag = (e.target.tagName || '').toLowerCase();
    if (tag === 'input' || tag === 'textarea' || e.target.isContentEditable) {
      // Allow Esc inside the search input itself to clear
      if (e.key === 'Escape' && e.target === input) {
        if (input.value) {
          input.value = '';
          applyFilter('');
          updateUrlState('');
        } else {
          input.blur();
        }
        e.preventDefault();
      }
      return;
    }
    if (e.key === '/' && !e.metaKey && !e.ctrlKey && !e.altKey) {
      e.preventDefault();
      input.focus();
      input.select();
    }
  });

  input.addEventListener('input', onInput);

  // ----- Jump-nav scroll-spy -----
  if (jumpNav && 'IntersectionObserver' in window) {
    var pills = Array.prototype.slice.call(
      jumpNav.querySelectorAll('.sitemap-jump-pill[data-jump-target]')
    );
    var pillByTarget = {};
    pills.forEach(function (p) {
      pillByTarget[p.getAttribute('data-jump-target')] = p;
    });

    function setActive(targetId) {
      pills.forEach(function (p) {
        if (p.getAttribute('data-jump-target') === targetId) {
          p.classList.add('is-active');
        } else {
          p.classList.remove('is-active');
        }
      });
    }

    var observer = new IntersectionObserver(
      function (entries) {
        // Pick the topmost intersecting card
        var visible = entries
          .filter(function (e) { return e.isIntersecting; })
          .sort(function (a, b) { return a.boundingClientRect.top - b.boundingClientRect.top; });
        if (visible.length > 0) {
          var id = visible[0].target.id;
          if (pillByTarget[id]) setActive(id);
        }
      },
      {
        // Trigger when the card is in the upper third of the viewport (below sticky search)
        rootMargin: '-160px 0px -55% 0px',
        threshold: 0,
      }
    );
    laneCards.forEach(function (lane) {
      if (lane.id) observer.observe(lane);
    });
  }

  // Init
  readInitialState();
})();
