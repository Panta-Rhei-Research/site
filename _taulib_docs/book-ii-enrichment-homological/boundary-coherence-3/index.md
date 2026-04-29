---
{
  "projection_kind": "taulib_declaration",
  "title": "boundary_coherence_3",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-homological/boundary-coherence-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.Homological`.",
  "declaration_id": "TauLib.BookII.Enrichment.Homological::boundary_coherence_3",
  "declaration_slug": "boundary-coherence-3",
  "kind": "theorem",
  "name": "boundary_coherence_3",
  "module_name": "TauLib.BookII.Enrichment.Homological",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-homological/",
  "source_line_start": 171,
  "source_line_end": 172,
  "registry_ids": [
    "II.T54"
  ],
  "related_registry_items": [
    {
      "id": "II.T54",
      "title": "Tower Coherence",
      "url": "/registry/object/II.T54/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L171-L172",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.Homological",
        "url": "/verify/taulib/docs/book-ii-enrichment-homological/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L171-L172",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookII.Enrichment.Homological](/verify/taulib/docs/book-ii-enrichment-homological/)
- Source path: [`TauLib/BookII/Enrichment/Homological.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L171-L172)
- Source range: L171-L172
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T54` — Tower Coherence

## Immediate Comment / Docstring

```lean
/-- [II.T54] Tower coherence at stage 3. -/
```

## Source Excerpt

```lean
theorem boundary_coherence_3 :
    boundary_coherence_check 3 = true := by native_decide
```
