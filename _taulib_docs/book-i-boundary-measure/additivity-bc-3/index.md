---
{
  "projection_kind": "taulib_declaration",
  "title": "additivity_bc_3",
  "permalink": "/verify/taulib/docs/book-i-boundary-measure/additivity-bc-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Measure`.",
  "declaration_id": "TauLib.BookI.Boundary.Measure::additivity_bc_3",
  "declaration_slug": "additivity-bc-3",
  "kind": "theorem",
  "name": "additivity_bc_3",
  "module_name": "TauLib.BookI.Boundary.Measure",
  "module_url": "/verify/taulib/docs/book-i-boundary-measure/",
  "source_line_start": 191,
  "source_line_end": 193,
  "registry_ids": [
    "I.T49"
  ],
  "related_registry_items": [
    {
      "id": "I.T49",
      "title": "Countable Additivity",
      "url": "/registry/object/I.T49/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L191-L193",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Measure",
        "url": "/verify/taulib/docs/book-i-boundary-measure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L191-L193",
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

- Module: [TauLib.BookI.Boundary.Measure](/verify/taulib/docs/book-i-boundary-measure/)
- Source path: [`TauLib/BookI/Boundary/Measure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L191-L193)
- Source range: L191-L193
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T49` — Countable Additivity

## Immediate Comment / Docstring

```lean
/-- [I.T49] Additivity for B/C sector partition at stage 3. -/
```

## Source Excerpt

```lean
theorem additivity_bc_3 :
    countable_additivity_check (fun x => x % 4 == 1)
      (fun x => x % 4 == 3) 3 = true := by native_decide
```
