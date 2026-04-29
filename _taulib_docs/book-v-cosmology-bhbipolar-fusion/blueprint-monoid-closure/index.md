---
{
  "projection_kind": "taulib_declaration",
  "title": "blueprint_monoid_closure",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/blueprint-monoid-closure/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BHBipolarFusion`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBipolarFusion::blueprint_monoid_closure",
  "declaration_slug": "blueprint-monoid-closure",
  "kind": "theorem",
  "name": "blueprint_monoid_closure",
  "module_name": "TauLib.BookV.Cosmology.BHBipolarFusion",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/",
  "source_line_start": 212,
  "source_line_end": 217,
  "registry_ids": [
    "V.T112"
  ],
  "related_registry_items": [
    {
      "id": "V.T112",
      "title": "Blueprint Monoid Closure",
      "url": "/registry/object/V.T112/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L212-L217",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BHBipolarFusion",
        "url": "/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L212-L217",
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

- Module: [TauLib.BookV.Cosmology.BHBipolarFusion](/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/)
- Source path: [`TauLib/BookV/Cosmology/BHBipolarFusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L212-L217)
- Source range: L212-L217
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T112` — Blueprint Monoid Closure

## Immediate Comment / Docstring

```lean
/-- [V.T112] Blueprint monoid closure: Fuse_ω is closed, associative,
    and has an identity element (vacuum blueprint).

    Closure proof: fusion of two blueprints yields a blueprint
    (product of positive naturals is positive). -/
```

## Source Excerpt

```lean
theorem blueprint_monoid_closure (b1 b2 : BHBlueprint) :
    (BlueprintFusion b1 b2).bipolarity.chi_plus > 0 ∧
    (BlueprintFusion b1 b2).bipolarity.chi_minus > 0 := by
  constructor
  · exact Nat.mul_pos b1.bipolarity.plus_pos b2.bipolarity.plus_pos
  · exact Nat.mul_pos b1.bipolarity.minus_pos b2.bipolarity.minus_pos
```
