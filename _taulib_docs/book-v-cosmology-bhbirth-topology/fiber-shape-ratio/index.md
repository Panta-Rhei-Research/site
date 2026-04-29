---
{
  "projection_kind": "taulib_declaration",
  "title": "FiberShapeRatio",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/fiber-shape-ratio/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BHBirthTopology`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBirthTopology::FiberShapeRatio",
  "declaration_slug": "fiber-shape-ratio",
  "kind": "structure",
  "name": "FiberShapeRatio",
  "module_name": "TauLib.BookV.Cosmology.BHBirthTopology",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/",
  "source_line_start": 274,
  "source_line_end": 285,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L274-L285",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BHBirthTopology",
        "url": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L274-L285",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookV.Cosmology.BHBirthTopology](/verify/taulib/docs/book-v-cosmology-bhbirth-topology/)
- Source path: [`TauLib/BookV/Cosmology/BHBirthTopology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L274-L285)
- Source range: L274-L285
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.P131 upgrade] T² shape ratio r/R = ι_τ from fiber structure.

    The two T² circles correspond to:
    - γ-generator (EM sector): radius R
    - η-generator (Strong sector): radius r

    The fiber parameter ι_τ controls the "breathing fraction"
    of the τ³ fibration τ¹ ×_f T². By definition of the fiber
    structure, R = ℓ_τ and r = ι_τ·ℓ_τ, so r/R = ι_τ.

    This makes the shape ratio tautological from the fibration:
    it is the master constant's geometric meaning as the
    fiber breathing fraction. -/
```

## Source Excerpt

```lean
structure FiberShapeRatio where
  /-- r/R = ι_τ from fibration. -/
  ratio_is_iota : Bool := true
  /-- R corresponds to γ-generator (EM). -/
  r_big_is_gamma : Bool := true
  /-- r corresponds to η-generator (Strong). -/
  r_small_is_eta : Bool := true
  /-- ι_τ is the fiber breathing fraction. -/
  breathing_fraction : Bool := true
  /-- QNM ratio = ι_τ⁻¹ ≈ 2.93. -/
  qnm_ratio_inverse : Bool := true
  deriving Repr
```
