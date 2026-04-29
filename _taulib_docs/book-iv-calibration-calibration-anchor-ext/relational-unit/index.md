---
{
  "projection_kind": "taulib_declaration",
  "title": "RelationalUnit",
  "permalink": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/relational-unit/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.CalibrationAnchorExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.CalibrationAnchorExt::RelationalUnit",
  "declaration_slug": "relational-unit",
  "kind": "structure",
  "name": "RelationalUnit",
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchorExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/",
  "source_line_start": 70,
  "source_line_end": 81,
  "registry_ids": [
    "IV.D289"
  ],
  "related_registry_items": [
    {
      "id": "IV.D289",
      "title": "Five Relational Units",
      "url": "/registry/object/IV.D289/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L70-L81",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.CalibrationAnchorExt",
        "url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L70-L81",
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

- Module: [TauLib.BookIV.Calibration.CalibrationAnchorExt](/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/)
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchorExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L70-L81)
- Source range: L70-L81
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D289` — Five Relational Units

## Immediate Comment / Docstring

```lean
/-- [IV.D289] A relational unit from the Springer Nature paper.

    The paper used five independent quantities (M, L, H, Q, R).
    Each has a symbol, a physical meaning, and a scaled Nat value
    (encoding the dimensional constant in appropriate SI units). -/
```

## Source Excerpt

```lean
structure RelationalUnit where
  /-- Symbol: M, L, H, Q, or R. -/
  symbol : String
  /-- Physical interpretation. -/
  meaning : String
  /-- Scaled numerator (SI value encoding). -/
  scaled_numer : Nat
  /-- Scaled denominator (SI value encoding). -/
  scaled_denom : Nat
  /-- Denominator is positive. -/
  denom_pos : scaled_denom > 0
  deriving Repr
```
