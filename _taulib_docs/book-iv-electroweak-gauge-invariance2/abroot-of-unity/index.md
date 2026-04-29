---
{
  "projection_kind": "taulib_declaration",
  "title": "ABRootOfUnity",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/abroot-of-unity/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance2::ABRootOfUnity",
  "declaration_slug": "abroot-of-unity",
  "kind": "structure",
  "name": "ABRootOfUnity",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/",
  "source_line_start": 152,
  "source_line_end": 159,
  "registry_ids": [
    "IV.T40"
  ],
  "related_registry_items": [
    {
      "id": "IV.T40",
      "title": "AB Phase Quantization",
      "url": "/registry/object/IV.T40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L152-L159",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.GaugeInvariance2",
        "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L152-L159",
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

- Module: [TauLib.BookIV.Electroweak.GaugeInvariance2](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/)
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L152-L159)
- Source range: L152-L159
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T40` — AB Phase Quantization

## Immediate Comment / Docstring

```lean
/-- [IV.T40] AB phase is a root of unity iff flux is rational:
    Φ/Φ₀ ∈ ℚ ⟹ exp(2πi·Φ/Φ₀) is a root of unity.
    On T², all fluxes are integer (quantized), so always a root. -/
```

## Source Excerpt

```lean
structure ABRootOfUnity where
  /-- Flux is rational (numerator/denominator). -/
  flux_numer : Int
  flux_denom : Nat
  denom_pos : flux_denom > 0
  /-- The phase is a root of unity. -/
  is_root : Bool := true
  deriving Repr
```
