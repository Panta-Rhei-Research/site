import assert from "node:assert/strict";
import worker, { ROUTE_ENTRIES, shortRouteTarget } from "../workers/prrp-short-routes.js";

const expectedRoutes = new Map(ROUTE_ENTRIES);

assert.equal(expectedRoutes.size, ROUTE_ENTRIES.length, "short routes must be unique");
assert(expectedRoutes.size >= 280, "route table should include publication and 100-step routes");

for (const [source, target] of expectedRoutes) {
  assert.equal(shortRouteTarget(`https://prrp.site${source}`), target);
  if (source !== "/") {
    assert.equal(shortRouteTarget(`https://prrp.site${source}/`), target);
  }
}

const samples = new Map([
  ["https://prrp.site/", "https://panta-rhei.site/"],
  ["https://prrp.site/wp000", "https://panta-rhei.site/publications/anchor-documents/wp000-panta-rhei-at-a-glance/"],
  ["https://prrp.site/rn007", "https://panta-rhei.site/publications/research-notes/aesthetic-topology-pre-symbolic-readout/"],
  ["https://prrp.site/rp005", "https://panta-rhei.site/publications/research-papers/tau-holomorphy-boundary-algebra/"],
  ["https://prrp.site/pgd044", "https://panta-rhei.site/publications/research-briefings/public-good/wildfire-smoke-heat-compound-extreme-health-protection/"],
  ["https://prrp.site/s1", "https://panta-rhei.site/corpus/construction-spine/steps/001-non-import-discipline/"],
  ["https://prrp.site/s001", "https://panta-rhei.site/corpus/construction-spine/steps/001-non-import-discipline/"],
  ["https://prrp.site/s64", "https://panta-rhei.site/corpus/construction-spine/steps/064-tau-einstein-identity/"],
  ["https://prrp.site/s100", "https://panta-rhei.site/corpus/construction-spine/steps/100-logos-boundary-and-ontic-closure-burden/"]
]);

for (const [source, target] of samples) {
  assert.equal(shortRouteTarget(source), target);
}

assert.equal(
  shortRouteTarget("https://prrp.site/wp000?utm_source=test"),
  "https://panta-rhei.site/publications/anchor-documents/wp000-panta-rhei-at-a-glance/?utm_source=test"
);
assert.equal(shortRouteTarget("https://prrp.site/not-a-route"), null);

const response = await worker.fetch(new Request("https://prrp.site/rn007"));
assert.equal(response.status, 301);
assert.equal(
  response.headers.get("Location"),
  "https://panta-rhei.site/publications/research-notes/aesthetic-topology-pre-symbolic-readout/"
);

const missing = await worker.fetch(new Request("https://prrp.site/not-a-route"));
assert.equal(missing.status, 404);
