---
{
  "projection_kind": "taulib_declaration",
  "title": "r0_lt_1840",
  "permalink": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/r0-lt-1840/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.MassRatioFormula`.",
  "declaration_id": "TauLib.BookIV.Calibration.MassRatioFormula::r0_lt_1840",
  "declaration_slug": "r0-lt-1840",
  "kind": "theorem",
  "name": "r0_lt_1840",
  "module_name": "TauLib.BookIV.Calibration.MassRatioFormula",
  "module_url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/",
  "source_line_start": 196,
  "source_line_end": 199,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L196-L199",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.MassRatioFormula",
        "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L196-L199",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIV.Calibration.MassRatioFormula](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/)
- Source path: [`TauLib/BookIV/Calibration/MassRatioFormula.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L196-L199)
- Source range: L196-L199
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- R₀ < 1840.
    bulk_numer × correction0_denom < correction0_numer × bulk_denom + 1840 × bulk_denom × correction0_denom -/
```

## Source Excerpt

```lean
theorem r0_lt_1840 :
    bulk_numer * correction0_denom <
    correction0_numer * bulk_denom + 1840 * bulk_denom * correction0_denom := by
  native_decide
```
