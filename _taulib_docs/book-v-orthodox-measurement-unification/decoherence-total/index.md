---
{
  "projection_kind": "taulib_declaration",
  "title": "decoherence_total",
  "permalink": "/verify/taulib/docs/book-v-orthodox-measurement-unification/decoherence-total/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Orthodox.MeasurementUnification`.",
  "declaration_id": "TauLib.BookV.Orthodox.MeasurementUnification::decoherence_total",
  "declaration_slug": "decoherence-total",
  "kind": "theorem",
  "name": "decoherence_total",
  "module_name": "TauLib.BookV.Orthodox.MeasurementUnification",
  "module_url": "/verify/taulib/docs/book-v-orthodox-measurement-unification/",
  "source_line_start": 235,
  "source_line_end": 236,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L235-L236",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L235-L236",
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

- Module: [TauLib.BookV.Orthodox.MeasurementUnification](/verify/taulib/docs/book-v-orthodox-measurement-unification/)
- Source path: [`TauLib/BookV/Orthodox/MeasurementUnification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L235-L236)
- Source range: L235-L236
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The total character count is the sum of system and environment. -/
```

## Source Excerpt

```lean
theorem decoherence_total (d : DecoherenceShadow) :
    d.total = d.system_chars + d.env_chars := d.total_eq
```
