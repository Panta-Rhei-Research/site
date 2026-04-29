---
{
  "projection_kind": "taulib_declaration",
  "title": "decompose_functorial_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/decompose-functorial-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.IdempotentDecomposition`.",
  "declaration_id": "TauLib.BookII.Regularity.IdempotentDecomposition::decompose_functorial_check",
  "declaration_slug": "decompose-functorial-check",
  "kind": "def",
  "name": "decompose_functorial_check",
  "module_name": "TauLib.BookII.Regularity.IdempotentDecomposition",
  "module_url": "/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/",
  "source_line_start": 201,
  "source_line_end": 225,
  "registry_ids": [
    "II.P10"
  ],
  "related_registry_items": [
    {
      "id": "II.P10",
      "title": "Functions as Tau-Objects",
      "url": "/registry/object/II.P10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L201-L225",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.IdempotentDecomposition",
        "url": "/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L201-L225",
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

- Module: [TauLib.BookII.Regularity.IdempotentDecomposition](/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/)
- Source path: [`TauLib/BookII/Regularity/IdempotentDecomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L201-L225)
- Source range: L201-L225
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P10` — Functions as Tau-Objects

## Immediate Comment / Docstring

```lean
/-- [II.P10] Decomposition functoriality check:
    the idempotent decomposition commutes with holomorphic composition.

    For endomorphisms f, g on the primorial tower:
    proj_plus(f . g) = proj_plus(f) . proj_plus(g)
    proj_minus(f . g) = proj_minus(f) . proj_minus(g)

    In the stagefun setting, this means the B-channel of a composition
    equals the composition of B-channels, and similarly for C-channels. -/
```

## Source Excerpt

```lean
def decompose_functorial_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      -- Use chi_plus_stage and id_stage as test endomorphisms
      let f := chi_plus_stage
      let g := id_stage
      -- Compose, then decompose
      let comp := StageFun.comp f g
      let (comp_b, comp_c) := stagefun_decompose comp
      -- Decompose, then compose
      let (f_b, f_c) := stagefun_decompose f
      let (g_b, g_c) := stagefun_decompose g
      let b_comp := StageFun.comp f_b g_b
      let c_comp := StageFun.comp f_c g_c
      -- B-channels match
      let b_ok := comp_b.b_fun x k == b_comp.b_fun x k
      -- C-channels match
      let c_ok := comp_c.c_fun x k == c_comp.c_fun x k
      b_ok && c_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
