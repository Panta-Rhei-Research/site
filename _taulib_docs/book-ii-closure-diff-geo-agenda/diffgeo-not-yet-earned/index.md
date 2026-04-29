---
{
  "projection_kind": "taulib_declaration",
  "title": "diffgeo_not_yet_earned",
  "permalink": "/verify/taulib/docs/book-ii-closure-diff-geo-agenda/diffgeo-not-yet-earned/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.DiffGeoAgenda`.",
  "declaration_id": "TauLib.BookII.Closure.DiffGeoAgenda::diffgeo_not_yet_earned",
  "declaration_slug": "diffgeo-not-yet-earned",
  "kind": "def",
  "name": "diffgeo_not_yet_earned",
  "module_name": "TauLib.BookII.Closure.DiffGeoAgenda",
  "module_url": "/verify/taulib/docs/book-ii-closure-diff-geo-agenda/",
  "source_line_start": 78,
  "source_line_end": 81,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/DiffGeoAgenda.lean#L78-L81",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/DiffGeoAgenda.lean#L78-L81",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookII/Closure/DiffGeoAgenda.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/DiffGeoAgenda.lean#L78-L81)
- Source range: L78-L81
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.R21` — Differential-Geometric Agenda

## Immediate Comment / Docstring

```lean
/-- [II.R21] None of the diff-geo structures are earned yet. -/
```

## Source Excerpt

```lean
def diffgeo_not_yet_earned : Bool :=
  default_connection.earned == false &&
  default_curvature.earned == false &&
  default_holonomy.earned == false
```
