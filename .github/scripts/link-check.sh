#!/usr/bin/env bash
# ============================================================
# Dead-link audit for panta-rhei.site
# ============================================================
# Runs html-proofer against the built _site/ tree. Internal-only
# (external link validation is a separate, slower check).
#
# Runs AFTER Jekyll build + Pagefind, BEFORE Pages artifact upload.
# Fails the build visibly if any NEW broken internal link appears.
#
# Known-broken URLs are listed in IGNORE_URLS below — each is tracked
# in atlas/audits/site/2026-04-19-dead-link-audit.md with category,
# root cause, and recommended fix. Remove from IGNORE_URLS when fixed.
#
# Usage:
#   ./link-check.sh [path/to/_site]
#
# Exit codes:
#   0 — all checks passed
#   1 — at least one new broken link found
# ============================================================

set -u

SITE="${1:-_site}"
if [ ! -d "$SITE" ]; then
  echo "ERROR: $SITE is not a directory"
  echo "Usage: $0 <path-to-_site>"
  exit 2
fi

export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

# Ignore patterns (comma-separated list; /regex/ for patterns, otherwise literal string)
IGNORE_URLS=$(cat <<'EOF' | tr '\n' ',' | sed 's/,$//'
/\/pagefind\//
/registry/object/IV.D417/
/registry/object/IV.D468/
/registry/object/IV.D505/
/registry/object/IV.P243/
/registry/object/IV.P269/
/registry/object/IV.P361/
/registry/object/IV.P366/
/registry/object/IV.T270/
/registry/object/IV.T342/
/registry/object/V.D06/
/registry/object/V.D11/
/registry/object/V.T04/
/framework/about/guided-tours/
/framework/about/key-results-overview/
/framework/about/verify-it-yourself/
/framework/mathematics-hyperbolic-geometry/
/framework/mathematics-linear-logic/
/results/fine-structure-constant/
/results/hubble-tension/
/results/problem/gettier-problem-resolved/
/results/prologue/the-shape-of-mathematics-in-the-tau-framework/
/research-program/claims-and-validation/
/publications/books/book-vii/part-11-categorical-genesis/
/assets/assessments/dossier-template.json
/assets/assessments/scorecard-template.csv
EOF
)

echo "═══════════════════════════════════════════════════════════"
echo " Dead-link audit against ${SITE}/"
echo "═══════════════════════════════════════════════════════════"
echo "  Ignored patterns: $(echo "$IGNORE_URLS" | tr ',' '\n' | wc -l | tr -d ' ')"
echo ""

bundle exec htmlproofer "$SITE" \
  --disable-external \
  --checks Links,Images,Scripts \
  --ignore-missing-alt \
  --no-check-internal-hash \
  --ignore-urls "$IGNORE_URLS"
