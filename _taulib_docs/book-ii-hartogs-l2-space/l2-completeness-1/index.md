---
{
  "projection_kind": "taulib_declaration",
  "title": "l2_completeness_1",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-l2-space/l2-completeness-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.L2Space`.",
  "declaration_id": "TauLib.BookII.Hartogs.L2Space::l2_completeness_1",
  "declaration_slug": "l2-completeness-1",
  "kind": "theorem",
  "name": "l2_completeness_1",
  "module_name": "TauLib.BookII.Hartogs.L2Space",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-l2-space/",
  "source_line_start": 217,
  "source_line_end": 218,
  "registry_ids": [
    "II.P18"
  ],
  "related_registry_items": [
    {
      "id": "II.P18",
      "title": "L² Completeness",
      "url": "/registry/object/II.P18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L217-L218",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.L2Space",
        "url": "/verify/taulib/docs/book-ii-hartogs-l2-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L217-L218",
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

- Module: [TauLib.BookII.Hartogs.L2Space](/verify/taulib/docs/book-ii-hartogs-l2-space/)
- Source path: [`TauLib/BookII/Hartogs/L2Space.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L217-L218)
- Source range: L217-L218
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.P18` — L² Completeness

## Immediate Comment / Docstring

```lean
/-- [II.P18] L² completeness at stage 1. -/
```

## Source Excerpt

```lean
theorem l2_completeness_1 :
    l2_completeness_check 1 = true := by native_decide
```
