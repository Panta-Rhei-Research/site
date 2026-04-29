---
{
  "projection_kind": "taulib_declaration",
  "title": "BreathingOperator",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/breathing-operator/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.MassDerivation.BreathingModes`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.BreathingModes::BreathingOperator",
  "declaration_slug": "breathing-operator",
  "kind": "structure",
  "name": "BreathingOperator",
  "module_name": "TauLib.BookIV.MassDerivation.BreathingModes",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/",
  "source_line_start": 59,
  "source_line_end": 64,
  "registry_ids": [
    "IV.D309"
  ],
  "related_registry_items": [
    {
      "id": "IV.D309",
      "title": "Breathing operator",
      "url": "/registry/object/IV.D309/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L59-L64",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.MassDerivation.BreathingModes",
        "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L59-L64",
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

- Module: [TauLib.BookIV.MassDerivation.BreathingModes](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/)
- Source path: [`TauLib/BookIV/MassDerivation/BreathingModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L59-L64)
- Source range: L59-L64
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D309` — Breathing operator

## Immediate Comment / Docstring

```lean
/-- [IV.D309] Breathing operator B = (1/ι_τ²)·Δ_Hodge⁻¹ on fiber T². -/
```

## Source Excerpt

```lean
structure BreathingOperator where
  inv_coeff_numer : Nat
  inv_coeff_denom : Nat
  denom_pos : inv_coeff_denom > 0
  fiber_restricted : Bool := true
  deriving Repr
```
