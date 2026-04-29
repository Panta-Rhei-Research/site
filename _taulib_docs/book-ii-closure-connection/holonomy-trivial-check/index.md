---
{
  "projection_kind": "taulib_declaration",
  "title": "holonomy_trivial_check",
  "permalink": "/verify/taulib/docs/book-ii-closure-connection/holonomy-trivial-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.Connection`.",
  "declaration_id": "TauLib.BookII.Closure.Connection::holonomy_trivial_check",
  "declaration_slug": "holonomy-trivial-check",
  "kind": "def",
  "name": "holonomy_trivial_check",
  "module_name": "TauLib.BookII.Closure.Connection",
  "module_url": "/verify/taulib/docs/book-ii-closure-connection/",
  "source_line_start": 158,
  "source_line_end": 178,
  "registry_ids": [
    "II.P16"
  ],
  "related_registry_items": [
    {
      "id": "II.P16",
      "title": "Holonomy Triviality",
      "url": "/registry/object/II.P16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L158-L178",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L158-L178",
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
- Source path: [`TauLib/BookII/Closure/Connection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L158-L178)
- Source range: L158-L178
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P16` — Holonomy Triviality

## Immediate Comment / Docstring

```lean
/-- [II.P16] Holonomy check: for every starting point and every closed
    loop of length ≤ 3, the flat connection returns to the origin.
    Tests at stage k with small loops. -/
```

## Source Excerpt

```lean
def holonomy_trivial_check (k : Nat) : Bool :=
  let pk := primorial k
  -- For the flat connection, every closed loop returns to start
  -- because (x + v1 + v2 + ... + vn) mod pk = x when Σvi ≡ 0 mod pk
  go 0 pk pk
where
  go (x pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= pk then true
    else
      -- Test: transport by v then by (pk - v) returns to x
      go_loop x 0 pk pk && go (x + 1) pk (fuel - 1)
  termination_by fuel
  go_loop (x v pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if v >= pk then true
    else
      let fwd := flat_connection.transport k x v
      let back := flat_connection.transport k fwd (pk - v)
      (back == x) && go_loop x (v + 1) pk (fuel - 1)
  termination_by fuel
```
