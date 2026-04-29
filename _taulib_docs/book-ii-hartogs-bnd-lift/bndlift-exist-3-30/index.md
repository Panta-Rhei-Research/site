---
{
  "projection_kind": "taulib_declaration",
  "title": "bndlift_exist_3_30",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/bndlift-exist-3-30/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.BndLift`.",
  "declaration_id": "TauLib.BookII.Hartogs.BndLift::bndlift_exist_3_30",
  "declaration_slug": "bndlift-exist-3-30",
  "kind": "theorem",
  "name": "bndlift_exist_3_30",
  "module_name": "TauLib.BookII.Hartogs.BndLift",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/",
  "source_line_start": 453,
  "source_line_end": 453,
  "registry_ids": [
    "II.T26"
  ],
  "related_registry_items": [
    {
      "id": "II.T26",
      "title": "BndLift Existence",
      "url": "/registry/object/II.T26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L453-L453",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.BndLift",
        "url": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L453-L453",
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

- Module: [TauLib.BookII.Hartogs.BndLift](/verify/taulib/docs/book-ii-hartogs-bnd-lift/)
- Source path: [`TauLib/BookII/Hartogs/BndLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L453-L453)
- Source range: L453-L453
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T26` — BndLift Existence

## Immediate Comment / Docstring

```lean
-- Tower coherence [II.T26]
```

## Source Excerpt

```lean
theorem bndlift_exist_3_30 : bndlift_existence_check 3 30 = true := by native_decide
```
