---
{
  "projection_kind": "taulib_declaration",
  "title": "diffgeo_not_earned",
  "permalink": "/verify/taulib/docs/book-ii-closure-diff-geo-agenda/diffgeo-not-earned/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.DiffGeoAgenda`.",
  "declaration_id": "TauLib.BookII.Closure.DiffGeoAgenda::diffgeo_not_earned",
  "declaration_slug": "diffgeo-not-earned",
  "kind": "theorem",
  "name": "diffgeo_not_earned",
  "module_name": "TauLib.BookII.Closure.DiffGeoAgenda",
  "module_url": "/verify/taulib/docs/book-ii-closure-diff-geo-agenda/",
  "source_line_start": 129,
  "source_line_end": 130,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/DiffGeoAgenda.lean#L129-L130",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/DiffGeoAgenda.lean#L129-L130",
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

- Module: [TauLib.BookII.Closure.DiffGeoAgenda](/verify/taulib/docs/book-ii-closure-diff-geo-agenda/)
- Source path: [`TauLib/BookII/Closure/DiffGeoAgenda.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/DiffGeoAgenda.lean#L129-L130)
- Source range: L129-L130
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.R21` — Differential-Geometric Agenda

## Immediate Comment / Docstring

```lean
-- ============================================================
-- FORMAL VERIFICATION (native_decide)
-- ============================================================

-- Diff-geo not earned [II.R21]
```

## Source Excerpt

```lean
theorem diffgeo_not_earned :
    diffgeo_not_yet_earned = true := by native_decide
```
