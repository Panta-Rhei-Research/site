---
{
  "projection_kind": "taulib_declaration",
  "title": "FiberHolonomyCorrection",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/fiber-holonomy-correction/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BBNNuclearNetwork`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNNuclearNetwork::FiberHolonomyCorrection",
  "declaration_slug": "fiber-holonomy-correction",
  "kind": "structure",
  "name": "FiberHolonomyCorrection",
  "module_name": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/",
  "source_line_start": 214,
  "source_line_end": 223,
  "registry_ids": [
    "V.D305"
  ],
  "related_registry_items": [
    {
      "id": "V.D305",
      "title": "T² Fiber Holonomy Correction",
      "url": "/registry/object/V.D305/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L214-L223",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L214-L223",
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
- Source path: [`TauLib/BookV/Cosmology/BBNNuclearNetwork.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L214-L223)
- Source range: L214-L223
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D305` — T² Fiber Holonomy Correction

## Immediate Comment / Docstring

```lean
/-- [V.D305] T² fiber holonomy correction for EM captures.
    At ⁷Be formation temperature, the B-sector EM capture
    phase space is restricted to the base τ¹. -/
```

## Source Excerpt

```lean
structure FiberHolonomyCorrection where
  /-- Dimension of τ¹ (base). -/
  dim_tau1 : Nat := 1
  /-- Dimension of T² (fiber). -/
  dim_T2 : Nat := 2
  /-- Dimension of τ³ (total). -/
  dim_tau3 : Nat := 3
  /-- τ³ = τ¹ ×_f T², so dim(τ³) = dim(τ¹) + dim(T²). -/
  fibration_dim : dim_tau3 = dim_tau1 + dim_T2
  deriving Repr
```
