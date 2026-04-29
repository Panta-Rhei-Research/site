---
{
  "projection_kind": "taulib_declaration",
  "title": "tree_level_deviation",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewmixing/tree-level-deviation/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.EWMixing`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWMixing::tree_level_deviation",
  "declaration_slug": "tree-level-deviation",
  "kind": "theorem",
  "name": "tree_level_deviation",
  "module_name": "TauLib.BookIV.Electroweak.EWMixing",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/",
  "source_line_start": 369,
  "source_line_end": 375,
  "registry_ids": [
    "IV.P69"
  ],
  "related_registry_items": [
    {
      "id": "IV.P69",
      "title": "Weinberg Angle Residual Analysis",
      "url": "/registry/object/IV.P69/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L369-L375",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWMixing",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L369-L375",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookIV.Electroweak.EWMixing](/verify/taulib/docs/book-iv-electroweak-ewmixing/)
- Source path: [`TauLib/BookIV/Electroweak/EWMixing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L369-L375)
- Source range: L369-L375
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P69` — Weinberg Angle Residual Analysis

## Immediate Comment / Docstring

```lean
/-- [IV.P69] Tree-level deviation: τ predicts 0.2249, experiment gives 0.2312.
    The deviation is |0.2312 - 0.2249| / 0.2312 ≈ 2.7%.

    This is EXPECTED at tree level. Loop corrections (radiative, threshold)
    close the gap, analogous to running coupling constants in QFT. -/
```

## Source Excerpt

```lean
theorem tree_level_deviation :
    sin2_exp_numer * weinberg_angle_tau.sin2_denom >
    weinberg_angle_tau.sin2_numer * sin2_exp_denom ∧
    (sin2_exp_numer * weinberg_angle_tau.sin2_denom -
     weinberg_angle_tau.sin2_numer * sin2_exp_denom) * 100 <
    4 * sin2_exp_numer * weinberg_angle_tau.sin2_denom := by
  exact ⟨by native_decide, by native_decide⟩
```
