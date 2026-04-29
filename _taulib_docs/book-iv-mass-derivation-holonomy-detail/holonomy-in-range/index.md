---
{
  "projection_kind": "taulib_declaration",
  "title": "holonomy_in_range",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-holonomy-detail/holonomy-in-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.MassDerivation.HolonomyDetail`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.HolonomyDetail::holonomy_in_range",
  "declaration_slug": "holonomy-in-range",
  "kind": "theorem",
  "name": "holonomy_in_range",
  "module_name": "TauLib.BookIV.MassDerivation.HolonomyDetail",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-holonomy-detail/",
  "source_line_start": 129,
  "source_line_end": 132,
  "registry_ids": [
    "IV.T116"
  ],
  "related_registry_items": [
    {
      "id": "IV.T116",
      "title": "Correction Smallness --- IV.T12",
      "url": "/registry/object/IV.T116/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L129-L132",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.MassDerivation.HolonomyDetail",
        "url": "/verify/taulib/docs/book-iv-mass-derivation-holonomy-detail/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L129-L132",
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

- Module: [TauLib.BookIV.MassDerivation.HolonomyDetail](/verify/taulib/docs/book-iv-mass-derivation-holonomy-detail/)
- Source path: [`TauLib/BookIV/MassDerivation/HolonomyDetail.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L129-L132)
- Source range: L129-L132
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T116` — Correction Smallness --- IV.T12

## Immediate Comment / Docstring

```lean
/-- [IV.T116] The holonomy correction π³α² is in (0.001, 0.002).

    This wraps the range proofs from HolonomyCorrection:
    - π³α² > 0.001 (correction_gt_1_per_mille)
    - π³α² < 0.002 (correction_lt_2_per_mille)

    Combined: π³α² ∈ (0.001, 0.002), confirming the
    perturbative hierarchy (π³α² << √3 by a factor of ~1050). -/
```

## Source Excerpt

```lean
theorem holonomy_in_range :
    holonomy_correction.numer * 1000 > holonomy_correction.denom ∧
    holonomy_correction.numer * 1000 < 2 * holonomy_correction.denom :=
  ⟨correction_gt_1_per_mille, correction_lt_2_per_mille⟩
```
