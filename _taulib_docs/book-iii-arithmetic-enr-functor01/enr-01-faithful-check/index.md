---
{
  "projection_kind": "taulib_declaration",
  "title": "enr_01_faithful_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-enr-functor01/enr-01-faithful-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.EnrFunctor01`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.EnrFunctor01::enr_01_faithful_check",
  "declaration_slug": "enr-01-faithful-check",
  "kind": "def",
  "name": "enr_01_faithful_check",
  "module_name": "TauLib.BookIII.Arithmetic.EnrFunctor01",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-enr-functor01/",
  "source_line_start": 71,
  "source_line_end": 87,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L71-L87",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L71-L87",
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
- Source path: [`TauLib/BookIII/Arithmetic/EnrFunctor01.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L71-L87)
- Source range: L71-L87
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D57` — Enrichment Functor Enr₀₁

## Immediate Comment / Docstring

```lean
/-- [III.D57] Functor composition check: Enr₀₁ at level k composed with
    projection back to E₀ is the identity. -/
```

## Source Excerpt

```lean
def enr_01_faithful_check (bound db : TauIdx) : Bool :=
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
        let nf := boundary_normal_form xr k
        -- Enrichment then forget = identity
        let sum := (nf.b_part + nf.c_part + nf.x_part) % pk
        sum == xr && go x (k + 1) (fuel - 1)
  termination_by fuel
```
