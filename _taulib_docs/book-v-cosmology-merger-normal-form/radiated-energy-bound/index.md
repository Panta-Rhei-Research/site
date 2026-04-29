---
{
  "projection_kind": "taulib_declaration",
  "title": "RadiatedEnergyBound",
  "permalink": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/radiated-energy-bound/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.MergerNormalForm`.",
  "declaration_id": "TauLib.BookV.Cosmology.MergerNormalForm::RadiatedEnergyBound",
  "declaration_slug": "radiated-energy-bound",
  "kind": "structure",
  "name": "RadiatedEnergyBound",
  "module_name": "TauLib.BookV.Cosmology.MergerNormalForm",
  "module_url": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/",
  "source_line_start": 267,
  "source_line_end": 276,
  "registry_ids": [
    "V.P101"
  ],
  "related_registry_items": [
    {
      "id": "V.P101",
      "title": "Radiated energy bound",
      "url": "/registry/object/V.P101/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L267-L276",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L267-L276",
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
- Source path: [`TauLib/BookV/Cosmology/MergerNormalForm.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L267-L276)
- Source range: L267-L276
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P101` — Radiated energy bound

## Immediate Comment / Docstring

```lean
/-- [V.P101] Radiated energy bound: ΔE / ((M₁+M₂)c²) ≤ 1 − 1/√2.

    1 − 1/√2 ≈ 0.2929. Encoded as 2929/10000.
    This is the Penrose extraction limit for Kerr BHs. In τ, the
    same bound arises from the blueprint monoid structure. -/
```

## Source Excerpt

```lean
structure RadiatedEnergyBound where
  /-- Bound numerator. -/
  bound_numer : Nat
  /-- Bound denominator. -/
  bound_denom : Nat
  /-- Denominator positive. -/
  denom_pos : bound_denom > 0
  /-- Bound is approximately 0.293: 2929/10000. -/
  approx : bound_numer > 2900 ∧ bound_numer < 3000
  deriving Repr
```
