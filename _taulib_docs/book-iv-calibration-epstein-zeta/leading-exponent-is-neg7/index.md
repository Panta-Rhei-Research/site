---
{
  "projection_kind": "taulib_declaration",
  "title": "leading_exponent_is_neg7",
  "permalink": "/verify/taulib/docs/book-iv-calibration-epstein-zeta/leading-exponent-is-neg7/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.EpsteinZeta`.",
  "declaration_id": "TauLib.BookIV.Calibration.EpsteinZeta::leading_exponent_is_neg7",
  "declaration_slug": "leading-exponent-is-neg7",
  "kind": "theorem",
  "name": "leading_exponent_is_neg7",
  "module_name": "TauLib.BookIV.Calibration.EpsteinZeta",
  "module_url": "/verify/taulib/docs/book-iv-calibration-epstein-zeta/",
  "source_line_start": 132,
  "source_line_end": 133,
  "registry_ids": [
    "IV.T10"
  ],
  "related_registry_items": [
    {
      "id": "IV.T10",
      "title": "Leading Exponent",
      "url": "/registry/object/IV.T10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/EpsteinZeta.lean#L132-L133",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.EpsteinZeta",
        "url": "/verify/taulib/docs/book-iv-calibration-epstein-zeta/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/EpsteinZeta.lean#L132-L133",
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

- Module: [TauLib.BookIV.Calibration.EpsteinZeta](/verify/taulib/docs/book-iv-calibration-epstein-zeta/)
- Source path: [`TauLib/BookIV/Calibration/EpsteinZeta.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/EpsteinZeta.lean#L132-L133)
- Source range: L132-L133
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T10` — Leading Exponent

## Immediate Comment / Docstring

```lean
/-- [IV.T10] The Chowla-Selberg leading exponent at s = 4 is -7.

    This is the origin of ι_τ^(-7) in the mass ratio formula:
    the Epstein zeta function Z(4; iι_τ) has its leading term
    proportional to ι_τ^(1-2×4) = ι_τ^(-7). -/
```

## Source Excerpt

```lean
theorem leading_exponent_is_neg7 :
    chowla_selberg_s4.leading_exp = -7 := by rfl
```
