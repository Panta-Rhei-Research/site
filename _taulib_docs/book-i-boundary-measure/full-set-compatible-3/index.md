---
{
  "projection_kind": "taulib_declaration",
  "title": "full_set_compatible_3",
  "permalink": "/verify/taulib/docs/book-i-boundary-measure/full-set-compatible-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Measure`.",
  "declaration_id": "TauLib.BookI.Boundary.Measure::full_set_compatible_3",
  "declaration_slug": "full-set-compatible-3",
  "kind": "theorem",
  "name": "full_set_compatible_3",
  "module_name": "TauLib.BookI.Boundary.Measure",
  "module_url": "/verify/taulib/docs/book-i-boundary-measure/",
  "source_line_start": 196,
  "source_line_end": 197,
  "registry_ids": [
    "I.P43"
  ],
  "related_registry_items": [
    {
      "id": "I.P43",
      "title": "Measure Compatibility",
      "url": "/registry/object/I.P43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L196-L197",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L196-L197",
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
- Source path: [`TauLib/BookI/Boundary/Measure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Measure.lean#L196-L197)
- Source range: L196-L197
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P43` — Measure Compatibility

## Immediate Comment / Docstring

```lean
/-- [I.P43] Full set is tower-compatible up to stage 3. -/
```

## Source Excerpt

```lean
theorem full_set_compatible_3 :
    sigma_algebra_check full_set 3 = true := by native_decide
```
