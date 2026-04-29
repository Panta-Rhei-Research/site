---
{
  "projection_kind": "taulib_declaration",
  "title": "between_identity_check",
  "permalink": "/verify/taulib/docs/book-ii-geometry-betweenness/between-identity-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.Betweenness`.",
  "declaration_id": "TauLib.BookII.Geometry.Betweenness::between_identity_check",
  "declaration_slug": "between-identity-check",
  "kind": "def",
  "name": "between_identity_check",
  "module_name": "TauLib.BookII.Geometry.Betweenness",
  "module_url": "/verify/taulib/docs/book-ii-geometry-betweenness/",
  "source_line_start": 51,
  "source_line_end": 61,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Betweenness.lean#L51-L61",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Betweenness.lean#L51-L61",
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
- Source path: [`TauLib/BookII/Geometry/Betweenness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Betweenness.lean#L51-L61)
- Source range: L51-L61
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.T15, T1] Identity: B(x,y,x) ⟹ x = y.
    If δ(x,x) = min(δ(x,y), δ(y,x)), then δ(x,y) = ∞, so x = y.
    Check: B(x,y,x) is true only when x = y. -/
```

## Source Excerpt

```lean
def between_identity_check (bound db : TauIdx) : Bool :=
  go 2 2 ((bound + 1) * (bound + 1))
where
  go (x y fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if y > bound then go (x + 1) 2 (fuel - 1)
    else
      let ok := !between x y x db || x == y
      ok && go x (y + 1) (fuel - 1)
  termination_by fuel
```
