---
{
  "projection_kind": "taulib_declaration",
  "title": "bsd_three_ingredient_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-bsd/bsd-three-ingredient-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.BSD`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.BSD::bsd_three_ingredient_check",
  "declaration_slug": "bsd-three-ingredient-check",
  "kind": "def",
  "name": "bsd_three_ingredient_check",
  "module_name": "TauLib.BookIII.Arithmetic.BSD",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-bsd/",
  "source_line_start": 96,
  "source_line_end": 117,
  "registry_ids": [
    "III.P27"
  ],
  "related_registry_items": [
    {
      "id": "III.P27",
      "title": "BSD Three-Ingredient Proof",
      "url": "/registry/object/III.P27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/BSD.lean#L96-L117",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.BSD",
        "url": "/verify/taulib/docs/book-iii-arithmetic-bsd/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/BSD.lean#L96-L117",
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

- Module: [TauLib.BookIII.Arithmetic.BSD](/verify/taulib/docs/book-iii-arithmetic-bsd/)
- Source path: [`TauLib/BookIII/Arithmetic/BSD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/BSD.lean#L96-L117)
- Source range: L96-L117
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P27` — BSD Three-Ingredient Proof

## Immediate Comment / Docstring

```lean
/-- [III.P27] BSD three-ingredient proof:
    (1) Rank stabilization: ranks are bounded
    (2) L-value stabilization: split-zeta products stabilize
    (3) E₁ MD equality: boundary determines interior determines spectral -/
```

## Source Excerpt

```lean
def bsd_three_ingredient_check (bound db : TauIdx) : Bool :=
  -- Ingredient 1: rank stabilization
  let rank_stab := rank_stabilization_check bound db
  -- Ingredient 2: L-value stabilization (sector products extend)
  let l_stab := l_value_stab_go 1 db (db + 1)
  -- Ingredient 3: E₁ Mutual Determination
  let md := e1_md_instance_check bound db
  rank_stab && l_stab && md
where
  /-- L-value stabilization: B and C products at k divide those at k+1. -/
  l_value_stab_go (k db fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k >= db then true
    else
      let bp_k := split_zeta_b k
      let bp_k1 := split_zeta_b (k + 1)
      let cp_k := split_zeta_c k
      let cp_k1 := split_zeta_c (k + 1)
      let b_extends := if bp_k > 0 then bp_k1 % bp_k == 0 else true
      let c_extends := if cp_k > 0 then cp_k1 % cp_k == 0 else true
      b_extends && c_extends && l_value_stab_go (k + 1) db (fuel - 1)
  termination_by fuel
```
