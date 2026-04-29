---
{
  "projection_kind": "taulib_declaration",
  "title": "bsd_functional",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-proto-codes/bsd-functional/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.ProtoCodes`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ProtoCodes::bsd_functional",
  "declaration_slug": "bsd-functional",
  "kind": "def",
  "name": "bsd_functional",
  "module_name": "TauLib.BookIII.Arithmetic.ProtoCodes",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-proto-codes/",
  "source_line_start": 86,
  "source_line_end": 103,
  "registry_ids": [
    "III.D62"
  ],
  "related_registry_items": [
    {
      "id": "III.D62",
      "title": "BSD Functional",
      "url": "/registry/object/III.D62/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L86-L103",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.ProtoCodes",
        "url": "/verify/taulib/docs/book-iii-arithmetic-proto-codes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L86-L103",
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

- Module: [TauLib.BookIII.Arithmetic.ProtoCodes](/verify/taulib/docs/book-iii-arithmetic-proto-codes/)
- Source path: [`TauLib/BookIII/Arithmetic/ProtoCodes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L86-L103)
- Source range: L86-L103
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D62` — BSD Functional

## Immediate Comment / Docstring

```lean
/-- [III.D62] BSD functional: BSD_τ(k) = rank_count(k) · derivative_approx(k).
    rank_count = number of distinct ranks at level k.
    derivative_approx = difference of split-zeta products. -/
```

## Source Excerpt

```lean
def bsd_functional (k : TauIdx) : TauIdx :=
  let pk := primorial k
  if pk == 0 || pk > 100 then 0
  else
    -- Count of distinct ranks at this level
    let rank_ct := count_ranks 0 pk k 0
    -- L-value derivative approximation: |B_prod - C_prod|
    let bp := split_zeta_b k
    let cp := split_zeta_c k
    let l_deriv := if bp >= cp then bp - cp else cp - bp
    rank_ct * l_deriv
where
  count_ranks (x pk k acc : Nat) : Nat :=
    if x >= pk then acc
    else
      let r := rank_as_depth x k
      let new_acc := if r > 0 then acc + 1 else acc
      count_ranks (x + 1) pk k new_acc
```
