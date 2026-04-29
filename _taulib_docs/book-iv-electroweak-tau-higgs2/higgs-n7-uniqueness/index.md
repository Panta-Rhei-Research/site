---
{
  "projection_kind": "taulib_declaration",
  "title": "HiggsN7Uniqueness",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-n7-uniqueness/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::HiggsN7Uniqueness",
  "declaration_slug": "higgs-n7-uniqueness",
  "kind": "structure",
  "name": "HiggsN7Uniqueness",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 555,
  "source_line_end": 576,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L555-L576",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs2",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L555-L576",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs2](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L555-L576)
- Source range: L555-L576
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [IV.P199 upgrade] Structural uniqueness of n=7.

    The Hessian eigenvalue computation for V_n at level n samples:
    - 2 lobes of L = S¹ ∨ S¹ (providing doublet structure)
    - Each lobe contributes 2 channels (χ⁺/χ⁻ polarity)
    - 3 force sectors {A, B, C} (providing triplet channels)
    - Total: 2·2 + 3 = 7

    n-scan evidence: n=5 gives +892 ppm, n=6 gives +466 ppm,
    n=7 gives +8.0 ppm, n=8 gives −486 ppm.
    n=7 is the unique minimum. -/
```

## Source Excerpt

```lean
structure HiggsN7Uniqueness where
  /-- Number of lobes. -/
  n_lobes : Nat := 2
  /-- Polarity channels per lobe. -/
  polarity_per_lobe : Nat := 2
  /-- Force sectors. -/
  n_sectors : Nat := 3
  /-- n = doublet + triplet. -/
  n_value : Nat := 7
  /-- Structural decomposition. -/
  decomp : n_value = n_lobes * polarity_per_lobe + n_sectors
  /-- Absolute deviation in ppm for n=5 scan point. -/
  dev_n5_ppm : Nat := 892
  /-- Absolute deviation in ppm for n=6 scan point. -/
  dev_n6_ppm : Nat := 466
  /-- Absolute deviation in ppm for n=7 scan point. -/
  dev_n7_ppm : Nat := 8
  /-- Absolute deviation in ppm for n=8 scan point. -/
  dev_n8_ppm : Nat := 486
  /-- n=7 has minimum deviation among scan points. -/
  n7_is_minimum : dev_n7_ppm < dev_n5_ppm ∧ dev_n7_ppm < dev_n6_ppm ∧ dev_n7_ppm < dev_n8_ppm
  deriving Repr
```
