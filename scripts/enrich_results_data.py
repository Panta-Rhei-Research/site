#!/usr/bin/env python3
"""
Enrich _data/results/results.json with derived metadata fields per the
results-browse-metadata-refinement-pack spec.

Fields added per result entry:
  - primary_domain: alias of existing `topic` (cleaner field name for the spec)
  - secondary_domains: list derived from `layer` when it differs from `topic`
  - stance_type: mapped from existing `bridge_status`
  - wikipedia_url: looked up from wikipedia_links.json (only for mapped slugs)

Runs idempotently: re-running will overwrite the same derived fields without
duplicating data.
"""
import json
from pathlib import Path

ROOT = Path("/Users/thorfuchs/Panta-Rhei-Research/site/_data/results")
RESULTS_FILE = ROOT / "results.json"
WIKI_FILE = ROOT / "wikipedia_links.json"

# bridge_status -> stance_type mapping (from briefing pack controlled values)
STANCE_MAP = {
    "resolved": "full-solution",
    "partial": "partial-solution",
    "qualitative": "tau-internal-only",
    "contradicted": "contradicts-dominant-hypothesis",
    "not_addressed": "bridge-claim",
    "internal": "internal-structural-result",
}


def main():
    results = json.loads(RESULTS_FILE.read_text(encoding="utf-8"))
    wiki_links = json.loads(WIKI_FILE.read_text(encoding="utf-8"))

    enriched_count = 0
    wiki_matched = 0

    for entry in results:
        topic = entry.get("topic", "")
        layer = entry.get("layer", "")
        bridge = entry.get("bridge_status", "")
        slug = entry.get("slug", "")

        # primary_domain: alias for topic (new canonical field name)
        entry["primary_domain"] = topic

        # secondary_domains: include layer if it differs from topic
        secondary = []
        if layer and layer != topic:
            secondary.append(layer)
        entry["secondary_domains"] = secondary

        # stance_type: mapped from bridge_status
        if bridge in STANCE_MAP:
            entry["stance_type"] = STANCE_MAP[bridge]
        else:
            entry["stance_type"] = "internal-structural-result"

        # wikipedia_url: lookup from mapping (None if unmapped)
        wiki_url = wiki_links.get(slug)
        if wiki_url:
            entry["wikipedia_url"] = wiki_url
            wiki_matched += 1
        elif "wikipedia_url" in entry:
            # Remove stale field if mapping no longer includes this slug
            del entry["wikipedia_url"]

        enriched_count += 1

    # Write back with stable JSON formatting (2-space indent, preserves unicode)
    RESULTS_FILE.write_text(
        json.dumps(results, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(f"  Enriched {enriched_count} result entries")
    print(f"  Wikipedia links matched: {wiki_matched} of {len(wiki_links)} mapping entries")
    print(f"  Wrote {RESULTS_FILE}")


if __name__ == "__main__":
    main()
