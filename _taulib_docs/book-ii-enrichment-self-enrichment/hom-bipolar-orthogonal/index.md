---
{
  "projection_kind": "taulib_declaration",
  "title": "hom_bipolar_orthogonal",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/hom-bipolar-orthogonal/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.SelfEnrichment`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfEnrichment::hom_bipolar_orthogonal",
  "declaration_slug": "hom-bipolar-orthogonal",
  "kind": "theorem",
  "name": "hom_bipolar_orthogonal",
  "module_name": "TauLib.BookII.Enrichment.SelfEnrichment",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/",
  "source_line_start": 360,
  "source_line_end": 363,
  "registry_ids": [
    "II.P12"
  ],
  "related_registry_items": [
    {
      "id": "II.P12",
      "title": "Enrichment Iteration",
      "url": "/registry/object/II.P12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L360-L363",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.SelfEnrichment",
        "url": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L360-L363",
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

- Module: [TauLib.BookII.Enrichment.SelfEnrichment](/verify/taulib/docs/book-ii-enrichment-self-enrichment/)
- Source path: [`TauLib/BookII/Enrichment/SelfEnrichment.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L360-L363)
- Source range: L360-L363
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.P12` — Enrichment Iteration

## Immediate Comment / Docstring

```lean
/-- [II.P12] Formal proof: bipolar projections are orthogonal.
    e_plus * (e_minus * sp) = (0, 0) for any sector pair sp. -/
```

## Source Excerpt

```lean
theorem hom_bipolar_orthogonal (sp : SectorPair) :
    SectorPair.mul e_plus_sector (SectorPair.mul e_minus_sector sp) =
    ⟨0, 0⟩ := by
  simp [SectorPair.mul, e_plus_sector, e_minus_sector]
```
