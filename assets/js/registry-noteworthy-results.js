(function () {
  const controls = document.getElementById("registry-noteworthy-controls");
  const grid = document.getElementById("registry-noteworthy-grid");
  if (!controls || !grid) return;

  const cards = Array.from(grid.querySelectorAll(".result-card"));
  const count = document.getElementById("registry-noteworthy-count");
  const clear = document.getElementById("registry-noteworthy-clear");
  const empty = document.getElementById("registry-noteworthy-empty");
  const emptyClear = document.getElementById("registry-noteworthy-empty-clear");
  const active = new Map();

  function applyFilters() {
    let visible = 0;
    cards.forEach((card) => {
      const matches = Array.from(active.entries()).every(([filter, value]) => {
        return card.dataset[filter] === value;
      });
      card.hidden = !matches;
      if (matches) visible += 1;
    });
    if (count) count.textContent = String(visible);
    if (empty) empty.hidden = visible !== 0;
  }

  function clearFilters() {
    active.clear();
    controls.querySelectorAll(".filter-chip.is-active").forEach((chip) => chip.classList.remove("is-active"));
    applyFilters();
  }

  controls.addEventListener("click", (event) => {
    const button = event.target.closest("[data-filter]");
    if (!button) return;
    const filter = button.dataset.filter;
    const value = button.dataset.value;
    const wasActive = button.classList.contains("is-active");
    controls
      .querySelectorAll(`[data-filter="${filter}"].is-active`)
      .forEach((chip) => chip.classList.remove("is-active"));
    if (wasActive) {
      active.delete(filter);
    } else {
      active.set(filter, value);
      button.classList.add("is-active");
    }
    applyFilters();
  });

  if (clear) clear.addEventListener("click", clearFilters);
  if (emptyClear) emptyClear.addEventListener("click", clearFilters);
  applyFilters();
})();
