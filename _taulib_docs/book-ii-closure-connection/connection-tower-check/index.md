---
{
  "projection_kind": "taulib_declaration",
  "title": "connection_tower_check",
  "permalink": "/verify/taulib/docs/book-ii-closure-connection/connection-tower-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.Connection`.",
  "declaration_id": "TauLib.BookII.Closure.Connection::connection_tower_check",
  "declaration_slug": "connection-tower-check",
  "kind": "def",
  "name": "connection_tower_check",
  "module_name": "TauLib.BookII.Closure.Connection",
  "module_url": "/verify/taulib/docs/book-ii-closure-connection/",
  "source_line_start": 64,
  "source_line_end": 79,
  "registry_ids": [
    "II.D78"
  ],
  "related_registry_items": [
    {
      "id": "II.D78",
      "title": "τ-Connection",
      "url": "/registry/object/II.D78/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L64-L79",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L64-L79",
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
- Source path: [`TauLib/BookII/Closure/Connection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L64-L79)
- Source range: L64-L79
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D78` — τ-Connection

## Immediate Comment / Docstring

```lean
/-- [II.D78] Connection tower compatibility check: transport at stage k+1
    composed with reduction equals reduction composed with transport at
    stage k. Formally: reduce(Γ_{k+1}(x,v), k) = Γ_k(reduce(x,k), reduce(v,k)). -/
```

## Source Excerpt

```lean
def connection_tower_check (conn : TauConnection) (k : Nat) : Bool :=
  go 0 (primorial (k + 1)) 0
where
  go (x pk1 v_fuel : Nat) : Bool :=
    if x >= pk1 then true
    else
      let pk := primorial k
      go_v x pk pk1 0 pk1 && go (x + 1) pk1 v_fuel
  termination_by pk1 - x
  go_v (x pk pk1 v v_fuel : Nat) : Bool :=
    if v >= pk1 then true
    else
      let lhs := conn.transport (k + 1) x v % pk  -- transport then reduce
      let rhs := conn.transport k (x % pk) (v % pk)  -- reduce then transport
      (lhs == rhs) && go_v x pk pk1 (v + 1) v_fuel
  termination_by pk1 - v
```
