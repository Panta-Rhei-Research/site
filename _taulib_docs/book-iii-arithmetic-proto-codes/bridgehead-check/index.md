---
{
  "projection_kind": "taulib_declaration",
  "title": "bridgehead_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-proto-codes/bridgehead-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.ProtoCodes`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ProtoCodes::bridgehead_check",
  "declaration_slug": "bridgehead-check",
  "kind": "def",
  "name": "bridgehead_check",
  "module_name": "TauLib.BookIII.Arithmetic.ProtoCodes",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-proto-codes/",
  "source_line_start": 127,
  "source_line_end": 146,
  "registry_ids": [
    "III.P26"
  ],
  "related_registry_items": [
    {
      "id": "III.P26",
      "title": "Bridgehead Proposition",
      "url": "/registry/object/III.P26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L127-L146",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.ProtoCodes",
        "url": "/verify/taulib/docs/book-iii-arithmetic-proto-codes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L127-L146",
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

- Module: [TauLib.BookIII.Arithmetic.ProtoCodes](/verify/taulib/docs/book-iii-arithmetic-proto-codes/)
- Source path: [`TauLib/BookIII/Arithmetic/ProtoCodes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L127-L146)
- Source range: L127-L146
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P26` — Bridgehead Proposition

## Immediate Comment / Docstring

```lean
/-- [III.P26] Bridgehead: proto-codes are non-trivial (rank > 0 somewhere)
    at sufficiently high depth. This is the seed for E₂ emergence. -/
```

## Source Excerpt

```lean
def bridgehead_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      if pk == 0 || pk > 100 then go (k + 1) (fuel - 1)
      else
        -- At least one proto-code has rank > 0
        let has_nontrivial := check_nontrivial 1 pk k
        has_nontrivial && go (k + 1) (fuel - 1)
  termination_by fuel
  check_nontrivial (x pk k : Nat) : Bool :=
    if x >= pk then false  -- exhausted search: no nontrivial proto-code found
    else
      let pc := make_proto_code x k
      if pc.rank > 0 then true
      else check_nontrivial (x + 1) pk k
```
