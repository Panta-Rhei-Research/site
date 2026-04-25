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
    note_type: new Set(),
    domain: new Set(),
    status: new Set(),
    relation: new Set()
  };

  function readStateFromUrl() {
    var params = new URLSearchParams(window.location.search);
    Object.keys(state).forEach(function (key) {
      state[key].clear();
      var raw = params.get(key);
      if (raw) {
        raw.split(',').forEach(function (value) {
          if (value) state[key].add(value);
        });
      }
    });
  }

  function writeStateToUrl() {
    var params = new URLSearchParams();
    Object.keys(state).forEach(function (key) {
      if (state[key].size > 0) params.set(key, Array.from(state[key]).join(','));
    });
    var query = params.toString();
    window.history.replaceState(null, '', window.location.pathname + (query ? '?' + query : ''));
  }

  function matchesSet(set, value) {
    return set.size === 0 || set.has(value);
  }

  function matchesList(set, rawValue) {
    if (set.size === 0) return true;
    var values = (rawValue || '').split(',').filter(Boolean);
    for (var i = 0; i < values.length; i += 1) {
      if (set.has(values[i])) return true;
    }
    return false;
  }

  function matchesFilters(card) {
    if (!matchesSet(state.note_type, card.dataset.noteType)) return false;
    if (!matchesSet(state.domain, card.dataset.domain)) return false;
    if (!matchesSet(state.status, card.dataset.status)) return false;
    if (!matchesList(state.relation, card.dataset.relations)) return false;
    return true;
  }

  function applyFilters() {
    var visible = 0;
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
      var value = button.dataset.value;
      if (state[filter] && state[filter].has(value)) {
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
    var filter = button.dataset.filter;
    var value = button.dataset.value;
    if (!state[filter]) return;
    if (state[filter].has(value)) state[filter].delete(value);
    else state[filter].add(value);
    refresh();
  });

  function clearAll() {
    Object.keys(state).forEach(function (key) {
      state[key].clear();
    });
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
