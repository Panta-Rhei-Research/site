import assert from "node:assert/strict";
import {
  applyEdgeHeaders,
  corsPreflightResponse,
  edgeRedirectFor,
  fetchOptionsFor,
  originRequestFor
} from "../workers/site-edge-headers.js";

const SECURITY_EXPECTATIONS = {
  "X-Content-Type-Options": "nosniff",
  "X-Frame-Options": "DENY",
  "Referrer-Policy": "strict-origin-when-cross-origin",
  "Permissions-Policy": "camera=(), microphone=(), geolocation=()"
};

function originResponse(contentType = "text/html; charset=utf-8") {
  return new Response("ok", {
    status: 200,
    headers: {
      "Content-Type": contentType,
      "Cache-Control": "max-age=600"
    }
  });
}

function apply(path, contentType) {
  return applyEdgeHeaders(`https://panta-rhei.site${path}`, originResponse(contentType));
}

function assertSecurityHeaders(response) {
  for (const [name, value] of Object.entries(SECURITY_EXPECTATIONS)) {
    assert.equal(response.headers.get(name), value, `${name} should be enforced`);
  }

  assert.match(response.headers.get("Link"), /rel="sitemap"/);
  assert.match(response.headers.get("Link"), /rel="license"/);
  assert.match(response.headers.get("Link"), /rel="service-doc"/);
}

const cases = [
  ["/", "text/html; charset=utf-8", "public, max-age=3600, must-revalidate"],
  ["/program/", "text/html; charset=utf-8", "public, max-age=3600, must-revalidate"],
  ["/research-program/index.html", "text/html; charset=utf-8", "public, max-age=3600, must-revalidate"],
  [
    "/assets/pdfs/research-briefings/public-good/public-good-impact-dossier-2026-05-02-solar-synchronized-flexible-demand-grid-logistics.pdf",
    "application/pdf",
    "public, max-age=3600, must-revalidate"
  ],
  [
    "/assets/pdfs/research-notes/research-note-2026-04-25-structural-prior-dynamic-chirality-induced-spin-selectivity.pdf",
    "application/pdf",
    "public, max-age=3600, must-revalidate"
  ],
  // Fingerprinted CSS/JS (10-hex hash before extension) → immutable.
  // These are the actual production filenames after the asset-fingerprint
  // plugin runs; any content change produces a new URL so immutable is safe.
  ["/assets/css/main.abc1234567.css", "text/css", "public, max-age=31536000, immutable"],
  ["/assets/js/site.0123456789.js", "text/javascript", "public, max-age=31536000, immutable"],
  // Unfingerprinted /assets/* — brand SVGs, OG cards, fonts, data files,
  // and any CSS/JS that escapes the fingerprint plugin (e.g. /assets/css/
  // *.css before fingerprinting in dev). Use must-revalidate so a content
  // edit propagates within the 1-day TTL without waiting for the next
  // CDN-wide purge. This is the hotfix doctrine codified in PR #251.
  ["/assets/css/site.css", "text/css", "public, max-age=86400, must-revalidate"],
  ["/assets/brand/observatory-plate.v5.svg", "image/svg+xml", "public, max-age=86400, must-revalidate"],
  ["/assets/og/png/index.png", "image/png", "public, max-age=86400, must-revalidate"],
  ["/assets/site.webmanifest", "application/manifest+json", "public, max-age=604800"],
  ["/pagefind/pagefind.js", "text/javascript", "public, max-age=31536000, immutable"],
  ["/sitemap.xml", "application/xml", "public, max-age=86400"],
  ["/robots.txt", "text/plain", "public, max-age=86400"],
  ["/api/plates.json", "text/plain", "public, max-age=3600, stale-while-revalidate=86400"]
];

for (const [path, contentType, expectedCacheControl] of cases) {
  const response = apply(path, contentType);
  assert.equal(response.headers.get("Cache-Control"), expectedCacheControl, `${path} cache policy`);
  assertSecurityHeaders(response);
}

// CORS endpoints: /api/* should be cross-site-fetchable with CC BY 4.0 content
{
  const apiResponse = apply("/api/plates.json", "text/plain");
  assert.equal(apiResponse.headers.get("Access-Control-Allow-Origin"), "*", "/api/* should allow cross-origin GET");
  assert.equal(apiResponse.headers.get("Access-Control-Allow-Methods"), "GET, HEAD, OPTIONS", "/api/* should advertise simple methods");
  assert.equal(apiResponse.headers.get("Access-Control-Allow-Headers"), "Content-Type", "/api/* should allow Content-Type header");
  assert.equal(apiResponse.headers.get("Access-Control-Max-Age"), "86400", "/api/* preflight should cache for 24h");
  assert.equal(apiResponse.headers.get("Content-Type"), "application/json; charset=utf-8", "/api/*.json should override Content-Type to JSON");
}

// Negative CORS cases — non-/api/ paths must NOT receive CORS headers
for (const negativePath of ["/", "/results/", "/assets/css/site.css", "/sitemap.xml"]) {
  const negResponse = apply(negativePath, "text/html");
  assert.equal(negResponse.headers.get("Access-Control-Allow-Origin"), null, `${negativePath} must not be CORS-permissive`);
}

// CORS preflight: OPTIONS /api/* must short-circuit with 204 + full CORS contract
{
  const preflight = corsPreflightResponse(new URL("https://panta-rhei.site/api/plates.json"));
  assert.ok(preflight, "OPTIONS /api/plates.json should short-circuit with a Response");
  assert.equal(preflight.status, 204, "preflight should be 204 No Content");
  const decorated = applyEdgeHeaders("https://panta-rhei.site/api/plates.json", preflight);
  assert.equal(decorated.headers.get("Access-Control-Allow-Origin"), "*", "preflight must carry Allow-Origin: *");
  assert.equal(decorated.headers.get("Access-Control-Allow-Methods"), "GET, HEAD, OPTIONS", "preflight must advertise simple methods");
  assert.equal(decorated.headers.get("Access-Control-Max-Age"), "86400", "preflight must cache for 24h");
}

// Negative preflight: OPTIONS / must NOT short-circuit (falls through to origin → 405)
assert.equal(corsPreflightResponse(new URL("https://panta-rhei.site/")), null, "OPTIONS / must not short-circuit (no broad preflight)");

{
  const publicGoodPdf =
    "/assets/pdfs/research-briefings/public-good/public-good-impact-dossier-2026-05-02-solar-synchronized-flexible-demand-grid-logistics.pdf";
  const researchNotePdf =
    "/assets/pdfs/research-notes/research-note-2026-04-25-structural-prior-dynamic-chirality-induced-spin-selectivity.pdf";
  assert.deepEqual(
    fetchOptionsFor(`https://panta-rhei.site${publicGoodPdf}`),
    { cf: { cacheTtl: 0, cacheEverything: false } },
    "Public-good PDFs should bypass Cloudflare's stale edge cache"
  );
  assert.deepEqual(
    fetchOptionsFor(`https://panta-rhei.site${researchNotePdf}`),
    { cf: { cacheTtl: 0, cacheEverything: false } },
    "Research-note PDFs should bypass Cloudflare's stale edge cache"
  );
  assert.equal(fetchOptionsFor("https://panta-rhei.site/assets/css/site.css"), undefined);

  const originRequest = originRequestFor(`https://panta-rhei.site${publicGoodPdf}`);
  assert.equal(
    new URL(originRequest.url).searchParams.get("__prr_pdf_release"),
    "2026-05-02-template-polish",
    "Public-good PDF origin fetches should use a release-specific cache key"
  );
  const researchNoteOriginRequest = originRequestFor(`https://panta-rhei.site${researchNotePdf}`);
  assert.equal(
    new URL(researchNoteOriginRequest.url).searchParams.get("__prr_pdf_release"),
    "2026-05-16-rn002-title-polish",
    "Research-note PDF origin fetches should use a release-specific cache key"
  );
  assert.equal(originRequestFor("https://panta-rhei.site/assets/css/site.css"), "https://panta-rhei.site/assets/css/site.css");
}

for (const path of ["/publications/physics-ledger", "/publications/physics-ledger/", "/publications/numerical-physics-ledger/"]) {
  const redirect = edgeRedirectFor(`https://panta-rhei.site${path}`);
  assert.ok(redirect, `${path} should redirect at the edge`);
  assert.equal(redirect.status, 301, `${path} should be permanent`);
  assert.equal(
    redirect.headers.get("Location"),
    "https://panta-rhei.site/publications/monograph-supplements/numerical-physics-ledger/",
    `${path} redirect target`
  );
}

for (const [path, target] of [
  ["/publications/categorical-genesis", "/publications/monograph-supplements/categorical-genesis/"],
  ["/publications/categorical-genesis/", "/publications/monograph-supplements/categorical-genesis/"],
  ["/publications/companion-papers", "/publications/research-briefings/public-good/"],
  ["/publications/companion-papers/", "/publications/research-briefings/public-good/"],
  [
    "/publications/books/book-i/part-01-the-coherence-kernel/",
    "/corpus/monographs/book-i/part-01-the-coherence-kernel/"
  ],
  [
    "/publications/books/book-i/part-01-the-coherence-kernel/chapter-02-the-five-generators/",
    "/corpus/monographs/book-i/part-01-the-coherence-kernel/chapter-02-the-five-generators/"
  ],
  ["/verify/taulib/docs/book-i/", "/corpus/taulib/docs/book-i/"],
  [
    "/verify/taulib/docs/book-iii-arithmetic-abcconjecture/",
    "/corpus/taulib/docs/book-iii-arithmetic-abcconjecture/"
  ],
  ["/agenda/problem-ledger", "/agenda/structural-challenge-ledger/"],
  ["/agenda/problem-ledger/life/origin-of-life/", "/agenda/structural-challenge-ledger/"],
  ["/agenda/problem-ledger-source-policy/", "/agenda/structural-challenge-ledger/source-policy/"],
  ["/program/research-agenda/problem-ledger/physics/", "/agenda/structural-challenge-ledger/"],
  ["/program/research-agenda/problem-ledger-source-policy/", "/agenda/structural-challenge-ledger/source-policy/"],
  ["/results/problem-ledger-answers/physics/hubble-tension/", "/results/challenge-responses/"],
  ["/results/problem-answers/", "/results/challenge-responses/"],
  ["/results/problem-ledger/", "/results/challenge-responses/"],
  ["/results/by-problem/", "/results/challenge-responses/"],
  ["/framework", "/corpus/"],
  ["/framework/about/", "/corpus/"],
  ["/framework/mathematics-coherence-kernel/", "/corpus/"],
  [
    "/framework/prior-art/wolfram/",
    "/agenda/kernel-model-reality/related-approaches/deep-comparison/"
  ]
]) {
  const redirect = edgeRedirectFor(`https://panta-rhei.site${path}`);
  assert.ok(redirect, `${path} should redirect at the edge`);
  assert.equal(redirect.status, 301, `${path} should be permanent`);
  assert.equal(redirect.headers.get("Location"), `https://panta-rhei.site${target}`, `${path} redirect target`);
}

assert.equal(edgeRedirectFor("https://panta-rhei.site/publications/monograph-supplements/numerical-physics-ledger/"), null);
assert.equal(edgeRedirectFor("https://panta-rhei.site/publications/books/book-i/"), null);
assert.equal(edgeRedirectFor("https://panta-rhei.site/verify/taulib/docs/"), null);

// /agenda/* IS the canonical lane root since v4 — must NOT redirect at the edge.
// (Removed in 2026-05-20 hotfix; was producing an infinite loop with the static
// redirect stub at /program/research-agenda/index.html.)
assert.equal(edgeRedirectFor("https://panta-rhei.site/agenda"), null);
assert.equal(edgeRedirectFor("https://panta-rhei.site/agenda/"), null);
assert.equal(edgeRedirectFor("https://panta-rhei.site/agenda/research-aim-and-desiderata/"), null);

console.log(`site-edge-headers: ${cases.length} header cases, 5 CORS assertions, 4 CORS-negative cases, 4 preflight assertions, 3 fetch-option assertions, 3 origin-request assertions, and 24 redirect cases passed`);
