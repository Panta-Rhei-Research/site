// Research Notes filters — static-first progressive enhancement.
(function () {
  'use strict';

  var controls = document.getElementById('research-notes-controls');
  var grid = document.getElementById('research-notes-grid');
  if (!controls || !grid) return;

  var cards = Array.prototype.slice.call(grid.querySelectorAll('.research-note-card'));
  var countEl = document.getElementById('research-notes-count');
  var emptyEl = document.getElementById('research-notes-empty');
  var clearBtn = document.getElementById('research-notes-clear-filters');
  var emptyClearBtn = document.getElementById('research-notes-empty-clear');

  var state = {
    domain: 'all',
    sort: 'date-desc'
  };

  function readStateFromUrl() {
    var params = new URLSearchParams(window.location.search);
    state.domain = params.get('domain') || 'all';
    state.sort = params.get('sort') || 'date-desc';
  }

  function writeStateToUrl() {
    var params = new URLSearchParams();
    if (state.domain && state.domain !== 'all') params.set('domain', state.domain);
    if (state.sort && state.sort !== 'date-desc') params.set('sort', state.sort);
    var query = params.toString();
    window.history.replaceState(null, '', window.location.pathname + (query ? '?' + query : ''));
  }

  function matchesFilters(card) {
    if (state.domain !== 'all' && card.dataset.domain !== state.domain) return false;
    return true;
  }

  function compareCards(a, b) {
    if (state.sort === 'date-asc') {
      return (a.dataset.date || '').localeCompare(b.dataset.date || '');
    }
    if (state.sort === 'title-asc') {
      return (a.dataset.title || '').localeCompare(b.dataset.title || '');
    }
    return (b.dataset.date || '').localeCompare(a.dataset.date || '');
  }

  function applyFilters() {
    var visible = 0;
    cards.sort(compareCards).forEach(function (card) {
      grid.appendChild(card);
    });
    cards.forEach(function (card) {
      if (matchesFilters(card)) {
        card.removeAttribute('hidden');
        visible += 1;
      } else {
        card.setAttribute('hidden', '');
      }
    });
    if (countEl) countEl.textContent = visible;
    if (emptyEl) emptyEl.hidden = visible > 0;
  }

  function syncChipStates() {
    controls.querySelectorAll('.filter-chip').forEach(function (button) {
      var filter = button.dataset.filter;
      var isActive = false;
      if (filter === 'domain') isActive = button.dataset.value === state.domain;
      if (button.dataset.sort) isActive = button.dataset.sort === state.sort;
      if (isActive) {
        button.classList.add('is-active');
        button.setAttribute('aria-pressed', 'true');
      } else {
        button.classList.remove('is-active');
        button.setAttribute('aria-pressed', 'false');
      }
    });
  }

  function refresh() {
    syncChipStates();
    applyFilters();
    writeStateToUrl();
  }

  controls.addEventListener('click', function (event) {
    var button = event.target.closest('.filter-chip');
    if (!button) return;
    event.preventDefault();
    if (button.dataset.filter === 'domain') state.domain = button.dataset.value || 'all';
    if (button.dataset.sort) state.sort = button.dataset.sort;
    refresh();
  });

  function clearAll() {
    state.domain = 'all';
    state.sort = 'date-desc';
    refresh();
  }

  if (clearBtn) clearBtn.addEventListener('click', clearAll);
  if (emptyClearBtn) emptyClearBtn.addEventListener('click', clearAll);
  window.addEventListener('popstate', function () {
    readStateFromUrl();
    refresh();
  });

  readStateFromUrl();
  refresh();
})();
