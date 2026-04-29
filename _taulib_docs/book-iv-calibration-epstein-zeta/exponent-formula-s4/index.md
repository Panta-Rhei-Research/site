---
{
  "projection_kind": "taulib_declaration",
  "title": "exponent_formula_s4",
  "permalink": "/verify/taulib/docs/book-iv-calibration-epstein-zeta/exponent-formula-s4/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.EpsteinZeta`.",
  "declaration_id": "TauLib.BookIV.Calibration.EpsteinZeta::exponent_formula_s4",
  "declaration_slug": "exponent-formula-s4",
  "kind": "theorem",
  "name": "exponent_formula_s4",
  "module_name": "TauLib.BookIV.Calibration.EpsteinZeta",
  "module_url": "/verify/taulib/docs/book-iv-calibration-epstein-zeta/",
  "source_line_start": 136,
  "source_line_end": 137,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/EpsteinZeta.lean#L136-L137",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/EpsteinZeta.lean#L136-L137",
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
- Source path: [`TauLib/BookIV/Calibration/EpsteinZeta.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/EpsteinZeta.lean#L136-L137)
- Source range: L136-L137
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- At s = 4, the exponent formula gives 1 - 8 = -7. -/
```

## Source Excerpt

```lean
theorem exponent_formula_s4 :
    (1 : Int) - 2 * (4 : Int) = -7 := by omega
```
