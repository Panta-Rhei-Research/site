---
{
  "projection_kind": "taulib_declaration",
  "title": "between_transitivity_check",
  "permalink": "/verify/taulib/docs/book-ii-geometry-betweenness/between-transitivity-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.Betweenness`.",
  "declaration_id": "TauLib.BookII.Geometry.Betweenness::between_transitivity_check",
  "declaration_slug": "between-transitivity-check",
  "kind": "def",
  "name": "between_transitivity_check",
  "module_name": "TauLib.BookII.Geometry.Betweenness",
  "module_url": "/verify/taulib/docs/book-ii-geometry-betweenness/",
  "source_line_start": 83,
  "source_line_end": 95,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Betweenness.lean#L83-L95",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Geometry.Betweenness",
        "url": "/verify/taulib/docs/book-ii-geometry-betweenness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Betweenness.lean#L83-L95",
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

- Module: [TauLib.BookII.Geometry.Betweenness](/verify/taulib/docs/book-ii-geometry-betweenness/)
- Source path: [`TauLib/BookII/Geometry/Betweenness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Betweenness.lean#L83-L95)
- Source range: L83-L95
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.T15, T2] Outer transitivity: B(x,y,z) ∧ B(x,z,w) ⟹ B(x,y,w).
    If y is between x and z, and z is between x and w,
    then y is between x and w (monotonic along rays from x).
    Verified exhaustively for small range. -/
```

## Source Excerpt

```lean
def between_transitivity_check (bound db : TauIdx) : Bool :=
  go 2 2 2 2 ((bound + 1) * (bound + 1) * (bound + 1) * (bound + 1))
where
  go (x y z w fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if y > bound then go (x + 1) 2 2 2 (fuel - 1)
    else if z > bound then go x (y + 1) 2 2 (fuel - 1)
    else if w > bound then go x y (z + 1) 2 (fuel - 1)
    else
      let ok := !(between x y z db && between x z w db) || between x y w db
      ok && go x y z (w + 1) (fuel - 1)
  termination_by fuel
```
