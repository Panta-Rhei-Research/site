---
{
  "projection_kind": "taulib_declaration",
  "title": "correction_lt_2_per_mille",
  "permalink": "/verify/taulib/docs/book-iv-physics-holonomy-correction/correction-lt-2-per-mille/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.HolonomyCorrection`.",
  "declaration_id": "TauLib.BookIV.Physics.HolonomyCorrection::correction_lt_2_per_mille",
  "declaration_slug": "correction-lt-2-per-mille",
  "kind": "theorem",
  "name": "correction_lt_2_per_mille",
  "module_name": "TauLib.BookIV.Physics.HolonomyCorrection",
  "module_url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/",
  "source_line_start": 188,
  "source_line_end": 193,
  "registry_ids": [
    "IV.T12"
  ],
  "related_registry_items": [
    {
      "id": "IV.T12",
      "title": "Correction Smallness",
      "url": "/registry/object/IV.T12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L188-L193",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.HolonomyCorrection",
        "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L188-L193",
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

- Module: [TauLib.BookIV.Physics.HolonomyCorrection](/verify/taulib/docs/book-iv-physics-holonomy-correction/)
- Source path: [`TauLib/BookIV/Physics/HolonomyCorrection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L188-L193)
- Source range: L188-L193
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T12` — Correction Smallness

## Immediate Comment / Docstring

```lean
/-- [IV.T12] The holonomy correction π³α² < 0.002.

    This proves the perturbative hierarchy:
    π³α² ≈ 0.00165 << √3 ≈ 1.732

    Cross-multiplied: numer × 1000 < 2 × denom. -/
```

## Source Excerpt

```lean
theorem correction_lt_2_per_mille :
    holonomy_correction.numer * 1000 < 2 * holonomy_correction.denom := by
  simp [holonomy_correction, pi_cubed_numer, pi_cubed_denom,
        alpha_sq_numer, alpha_sq_denom,
        iota_fourth_numer, iota_fourth_denom,
        iota, iotaD, iota_tau_numer, iota_tau_denom]
```
