---
{
  "projection_kind": "taulib_declaration",
  "title": "ReadoutStatus",
  "permalink": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/readout-status/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Orthodox.MeasurementUnification`.",
  "declaration_id": "TauLib.BookV.Orthodox.MeasurementUnification::ReadoutStatus",
  "declaration_slug": "readout-status",
  "kind": "inductive",
  "name": "ReadoutStatus",
  "module_name": "TauLib.BookV.Orthodox.MeasurementUnification",
  "module_url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/",
  "source_line_start": 66,
  "source_line_end": 71,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L66-L71",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.MeasurementUnification",
        "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L66-L71",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookV.Orthodox.MeasurementUnification](/corpus/taulib/docs/book-v-orthodox-measurement-unification/)
- Source path: [`TauLib/BookV/Orthodox/MeasurementUnification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L66-L71)
- Source range: L66-L71
- Kind: `inductive`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Readout status of a quantum state. -/
```

## Source Excerpt

```lean
inductive ReadoutStatus where
  /-- Unresolved: superposition in the VM (no address resolution yet). -/
  | Unresolved
  /-- Resolved: definite boundary character selected. -/
  | Resolved
  deriving Repr, DecidableEq, BEq
```
