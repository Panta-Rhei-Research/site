import assert from "node:assert/strict";
import worker, { shortRouteTarget } from "../workers/prrp-short-routes.js";

const expectedRoutes = new Map([
  ["https://prrp.site/", "https://panta-rhei.site/"],
  ["https://prrp.site/wp000", "https://panta-rhei.site/publications/anchor-documents/wp000-panta-rhei-at-a-glance/"],
  ["https://prrp.site/wp-glance", "https://panta-rhei.site/publications/anchor-documents/wp000-panta-rhei-at-a-glance/"],
  ["https://prrp.site/c001", "https://panta-rhei.site/program/about/standing-in-the-inquiry-of-being/"],
  ["https://prrp.site/wp001", "https://panta-rhei.site/publications/anchor-documents/wp001-panta-rhei-research-program-executive-overview/"],
  ["https://prrp.site/wp002", "https://panta-rhei.site/publications/anchor-documents/wp002-t-theory-executive-synopsis/"],
  ["https://prrp.site/wp-theory", "https://panta-rhei.site/publications/anchor-documents/wp002-t-theory-executive-synopsis/"],
  ["https://prrp.site/wp003", "https://panta-rhei.site/publications/anchor-documents/wp003-taulib-technical-overview/"],
  ["https://prrp.site/wp-taulib", "https://panta-rhei.site/publications/anchor-documents/wp003-taulib-technical-overview/"],
  ["https://prrp.site/wp004", "https://panta-rhei.site/publications/anchor-documents/wp004-public-research-observatory-blueprint/"],
  ["https://prrp.site/wp-observatory", "https://panta-rhei.site/publications/anchor-documents/wp004-public-research-observatory-blueprint/"],
  ["https://prrp.site/wp005", "https://panta-rhei.site/publications/anchor-documents/wp005-global-public-good-impact-overview/"],
  ["https://prrp.site/wp-impact", "https://panta-rhei.site/publications/anchor-documents/wp005-global-public-good-impact-overview/"],
  ["https://prrp.site/30-questions", "https://panta-rhei.site/publications/research-notes/thirty-open-problems-tau-readout-surfaces/"],
  ["https://prrp.site/anchor-documents", "https://panta-rhei.site/publications/anchor-documents/"]
]);

for (const [source, target] of expectedRoutes) {
  assert.equal(shortRouteTarget(source), target);
  assert.equal(shortRouteTarget(`${source}/`), target);
}

assert.equal(
  shortRouteTarget("https://prrp.site/wp000?utm_source=test"),
  "https://panta-rhei.site/publications/anchor-documents/wp000-panta-rhei-at-a-glance/?utm_source=test"
);
assert.equal(shortRouteTarget("https://prrp.site/not-a-route"), null);

const response = await worker.fetch(new Request("https://prrp.site/wp004"));
assert.equal(response.status, 301);
assert.equal(
  response.headers.get("Location"),
  "https://panta-rhei.site/publications/anchor-documents/wp004-public-research-observatory-blueprint/"
);

const missing = await worker.fetch(new Request("https://prrp.site/not-a-route"));
assert.equal(missing.status, 404);
