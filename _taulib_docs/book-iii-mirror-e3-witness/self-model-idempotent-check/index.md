---
{
  "projection_kind": "taulib_declaration",
  "title": "self_model_idempotent_check",
  "permalink": "/verify/taulib/docs/book-iii-mirror-e3-witness/self-model-idempotent-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.E3Witness`.",
  "declaration_id": "TauLib.BookIII.Mirror.E3Witness::self_model_idempotent_check",
  "declaration_slug": "self-model-idempotent-check",
  "kind": "def",
  "name": "self_model_idempotent_check",
  "module_name": "TauLib.BookIII.Mirror.E3Witness",
  "module_url": "/verify/taulib/docs/book-iii-mirror-e3-witness/",
  "source_line_start": 209,
  "source_line_end": 227,
  "registry_ids": [
    "III.P35"
  ],
  "related_registry_items": [
    {
      "id": "III.P35",
      "title": "Saturation Semantics",
      "url": "/registry/object/III.P35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L209-L227",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Mirror.E3Witness",
        "url": "/verify/taulib/docs/book-iii-mirror-e3-witness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L209-L227",
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

- Module: [TauLib.BookIII.Mirror.E3Witness](/verify/taulib/docs/book-iii-mirror-e3-witness/)
- Source path: [`TauLib/BookIII/Mirror/E3Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L209-L227)
- Source range: L209-L227
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P35` — Saturation Semantics

## Immediate Comment / Docstring

```lean
/-- [III.P35] Semantic invariant: the self-model of the self-model
    is isomorphic to the self-model. -/
```

## Source Excerpt

```lean
def self_model_idempotent_check (db : Nat) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      go_x 0 pk k fuel && go (k + 1) (fuel - 1)
  termination_by fuel
  go_x (x pk k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= pk then true
    else
      -- Self-model decoder applied twice = applied once
      let d1 := reduce (reduce x k) k
      let d2 := reduce (reduce d1 k) k
      (d1 == d2) && go_x (x + 1) pk k (fuel - 1)
  termination_by fuel
```
