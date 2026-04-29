---
{
  "projection_kind": "taulib_declaration",
  "title": "scaling_chain_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-tower-assembly/scaling-chain-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.TowerAssembly`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.TowerAssembly::scaling_chain_check",
  "declaration_slug": "scaling-chain-check",
  "kind": "def",
  "name": "scaling_chain_check",
  "module_name": "TauLib.BookIII.Arithmetic.TowerAssembly",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-tower-assembly/",
  "source_line_start": 60,
  "source_line_end": 94,
  "registry_ids": [
    "III.T40"
  ],
  "related_registry_items": [
    {
      "id": "III.T40",
      "title": "Enrichment Tower Assembly",
      "url": "/registry/object/III.T40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L60-L94",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.TowerAssembly",
        "url": "/verify/taulib/docs/book-iii-arithmetic-tower-assembly/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L60-L94",
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

- Module: [TauLib.BookIII.Arithmetic.TowerAssembly](/verify/taulib/docs/book-iii-arithmetic-tower-assembly/)
- Source path: [`TauLib/BookIII/Arithmetic/TowerAssembly.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L60-L94)
- Source range: L60-L94
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T40` — Enrichment Tower Assembly

## Immediate Comment / Docstring

```lean
/-- [III.T40] Bi-square scaling chain: all three bi-squares have the same
    structural shape (CRT roundtrip + BNF decomposition + sector products). -/
```

## Source Excerpt

```lean
def scaling_chain_check (bound db : TauIdx) : Bool :=
  -- Level 1: algebraic bi-square shape (CRT roundtrip)
  let alg := crt_roundtrip_go 0 1 bound db ((bound + 1) * (db + 1))
  -- Level 2: topological shape (BNF decomposition)
  let top := bnf_decomposition_go 0 1 bound db ((bound + 1) * (db + 1))
  -- Level 3: enriched shape (sector products)
  let enr := enriched_bisquare_check bound db
  alg && top && enr
where
  /-- Algebraic: CRT roundtrip. -/
  crt_roundtrip_go (x k bound db fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then crt_roundtrip_go (x + 1) 1 bound db (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then crt_roundtrip_go x (k + 1) bound db (fuel - 1)
      else
        let xr := x % pk
        let recon := crt_reconstruct (crt_decompose xr k) k
        recon == xr && crt_roundtrip_go x (k + 1) bound db (fuel - 1)
  termination_by fuel
  /-- Topological: BNF decomposition. -/
  bnf_decomposition_go (x k bound db fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then bnf_decomposition_go (x + 1) 1 bound db (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then bnf_decomposition_go x (k + 1) bound db (fuel - 1)
      else
        let xr := x % pk
        let nf := boundary_normal_form xr k
        (nf.b_part + nf.c_part + nf.x_part) % pk == xr && bnf_decomposition_go x (k + 1) bound db (fuel - 1)
  termination_by fuel
```
