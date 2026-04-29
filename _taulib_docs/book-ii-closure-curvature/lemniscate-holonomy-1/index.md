---
{
  "projection_kind": "taulib_declaration",
  "title": "lemniscate_holonomy_1",
  "permalink": "/verify/taulib/docs/book-ii-closure-curvature/lemniscate-holonomy-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.Curvature`.",
  "declaration_id": "TauLib.BookII.Closure.Curvature::lemniscate_holonomy_1",
  "declaration_slug": "lemniscate-holonomy-1",
  "kind": "theorem",
  "name": "lemniscate_holonomy_1",
  "module_name": "TauLib.BookII.Closure.Curvature",
  "module_url": "/verify/taulib/docs/book-ii-closure-curvature/",
  "source_line_start": 189,
  "source_line_end": 190,
  "registry_ids": [
    "II.T52"
  ],
  "related_registry_items": [
    {
      "id": "II.T52",
      "title": "Lemniscate Holonomy",
      "url": "/registry/object/II.T52/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L189-L190",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.Curvature",
        "url": "/verify/taulib/docs/book-ii-closure-curvature/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L189-L190",
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

- Module: [TauLib.BookII.Closure.Curvature](/verify/taulib/docs/book-ii-closure-curvature/)
- Source path: [`TauLib/BookII/Closure/Curvature.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L189-L190)
- Source range: L189-L190
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T52` — Lemniscate Holonomy

## Immediate Comment / Docstring

```lean
/-- [II.T52] Lemniscate holonomy has order M_k at stage 1. -/
```

## Source Excerpt

```lean
theorem lemniscate_holonomy_1 :
    lemniscate_holonomy_check 1 = true := by native_decide
```
