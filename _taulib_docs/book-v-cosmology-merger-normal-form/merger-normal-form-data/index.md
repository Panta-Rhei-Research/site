---
{
  "projection_kind": "taulib_declaration",
  "title": "MergerNormalFormData",
  "permalink": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/merger-normal-form-data/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.MergerNormalForm`.",
  "declaration_id": "TauLib.BookV.Cosmology.MergerNormalForm::MergerNormalFormData",
  "declaration_slug": "merger-normal-form-data",
  "kind": "structure",
  "name": "MergerNormalFormData",
  "module_name": "TauLib.BookV.Cosmology.MergerNormalForm",
  "module_url": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/",
  "source_line_start": 76,
  "source_line_end": 92,
  "registry_ids": [
    "V.T115"
  ],
  "related_registry_items": [
    {
      "id": "V.T115",
      "title": "Merger Normal Form",
      "url": "/registry/object/V.T115/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L76-L92",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L76-L92",
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
- Source path: [`TauLib/BookV/Cosmology/MergerNormalForm.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L76-L92)
- Source range: L76-L92
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T115` — Merger Normal Form

## Immediate Comment / Docstring

```lean
/-- [V.T115] Merger normal form: when two single-excision BHs
    satisfy the approach condition, the merger produces a single
    excision with determined mass and angular momentum.

    M_final ≤ M₁ + M₂ (energy radiated as GW).
    M_final ≥ max(M₁, M₂) (no-shrink for final BH). -/
```

## Source Excerpt

```lean
structure MergerNormalFormData where
  /-- Mass of BH 1 (scaled). -/
  mass_1 : Nat
  /-- Mass of BH 2 (scaled). -/
  mass_2 : Nat
  /-- Mass of final BH (scaled). -/
  mass_final : Nat
  /-- Radiated energy (scaled, = M₁ + M₂ − M_final). -/
  radiated : Nat
  /-- Both masses positive. -/
  mass1_pos : mass_1 > 0
  mass2_pos : mass_2 > 0
  /-- Final mass is sum minus radiated. -/
  mass_balance : mass_final + radiated = mass_1 + mass_2
  /-- Final mass at least max of inputs. -/
  no_shrink : mass_final ≥ mass_1 ∨ mass_final ≥ mass_2
  deriving Repr
```
