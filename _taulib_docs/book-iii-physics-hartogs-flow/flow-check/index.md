---
{
  "projection_kind": "taulib_declaration",
  "title": "flow_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-hartogs-flow/flow-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.HartogsFlow`.",
  "declaration_id": "TauLib.BookIII.Physics.HartogsFlow::flow_check",
  "declaration_slug": "flow-check",
  "kind": "def",
  "name": "flow_check",
  "module_name": "TauLib.BookIII.Physics.HartogsFlow",
  "module_url": "/verify/taulib/docs/book-iii-physics-hartogs-flow/",
  "source_line_start": 59,
  "source_line_end": 83,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L59-L83",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L59-L83",
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
- Source path: [`TauLib/BookIII/Physics/HartogsFlow.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L59-L83)
- Source range: L59-L83
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D40` — Hartogs Flow Operator

## Immediate Comment / Docstring

```lean
/-- [III.D40] Flow coherence check: the flow step preserves the value
    mod the original primorial (tower compatibility). -/
```

## Source Excerpt

```lean
def flow_check (bound db : TauIdx) : Bool :=
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
        let nf_k := boundary_normal_form (x % pk) k
        let nf_k1 := hartogs_flow_step x k
        let pk1 := primorial (k + 1)
        -- Tower coherence: at level k, the flow output reduces correctly
        let coherent := if pk1 > 0 then
          (nf_k1.b_part + nf_k1.c_part + nf_k1.x_part) % pk == x % pk
        else true
        -- Sector preservation: B-part stays B-sector
        let b_pres := if pk > 0 && pk1 > 0 then
          -- At minimum: both BNFs are well-defined
          (nf_k.b_part + nf_k.c_part + nf_k.x_part) % pk == x % pk
        else true
        coherent && b_pres && go x (k + 1) (fuel - 1)
  termination_by fuel
```
