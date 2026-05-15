---
{
  "projection_kind": "taulib_declaration",
  "title": "tower_coherence_transitive",
  "permalink": "/corpus/taulib/docs/book-ii-enrichment-enrichment-ladder/tower-coherence-transitive/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.EnrichmentLadder`.",
  "declaration_id": "TauLib.BookII.Enrichment.EnrichmentLadder::tower_coherence_transitive",
  "declaration_slug": "tower-coherence-transitive",
  "kind": "theorem",
  "name": "tower_coherence_transitive",
  "module_name": "TauLib.BookII.Enrichment.EnrichmentLadder",
  "module_url": "/corpus/taulib/docs/book-ii-enrichment-enrichment-ladder/",
  "source_line_start": 266,
  "source_line_end": 268,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L266-L268",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.EnrichmentLadder",
        "url": "/corpus/taulib/docs/book-ii-enrichment-enrichment-ladder/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L266-L268",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookII.Enrichment.EnrichmentLadder](/corpus/taulib/docs/book-ii-enrichment-enrichment-ladder/)
- Source path: [`TauLib/BookII/Enrichment/EnrichmentLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L266-L268)
- Source range: L266-L268
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Tower coherence is transitive: if f is coherent at (k, l) and (j, k),
    then f is coherent at (j, l). For the identity:
    reduce(reduce(x, l), j) = reduce(x, j) for j <= k <= l.
    This follows directly from reduction_compat. -/
```

## Source Excerpt

```lean
theorem tower_coherence_transitive (x : TauIdx) {j l : TauIdx} (h : j ≤ l) :
    reduce (reduce x l) j = reduce x j :=
  reduction_compat x h
```
