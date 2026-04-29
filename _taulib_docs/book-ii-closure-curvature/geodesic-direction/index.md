---
{
  "projection_kind": "taulib_declaration",
  "title": "geodesic_direction",
  "permalink": "/verify/taulib/docs/book-ii-closure-curvature/geodesic-direction/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.Curvature`.",
  "declaration_id": "TauLib.BookII.Closure.Curvature::geodesic_direction",
  "declaration_slug": "geodesic-direction",
  "kind": "def",
  "name": "geodesic_direction",
  "module_name": "TauLib.BookII.Closure.Curvature",
  "module_url": "/verify/taulib/docs/book-ii-closure-curvature/",
  "source_line_start": 87,
  "source_line_end": 90,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L87-L90",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L87-L90",
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

- Module: [TauLib.BookII.Closure.Curvature](/verify/taulib/docs/book-ii-closure-curvature/)
- Source path: [`TauLib/BookII/Closure/Curvature.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L87-L90)
- Source range: L87-L90
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D81` — τ-Geodesic

## Immediate Comment / Docstring

```lean
/-- [II.D81] A geodesic from x to y at stage k: the shortest path.
    Returns the direction vector. -/
```

## Source Excerpt

```lean
def geodesic_direction (x y k : Nat) : Nat :=
  let pk := primorial k
  let d := (y + pk - x) % pk
  if d ≤ pk / 2 then d else pk - d
```
