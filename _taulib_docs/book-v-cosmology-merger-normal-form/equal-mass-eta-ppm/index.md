---
{
  "projection_kind": "taulib_declaration",
  "title": "equal_mass_eta_ppm",
  "permalink": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/equal-mass-eta-ppm/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.MergerNormalForm`.",
  "declaration_id": "TauLib.BookV.Cosmology.MergerNormalForm::equal_mass_eta_ppm",
  "declaration_slug": "equal-mass-eta-ppm",
  "kind": "def",
  "name": "equal_mass_eta_ppm",
  "module_name": "TauLib.BookV.Cosmology.MergerNormalForm",
  "module_url": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/",
  "source_line_start": 381,
  "source_line_end": 381,
  "registry_ids": [
    "V.P150"
  ],
  "related_registry_items": [
    {
      "id": "V.P150",
      "title": "Equal-Mass Energy Fraction",
      "url": "/registry/object/V.P150/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L381-L381",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L381-L381",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookV/Cosmology/MergerNormalForm.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L381-L381)
- Source range: L381-L381
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.P150` — Equal-Mass Energy Fraction

## Immediate Comment / Docstring

```lean
/-- [V.P150] Equal-mass energy fraction:
    η(q=1) = ι_τ²/4 ≈ 0.02912, stored as parts per million. -/
```

## Source Excerpt

```lean
def equal_mass_eta_ppm : Nat := 29122  -- ι_τ²/4 × 10⁶
```
