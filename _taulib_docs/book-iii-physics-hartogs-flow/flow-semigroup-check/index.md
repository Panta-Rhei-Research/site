---
{
  "projection_kind": "taulib_declaration",
  "title": "flow_semigroup_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-hartogs-flow/flow-semigroup-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.HartogsFlow`.",
  "declaration_id": "TauLib.BookIII.Physics.HartogsFlow::flow_semigroup_check",
  "declaration_slug": "flow-semigroup-check",
  "kind": "def",
  "name": "flow_semigroup_check",
  "module_name": "TauLib.BookIII.Physics.HartogsFlow",
  "module_url": "/verify/taulib/docs/book-iii-physics-hartogs-flow/",
  "source_line_start": 88,
  "source_line_end": 105,
  "registry_ids": [
    "III.D40"
  ],
  "related_registry_items": [
    {
      "id": "III.D40",
      "title": "Hartogs Flow Operator",
      "url": "/registry/object/III.D40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L88-L105",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.HartogsFlow",
        "url": "/verify/taulib/docs/book-iii-physics-hartogs-flow/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L88-L105",
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

- Module: [TauLib.BookIII.Physics.HartogsFlow](/verify/taulib/docs/book-iii-physics-hartogs-flow/)
- Source path: [`TauLib/BookIII/Physics/HartogsFlow.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L88-L105)
- Source range: L88-L105
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D40` — Hartogs Flow Operator

## Immediate Comment / Docstring

```lean
/-- [III.D40] Semigroup projection check: applying the flow at level k,
    then projecting back to level k, recovers the original value.
    This is the tower-projection semigroup property: π_k ∘ Φ_k = id. -/
```

## Source Excerpt

```lean
def flow_semigroup_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then go x (k + 1) (fuel - 1)
      else
        -- Flow from k to k+1
        let nf_k1 := hartogs_flow_step x k
        let val_k1 := nf_k1.b_part + nf_k1.c_part + nf_k1.x_part
        -- Project back to level k: val_k1 mod Prim(k) should equal x mod Prim(k)
        let ok := val_k1 % pk == x % pk
        ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
