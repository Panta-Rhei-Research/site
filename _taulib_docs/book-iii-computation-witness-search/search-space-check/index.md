---
{
  "projection_kind": "taulib_declaration",
  "title": "search_space_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-witness-search/search-space-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.WitnessSearch`.",
  "declaration_id": "TauLib.BookIII.Computation.WitnessSearch::search_space_check",
  "declaration_slug": "search-space-check",
  "kind": "def",
  "name": "search_space_check",
  "module_name": "TauLib.BookIII.Computation.WitnessSearch",
  "module_url": "/verify/taulib/docs/book-iii-computation-witness-search/",
  "source_line_start": 107,
  "source_line_end": 124,
  "registry_ids": [
    "III.P22"
  ],
  "related_registry_items": [
    {
      "id": "III.P22",
      "title": "CRT Witness Decomposition",
      "url": "/registry/object/III.P22/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L107-L124",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L107-L124",
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
- Source path: [`TauLib/BookIII/Computation/WitnessSearch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L107-L124)
- Source range: L107-L124
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P22` — CRT Witness Decomposition

## Immediate Comment / Docstring

```lean
/-- [III.P22] Per-prime search space: the number of candidates at each
    prime is exactly p_i. Total = ∑ p_i (not ∏ p_i). -/
```

## Source Excerpt

```lean
def search_space_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      -- Total search = sum of primes (not product!)
      let sum_primes := sum_of_primes 1 k 0
      let prod_primes := primorial k
      -- Sum is much smaller than product for k ≥ 3
      let polynomial := if k >= 3 then sum_primes < prod_primes else true
      polynomial && go (k + 1) (fuel - 1)
  termination_by fuel
  sum_of_primes (i k acc : Nat) : Nat :=
    if i > k then acc
    else sum_of_primes (i + 1) k (acc + nth_prime i)
  termination_by k + 1 - i
```
