---
{
  "projection_kind": "taulib_declaration",
  "title": "euler_product_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-adeles/euler-product-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.Adeles`.",
  "declaration_id": "TauLib.BookIII.Spectral.Adeles::euler_product_check",
  "declaration_slug": "euler-product-check",
  "kind": "def",
  "name": "euler_product_check",
  "module_name": "TauLib.BookIII.Spectral.Adeles",
  "module_url": "/verify/taulib/docs/book-iii-spectral-adeles/",
  "source_line_start": 155,
  "source_line_end": 173,
  "registry_ids": [
    "III.P07"
  ],
  "related_registry_items": [
    {
      "id": "III.P07",
      "title": "Adelic Euler Product",
      "url": "/registry/object/III.P07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Adeles.lean#L155-L173",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.Adeles",
        "url": "/verify/taulib/docs/book-iii-spectral-adeles/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Adeles.lean#L155-L173",
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

- Module: [TauLib.BookIII.Spectral.Adeles](/verify/taulib/docs/book-iii-spectral-adeles/)
- Source path: [`TauLib/BookIII/Spectral/Adeles.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Adeles.lean#L155-L173)
- Source range: L155-L173
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P07` — Adelic Euler Product

## Immediate Comment / Docstring

```lean
/-- [III.P07] Euler product: a multiplicative function on ℤ/Prim(k)ℤ
    decomposes as a product of local factors.
    f(x) = ∏ f_p(x mod p) where f_p is the p-local factor. -/
```

## Source Excerpt

```lean
def euler_product_check (bound db : TauIdx) : Bool :=
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
        -- Test function: f(x) = x² mod Prim(k) (squaring, exercises Nat.mul_mod)
        let fx := (x * x) % pk
        -- CRT decomposition: product of local values
        let residues := crt_decompose fx k
        let reconstructed := crt_reconstruct residues k
        -- Euler product: CRT roundtrip of x² recovers x²
        reconstructed == fx && go x (k + 1) (fuel - 1)
  termination_by fuel
```
