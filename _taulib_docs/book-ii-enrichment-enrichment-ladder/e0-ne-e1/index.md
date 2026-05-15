---
{
  "projection_kind": "taulib_declaration",
  "title": "e0_ne_e1",
  "permalink": "/corpus/taulib/docs/book-ii-enrichment-enrichment-ladder/e0-ne-e1/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.EnrichmentLadder`.",
  "declaration_id": "TauLib.BookII.Enrichment.EnrichmentLadder::e0_ne_e1",
  "declaration_slug": "e0-ne-e1",
  "kind": "theorem",
  "name": "e0_ne_e1",
  "module_name": "TauLib.BookII.Enrichment.EnrichmentLadder",
  "module_url": "/corpus/taulib/docs/book-ii-enrichment-enrichment-ladder/",
  "source_line_start": 271,
  "source_line_end": 273,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L271-L273",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L271-L273",
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
- Source path: [`TauLib/BookII/Enrichment/EnrichmentLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L271-L273)
- Source range: L271-L273
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The E0 and E1 levels are distinct (structural). -/
```

## Source Excerpt

```lean
theorem e0_ne_e1 : EnrichmentLevel.E0 ≠ EnrichmentLevel.E1 := by
  intro h
  cases h
```
