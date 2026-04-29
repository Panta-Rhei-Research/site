---
{
  "projection_kind": "taulib_declaration",
  "title": "MeasurementDissolution",
  "permalink": "/verify/taulib/docs/book-v-orthodox-measurement-unification/measurement-dissolution/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Orthodox.MeasurementUnification`.",
  "declaration_id": "TauLib.BookV.Orthodox.MeasurementUnification::MeasurementDissolution",
  "declaration_slug": "measurement-dissolution",
  "kind": "structure",
  "name": "MeasurementDissolution",
  "module_name": "TauLib.BookV.Orthodox.MeasurementUnification",
  "module_url": "/verify/taulib/docs/book-v-orthodox-measurement-unification/",
  "source_line_start": 107,
  "source_line_end": 116,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L107-L116",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.MeasurementUnification",
        "url": "/verify/taulib/docs/book-v-orthodox-measurement-unification/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L107-L116",
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

- Module: [TauLib.BookV.Orthodox.MeasurementUnification](/verify/taulib/docs/book-v-orthodox-measurement-unification/)
- Source path: [`TauLib/BookV/Orthodox/MeasurementUnification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L107-L116)
- Source range: L107-L116
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The three-part dissolution of the measurement problem. -/
```

## Source Excerpt

```lean
structure MeasurementDissolution where
  /-- Part 1: unitary evolution = character evolution readout. -/
  unitary_is_readout : Bool := true
  /-- Part 2: collapse = address resolution (not physical). -/
  collapse_is_address_resolution : Bool := true
  /-- Part 3: Born rule = Pythagorean theorem on characters. -/
  born_from_pythagorean : Bool := true
  /-- All three parts hold. -/
  all_parts : Bool := true
  deriving Repr
```
