---
{
  "projection_kind": "taulib_declaration",
  "title": "StructuralIndependence",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/structural-independence/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.AlphaDerivation`.",
  "declaration_id": "TauLib.BookIV.Electroweak.AlphaDerivation::StructuralIndependence",
  "declaration_slug": "structural-independence",
  "kind": "structure",
  "name": "StructuralIndependence",
  "module_name": "TauLib.BookIV.Electroweak.AlphaDerivation",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/",
  "source_line_start": 344,
  "source_line_end": 351,
  "registry_ids": [
    "IV.P51"
  ],
  "related_registry_items": [
    {
      "id": "IV.P51",
      "title": "alpha_em versus iota_tau",
      "url": "/registry/object/IV.P51/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L344-L351",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.AlphaDerivation",
        "url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L344-L351",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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

- Module: [TauLib.BookIV.Electroweak.AlphaDerivation](/verify/taulib/docs/book-iv-electroweak-alpha-derivation/)
- Source path: [`TauLib/BookIV/Electroweak/AlphaDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L344-L351)
- Source range: L344-L351
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P51` — alpha_em versus iota_tau

## Immediate Comment / Docstring

```lean
/-- [IV.P51] α and ι_τ are structurally independent constants:
    α depends on ι_τ via (8/15)·ι_τ⁴·R, but ι_τ is the master
    constant from which α is derived (not vice versa).
    Their ratio is not a simple number. -/
```

## Source Excerpt

```lean
structure StructuralIndependence where
  /-- α is derived from ι_τ. -/
  alpha_from_iota : Bool := true
  /-- ι_τ is the master constant. -/
  iota_is_master : Bool := true
  /-- The derivation goes through spectral formula. -/
  via_spectral : Bool := true
  deriving Repr
```
