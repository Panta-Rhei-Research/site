---
{
  "projection_kind": "taulib_declaration",
  "title": "EpsteinZetaStructure",
  "permalink": "/verify/taulib/docs/book-iv-calibration-epstein-zeta/epstein-zeta-structure/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.EpsteinZeta`.",
  "declaration_id": "TauLib.BookIV.Calibration.EpsteinZeta::EpsteinZetaStructure",
  "declaration_slug": "epstein-zeta-structure",
  "kind": "structure",
  "name": "EpsteinZetaStructure",
  "module_name": "TauLib.BookIV.Calibration.EpsteinZeta",
  "module_url": "/verify/taulib/docs/book-iv-calibration-epstein-zeta/",
  "source_line_start": 74,
  "source_line_end": 85,
  "registry_ids": [
    "IV.D40"
  ],
  "related_registry_items": [
    {
      "id": "IV.D40",
      "title": "Epstein Zeta Structure",
      "url": "/registry/object/IV.D40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/EpsteinZeta.lean#L74-L85",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.EpsteinZeta",
        "url": "/verify/taulib/docs/book-iv-calibration-epstein-zeta/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/EpsteinZeta.lean#L74-L85",
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

- Module: [TauLib.BookIV.Calibration.EpsteinZeta](/verify/taulib/docs/book-iv-calibration-epstein-zeta/)
- Source path: [`TauLib/BookIV/Calibration/EpsteinZeta.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/EpsteinZeta.lean#L74-L85)
- Source range: L74-L85
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D40` — Epstein Zeta Structure

## Immediate Comment / Docstring

```lean
/-- [IV.D40] The Epstein zeta function on a rectangular lattice.

    Z(s; iτ) = Σ'_{(m,n) ∈ ℤ²} (m² + τ²n²)^{-s}

    The lattice is determined by the shape parameter τ (aspect ratio).
    For the τ-framework torus, τ = ι_τ = 2/(π+e). -/
```

## Source Excerpt

```lean
structure EpsteinZetaStructure where
  /-- Shape parameter numerator (rational approximation). -/
  shape_numer : Nat
  /-- Shape parameter denominator. -/
  shape_denom : Nat
  /-- Denominator positive. -/
  denom_pos : shape_denom > 0
  /-- Critical exponent s at which Z is evaluated. -/
  eval_point : Nat
  /-- Scope label. -/
  scope : String := "tau-effective"
  deriving Repr
```
