---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.equiv",
  "permalink": "/verify/taulib/docs/book-i-boundary-constructive-reals/equiv/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.ConstructiveReals`.",
  "declaration_id": "TauLib.BookI.Boundary.ConstructiveReals::TauReal.equiv",
  "declaration_slug": "equiv",
  "kind": "def",
  "name": "TauReal.equiv",
  "module_name": "TauLib.BookI.Boundary.ConstructiveReals",
  "module_url": "/verify/taulib/docs/book-i-boundary-constructive-reals/",
  "source_line_start": 199,
  "source_line_end": 202,
  "registry_ids": [
    "I.D112"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L199-L202",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L199-L202",
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
- Source path: [`TauLib/BookI/Boundary/ConstructiveReals.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L199-L202)
- Source range: L199-L202
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.D112] Two TauReals are **Cauchy-equivalent** if the pointwise
    difference sequence converges to zero at some explicit rate.

    Formally: there is a modulus `μ : Nat → Nat` such that for every
    tolerance level `k`, past index `μ k` the pointwise difference
    `|a.approx n - b.approx n|` is below `1 / (k + 1)`.

    This is the correct notion of equality in the Cauchy completion of
    TauRat and is strictly weaker than pointwise `TauRat.equiv` at every
    index (captured by `TauReal.equiv_of_pointwise` below).  Downstream
    callers that previously supplied a pointwise witness now route
    through that bridge. -/
```

## Source Excerpt

```lean
def TauReal.equiv (a b : TauReal) : Prop :=
  ∃ modulus : Nat → Nat, ∀ k n : Nat,
    modulus k ≤ n →
    TauRat.lt ((a.approx n).sub (b.approx n)).abs (TauRat.ofNatRecip k)
```
