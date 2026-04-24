import assert from "node:assert/strict";

const origin = process.env.SITE_ORIGIN || "https://panta-rhei.site";

const securityExpectations = {
  "x-content-type-options": "nosniff",
  "x-frame-options": "DENY",
  "referrer-policy": "strict-origin-when-cross-origin",
  "permissions-policy": "camera=(), microphone=(), geolocation=()"
};

const checks = [
  ["/", "cache-control", /max-age=3600/],
  ["/program/", "cache-control", /max-age=3600/],
  ["/assets/site.webmanifest", "cache-control", /max-age=604800/],
  ["/sitemap.xml", "cache-control", /max-age=86400/],
  ["/robots.txt", "cache-control", /max-age=86400/],
  ["/pagefind/pagefind.js", "cache-control", /max-age=31536000/]
];

async function fetchHead(path) {
  const response = await fetch(new URL(path, origin), {
    method: "HEAD",
    redirect: "manual"
  });

  if (response.status === 405) {
    return fetch(new URL(path, origin), { method: "GET", redirect: "manual" });
  }

  return response;
}

for (const [path, headerName, expectedPattern] of checks) {
  const response = await fetchHead(path);
  assert(response.status < 400, `${path} returned HTTP ${response.status}`);

  for (const [name, expectedValue] of Object.entries(securityExpectations)) {
    assert.equal(response.headers.get(name), expectedValue, `${path} ${name}`);
  }

  const cacheControl = response.headers.get(headerName) || "";
  assert.match(cacheControl, expectedPattern, `${path} ${headerName}`);

  const link = response.headers.get("link") || "";
  assert.match(link, /rel="sitemap"/, `${path} Link sitemap relation`);
  assert.match(link, /rel="license"/, `${path} Link license relation`);
}

console.log(`Live edge headers passed for ${checks.length} paths at ${origin}`);

