---
{
  "projection_kind": "taulib_declaration",
  "title": "two_sq_mediates_at_reduce",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-two-categories/two-sq-mediates-at-reduce/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.TwoCategories`.",
  "declaration_id": "TauLib.BookII.Enrichment.TwoCategories::two_sq_mediates_at_reduce",
  "declaration_slug": "two-sq-mediates-at-reduce",
  "kind": "theorem",
  "name": "two_sq_mediates_at_reduce",
  "module_name": "TauLib.BookII.Enrichment.TwoCategories",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-two-categories/",
  "source_line_start": 453,
  "source_line_end": 457,
  "registry_ids": [
    "II.D56"
  ],
  "related_registry_items": [
    {
      "id": "II.D56",
      "title": "2-Morphism",
      "url": "/registry/object/II.D56/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L453-L457",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.TwoCategories",
        "url": "/verify/taulib/docs/book-ii-enrichment-two-categories/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L453-L457",
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

- Module: [TauLib.BookII.Enrichment.TwoCategories](/verify/taulib/docs/book-ii-enrichment-two-categories/)
- Source path: [`TauLib/BookII/Enrichment/TwoCategories.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L453-L457)
- Source range: L453-L457
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D56` — 2-Morphism

## Immediate Comment / Docstring

```lean
/-- [II.D56] Formal proof: two_sq mediates one_id => one_sq.
    two_sq(one_id(x, k), k) = one_sq(x, k).
    LHS = reduce((reduce(x, k))^2, k), RHS = reduce(x^2, k).
    i.e., (x % P_k) * (x % P_k) % P_k = x * x % P_k. -/
```

## Source Excerpt

```lean
theorem two_sq_mediates_at_reduce (x k : TauIdx) :
    two_sq (one_id x k) k = one_sq x k := by
  simp only [two_sq, one_id, one_sq, reduce]
  conv_lhs => rw [Nat.mul_mod (x % primorial k) (x % primorial k) (primorial k)]
  simp [Nat.mod_mod_of_dvd x (dvd_refl (primorial k)), Nat.mul_mod]
```
