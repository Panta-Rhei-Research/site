---
{
  "projection_kind": "taulib_declaration",
  "title": "geodesic_correct_2",
  "permalink": "/verify/taulib/docs/book-ii-closure-curvature/geodesic-correct-2/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.Curvature`.",
  "declaration_id": "TauLib.BookII.Closure.Curvature::geodesic_correct_2",
  "declaration_slug": "geodesic-correct-2",
  "kind": "theorem",
  "name": "geodesic_correct_2",
  "module_name": "TauLib.BookII.Closure.Curvature",
  "module_url": "/verify/taulib/docs/book-ii-closure-curvature/",
  "source_line_start": 177,
  "source_line_end": 178,
  "registry_ids": [
    "II.D81"
  ],
  "related_registry_items": [
    {
      "id": "II.D81",
      "title": "τ-Geodesic",
      "url": "/registry/object/II.D81/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L177-L178",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L177-L178",
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
- Source path: [`TauLib/BookII/Closure/Curvature.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L177-L178)
- Source range: L177-L178
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D81` — τ-Geodesic

## Immediate Comment / Docstring

```lean
/-- [II.D81] Geodesics are correct at stage 2. -/
```

## Source Excerpt

```lean
theorem geodesic_correct_2 :
    geodesic_check 2 = true := by native_decide
```
