---
{
  "projection_kind": "taulib_declaration",
  "title": "AlphaPrecisionBarrier",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-precision-barrier/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.AlphaDerivation`.",
  "declaration_id": "TauLib.BookIV.Electroweak.AlphaDerivation::AlphaPrecisionBarrier",
  "declaration_slug": "alpha-precision-barrier",
  "kind": "structure",
  "name": "AlphaPrecisionBarrier",
  "module_name": "TauLib.BookIV.Electroweak.AlphaDerivation",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/",
  "source_line_start": 471,
  "source_line_end": 478,
  "registry_ids": [
    "IV.T205"
  ],
  "related_registry_items": [
    {
      "id": "IV.T205",
      "title": "α Precision Barrier at 9.8 ppm",
      "url": "/registry/object/IV.T205/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L471-L478",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L471-L478",
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
- Source path: [`TauLib/BookIV/Electroweak/AlphaDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L471-L478)
- Source range: L471-L478
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T205` — α Precision Barrier at 9.8 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.T205] α precision barrier: 9.8 ppm is the current limit.
    The fraction 11/15 is isolated (unique a/b ≤ 100 within 10 ppm)
    and all NLO candidates overshoot or have wrong sign. -/
```

## Source Excerpt

```lean
structure AlphaPrecisionBarrier where
  /-- Precision in ppm (tower formula). -/
  precision_ppm : Float := 9.8
  /-- 11/15 is isolated (unique in a,b ≤ 100). -/
  fraction_isolated : Bool := true
  /-- NLO catalog empty (no improvement found). -/
  nlo_improves : Bool := false
  deriving Repr
```
