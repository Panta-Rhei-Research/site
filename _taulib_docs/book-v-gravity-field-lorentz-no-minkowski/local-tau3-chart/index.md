---
{
  "projection_kind": "taulib_declaration",
  "title": "LocalTau3Chart",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/local-tau3-chart/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.LorentzNoMinkowski`.",
  "declaration_id": "TauLib.BookV.GravityField.LorentzNoMinkowski::LocalTau3Chart",
  "declaration_slug": "local-tau3-chart",
  "kind": "structure",
  "name": "LocalTau3Chart",
  "module_name": "TauLib.BookV.GravityField.LorentzNoMinkowski",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/",
  "source_line_start": 121,
  "source_line_end": 136,
  "registry_ids": [
    "V.D48"
  ],
  "related_registry_items": [
    {
      "id": "V.D48",
      "title": "Local tau^3 chart",
      "url": "/registry/object/V.D48/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L121-L136",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.LorentzNoMinkowski",
        "url": "/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L121-L136",
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

- Module: [TauLib.BookV.GravityField.LorentzNoMinkowski](/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/)
- Source path: [`TauLib/BookV/GravityField/LorentzNoMinkowski.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L121-L136)
- Source range: L121-L136
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D48` — Local tau^3 chart

## Immediate Comment / Docstring

```lean
/-- [V.D48] Local τ³ chart: coordinate neighborhood providing a
    4-dimensional readout at depth n.

    The chart provides:
    - 4 coordinates (1 temporal + 3 spatial)
    - Metric signature (1,3) = Lorentzian
    - Valid only in a local neighborhood (not global)
    - Readout approximation of boundary-character data -/
```

## Source Excerpt

```lean
structure LocalTau3Chart where
  /-- Refinement depth. -/
  depth : Nat
  /-- Depth positive. -/
  depth_pos : depth > 0
  /-- Total dimension (must be 4). -/
  dimension : Nat
  /-- Dimension is 4. -/
  dim_is_four : dimension = 4
  /-- Metric signature. -/
  signature : MetricSignature
  /-- Signature is Lorentzian (1,3). -/
  sig_lorentzian : signature = lorentzian_signature
  /-- Chart is local (not global). -/
  is_local : Bool := true
  deriving Repr
```
