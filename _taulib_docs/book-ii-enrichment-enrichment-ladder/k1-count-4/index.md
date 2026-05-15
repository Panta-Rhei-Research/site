---
{
  "projection_kind": "taulib_declaration",
  "title": "k1_count_4",
  "permalink": "/corpus/taulib/docs/book-ii-enrichment-enrichment-ladder/k1-count-4/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.EnrichmentLadder`.",
  "declaration_id": "TauLib.BookII.Enrichment.EnrichmentLadder::k1_count_4",
  "declaration_slug": "k1-count-4",
  "kind": "theorem",
  "name": "k1_count_4",
  "module_name": "TauLib.BookII.Enrichment.EnrichmentLadder",
  "module_url": "/corpus/taulib/docs/book-ii-enrichment-enrichment-ladder/",
  "source_line_start": 320,
  "source_line_end": 321,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L320-L321",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L320-L321",
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
- Source path: [`TauLib/BookII/Enrichment/EnrichmentLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L320-L321)
- Source range: L320-L321
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- k=1 endomorphism count
```

## Source Excerpt

```lean
theorem k1_count_4 :
    count_rc_endomorphisms_k1 = 4 := by native_decide
```
