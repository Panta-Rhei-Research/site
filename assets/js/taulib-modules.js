(function () {
  function norm(value) {
    return (value || "").toString().trim().toLowerCase();
  }

  function ready(fn) {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", fn);
    } else {
      fn();
    }
  }

  ready(function () {
    var root = document.getElementById("taulib-module-explorer");
    if (!root) return;

    var book = document.getElementById("taulib-book-filter");
    var family = document.getElementById("taulib-family-filter");
    var registry = document.getElementById("taulib-registry-filter");
    var search = document.getElementById("taulib-search-filter");
    var clear = document.getElementById("taulib-clear-filters");
    var count = document.getElementById("taulib-module-count");
    var cards = Array.prototype.slice.call(root.querySelectorAll(".module-card"));

    function apply() {
      var bookValue = norm(book && book.value);
      var familyValue = norm(family && family.value);
      var registryValue = norm(registry && registry.value);
      var searchValue = norm(search && search.value);
      var visible = 0;

      cards.forEach(function (card) {
        var ok = true;
        if (bookValue && norm(card.dataset.book) !== bookValue) ok = false;
        if (familyValue && norm(card.dataset.family).indexOf(familyValue) === -1) ok = false;
        if (registryValue && norm(card.dataset.registry).indexOf(registryValue) === -1) ok = false;
        if (searchValue && norm(card.dataset.module).indexOf(searchValue) === -1) ok = false;
        card.hidden = !ok;
        if (ok) visible += 1;
      });

      if (count) count.textContent = visible + " of " + cards.length + " modules";
    }

    [book, family, registry, search].forEach(function (control) {
      if (control) control.addEventListener("input", apply);
      if (control) control.addEventListener("change", apply);
    });
    if (clear) {
      clear.addEventListener("click", function () {
        [book, family, registry, search].forEach(function (control) {
          if (control) control.value = "";
        });
        apply();
      });
    }
    apply();
  });
})();
