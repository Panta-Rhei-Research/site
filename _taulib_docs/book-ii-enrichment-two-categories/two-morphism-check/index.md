---
{
  "projection_kind": "taulib_declaration",
  "title": "two_morphism_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-two-categories/two-morphism-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.TwoCategories`.",
  "declaration_id": "TauLib.BookII.Enrichment.TwoCategories::two_morphism_check",
  "declaration_slug": "two-morphism-check",
  "kind": "def",
  "name": "two_morphism_check",
  "module_name": "TauLib.BookII.Enrichment.TwoCategories",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-two-categories/",
  "source_line_start": 207,
  "source_line_end": 219,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L207-L219",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L207-L219",
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

- Module: [TauLib.BookII.Enrichment.TwoCategories](/verify/taulib/docs/book-ii-enrichment-two-categories/)
- Source path: [`TauLib/BookII/Enrichment/TwoCategories.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L207-L219)
- Source range: L207-L219
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D56` — 2-Morphism

## Immediate Comment / Docstring

```lean
/-- [II.D56] 2-morphism mediating check:
    eta mediates f => g means eta(f(x, k), k) = g(x, k).
    We verify: two_sq mediates one_id => one_sq.
    two_sq(one_id(x, k), k) = reduce(reduce(x,k)^2, k) = one_sq(x, k). -/
```

## Source Excerpt

```lean
def two_morphism_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      -- two_sq mediates one_id => one_sq
      let lhs := two_sq (one_id x k) k   -- sq(reduce(x,k), k)
      let rhs := one_sq x k               -- reduce(x^2, k)
      (lhs == rhs) && go x (k + 1) (fuel - 1)
  termination_by fuel
```
