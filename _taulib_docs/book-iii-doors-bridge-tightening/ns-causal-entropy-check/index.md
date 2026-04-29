---
{
  "projection_kind": "taulib_declaration",
  "title": "ns_causal_entropy_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-bridge-tightening/ns-causal-entropy-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.BridgeTightening`.",
  "declaration_id": "TauLib.BookIII.Doors.BridgeTightening::ns_causal_entropy_check",
  "declaration_slug": "ns-causal-entropy-check",
  "kind": "def",
  "name": "ns_causal_entropy_check",
  "module_name": "TauLib.BookIII.Doors.BridgeTightening",
  "module_url": "/verify/taulib/docs/book-iii-doors-bridge-tightening/",
  "source_line_start": 146,
  "source_line_end": 169,
  "registry_ids": [
    "III.T62"
  ],
  "related_registry_items": [
    {
      "id": "III.T62",
      "title": "NS Flow Causal Arrow",
      "url": "/registry/object/III.T62/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L146-L169",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L146-L169",
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
- Source path: [`TauLib/BookIII/Doors/BridgeTightening.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L146-L169)
- Source range: L146-L169
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T62` — NS Flow Causal Arrow

## Immediate Comment / Docstring

```lean
/-- [III.T62] Causal entropy check: the asymmetry is persistent and
    grows, establishing an arrow of time for the flow. -/
```

## Source Excerpt

```lean
def ns_causal_entropy_check (db : Nat) : Bool :=
  go 2 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      -- Asymmetry is non-negative (always true by definition)
      let asymm := ns_causal_asymmetry k
      -- Positive for k ≥ 2 (B and C differ)
      let positive := k < 2 || asymm > 0
      -- BNF fixed point: reduce is a fixed-point map
      let fixed_point := go_fp 0 (primorial k) k (primorial k + 1)
      positive && fixed_point && go (k + 1) (fuel - 1)
  termination_by fuel
  go_fp (x pk k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= pk then true
    else
      -- Fixed-point property: reduce(reduce(x, k), k) = reduce(x, k)
      let r1 := reduce x k
      let r2 := reduce r1 k
      (r1 == r2) && go_fp (x + 1) pk k (fuel - 1)
  termination_by fuel
```
