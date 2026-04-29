---
{
  "projection_kind": "taulib_declaration",
  "title": "sum_less_prod_3",
  "permalink": "/verify/taulib/docs/book-iii-computation-witness-search/sum-less-prod-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Computation.WitnessSearch`.",
  "declaration_id": "TauLib.BookIII.Computation.WitnessSearch::sum_less_prod_3",
  "declaration_slug": "sum-less-prod-3",
  "kind": "theorem",
  "name": "sum_less_prod_3",
  "module_name": "TauLib.BookIII.Computation.WitnessSearch",
  "module_url": "/verify/taulib/docs/book-iii-computation-witness-search/",
  "source_line_start": 208,
  "source_line_end": 212,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L208-L212",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L208-L212",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIII/Computation/WitnessSearch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L208-L212)
- Source range: L208-L212
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P23` — Polynomial Refinement

## Immediate Comment / Docstring

```lean
/-- [III.P23] Structural: sum of first 3 primes < primorial 3. -/
```

## Source Excerpt

```lean
theorem sum_less_prod_3 :
    (complexity_comparison 3).1 < (complexity_comparison 3).2 := by
  native_decide

end Tau.BookIII.Computation
```
