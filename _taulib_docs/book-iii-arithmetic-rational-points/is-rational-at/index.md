---
{
  "projection_kind": "taulib_declaration",
  "title": "is_rational_at",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-rational-points/is-rational-at/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.RationalPoints`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.RationalPoints::is_rational_at",
  "declaration_slug": "is-rational-at",
  "kind": "def",
  "name": "is_rational_at",
  "module_name": "TauLib.BookIII.Arithmetic.RationalPoints",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-rational-points/",
  "source_line_start": 48,
  "source_line_end": 60,
  "registry_ids": [
    "III.D59"
  ],
  "related_registry_items": [
    {
      "id": "III.D59",
      "title": "τ-Rational Point",
      "url": "/registry/object/III.D59/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L48-L60",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.RationalPoints",
        "url": "/verify/taulib/docs/book-iii-arithmetic-rational-points/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L48-L60",
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

- Module: [TauLib.BookIII.Arithmetic.RationalPoints](/verify/taulib/docs/book-iii-arithmetic-rational-points/)
- Source path: [`TauLib/BookIII/Arithmetic/RationalPoints.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L48-L60)
- Source range: L48-L60
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D59` — τ-Rational Point

## Immediate Comment / Docstring

```lean
/-- [III.D59] Check if x is τ-rational at depth k: BNF is tower-compatible
    at levels k and k+1. -/
```

## Source Excerpt

```lean
def is_rational_at (x k : TauIdx) : Bool :=
  let pk := primorial k
  let pk1 := primorial (k + 1)
  if pk == 0 || pk1 == 0 then true
  else
    let nf_k := boundary_normal_form (x % pk) k
    let nf_k1 := boundary_normal_form (x % pk1) (k + 1)
    -- BNF surjectivity at both levels
    let sum_k := (nf_k.b_part + nf_k.c_part + nf_k.x_part) % pk
    let sum_k1 := (nf_k1.b_part + nf_k1.c_part + nf_k1.x_part) % pk1
    -- Tower compatibility: BNF recovers x at each level AND projects correctly
    -- (exercises Nat.mod_mod_of_dvd via primorial divisibility)
    sum_k == x % pk && sum_k1 == x % pk1 && (sum_k1 % pk) == sum_k
```
