(function () {
  function byId(list) {
    return list.reduce(function (acc, item) {
      acc[item.id] = item;
      return acc;
    }, {});
  }

  function linkFor(item) {
    if (!item) return "";
    return '<a href="' + item.url + '">' + item.id + " · " + item.name + "</a>";
  }

  function ready(fn) {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", fn);
    } else {
      fn();
    }
  }

  ready(function () {
    var root = document.getElementById("registry-graph-explorer");
    if (!root) return;
    var input = document.getElementById("registry-graph-search");
    var select = document.getElementById("registry-graph-select");
    var output = document.getElementById("registry-graph-output");
    if (!input || !select || !output) return;

    Promise.all([
      fetch("/assets/data/registry/objects.json").then(function (res) { return res.json(); }).catch(function () { return []; }),
      fetch("/assets/data/registry/adjacency.json").then(function (res) { return res.json(); }).catch(function () { return {}; }),
      fetch("/assets/data/registry/reverse-adjacency.json").then(function (res) { return res.json(); }).catch(function () { return {}; }),
      fetch("/assets/data/taulib/registry-links.json").then(function (res) { return res.json(); }).catch(function () { return []; })
    ]).then(function (data) {
      var objects = data[0];
      var adjacency = data[1];
      var reverse = data[2];
      var taulibLinks = data[3];
      var objectsById = byId(objects);
      var modulesByRegistry = taulibLinks.reduce(function (acc, link) {
        if (!acc[link.registry_id]) acc[link.registry_id] = [];
        acc[link.registry_id].push(link);
        return acc;
      }, {});

      objects.slice(0, 600).forEach(function (item) {
        var option = document.createElement("option");
        option.value = item.id;
        option.textContent = item.id + " · " + item.name;
        select.appendChild(option);
      });

      function render(id) {
        var item = objectsById[id];
        if (!item) {
          output.innerHTML = "<p>Select a Registry object to inspect its neighborhood.</p>";
          return;
        }
        var upstream = (adjacency[id] || []).map(function (dep) { return "<li>" + linkFor(objectsById[dep]) + "</li>"; }).join("") || "<li>No upstream dependencies declared.</li>";
        var downstream = (reverse[id] || []).map(function (dep) { return "<li>" + linkFor(objectsById[dep]) + "</li>"; }).join("") || "<li>No downstream uses declared.</li>";
        var modules = (modulesByRegistry[id] || []).map(function (link) {
          var url = link.corpus_url || link.verify_url || "#";
          return '<li><a href="' + url + '">' + link.module + "</a></li>";
        }).join("") || "<li>No TauLib module mapped.</li>";
        output.innerHTML =
          '<article class="v2-tile graph-detail">' +
          "<h3>" + item.id + " · " + item.name + "</h3>" +
          "<p>" + item.type + " · Book " + item.book + " · " + item.scope + " · " + item.formalization + "</p>" +
          '<p><a class="btn-secondary" href="' + item.url + '">Open Registry object</a></p>' +
          "<h4>Upstream dependencies</h4><ul>" + upstream + "</ul>" +
          "<h4>Downstream uses</h4><ul>" + downstream + "</ul>" +
          "<h4>TauLib modules</h4><ul>" + modules + "</ul>" +
          "</article>";
      }

      function syncFromSearch() {
        var term = input.value.trim().toLowerCase();
        var match = objects.find(function (item) {
          return item.id.toLowerCase() === term || item.name.toLowerCase().indexOf(term) !== -1;
        });
        if (match) {
          select.value = match.id;
          render(match.id);
        }
      }

      select.addEventListener("change", function () { render(select.value); });
      input.addEventListener("input", syncFromSearch);
      render(select.value || "I.D01");
    });
  });
})();
