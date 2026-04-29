---
{
  "projection_kind": "taulib_declaration",
  "title": "complexity_comparison",
  "permalink": "/verify/taulib/docs/book-iii-computation-witness-search/complexity-comparison/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.WitnessSearch`.",
  "declaration_id": "TauLib.BookIII.Computation.WitnessSearch::complexity_comparison",
  "declaration_slug": "complexity-comparison",
  "kind": "def",
  "name": "complexity_comparison",
  "module_name": "TauLib.BookIII.Computation.WitnessSearch",
  "module_url": "/verify/taulib/docs/book-iii-computation-witness-search/",
  "source_line_start": 157,
  "source_line_end": 165,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L157-L165",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L157-L165",
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
- Source path: [`TauLib/BookIII/Computation/WitnessSearch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L157-L165)
- Source range: L157-L165
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P23` — Polynomial Refinement

## Immediate Comment / Docstring

```lean
/-- [III.P23] Complexity comparison: sum of primes vs primorial at each depth. -/
```

## Source Excerpt

```lean
def complexity_comparison (k : TauIdx) : (TauIdx × TauIdx) :=
  let sum := sum_primes 1 k 0
  let prod := primorial k
  (sum, prod)
where
  sum_primes (i k acc : Nat) : Nat :=
    if i > k then acc
    else sum_primes (i + 1) k (acc + nth_prime i)
  termination_by k + 1 - i
```
