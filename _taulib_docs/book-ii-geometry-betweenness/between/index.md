---
{
  "projection_kind": "taulib_declaration",
  "title": "between",
  "permalink": "/corpus/taulib/docs/book-ii-geometry-betweenness/between/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.Betweenness`.",
  "declaration_id": "TauLib.BookII.Geometry.Betweenness::between",
  "declaration_slug": "between",
  "kind": "def",
  "name": "between",
  "module_name": "TauLib.BookII.Geometry.Betweenness",
  "module_url": "/corpus/taulib/docs/book-ii-geometry-betweenness/",
  "source_line_start": 38,
  "source_line_end": 42,
  "registry_ids": [
    "II.D19"
  ],
  "related_registry_items": [
    {
      "id": "II.D19",
      "title": "Betweenness Relation",
      "url": "/registry/object/II.D19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Betweenness.lean#L38-L42",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Geometry.Betweenness",
        "url": "/corpus/taulib/docs/book-ii-geometry-betweenness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Betweenness.lean#L38-L42",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookII.Geometry.Betweenness](/corpus/taulib/docs/book-ii-geometry-betweenness/)
- Source path: [`TauLib/BookII/Geometry/Betweenness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Betweenness.lean#L38-L42)
- Source range: L38-L42
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `II.D19` — Betweenness Relation

## Immediate Comment / Docstring

```lean
/-- [II.D19] Ultrametric betweenness: B(x,y,z) iff
    δ(x,z) = min(δ(x,y), δ(y,z)).
    y lies on the geodesic from x to z in the profinite tree. -/
```

## Source Excerpt

```lean
def between (x y z db : TauIdx) : Bool :=
  let dxz := disagree_depth x z db
  let dxy := disagree_depth x y db
  let dyz := disagree_depth y z db
  dxz == min dxy dyz
```
