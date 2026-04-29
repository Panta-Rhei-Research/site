---
{
  "projection_kind": "taulib_declaration",
  "title": "on_depth_line",
  "permalink": "/verify/taulib/docs/book-ii-geometry-pasch-parallel/on-depth-line/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.PaschParallel`.",
  "declaration_id": "TauLib.BookII.Geometry.PaschParallel::on_depth_line",
  "declaration_slug": "on-depth-line",
  "kind": "def",
  "name": "on_depth_line",
  "module_name": "TauLib.BookII.Geometry.PaschParallel",
  "module_url": "/verify/taulib/docs/book-ii-geometry-pasch-parallel/",
  "source_line_start": 83,
  "source_line_end": 85,
  "registry_ids": [
    "II.T18"
  ],
  "related_registry_items": [
    {
      "id": "II.T18",
      "title": "Parallel Postulate",
      "url": "/registry/object/II.T18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/PaschParallel.lean#L83-L85",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Geometry.PaschParallel",
        "url": "/verify/taulib/docs/book-ii-geometry-pasch-parallel/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/PaschParallel.lean#L83-L85",
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

- Module: [TauLib.BookII.Geometry.PaschParallel](/verify/taulib/docs/book-ii-geometry-pasch-parallel/)
- Source path: [`TauLib/BookII/Geometry/PaschParallel.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/PaschParallel.lean#L83-L85)
- Source range: L83-L85
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T18` — Parallel Postulate

## Immediate Comment / Docstring

```lean
/-- [II.T18] Depth-line: x and y determine a "line" at depth k = δ(x,y).
    The line through x,y consists of all z with δ(x,z) = k or δ(y,z) = k. -/
```

## Source Excerpt

```lean
def on_depth_line (x y z db : TauIdx) : Bool :=
  let k := disagree_depth x y db
  disagree_depth x z db == k || disagree_depth y z db == k
```
