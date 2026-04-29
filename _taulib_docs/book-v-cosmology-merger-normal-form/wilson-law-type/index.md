---
{
  "projection_kind": "taulib_declaration",
  "title": "WilsonLawType",
  "permalink": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/wilson-law-type/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Cosmology.MergerNormalForm`.",
  "declaration_id": "TauLib.BookV.Cosmology.MergerNormalForm::WilsonLawType",
  "declaration_slug": "wilson-law-type",
  "kind": "inductive",
  "name": "WilsonLawType",
  "module_name": "TauLib.BookV.Cosmology.MergerNormalForm",
  "module_url": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/",
  "source_line_start": 204,
  "source_line_end": 209,
  "registry_ids": [
    "V.D177"
  ],
  "related_registry_items": [
    {
      "id": "V.D177",
      "title": "Base Wilson loop",
      "url": "/registry/object/V.D177/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L204-L209",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L204-L209",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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
- Source path: [`TauLib/BookV/Cosmology/MergerNormalForm.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L204-L209)
- Source range: L204-L209
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `V.D177` — Base Wilson loop

## Immediate Comment / Docstring

```lean
/-- [V.D177] Base Wilson loop W_n = Tr(Hol_∂(τ¹; n)):
    the trace of the boundary holonomy around τ¹ at refinement depth n.

    Wilson loops diagnose confinement vs. deconfinement:
    - Area law ⟹ confinement (strong sector)
    - Perimeter law ⟹ deconfinement (gravitational sector) -/
```

## Source Excerpt

```lean
inductive WilsonLawType where
  /-- Perimeter law: W ~ exp(−κ·L), deconfined. -/
  | PerimeterLaw
  /-- Area law: W ~ exp(−σ·A), confined. -/
  | AreaLaw
  deriving Repr, DecidableEq, BEq
```
