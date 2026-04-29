---
{
  "projection_kind": "taulib_declaration",
  "title": "product_meet_collapse_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-comp-bi-square/product-meet-collapse-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.CompBiSquare`.",
  "declaration_id": "TauLib.BookIII.Computation.CompBiSquare::product_meet_collapse_check",
  "declaration_slug": "product-meet-collapse-check",
  "kind": "def",
  "name": "product_meet_collapse_check",
  "module_name": "TauLib.BookIII.Computation.CompBiSquare",
  "module_url": "/verify/taulib/docs/book-iii-computation-comp-bi-square/",
  "source_line_start": 50,
  "source_line_end": 70,
  "registry_ids": [
    "III.T32"
  ],
  "related_registry_items": [
    {
      "id": "III.T32",
      "title": "Product-Meet Collapse",
      "url": "/registry/object/III.T32/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L50-L70",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.CompBiSquare",
        "url": "/verify/taulib/docs/book-iii-computation-comp-bi-square/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L50-L70",
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

- Module: [TauLib.BookIII.Computation.CompBiSquare](/verify/taulib/docs/book-iii-computation-comp-bi-square/)
- Source path: [`TauLib/BookIII/Computation/CompBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L50-L70)
- Source range: L50-L70
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T32` — Product-Meet Collapse

## Immediate Comment / Docstring

```lean
/-- [III.T32] Product-Meet Collapse: at E₂ level, "finding a witness"
    (meet/search) IS "constructing a composite" (product/multiplication).
    Verified by: CRT decomposition turns ∏ into ∑, and the sum is
    reconstructible from the factors. -/
```

## Source Excerpt

```lean
def product_meet_collapse_check (bound db : TauIdx) : Bool :=
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
        -- Product: CRT reconstruction (constructing composite from factors)
        let residues := crt_decompose xr k
        let product := crt_reconstruct residues k
        -- Meet: the BNF decomposition (finding the unique address)
        let nf := boundary_normal_form xr k
        let meet := (nf.b_part + nf.c_part + nf.x_part) % pk
        -- Collapse: product = meet = original
        product == xr && meet == xr && go x (k + 1) (fuel - 1)
  termination_by fuel
```
