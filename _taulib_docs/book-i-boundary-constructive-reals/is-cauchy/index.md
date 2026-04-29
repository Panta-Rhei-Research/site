---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.IsCauchy",
  "permalink": "/verify/taulib/docs/book-i-boundary-constructive-reals/is-cauchy/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.ConstructiveReals`.",
  "declaration_id": "TauLib.BookI.Boundary.ConstructiveReals::TauReal.IsCauchy",
  "declaration_slug": "is-cauchy",
  "kind": "def",
  "name": "TauReal.IsCauchy",
  "module_name": "TauLib.BookI.Boundary.ConstructiveReals",
  "module_url": "/verify/taulib/docs/book-i-boundary-constructive-reals/",
  "source_line_start": 178,
  "source_line_end": 181,
  "registry_ids": [
    "I.D111"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L178-L181",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.ConstructiveReals",
        "url": "/verify/taulib/docs/book-i-boundary-constructive-reals/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L178-L181",
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

- Module: [TauLib.BookI.Boundary.ConstructiveReals](/verify/taulib/docs/book-i-boundary-constructive-reals/)
- Source path: [`TauLib/BookI/Boundary/ConstructiveReals.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L178-L181)
- Source range: L178-L181
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.D111] `TauReal.IsCauchy x`: the approximation sequence of `x`
    is Cauchy with an explicit (constructive) modulus of convergence.

    For every `k`, there is an index `modulus k` after which the
    pairwise distance of approximations stays below `1/(k+1)`. -/
```

## Source Excerpt

```lean
def TauReal.IsCauchy (x : TauReal) : Prop :=
  ∃ modulus : Nat → Nat, ∀ k m n : Nat,
    modulus k ≤ m → modulus k ≤ n →
    TauRat.lt ((x.approx m).sub (x.approx n)).abs (TauRat.ofNatRecip k)
```
