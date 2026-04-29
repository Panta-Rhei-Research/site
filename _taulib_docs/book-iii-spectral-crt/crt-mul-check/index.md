---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_mul_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-crt/crt-mul-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.CRT`.",
  "declaration_id": "TauLib.BookIII.Spectral.CRT::crt_mul_check",
  "declaration_slug": "crt-mul-check",
  "kind": "def",
  "name": "crt_mul_check",
  "module_name": "TauLib.BookIII.Spectral.CRT",
  "module_url": "/verify/taulib/docs/book-iii-spectral-crt/",
  "source_line_start": 94,
  "source_line_end": 121,
  "registry_ids": [
    "III.T10"
  ],
  "related_registry_items": [
    {
      "id": "III.T10",
      "title": "CRT Decomposition Theorem",
      "url": "/registry/object/III.T10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/CRT.lean#L94-L121",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.CRT",
        "url": "/verify/taulib/docs/book-iii-spectral-crt/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/CRT.lean#L94-L121",
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

- Module: [TauLib.BookIII.Spectral.CRT](/verify/taulib/docs/book-iii-spectral-crt/)
- Source path: [`TauLib/BookIII/Spectral/CRT.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/CRT.lean#L94-L121)
- Source range: L94-L121
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T10` — CRT Decomposition Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T10] CRT ring homomorphism: multiplication is preserved. -/
```

## Source Excerpt

```lean
def crt_mul_check (bound db : TauIdx) : Bool :=
  go 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
where
  go (x y k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if y > bound then go (x + 1) 0 1 (fuel - 1)
    else if k > db then go x (y + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then go x y (k + 1) (fuel - 1)
      else
        let prod_mod := (x * y) % pk
        let rx := crt_decompose x k
        let ry := crt_decompose y k
        let rprod := crt_decompose prod_mod k
        let componentwise_ok := go_mul_components rx ry rprod 0 k
        componentwise_ok && go x y (k + 1) (fuel - 1)
  termination_by fuel
  go_mul_components (rx ry rprod : List TauIdx) (i k : Nat) : Bool :=
    if i >= k then true
    else
      let p := nth_prime (i + 1)
      let prod_comp := if p > 0 then
        (rx.getD i 0 * ry.getD i 0) % p
      else 0
      let expected := rprod.getD i 0
      prod_comp == expected && go_mul_components rx ry rprod (i + 1) k
```
