---
{
  "projection_kind": "taulib_declaration",
  "title": "Be7SuppressionFactor",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/be7-suppression-factor/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BBNNuclearNetwork`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNNuclearNetwork::Be7SuppressionFactor",
  "declaration_slug": "be7-suppression-factor",
  "kind": "structure",
  "name": "Be7SuppressionFactor",
  "module_name": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/",
  "source_line_start": 236,
  "source_line_end": 245,
  "registry_ids": [
    "V.D306"
  ],
  "related_registry_items": [
    {
      "id": "V.D306",
      "title": "⁷Be Suppression Factor",
      "url": "/registry/object/V.D306/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L236-L245",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
        "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L236-L245",
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

- Module: [TauLib.BookV.Cosmology.BBNNuclearNetwork](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/)
- Source path: [`TauLib/BookV/Cosmology/BBNNuclearNetwork.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L236-L245)
- Source range: L236-L245
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D306` — ⁷Be Suppression Factor

## Immediate Comment / Docstring

```lean
/-- [V.D306] ⁷Be suppression factor S = dim(τ¹)/dim(τ³) = 1/3.
    The EM capture operates on the 1D base τ¹ rather than
    the full 3D τ³. -/
```

## Source Excerpt

```lean
structure Be7SuppressionFactor where
  /-- Suppression numerator = dim(τ¹). -/
  supp_num : Nat := 1
  /-- Suppression denominator = dim(τ³). -/
  supp_den : Nat := 3
  /-- Numerator = fiber_holonomy.dim_tau1. -/
  num_from_base : supp_num = fiber_holonomy.dim_tau1
  /-- Denominator = fiber_holonomy.dim_tau3. -/
  den_from_total : supp_den = fiber_holonomy.dim_tau3
  deriving Repr
```
