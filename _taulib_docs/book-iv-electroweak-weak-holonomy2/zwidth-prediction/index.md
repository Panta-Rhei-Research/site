---
{
  "projection_kind": "taulib_declaration",
  "title": "ZWidthPrediction",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/zwidth-prediction/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy2::ZWidthPrediction",
  "declaration_slug": "zwidth-prediction",
  "kind": "structure",
  "name": "ZWidthPrediction",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/",
  "source_line_start": 227,
  "source_line_end": 237,
  "registry_ids": [
    "IV.P64"
  ],
  "related_registry_items": [
    {
      "id": "IV.P64",
      "title": "Invisible Width and N_nu",
      "url": "/registry/object/IV.P64/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L227-L237",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakHolonomy2",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L227-L237",
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

- Module: [TauLib.BookIV.Electroweak.WeakHolonomy2](/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/)
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L227-L237)
- Source range: L227-L237
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P64` — Invisible Width and N_nu

## Immediate Comment / Docstring

```lean
/-- [IV.P64] The Z boson decay width constrains the number of light
    neutrino generations to exactly 3. Each neutrino flavor adds
    ~167 MeV to the invisible width. The measured invisible width
    (499 MeV) corresponds to N_nu = 2.9840, consistent with 3. -/
```

## Source Excerpt

```lean
structure ZWidthPrediction where
  /-- Number of light neutrino generations. -/
  n_nu : Nat
  n_nu_eq : n_nu = 3
  /-- Invisible width per neutrino (MeV, approximate). -/
  width_per_nu : Nat
  width_approx : width_per_nu = 167
  /-- Total invisible width (MeV, approximate). -/
  total_invisible : Nat
  total_eq : total_invisible = 499
  deriving Repr
```
