---
{
  "projection_kind": "taulib_declaration",
  "title": "factors_from_distinct_sources",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/factors-from-distinct-sources/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.ExponentDerivation`.",
  "declaration_id": "TauLib.BookV.GravityField.ExponentDerivation::factors_from_distinct_sources",
  "declaration_slug": "factors-from-distinct-sources",
  "kind": "theorem",
  "name": "factors_from_distinct_sources",
  "module_name": "TauLib.BookV.GravityField.ExponentDerivation",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/",
  "source_line_start": 145,
  "source_line_end": 154,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L145-L154",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.ExponentDerivation",
        "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L145-L154",
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

- Module: [TauLib.BookV.GravityField.ExponentDerivation](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/)
- Source path: [`TauLib/BookV/GravityField/ExponentDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L145-L154)
- Source range: L145-L154
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- All three factors come from distinct sources:
    fiber topology, manifold dimension, algebraic kernel. -/
```

## Source Excerpt

```lean
theorem factors_from_distinct_sources :
    canonical_factors.betti_1_fiber = 2 ∧
    canonical_factors.dim_tau3 = 3 ∧
    canonical_factors.solenoidal_card = 3 ∧
    -- They are verified against three independent existing Lean structures:
    canonical_factors.betti_1_fiber = canonical_coupling.tree_factor ∧
    canonical_factors.dim_tau3 = triple_holonomy.circle_count ∧
    canonical_factors.solenoidal_card = solenoidalGenerators.length :=
  ⟨rfl, rfl, rfl, betti_matches_tree_factor, dim_matches_holonomy_circles,
   solenoidal_matches_kernel⟩
```
