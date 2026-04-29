---
{
  "projection_kind": "taulib_declaration",
  "title": "polarity_swap_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-hartogs-flow/polarity-swap-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.HartogsFlow`.",
  "declaration_id": "TauLib.BookIII.Physics.HartogsFlow::polarity_swap_check",
  "declaration_slug": "polarity-swap-check",
  "kind": "def",
  "name": "polarity_swap_check",
  "module_name": "TauLib.BookIII.Physics.HartogsFlow",
  "module_url": "/verify/taulib/docs/book-iii-physics-hartogs-flow/",
  "source_line_start": 166,
  "source_line_end": 189,
  "registry_ids": [
    "III.D41"
  ],
  "related_registry_items": [
    {
      "id": "III.D41",
      "title": "Operator Polarity Swap",
      "url": "/registry/object/III.D41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L166-L189",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L166-L189",
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
- Source path: [`TauLib/BookIII/Physics/HartogsFlow.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L166-L189)
- Source range: L166-L189
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D41` — Operator Polarity Swap

## Immediate Comment / Docstring

```lean
/-- [III.D41] Polarity swap check: swapping and summing gives the same
    total as the original BNF. -/
```

## Source Excerpt

```lean
def polarity_swap_check (bound db : TauIdx) : Bool :=
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
        let nf := boundary_normal_form (x % pk) k
        let swapped := polarity_swap nf
        -- Sum preserved under swap (commutativity)
        let sum_orig := nf.b_part + nf.c_part + nf.x_part
        let sum_swap := swapped.b_part + swapped.c_part + swapped.x_part
        let sum_ok := sum_orig == sum_swap
        -- Non-trivial: swap changes BNF when b ≠ c, preserves when b = c
        let nontrivial := if nf.b_part != nf.c_part then
          swapped != nf  -- swap actually changes something
        else
          swapped == nf  -- σ-fixed: swap is identity
        sum_ok && nontrivial && go x (k + 1) (fuel - 1)
  termination_by fuel
```
