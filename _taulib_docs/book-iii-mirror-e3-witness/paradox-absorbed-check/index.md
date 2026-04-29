---
{
  "projection_kind": "taulib_declaration",
  "title": "paradox_absorbed_check",
  "permalink": "/verify/taulib/docs/book-iii-mirror-e3-witness/paradox-absorbed-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.E3Witness`.",
  "declaration_id": "TauLib.BookIII.Mirror.E3Witness::paradox_absorbed_check",
  "declaration_slug": "paradox-absorbed-check",
  "kind": "def",
  "name": "paradox_absorbed_check",
  "module_name": "TauLib.BookIII.Mirror.E3Witness",
  "module_url": "/verify/taulib/docs/book-iii-mirror-e3-witness/",
  "source_line_start": 126,
  "source_line_end": 146,
  "registry_ids": [
    "III.D86"
  ],
  "related_registry_items": [
    {
      "id": "III.D86",
      "title": "Paradox Absorption Map",
      "url": "/registry/object/III.D86/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L126-L146",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L126-L146",
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
- Source path: [`TauLib/BookIII/Mirror/E3Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L126-L146)
- Source range: L126-L146
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D86` — Paradox Absorption Map

## Immediate Comment / Docstring

```lean
/-- [III.D86] Paradox absorption: the result of each paradox construction
    is STILL a valid E₃ element (the self-model absorbs self-reference). -/
```

## Source Excerpt

```lean
def paradox_absorbed_check (db : Nat) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      go_p 0 pk k fuel && go (k + 1) (fuel - 1)
  termination_by fuel
  go_p (x pk k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= pk then true
    else
      -- All four paradox constructions produce E₃ elements
      let c := e3_predicate (paradox_construction .cantor x k) k
      let r := e3_predicate (paradox_construction .russell x k) k
      let g := e3_predicate (paradox_construction .goedel x k) k
      let t := e3_predicate (paradox_construction .turing x k) k
      c && r && g && t && go_p (x + 1) pk k (fuel - 1)
  termination_by fuel
```
