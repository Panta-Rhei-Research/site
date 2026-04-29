---
{
  "projection_kind": "taulib_declaration",
  "title": "null_selects_em",
  "permalink": "/verify/taulib/docs/book-v-temporal-macro-readout/null-selects-em/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.MacroReadout`.",
  "declaration_id": "TauLib.BookV.Temporal.MacroReadout::null_selects_em",
  "declaration_slug": "null-selects-em",
  "kind": "theorem",
  "name": "null_selects_em",
  "module_name": "TauLib.BookV.Temporal.MacroReadout",
  "module_url": "/verify/taulib/docs/book-v-temporal-macro-readout/",
  "source_line_start": 82,
  "source_line_end": 83,
  "registry_ids": [
    "V.P06"
  ],
  "related_registry_items": [
    {
      "id": "V.P06",
      "title": "Null Character Uniqueness",
      "url": "/registry/object/V.P06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L82-L83",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.MacroReadout",
        "url": "/verify/taulib/docs/book-v-temporal-macro-readout/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L82-L83",
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

- Module: [TauLib.BookV.Temporal.MacroReadout](/verify/taulib/docs/book-v-temporal-macro-readout/)
- Source path: [`TauLib/BookV/Temporal/MacroReadout.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L82-L83)
- Source range: L82-L83
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P06` — Null Character Uniqueness

## Immediate Comment / Docstring

```lean
/-- [V.P06] The null condition uniquely selects B-sector (EM).
    Only B supports null transport: D/A are depth 1 temporal,
    C is confined (χ₋), Omega is massive (crossing). -/
```

## Source Excerpt

```lean
theorem null_selects_em (n : NullIntertwiner) :
    n.sector = .B := n.null_is_em
```
