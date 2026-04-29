---
{
  "projection_kind": "taulib_declaration",
  "title": "empty_set_measure_3",
  "permalink": "/verify/taulib/docs/book-i-boundary-measure/empty-set-measure-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Measure`.",
  "declaration_id": "TauLib.BookI.Boundary.Measure::empty_set_measure_3",
  "declaration_slug": "empty-set-measure-3",
  "kind": "theorem",
  "name": "empty_set_measure_3",
  "module_name": "TauLib.BookI.Boundary.Measure",
  "module_url": "/verify/taulib/docs/book-i-boundary-measure/",
  "source_line_start": 212,
  "source_line_end": 213,
  "registry_ids": [
    "I.D95"
  ],
  "related_registry_items": [
    {
      "id": "I.D95",
      "title": "τ-Measure Space",
      "url": "/registry/object/I.D95/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L212-L213",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L212-L213",
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
- Source path: [`TauLib/BookI/Boundary/Measure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L212-L213)
- Source range: L212-L213
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.D95` — τ-Measure Space

## Immediate Comment / Docstring

```lean
/-- [I.D95] Empty set measure at stage 3: 0 / M_3 = 0. -/
```

## Source Excerpt

```lean
theorem empty_set_measure_3 :
    count_satisfying (fun _ => false) 3 = 0 := by native_decide
```
