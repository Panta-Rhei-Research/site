---
{
  "projection_kind": "taulib_declaration",
  "title": "BHMassScale",
  "permalink": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/bhmass-scale/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.MergerNormalForm`.",
  "declaration_id": "TauLib.BookV.Cosmology.MergerNormalForm::BHMassScale",
  "declaration_slug": "bhmass-scale",
  "kind": "structure",
  "name": "BHMassScale",
  "module_name": "TauLib.BookV.Cosmology.MergerNormalForm",
  "module_url": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/",
  "source_line_start": 141,
  "source_line_end": 152,
  "registry_ids": [
    "V.D176"
  ],
  "related_registry_items": [
    {
      "id": "V.D176",
      "title": "BH mass scale at depth n",
      "url": "/registry/object/V.D176/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L141-L152",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L141-L152",
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
- Source path: [`TauLib/BookV/Cosmology/MergerNormalForm.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L141-L152)
- Source range: L141-L152
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D176` — BH mass scale at depth n

## Immediate Comment / Docstring

```lean
/-- [V.D176] BH mass scale at refinement depth n:
    M_n = m_n · κ(D;1) = m_n · (1 − ι_τ).

    κ(D;1) ≈ 0.6585. The mass scale decreases with depth because m_n
    decreases as the refinement goes deeper (smaller structures). -/
```

## Source Excerpt

```lean
structure BHMassScale where
  /-- Primorial level index. -/
  level : Nat
  /-- Level positive. -/
  level_pos : level > 0
  /-- Mass scale numerator. -/
  mass_numer : Nat
  /-- Mass scale denominator. -/
  mass_denom : Nat
  /-- Denominator positive. -/
  denom_pos : mass_denom > 0
  deriving Repr
```
