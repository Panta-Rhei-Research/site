---
{
  "projection_kind": "taulib_declaration",
  "title": "CurvaturePlaceholder",
  "permalink": "/verify/taulib/docs/book-ii-closure-diff-geo-agenda/curvature-placeholder/",
  "summary_short": "`structure` declaration in `TauLib.BookII.Closure.DiffGeoAgenda`.",
  "declaration_id": "TauLib.BookII.Closure.DiffGeoAgenda::CurvaturePlaceholder",
  "declaration_slug": "curvature-placeholder",
  "kind": "structure",
  "name": "CurvaturePlaceholder",
  "module_name": "TauLib.BookII.Closure.DiffGeoAgenda",
  "module_url": "/verify/taulib/docs/book-ii-closure-diff-geo-agenda/",
  "source_line_start": 54,
  "source_line_end": 57,
  "registry_ids": [
    "II.R21"
  ],
  "related_registry_items": [
    {
      "id": "II.R21",
      "title": "Differential-Geometric Agenda",
      "url": "/registry/object/II.R21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/DiffGeoAgenda.lean#L54-L57",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.DiffGeoAgenda",
        "url": "/verify/taulib/docs/book-ii-closure-diff-geo-agenda/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/DiffGeoAgenda.lean#L54-L57",
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

- Module: [TauLib.BookII.Closure.DiffGeoAgenda](/verify/taulib/docs/book-ii-closure-diff-geo-agenda/)
- Source path: [`TauLib/BookII/Closure/DiffGeoAgenda.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/DiffGeoAgenda.lean#L54-L57)
- Source range: L54-L57
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `II.R21` — Differential-Geometric Agenda

## Immediate Comment / Docstring

```lean
/-- [II.R21] Placeholder: curvature structure (NOT earned in Book II). -/
```

## Source Excerpt

```lean
structure CurvaturePlaceholder where
  earned : Bool
  description : String
  deriving Repr, DecidableEq
```
