---
{
  "projection_kind": "taulib_declaration",
  "title": "UniqueMassless",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/unique-massless/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.AlphaDerivation`.",
  "declaration_id": "TauLib.BookIV.Electroweak.AlphaDerivation::UniqueMassless",
  "declaration_slug": "unique-massless",
  "kind": "structure",
  "name": "UniqueMassless",
  "module_name": "TauLib.BookIV.Electroweak.AlphaDerivation",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/",
  "source_line_start": 319,
  "source_line_end": 326,
  "registry_ids": [
    "IV.P50"
  ],
  "related_registry_items": [
    {
      "id": "IV.P50",
      "title": "Photon Uniqueness",
      "url": "/registry/object/IV.P50/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L319-L326",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L319-L326",
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
- Source path: [`TauLib/BookIV/Electroweak/AlphaDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L319-L326)
- Source range: L319-L326
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P50` — Photon Uniqueness

## Immediate Comment / Docstring

```lean
/-- [IV.P50] The photon is the unique massless transport mode in the
    B-sector: (0,0) is the only character in ker(Δ_Hodge) ∩ B.
    Any other B-sector mode has (m,n) ≠ (0,0) and hence mass > 0. -/
```

## Source Excerpt

```lean
structure UniqueMassless where
  /-- The photon character (0,0). -/
  photon_m : Int
  photon_n : Int
  is_zero : photon_m = 0 ∧ photon_n = 0
  /-- Uniqueness: any other B-mode has nonzero character. -/
  unique_in_b : Bool := true
  deriving Repr
```
