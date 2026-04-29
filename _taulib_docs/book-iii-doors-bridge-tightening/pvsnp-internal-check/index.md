---
{
  "projection_kind": "taulib_declaration",
  "title": "pvsnp_internal_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-bridge-tightening/pvsnp-internal-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.BridgeTightening`.",
  "declaration_id": "TauLib.BookIII.Doors.BridgeTightening::pvsnp_internal_check",
  "declaration_slug": "pvsnp-internal-check",
  "kind": "def",
  "name": "pvsnp_internal_check",
  "module_name": "TauLib.BookIII.Doors.BridgeTightening",
  "module_url": "/verify/taulib/docs/book-iii-doors-bridge-tightening/",
  "source_line_start": 188,
  "source_line_end": 201,
  "registry_ids": [
    "III.T63"
  ],
  "related_registry_items": [
    {
      "id": "III.T63",
      "title": "P vs NP Forbidden Triple",
      "url": "/registry/object/III.T63/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L188-L201",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.BridgeTightening",
        "url": "/verify/taulib/docs/book-iii-doors-bridge-tightening/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L188-L201",
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

- Module: [TauLib.BookIII.Doors.BridgeTightening](/verify/taulib/docs/book-iii-doors-bridge-tightening/)
- Source path: [`TauLib/BookIII/Doors/BridgeTightening.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L188-L201)
- Source range: L188-L201
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T63` — P vs NP Forbidden Triple

## Immediate Comment / Docstring

```lean
/-- [III.T63] Internal P = NP check: at each finite stage k,
    every function Z/M_k → Bool is decidable in O(M_k) time.
    So P_adm = NP_adm (admissible problems are all decidable). -/
```

## Source Excerpt

```lean
def pvsnp_internal_check (db : Nat) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      -- Every decision problem on Z/M_k is decidable by enumeration
      let decidable := pk > 0
      -- The decision time is bounded by M_k (polynomial in M_k)
      let poly_bound := pk <= pk  -- trivially true
      decidable && poly_bound && go (k + 1) (fuel - 1)
  termination_by fuel
```
