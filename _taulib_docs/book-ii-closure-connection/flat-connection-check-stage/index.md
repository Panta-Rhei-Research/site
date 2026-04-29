---
{
  "projection_kind": "taulib_declaration",
  "title": "flat_connection_check_stage",
  "permalink": "/verify/taulib/docs/book-ii-closure-connection/flat-connection-check-stage/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.Connection`.",
  "declaration_id": "TauLib.BookII.Closure.Connection::flat_connection_check_stage",
  "declaration_slug": "flat-connection-check-stage",
  "kind": "def",
  "name": "flat_connection_check_stage",
  "module_name": "TauLib.BookII.Closure.Connection",
  "module_url": "/verify/taulib/docs/book-ii-closure-connection/",
  "source_line_start": 121,
  "source_line_end": 139,
  "registry_ids": [
    "II.T50"
  ],
  "related_registry_items": [
    {
      "id": "II.T50",
      "title": "Flat Connection Existence",
      "url": "/registry/object/II.T50/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L121-L139",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.Connection",
        "url": "/verify/taulib/docs/book-ii-closure-connection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L121-L139",
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

- Module: [TauLib.BookII.Closure.Connection](/verify/taulib/docs/book-ii-closure-connection/)
- Source path: [`TauLib/BookII/Closure/Connection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L121-L139)
- Source range: L121-L139
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T50` — Flat Connection Existence

## Immediate Comment / Docstring

```lean
/-- [II.T50] Check flatness of the flat connection for small loops at stage k.
    Tests all triangular loops (v, w, -(v+w)) for v, w in [0, M_k). -/
```

## Source Excerpt

```lean
def flat_connection_check_stage (k : Nat) : Bool :=
  let pk := primorial k
  go 0 pk pk
where
  go (v pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if v >= pk then true
    else
      go_w v 0 pk pk && go (v + 1) pk (fuel - 1)
  termination_by fuel
  go_w (v w pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if w >= pk then true
    else
      let back := pk - ((v + w) % pk)
      let loop := [v, w, back]
      flatness_check_loop flat_connection k 0 loop &&
        go_w v (w + 1) pk (fuel - 1)
  termination_by fuel
```
