---
{
  "projection_kind": "taulib_declaration",
  "title": "SIConstant",
  "permalink": "/verify/taulib/docs/book-iv-calibration-sireference/siconstant/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.SIReference`.",
  "declaration_id": "TauLib.BookIV.Calibration.SIReference::SIConstant",
  "declaration_slug": "siconstant",
  "kind": "structure",
  "name": "SIConstant",
  "module_name": "TauLib.BookIV.Calibration.SIReference",
  "module_url": "/verify/taulib/docs/book-iv-calibration-sireference/",
  "source_line_start": 51,
  "source_line_end": 62,
  "registry_ids": [
    "IV.D26"
  ],
  "related_registry_items": [
    {
      "id": "IV.D26",
      "title": "SI Reference Table",
      "url": "/registry/object/IV.D26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L51-L62",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.SIReference",
        "url": "/verify/taulib/docs/book-iv-calibration-sireference/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L51-L62",
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

- Module: [TauLib.BookIV.Calibration.SIReference](/verify/taulib/docs/book-iv-calibration-sireference/)
- Source path: [`TauLib/BookIV/Calibration/SIReference.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L51-L62)
- Source range: L51-L62
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D26` — SI Reference Table

## Immediate Comment / Docstring

```lean
/-- [IV.D26] An SI physical constant stored as an exact scaled rational.
    The actual SI value is `numer / denom` in the appropriate SI unit.
    `is_exact = true` for constants that are exact by SI 2019 definition. -/
```

## Source Excerpt

```lean
structure SIConstant where
  /-- Display name of the constant. -/
  name : String
  /-- Scaled numerator. -/
  numer : Nat
  /-- Scale denominator. -/
  denom : Nat
  /-- Denominator is positive. -/
  denom_pos : denom > 0
  /-- True if the value is exact by SI definition (not measured). -/
  is_exact : Bool
  deriving Repr
```
