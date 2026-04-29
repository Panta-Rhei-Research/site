---
{
  "projection_kind": "taulib_declaration",
  "title": "enr_01_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-enr-functor01/enr-01-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.EnrFunctor01`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.EnrFunctor01::enr_01_check",
  "declaration_slug": "enr-01-check",
  "kind": "def",
  "name": "enr_01_check",
  "module_name": "TauLib.BookIII.Arithmetic.EnrFunctor01",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-enr-functor01/",
  "source_line_start": 43,
  "source_line_end": 67,
  "registry_ids": [
    "III.D57"
  ],
  "related_registry_items": [
    {
      "id": "III.D57",
      "title": "Enrichment Functor Enr₀₁",
      "url": "/registry/object/III.D57/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L43-L67",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.EnrFunctor01",
        "url": "/verify/taulib/docs/book-iii-arithmetic-enr-functor01/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L43-L67",
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

- Module: [TauLib.BookIII.Arithmetic.EnrFunctor01](/verify/taulib/docs/book-iii-arithmetic-enr-functor01/)
- Source path: [`TauLib/BookIII/Arithmetic/EnrFunctor01.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L43-L67)
- Source range: L43-L67
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D57` — Enrichment Functor Enr₀₁

## Immediate Comment / Docstring

```lean
/-- [III.D57] Enrichment functor check: E₀ → E₁ enrichment preserves
    tower structure while adding sector decomposition. Each E₀ object
    (BNF at level k) is enriched to an E₁ object (BNF + gauge data). -/
```

## Source Excerpt

```lean
def enr_01_check (bound db : TauIdx) : Bool :=
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
        -- E₀ object: bare BNF
        let nf := boundary_normal_form xr k
        -- E₁ enrichment: BNF + sector products
        let bp := split_zeta_b k
        let cp := split_zeta_c k
        let xp := split_zeta_x k
        -- Faithfulness: E₁ data determines E₀ data
        let sum := (nf.b_part + nf.c_part + nf.x_part) % pk
        let faithful := sum == xr
        -- Enrichment: sector products are well-defined
        let enriched := if pk > 0 then bp * cp * xp == pk else true
        faithful && enriched && go x (k + 1) (fuel - 1)
  termination_by fuel
```
