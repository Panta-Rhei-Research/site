---
{
  "projection_kind": "taulib_declaration",
  "title": "EMFieldTensor",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/emfield-tensor/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauMaxwell`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauMaxwell::EMFieldTensor",
  "declaration_slug": "emfield-tensor",
  "kind": "structure",
  "name": "EMFieldTensor",
  "module_name": "TauLib.BookIV.Electroweak.TauMaxwell",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/",
  "source_line_start": 121,
  "source_line_end": 132,
  "registry_ids": [
    "IV.D100"
  ],
  "related_registry_items": [
    {
      "id": "IV.D100",
      "title": "Electromagnetic Field Tensor",
      "url": "/registry/object/IV.D100/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L121-L132",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauMaxwell",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L121-L132",
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

- Module: [TauLib.BookIV.Electroweak.TauMaxwell](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/)
- Source path: [`TauLib/BookIV/Electroweak/TauMaxwell.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L121-L132)
- Source range: L121-L132
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D100` — Electromagnetic Field Tensor

## Immediate Comment / Docstring

```lean
/-- [IV.D100] EM field tensor F = dA: the curvature 2-form of the
    EM connection. An antisymmetric (0,2)-tensor with 6 independent
    components in 4D spacetime. -/
```

## Source Excerpt

```lean
structure EMFieldTensor where
  /-- Spacetime dimension. -/
  dim : Nat
  dim_eq : dim = 4
  /-- Independent components = d(d-1)/2. -/
  components : Nat
  comp_eq : components = 6
  /-- F = dA (exterior derivative of connection). -/
  is_exact : Bool := true
  /-- Gauge-invariant. -/
  gauge_invariant : Bool := true
  deriving Repr
```
