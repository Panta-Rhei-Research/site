---
{
  "projection_kind": "taulib_declaration",
  "title": "FieldStrengthTensor",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/field-strength-tensor/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance::FieldStrengthTensor",
  "declaration_slug": "field-strength-tensor",
  "kind": "structure",
  "name": "FieldStrengthTensor",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/",
  "source_line_start": 208,
  "source_line_end": 217,
  "registry_ids": [
    "IV.D92"
  ],
  "related_registry_items": [
    {
      "id": "IV.D92",
      "title": "Electromagnetic Field Strength",
      "url": "/registry/object/IV.D92/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L208-L217",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.GaugeInvariance",
        "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L208-L217",
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

- Module: [TauLib.BookIV.Electroweak.GaugeInvariance](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/)
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L208-L217)
- Source range: L208-L217
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D92` — Electromagnetic Field Strength

## Immediate Comment / Docstring

```lean
/-- [IV.D92] Field strength tensor F_μν = ∂_μA_ν − ∂_νA_μ (curvature).
    Antisymmetric 2-form on spacetime; encodes E and B fields.
    Independent components in 4D: 6 = 4·3/2. -/
```

## Source Excerpt

```lean
structure FieldStrengthTensor where
  /-- Spacetime dimension. -/
  spacetime_dim : Nat
  dim_eq : spacetime_dim = 4
  /-- Number of independent components = d(d-1)/2. -/
  independent_components : Nat
  comp_eq : independent_components = 6
  /-- Gauge-invariant (structural property). -/
  gauge_invariant : Bool := true
  deriving Repr
```
