---
{
  "projection_kind": "taulib_declaration",
  "title": "two_cat_unit_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-two-categories/two-cat-unit-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.TwoCategories`.",
  "declaration_id": "TauLib.BookII.Enrichment.TwoCategories::two_cat_unit_check",
  "declaration_slug": "two-cat-unit-check",
  "kind": "def",
  "name": "two_cat_unit_check",
  "module_name": "TauLib.BookII.Enrichment.TwoCategories",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-two-categories/",
  "source_line_start": 141,
  "source_line_end": 156,
  "registry_ids": [
    "II.D55"
  ],
  "related_registry_items": [
    {
      "id": "II.D55",
      "title": "2-Category Structure",
      "url": "/registry/object/II.D55/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L141-L156",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L141-L156",
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
- Source path: [`TauLib/BookII/Enrichment/TwoCategories.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L141-L156)
- Source range: L141-L156
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D55` — 2-Category Structure

## Immediate Comment / Docstring

```lean
/-- [II.D55] Identity 2-cell is a unit for vertical composition:
    (id_2 ∘_v eta)(x, k) = eta(x, k) when eta is reduce-normalized. -/
```

## Source Excerpt

```lean
def two_cat_unit_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      -- Left unit: id_2 ∘_v two_sq = two_sq (on reduced inputs)
      let lhs_l := vert_comp id_two_cell two_sq x k
      let rhs_l := two_sq x k
      -- Right unit: two_sq ∘_v id_2 = two_sq (on reduced inputs)
      let lhs_r := vert_comp two_sq id_two_cell x k
      let rhs_r := two_sq x k
      (lhs_l == rhs_l) && (lhs_r == rhs_r) && go x (k + 1) (fuel - 1)
  termination_by fuel
```
