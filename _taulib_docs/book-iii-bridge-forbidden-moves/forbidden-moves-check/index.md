---
{
  "projection_kind": "taulib_declaration",
  "title": "forbidden_moves_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-forbidden-moves/forbidden-moves-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.ForbiddenMoves`.",
  "declaration_id": "TauLib.BookIII.Bridge.ForbiddenMoves::forbidden_moves_check",
  "declaration_slug": "forbidden-moves-check",
  "kind": "def",
  "name": "forbidden_moves_check",
  "module_name": "TauLib.BookIII.Bridge.ForbiddenMoves",
  "module_url": "/verify/taulib/docs/book-iii-bridge-forbidden-moves/",
  "source_line_start": 118,
  "source_line_end": 133,
  "registry_ids": [
    "III.D69"
  ],
  "related_registry_items": [
    {
      "id": "III.D69",
      "title": "Five Forbidden Moves",
      "url": "/registry/object/III.D69/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L118-L133",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L118-L133",
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
- Source path: [`TauLib/BookIII/Bridge/ForbiddenMoves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L118-L133)
- Source range: L118-L133
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D69` — Five Forbidden Moves

## Immediate Comment / Docstring

```lean
/-- [III.D69] Forbidden moves check: verify that at each finite depth k,
    all five forbidden operations are constrained (i.e., the tau-system
    cannot express them unboundedly). -/
```

## Source Excerpt

```lean
def forbidden_moves_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      -- Each forbidden move is witnessed at this (x, k)
      let f1 := forbidden_witness .unbounded_fanout x k
      let f2 := forbidden_witness .global_equality x k
      let f3 := forbidden_witness .succinct_circuits x k
      let f4 := forbidden_witness .exponential_quantification x k
      let f5 := forbidden_witness .nonlocal_disguise x k
      f1 && f2 && f3 && f4 && f5 && go x (k + 1) (fuel - 1)
  termination_by fuel
```
