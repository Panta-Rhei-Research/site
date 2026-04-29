---
{
  "projection_kind": "taulib_declaration",
  "title": "BHBlueprint",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/bhblueprint/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BHBipolarFusion`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBipolarFusion::BHBlueprint",
  "declaration_slug": "bhblueprint",
  "kind": "structure",
  "name": "BHBlueprint",
  "module_name": "TauLib.BookV.Cosmology.BHBipolarFusion",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/",
  "source_line_start": 154,
  "source_line_end": 161,
  "registry_ids": [
    "V.D170"
  ],
  "related_registry_items": [
    {
      "id": "V.D170",
      "title": "Blueprint",
      "url": "/registry/object/V.D170/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L154-L161",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L154-L161",
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

- Module: [TauLib.BookV.Cosmology.BHBipolarFusion](/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/)
- Source path: [`TauLib/BookV/Cosmology/BHBipolarFusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L154-L161)
- Source range: L154-L161
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D170` — Blueprint

## Immediate Comment / Docstring

```lean
/-- [V.D170] Blueprint of a BH: the pair b_BH = (χ⁺, χ⁻) of
    boundary character components on the two lobes.

    The blueprint encodes the full bipolar structure of the BH. -/
```

## Source Excerpt

```lean
structure BHBlueprint where
  /-- Bipolar data. -/
  bipolarity : BHBipolarity
  /-- Mass scale (scaled). -/
  mass_index : Nat
  /-- Mass positive. -/
  mass_pos : mass_index > 0
  deriving Repr
```
