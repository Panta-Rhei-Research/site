---
{
  "projection_kind": "taulib_declaration",
  "title": "geodesic_check",
  "permalink": "/verify/taulib/docs/book-ii-closure-curvature/geodesic-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.Curvature`.",
  "declaration_id": "TauLib.BookII.Closure.Curvature::geodesic_check",
  "declaration_slug": "geodesic-check",
  "kind": "def",
  "name": "geodesic_check",
  "module_name": "TauLib.BookII.Closure.Curvature",
  "module_url": "/verify/taulib/docs/book-ii-closure-curvature/",
  "source_line_start": 93,
  "source_line_end": 109,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L93-L109",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L93-L109",
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
- Source path: [`TauLib/BookII/Closure/Curvature.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L93-L109)
- Source range: L93-L109
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D81` — τ-Geodesic

## Immediate Comment / Docstring

```lean
/-- [II.D81] Check that the geodesic direction transports x to y. -/
```

## Source Excerpt

```lean
def geodesic_check (k : Nat) : Bool :=
  let pk := primorial k
  go 0 pk pk
where
  go (x pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= pk then true
    else go_y x 0 pk pk && go (x + 1) pk (fuel - 1)
  termination_by fuel
  go_y (x y pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if y >= pk then true
    else
      let d := (y + pk - x) % pk
      let endpoint := flat_connection.transport k x d
      (endpoint == y) && go_y x (y + 1) pk (fuel - 1)
  termination_by fuel
```
