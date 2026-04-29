---
{
  "projection_kind": "taulib_declaration",
  "title": "curvature_check",
  "permalink": "/verify/taulib/docs/book-ii-closure-curvature/curvature-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.Curvature`.",
  "declaration_id": "TauLib.BookII.Closure.Curvature::curvature_check",
  "declaration_slug": "curvature-check",
  "kind": "def",
  "name": "curvature_check",
  "module_name": "TauLib.BookII.Closure.Curvature",
  "module_url": "/verify/taulib/docs/book-ii-closure-curvature/",
  "source_line_start": 51,
  "source_line_end": 72,
  "registry_ids": [
    "II.D80"
  ],
  "related_registry_items": [
    {
      "id": "II.D80",
      "title": "τ-Curvature",
      "url": "/registry/object/II.D80/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L51-L72",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L51-L72",
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
- Source path: [`TauLib/BookII/Closure/Curvature.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Curvature.lean#L51-L72)
- Source range: L51-L72
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D80` — τ-Curvature

## Immediate Comment / Docstring

```lean
/-- [II.D80] Curvature check: R(v,w)(x) = Γ(Γ(x,v),w) - Γ(Γ(x,w),v).
    For a flat connection, this should be 0. -/
```

## Source Excerpt

```lean
def curvature_check (conn : TauConnection) (k : Nat) : Bool :=
  let pk := primorial k
  go 0 pk pk
where
  go (x pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= pk then true
    else go_v x 0 pk pk && go (x + 1) pk (fuel - 1)
  termination_by fuel
  go_v (x v pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if v >= pk then true
    else go_w x v 0 pk pk && go_v x (v + 1) pk (fuel - 1)
  termination_by fuel
  go_w (x v w pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if w >= pk then true
    else
      let path_vw := conn.transport k (conn.transport k x v) w
      let path_wv := conn.transport k (conn.transport k x w) v
      (path_vw == path_wv) && go_w x v (w + 1) pk (fuel - 1)
  termination_by fuel
```
