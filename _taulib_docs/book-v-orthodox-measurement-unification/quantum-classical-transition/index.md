---
{
  "projection_kind": "taulib_declaration",
  "title": "QuantumClassicalTransition",
  "permalink": "/verify/taulib/docs/book-v-orthodox-measurement-unification/quantum-classical-transition/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Orthodox.MeasurementUnification`.",
  "declaration_id": "TauLib.BookV.Orthodox.MeasurementUnification::QuantumClassicalTransition",
  "declaration_slug": "quantum-classical-transition",
  "kind": "structure",
  "name": "QuantumClassicalTransition",
  "module_name": "TauLib.BookV.Orthodox.MeasurementUnification",
  "module_url": "/verify/taulib/docs/book-v-orthodox-measurement-unification/",
  "source_line_start": 251,
  "source_line_end": 258,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L251-L258",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L251-L258",
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
- Source path: [`TauLib/BookV/Orthodox/MeasurementUnification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L251-L258)
- Source range: L251-L258
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The quantum-classical transition is a change of VM zoom level,
    not a physical boundary.

    At fine resolution: individual boundary characters visible
    (quantum regime)
    At coarse resolution: averaged over many characters
    (classical regime)

    There is no physical "Heisenberg cut." -/
```

## Source Excerpt

```lean
structure QuantumClassicalTransition where
  /-- Fine resolution sees individual characters. -/
  fine_sees_individual : Bool := true
  /-- Coarse resolution sees averages. -/
  coarse_sees_average : Bool := true
  /-- No physical Heisenberg cut. -/
  no_heisenberg_cut : Bool := true
  deriving Repr
```
