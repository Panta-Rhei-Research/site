---
{
  "projection_kind": "taulib_declaration",
  "title": "geodesic_completeness_check",
  "permalink": "/verify/taulib/docs/book-ii-closure-curvature/geodesic-completeness-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.Curvature`.",
  "declaration_id": "TauLib.BookII.Closure.Curvature::geodesic_completeness_check",
  "declaration_slug": "geodesic-completeness-check",
  "kind": "def",
  "name": "geodesic_completeness_check",
  "module_name": "TauLib.BookII.Closure.Curvature",
  "module_url": "/verify/taulib/docs/book-ii-closure-curvature/",
  "source_line_start": 117,
  "source_line_end": 134,
  "registry_ids": [
    "II.P17"
  ],
  "related_registry_items": [
    {
      "id": "II.P17",
      "title": "Geodesic Completeness",
      "url": "/registry/object/II.P17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L117-L134",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L117-L134",
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
- Source path: [`TauLib/BookII/Closure/Curvature.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L117-L134)
- Source range: L117-L134
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P17` — Geodesic Completeness

## Immediate Comment / Docstring

```lean
/-- [II.P17] Geodesic completeness check: from any point x, transport in
    any direction v stays within Z/M_k Z and can be iterated. -/
```

## Source Excerpt

```lean
def geodesic_completeness_check (k : Nat) : Bool :=
  let pk := primorial k
  go 0 pk pk
where
  go (x pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= pk then true
    else
      -- Transport by every v stays in range
      go_v x 0 pk pk && go (x + 1) pk (fuel - 1)
  termination_by fuel
  go_v (x v pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if v >= pk then true
    else
      let result := flat_connection.transport k x v
      (result < pk) && go_v x (v + 1) pk (fuel - 1)
  termination_by fuel
```
