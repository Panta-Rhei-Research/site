---
{
  "projection_kind": "taulib_declaration",
  "title": "PrimorialMassGap",
  "permalink": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/primorial-mass-gap/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.MergerNormalForm`.",
  "declaration_id": "TauLib.BookV.Cosmology.MergerNormalForm::PrimorialMassGap",
  "declaration_slug": "primorial-mass-gap",
  "kind": "structure",
  "name": "PrimorialMassGap",
  "module_name": "TauLib.BookV.Cosmology.MergerNormalForm",
  "module_url": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/",
  "source_line_start": 164,
  "source_line_end": 175,
  "registry_ids": [
    "V.P98"
  ],
  "related_registry_items": [
    {
      "id": "V.P98",
      "title": "Mass gap between adjacent primorial levels",
      "url": "/registry/object/V.P98/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L164-L175",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L164-L175",
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
- Source path: [`TauLib/BookV/Cosmology/MergerNormalForm.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L164-L175)
- Source range: L164-L175
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P98` — Mass gap between adjacent primorial levels

## Immediate Comment / Docstring

```lean
/-- [V.P98] Mass gap between adjacent primorial levels:
    M_n / M_{n+1} ~ p_{n+1} (next prime).

    The primorial mass hierarchy predicts a natural gap in the
    BH mass spectrum. This may explain the intermediate-mass
    black hole (IMBH) desert. -/
```

## Source Excerpt

```lean
structure PrimorialMassGap where
  /-- Level n. -/
  level_n : Nat
  /-- Level n+1. -/
  level_np1 : Nat
  /-- Adjacent levels. -/
  adjacent : level_np1 = level_n + 1
  /-- Gap ratio (approximate: next prime at that level). -/
  gap_ratio : Nat
  /-- Gap is at least 2 (smallest prime). -/
  gap_min : gap_ratio ≥ 2
  deriving Repr
```
