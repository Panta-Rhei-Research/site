---
{
  "projection_kind": "taulib_declaration",
  "title": "holonomy_not_earned",
  "permalink": "/corpus/taulib/docs/book-ii-closure-diff-geo-agenda/holonomy-not-earned/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.DiffGeoAgenda`.",
  "declaration_id": "TauLib.BookII.Closure.DiffGeoAgenda::holonomy_not_earned",
  "declaration_slug": "holonomy-not-earned",
  "kind": "theorem",
  "name": "holonomy_not_earned",
  "module_name": "TauLib.BookII.Closure.DiffGeoAgenda",
  "module_url": "/corpus/taulib/docs/book-ii-closure-diff-geo-agenda/",
  "source_line_start": 153,
  "source_line_end": 154,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/DiffGeoAgenda.lean#L153-L154",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.DiffGeoAgenda",
        "url": "/corpus/taulib/docs/book-ii-closure-diff-geo-agenda/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/DiffGeoAgenda.lean#L153-L154",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookII.Closure.DiffGeoAgenda](/corpus/taulib/docs/book-ii-closure-diff-geo-agenda/)
- Source path: [`TauLib/BookII/Closure/DiffGeoAgenda.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/DiffGeoAgenda.lean#L153-L154)
- Source range: L153-L154
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `II.R21` — Differential-Geometric Agenda

## Immediate Comment / Docstring

```lean
/-- [II.R21] Holonomy is not earned: the placeholder records false. -/
```

## Source Excerpt

```lean
theorem holonomy_not_earned :
    default_holonomy.earned = false := by rfl
```
