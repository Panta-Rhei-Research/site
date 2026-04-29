---
{
  "projection_kind": "taulib_declaration",
  "title": "move_bridge_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-forbidden-moves/move-bridge-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.ForbiddenMoves`.",
  "declaration_id": "TauLib.BookIII.Bridge.ForbiddenMoves::move_bridge_check",
  "declaration_slug": "move-bridge-check",
  "kind": "def",
  "name": "move_bridge_check",
  "module_name": "TauLib.BookIII.Bridge.ForbiddenMoves",
  "module_url": "/verify/taulib/docs/book-iii-bridge-forbidden-moves/",
  "source_line_start": 156,
  "source_line_end": 182,
  "registry_ids": [
    "III.T43"
  ],
  "related_registry_items": [
    {
      "id": "III.T43",
      "title": "Move-Bridge Correspondence",
      "url": "/registry/object/III.T43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L156-L182",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.ForbiddenMoves",
        "url": "/verify/taulib/docs/book-iii-bridge-forbidden-moves/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L156-L182",
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

- Module: [TauLib.BookIII.Bridge.ForbiddenMoves](/verify/taulib/docs/book-iii-bridge-forbidden-moves/)
- Source path: [`TauLib/BookIII/Bridge/ForbiddenMoves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L156-L182)
- Source range: L156-L182
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T43` — Move-Bridge Correspondence

## Immediate Comment / Docstring

```lean
/-- [III.T43] Move-bridge correspondence check: verify that the bridge
    functor degenerates precisely at the five forbidden moves.
    At each depth k, the "safe" operations (non-forbidden) preserve
    full bridge structure, while forbidden operations degrade it. -/
```

## Source Excerpt

```lean
def move_bridge_check (bound db : TauIdx) : Bool :=
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
        let xr := x % pk
        -- Safe operation: reduce is faithful (bridge preserves it)
        let safe := reduce xr k == xr
        -- ZFC axiom operations are safe within primorial range
        let pair_safe := axiom_operation .pairing xr 0 k < pk
        let union_safe := axiom_operation .union xr 0 k < pk
        -- Forbidden operations each have bounded damage
        -- Damage ordering: mild(1) < severe(2) < break(3), correct tiers
        let moves_bounded :=
          bridge_damage .global_equality < bridge_damage .unbounded_fanout &&
          bridge_damage .unbounded_fanout < bridge_damage .succinct_circuits &&
          bridge_damage .succinct_circuits == bridge_damage .exponential_quantification &&
          bridge_damage .global_equality == bridge_damage .nonlocal_disguise
        safe && pair_safe && union_safe && moves_bounded &&
        go x (k + 1) (fuel - 1)
  termination_by fuel
```
