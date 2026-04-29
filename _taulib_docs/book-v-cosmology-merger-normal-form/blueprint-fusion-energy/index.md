---
{
  "projection_kind": "taulib_declaration",
  "title": "BlueprintFusionEnergy",
  "permalink": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/blueprint-fusion-energy/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.MergerNormalForm`.",
  "declaration_id": "TauLib.BookV.Cosmology.MergerNormalForm::BlueprintFusionEnergy",
  "declaration_slug": "blueprint-fusion-energy",
  "kind": "structure",
  "name": "BlueprintFusionEnergy",
  "module_name": "TauLib.BookV.Cosmology.MergerNormalForm",
  "module_url": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/",
  "source_line_start": 366,
  "source_line_end": 370,
  "registry_ids": [
    "V.D282"
  ],
  "related_registry_items": [
    {
      "id": "V.D282",
      "title": "Blueprint Fusion Energy",
      "url": "/registry/object/V.D282/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L366-L370",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.MergerNormalForm",
        "url": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L366-L370",
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

- Module: [TauLib.BookV.Cosmology.MergerNormalForm](/verify/taulib/docs/book-v-cosmology-merger-normal-form/)
- Source path: [`TauLib/BookV/Cosmology/MergerNormalForm.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L366-L370)
- Source range: L366-L370
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D282` — Blueprint Fusion Energy

## Immediate Comment / Docstring

```lean
/-- [V.D282] Blueprint fusion energy: radiated fraction
    η = ι_τ² · ν where ν = q/(1+q)² is the symmetric mass ratio.

    Derived from linking-class reduction during blueprint fusion
    at the lemniscate crossing point: pre-merger H₁(L₁)⊕H₁(L₂) ≅ ℤ⁴
    reduces to post-merger H₁(L_final) ≅ ℤ². The two lost classes
    release energy proportional to ι_τ² (D-sector holonomy constraint). -/
```

## Source Excerpt

```lean
structure BlueprintFusionEnergy where
  description : String
  formula : String              -- "η = ι_τ² · ν, ν = q/(1+q)²"
  iota_sq_x10000 : Nat         -- ι_τ² × 10000 ≈ 1165
  deriving Repr
```
