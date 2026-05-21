#!/usr/bin/env bash
# ============================================================
# Build-artifact smoke test for panta-rhei.site
# ============================================================
# Runs AFTER `bundle exec jekyll build` + Pagefind, BEFORE
# `upload-pages-artifact`. Validates the built `_site/` tree
# directly — no CDN, no network, no Cloudflare bot-protection
# false-positives.
#
# Catches:
#   · missing assets referenced from head.html
#   · missing core pages (v2 lane roots, publications)
#   · duplicate <title> / meta regressions
#   · accent-color drift, deprecated-org refs, local-path leaks
#   · empty / stubbed sitemap
#
# Usage:
#   ./smoke-test.sh path/to/_site
#
# Exit codes:
#   0 — all checks passed
#   1 — one or more checks failed
#   2 — usage error
# ============================================================

set -u

SITE="${1:-_site}"
if [ ! -d "$SITE" ]; then
  echo "ERROR: $SITE is not a directory"
  echo "Usage: $0 <path-to-_site>"
  exit 2
fi

FAILED=0
CHECK_COUNT=0

pass() { echo "  ✓ $*"; CHECK_COUNT=$((CHECK_COUNT+1)); }
fail() { echo "  ✗ $*"; CHECK_COUNT=$((CHECK_COUNT+1)); FAILED=$((FAILED+1)); }

check_file() {
  local rel="$1"
  if [ -f "$SITE$rel" ]; then
    pass "exists  $rel"
  else
    fail "MISSING $rel"
  fi
}

file_contains() {
  local rel="$1" needle="$2" label="$3"
  if [ ! -f "$SITE$rel" ]; then
    fail "$label  (target file $rel missing)"
    return
  fi
  if grep -qF -- "$needle" "$SITE$rel"; then
    pass "$label"
  else
    fail "$label  ($rel missing '$needle')"
  fi
}

file_count() {
  local rel="$1" needle="$2" expected="$3" label="$4"
  if [ ! -f "$SITE$rel" ]; then
    fail "$label  (target file $rel missing)"
    return
  fi
  local count
  count=$(grep -cF -- "$needle" "$SITE$rel")
  if [ "$count" = "$expected" ]; then
    pass "$label  (count=${expected})"
  else
    fail "$label  (expected ${expected}, got ${count})"
  fi
}

file_absent() {
  local rel="$1" needle="$2" label="$3"
  if [ ! -f "$SITE$rel" ]; then
    fail "$label  (target file $rel missing)"
    return
  fi
  local count
  count=$(grep -cF -- "$needle" "$SITE$rel")
  if [ "$count" = "0" ]; then
    pass "$label"
  else
    fail "$label  (found ${count} occurrence(s) — regression)"
  fi
}

echo "═══════════════════════════════════════════════════════════"
echo " Build-artifact smoke test against ${SITE}/"
echo "═══════════════════════════════════════════════════════════"
echo ""

echo "── Every expected file exists in _site/ ──────────────────"
# Fingerprinted main bundle: filename embeds a 10-char content hash at build
# time (see _plugins/asset_fingerprint.rb), so we can't check a literal name.
hashed_css=( "$SITE"/assets/css/main.*.css )
if [ -f "${hashed_css[0]}" ] && [ ${#hashed_css[@]} -eq 1 ]; then
  pass "exists  /assets/css/main.<hash>.css (${hashed_css[0]##*/})"
else
  fail "MISSING /assets/css/main.<hash>.css (found ${#hashed_css[@]} match(es))"
fi
CHECK_COUNT=$((CHECK_COUNT+1))

# Original (unhashed) main.css must NOT survive the rename — its presence
# would mean fingerprinting silently regressed and any reference still
# pointing at /assets/css/main.css would re-trigger the year-long cache lock.
if [ -f "$SITE/assets/css/main.css" ]; then
  fail "REGRESSION /assets/css/main.css present (fingerprint plugin failed to rename)"
else
  pass "absent  /assets/css/main.css (fingerprint plugin renamed it)"
fi
CHECK_COUNT=$((CHECK_COUNT+1))

for f in \
  "/index.html" \
  "/discover/index.html" \
  "/program/index.html" \
  "/corpus/index.html" \
  "/corpus/registry/index.html" \
  "/results/index.html" \
  "/verify/index.html" \
  "/publications/index.html" \
  "/impact/index.html" \
  "/engage/index.html" \
  "/research-program/index.html" \
  "/registry/index.html" \
  "/research-notes/index.html" \
  "/robots.txt" \
  "/sitemap.xml" \
  "/assets/og-image.png" \
  "/assets/favicon.svg" \
  "/assets/favicon-32x32.png" \
  "/assets/favicon-16x16.png" \
  "/assets/apple-touch-icon.png" \
  "/assets/site.webmanifest" \
  "/assets/fonts/InterVariable.woff2" \
  "/pagefind/pagefind.js" \
  "/pagefind/pagefind-ui.js" \
  "/pagefind/pagefind-ui.css"
do
  check_file "$f"
done

echo ""
echo "── Homepage integrity ────────────────────────────────────"
file_count    "/index.html" "<title>"                                         "1"  "single <title> tag"
file_contains "/index.html" 'name="theme-color"'                                   "theme-color meta present"
file_contains "/index.html" "#163e64"                                              "canonical navy #163e64 in head"
file_contains "/index.html" "orcid.org/0009-0007-0718-1042"                        "Thorsten ORCID in JSON-LD"
file_contains "/index.html" "orcid.org/0009-0007-3495-7416"                        "Anna-Sophie ORCID in JSON-LD"
file_contains "/index.html" "https://panta-rhei.site/assets/og/png/index.png" "homepage production OG card absolute URL"
# v5 HF-01 + AUD-07 — the homepage hero now carries TWO CTAs only (Verify
# it yourself + Start with Discover). The remaining lane CTAs migrate to
# the numbered lane index in §4 (HF-05, lands in Wave 3) and to inline
# section CTAs. The smoke-test still confirms each lane is reachable from
# the homepage but no longer asserts the v4 four-CTA hero stack.
file_contains "/index.html" "Start with Discover"                                  "v5 Discover CTA present"
file_contains "/index.html" "Verify it yourself"                                   "v5 Verify CTA present"
file_contains "/index.html" 'href="/corpus/"'                                      "Corpus lane link reachable from homepage"
file_contains "/index.html" 'href="/results/"'                                     "Results lane link reachable from homepage"
file_contains "/index.html" "taulib.site"                                          "reciprocal link to taulib.site"

echo ""
echo "── Anti-regression (zero-occurrence) ─────────────────────"
file_absent "/index.html" "Panta-Rhei-Framework"                   "no deprecated org references"
file_absent "/index.html" "/Users/thorfuchs"                       "no local filesystem paths leaked"
file_absent "/index.html" "#294b66"                                "no pre-migration accent color"

echo ""
echo "── robots.txt + sitemap.xml integrity ────────────────────"
file_contains "/robots.txt" "Content-Signal"                        "Content-Signal directive present"
file_contains "/robots.txt" "Sitemap: https://panta-rhei.site"      "sitemap reference present"

# /sitemap.xml is a sitemap INDEX referencing six child sitemaps (see
# _includes/sitemap-bucket.liquid). Validate:
#   1. /sitemap.xml is a <sitemapindex> (not a <urlset>)
#   2. All six child sitemap files exist
#   3. Each child contains a non-trivial number of <loc> URLs
#   4. Total URLs across children ≥ 5000 (canonical ~8,864 on prod)
if grep -q '<sitemapindex' "$SITE/sitemap.xml" 2>/dev/null; then
  pass "sitemap.xml is a <sitemapindex>"
else
  fail "sitemap.xml is not a <sitemapindex> — expected sitemap index format"
fi
CHECK_COUNT=$((CHECK_COUNT+1))

total_locs=0
declare -A child_min=(
  ["sitemap-core.xml"]=500
  ["sitemap-registry.xml"]=4000
  ["sitemap-bibliography.xml"]=1000
  ["sitemap-corpus-bulk.xml"]=1000
  ["sitemap-results-bulk.xml"]=500
  ["sitemap-predictions.xml"]=20
)
for child in sitemap-core.xml sitemap-registry.xml sitemap-bibliography.xml sitemap-corpus-bulk.xml sitemap-results-bulk.xml sitemap-predictions.xml; do
  if [ ! -f "$SITE/$child" ]; then
    fail "MISSING /$child"
    CHECK_COUNT=$((CHECK_COUNT+1))
    continue
  fi
  child_locs=$(grep -c '<loc>' "$SITE/$child" 2>/dev/null || echo "0")
  total_locs=$((total_locs + child_locs))
  min_expected=${child_min[$child]}
  if [ "$child_locs" -ge "$min_expected" ]; then
    pass "/$child has ${child_locs} URLs (≥${min_expected} expected)"
  else
    fail "/$child has only ${child_locs} URLs (expected ≥${min_expected})"
  fi
  CHECK_COUNT=$((CHECK_COUNT+1))
done

if [ "$total_locs" -ge 5000 ]; then
  pass "sitemap total URLs across children: ${total_locs} (≥5000 expected)"
else
  fail "sitemap total URLs across children: only ${total_locs} (expected ≥5000)"
fi
CHECK_COUNT=$((CHECK_COUNT+1))

echo ""
echo "═══════════════════════════════════════════════════════════"
if [ "$FAILED" -eq 0 ]; then
  echo " ✓ ALL ${CHECK_COUNT} CHECKS PASSED"
  echo "═══════════════════════════════════════════════════════════"
  exit 0
else
  echo " ✗ ${FAILED} of ${CHECK_COUNT} checks FAILED"
  echo "═══════════════════════════════════════════════════════════"
  exit 1
fi
