---
{
  "projection_kind": "taulib_declaration",
  "title": "interchange_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-two-categories/interchange-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.TwoCategories`.",
  "declaration_id": "TauLib.BookII.Enrichment.TwoCategories::interchange_check",
  "declaration_slug": "interchange-check",
  "kind": "def",
  "name": "interchange_check",
  "module_name": "TauLib.BookII.Enrichment.TwoCategories",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-two-categories/",
  "source_line_start": 298,
  "source_line_end": 316,
  "registry_ids": [
    "II.P13"
  ],
  "related_registry_items": [
    {
      "id": "II.P13",
      "title": "Character Decomposition",
      "url": "/registry/object/II.P13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L298-L316",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L298-L316",
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
- Source path: [`TauLib/BookII/Enrichment/TwoCategories.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L298-L316)
- Source range: L298-L316
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P13` — Character Decomposition

## Immediate Comment / Docstring

```lean
/-- [II.P13] Interchange law verification:
    (eta₂ ∘_v eta₁) ∘_h (mu₂ ∘_v mu₁) = (eta₂ ∘_h mu₂) ∘_v (eta₁ ∘_h mu₁).

    This is the fundamental coherence condition of a strict 2-category.
    Both sides expand to eta₂(mu₂(eta₁(mu₁(x, k), k), k), k) when the
    2-cells are "strict" (i.e., they compose pointwise via function application).

    In our representation:
    LHS = vert_comp(eta₂, eta₁)(horiz_comp(mu₂, mu₁)(x, k), k)
        = eta₂(eta₁(mu₂(mu₁(x, k), k), k), k)
    RHS = vert_comp(horiz_comp(eta₂, mu₂), horiz_comp(eta₁, mu₁))(x, k)
        = horiz_comp(eta₂, mu₂)(horiz_comp(eta₁, mu₁)(x, k), k)
        = eta₂(mu₂(eta₁(mu₁(x, k), k), k), k)

    These are equal when mu₂ and eta₁ commute in the appropriate sense.
    For reduce-based cells this holds. -/
```

## Source Excerpt

```lean
def interchange_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      -- eta₁ = id_two_cell, eta₂ = two_sq, mu₁ = id_two_cell, mu₂ = two_dbl
      -- LHS: (eta₂ ∘_v eta₁) ∘_h (mu₂ ∘_v mu₁)
      let vert_eta := vert_comp two_sq id_two_cell
      let vert_mu := vert_comp two_dbl id_two_cell
      let lhs := horiz_comp vert_eta vert_mu x k
      -- RHS: (eta₂ ∘_h mu₂) ∘_v (eta₁ ∘_h mu₁)
      let horiz_21 := horiz_comp two_sq two_dbl
      let horiz_11 := horiz_comp id_two_cell id_two_cell
      let rhs := vert_comp horiz_21 horiz_11 x k
      (lhs == rhs) && go x (k + 1) (fuel - 1)
  termination_by fuel
```
