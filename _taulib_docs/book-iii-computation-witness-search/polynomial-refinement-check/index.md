---
{
  "projection_kind": "taulib_declaration",
  "title": "polynomial_refinement_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-witness-search/polynomial-refinement-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.WitnessSearch`.",
  "declaration_id": "TauLib.BookIII.Computation.WitnessSearch::polynomial_refinement_check",
  "declaration_slug": "polynomial-refinement-check",
  "kind": "def",
  "name": "polynomial_refinement_check",
  "module_name": "TauLib.BookIII.Computation.WitnessSearch",
  "module_url": "/verify/taulib/docs/book-iii-computation-witness-search/",
  "source_line_start": 133,
  "source_line_end": 154,
  "registry_ids": [
    "III.P23"
  ],
  "related_registry_items": [
    {
      "id": "III.P23",
      "title": "Polynomial Refinement",
      "url": "/registry/object/III.P23/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L133-L154",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.WitnessSearch",
        "url": "/verify/taulib/docs/book-iii-computation-witness-search/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L133-L154",
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

- Module: [TauLib.BookIII.Computation.WitnessSearch](/verify/taulib/docs/book-iii-computation-witness-search/)
- Source path: [`TauLib/BookIII/Computation/WitnessSearch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L133-L154)
- Source range: L133-L154
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P23` — Polynomial Refinement

## Immediate Comment / Docstring

```lean
/-- [III.P23] Polynomial refinement: each per-prime search space has
    size at most p_i. The total cost ∑ p_i grows polynomially in k
    (O(k² log k) by PNT). -/
```

## Source Excerpt

```lean
def polynomial_refinement_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      -- Each prime's search space is bounded by itself
      let ok := check_per_prime 1 k 0
      -- Total is polynomial (less than k * max_prime ≤ k * p_k)
      ok && go (k + 1) (fuel - 1)
  termination_by fuel
  check_per_prime (i k prev : Nat) : Bool :=
    if i > k then true
    else
      let p := nth_prime i
      -- Primes are strictly increasing
      let increasing := p > prev
      -- Search space at p_i bounded by p_i
      let bounded := p > 0
      increasing && bounded && check_per_prime (i + 1) k p
  termination_by k + 1 - i
```
