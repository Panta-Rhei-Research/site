---
{
  "projection_kind": "taulib_declaration",
  "title": "flat_connection_check",
  "permalink": "/corpus/taulib/docs/book-ii-closure-connection/flat-connection-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.Connection`.",
  "declaration_id": "TauLib.BookII.Closure.Connection::flat_connection_check",
  "declaration_slug": "flat-connection-check",
  "kind": "def",
  "name": "flat_connection_check",
  "module_name": "TauLib.BookII.Closure.Connection",
  "module_url": "/corpus/taulib/docs/book-ii-closure-connection/",
  "source_line_start": 142,
  "source_line_end": 149,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L142-L149",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.Connection",
        "url": "/corpus/taulib/docs/book-ii-closure-connection/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L142-L149",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookII.Closure.Connection](/corpus/taulib/docs/book-ii-closure-connection/)
- Source path: [`TauLib/BookII/Closure/Connection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L142-L149)
- Source range: L142-L149
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `II.T50` — Flat Connection Existence

## Immediate Comment / Docstring

```lean
/-- [II.T50] Flat connection check for stages 1..db. -/
```

## Source Excerpt

```lean
def flat_connection_check (db : Nat) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k >= db then true
    else flat_connection_check_stage k && go (k + 1) (fuel - 1)
  termination_by fuel
```
