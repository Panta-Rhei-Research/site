---
{
  "projection_kind": "taulib_declaration",
  "title": "all_quantities_distinct",
  "permalink": "/verify/taulib/docs/book-iv-physics-quantity-framework/all-quantities-distinct/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.QuantityFramework`.",
  "declaration_id": "TauLib.BookIV.Physics.QuantityFramework::all_quantities_distinct",
  "declaration_slug": "all-quantities-distinct",
  "kind": "theorem",
  "name": "all_quantities_distinct",
  "module_name": "TauLib.BookIV.Physics.QuantityFramework",
  "module_url": "/verify/taulib/docs/book-iv-physics-quantity-framework/",
  "source_line_start": 229,
  "source_line_end": 240,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L229-L240",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.QuantityFramework",
        "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L229-L240",
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

- Module: [TauLib.BookIV.Physics.QuantityFramework](/verify/taulib/docs/book-iv-physics-quantity-framework/)
- Source path: [`TauLib/BookIV/Physics/QuantityFramework.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L229-L240)
- Source range: L229-L240
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- All 5 canonical quantities use distinct primary invariants. -/
```

## Source Excerpt

```lean
theorem all_quantities_distinct :
    entropy_quantity.invariant ≠ time_quantity.invariant ∧
    entropy_quantity.invariant ≠ energy_quantity.invariant ∧
    entropy_quantity.invariant ≠ mass_quantity.invariant ∧
    entropy_quantity.invariant ≠ gravity_quantity.invariant ∧
    time_quantity.invariant ≠ energy_quantity.invariant ∧
    time_quantity.invariant ≠ mass_quantity.invariant ∧
    time_quantity.invariant ≠ gravity_quantity.invariant ∧
    energy_quantity.invariant ≠ mass_quantity.invariant ∧
    energy_quantity.invariant ≠ gravity_quantity.invariant ∧
    mass_quantity.invariant ≠ gravity_quantity.invariant := by
  simp [entropy_quantity, time_quantity, energy_quantity, mass_quantity, gravity_quantity]
```
