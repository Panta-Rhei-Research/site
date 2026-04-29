---
{
  "projection_kind": "taulib_declaration",
  "title": "local_langlands_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-langlands/local-langlands-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.Langlands`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.Langlands::local_langlands_check",
  "declaration_slug": "local-langlands-check",
  "kind": "def",
  "name": "local_langlands_check",
  "module_name": "TauLib.BookIII.Arithmetic.Langlands",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-langlands/",
  "source_line_start": 80,
  "source_line_end": 101,
  "registry_ids": [
    "III.D64"
  ],
  "related_registry_items": [
    {
      "id": "III.D64",
      "title": "Local Langlands Instance",
      "url": "/registry/object/III.D64/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/Langlands.lean#L80-L101",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.Langlands",
        "url": "/verify/taulib/docs/book-iii-arithmetic-langlands/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/Langlands.lean#L80-L101",
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

- Module: [TauLib.BookIII.Arithmetic.Langlands](/verify/taulib/docs/book-iii-arithmetic-langlands/)
- Source path: [`TauLib/BookIII/Arithmetic/Langlands.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/Langlands.lean#L80-L101)
- Source range: L80-L101
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D64` — Local Langlands Instance

## Immediate Comment / Docstring

```lean
/-- [III.D64] Local Langlands at prime p: the Frobenius at p is encoded
    by the BNF component at the p-th prime position. The spectral character
    restricted to the m-axis gives the Frobenius eigenvalue. -/
```

## Source Excerpt

```lean
def local_langlands_check (bound db : TauIdx) : Bool :=
  go 1 1 ((bound + 1) * (db + 1))
where
  go (i k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if i > bound then true
    else if k > db then go (i + 1) 1 (fuel - 1)
    else
      let p := nth_prime i
      let label := label_direct p
      -- Local Langlands: label-product consistency
      -- B-type primes divide B-product, C into C, X into X
      let pk := primorial k
      let consistent := if pk > 0 && p > 0 && pk % p == 0 then
        -- p divides Prim(k), so p contributes to the matching split product
        match label with
        | .B => split_zeta_b k % p == 0
        | .C => split_zeta_c k % p == 0
        | .X => split_zeta_x k % p == 0
      else true
      consistent && go i (k + 1) (fuel - 1)
  termination_by fuel
```
