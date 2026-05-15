---
{
  "projection_kind": "taulib_declaration",
  "title": "BHBipolarity",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/bhbipolarity/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BHBipolarFusion`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBipolarFusion::BHBipolarity",
  "declaration_slug": "bhbipolarity",
  "kind": "structure",
  "name": "BHBipolarity",
  "module_name": "TauLib.BookV.Cosmology.BHBipolarFusion",
  "module_url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/",
  "source_line_start": 61,
  "source_line_end": 70,
  "registry_ids": [
    "V.D168"
  ],
  "related_registry_items": [
    {
      "id": "V.D168",
      "title": "BH Bipolarity",
      "url": "/registry/object/V.D168/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L61-L70",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BHBipolarFusion",
        "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L61-L70",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookV.Cosmology.BHBipolarFusion](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/)
- Source path: [`TauLib/BookV/Cosmology/BHBipolarFusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L61-L70)
- Source range: L61-L70
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `V.D168` — BH Bipolarity

## Immediate Comment / Docstring

```lean
/-- [V.D168] BH bipolarity: the BH boundary character χ_BH
    restricted to the linking boundary decomposes into two
    lobe components χ⁺ (positive lobe) and χ⁻ (negative lobe).

    Both are nonzero for every BH (bipolar = both lobes active). -/
```

## Source Excerpt

```lean
structure BHBipolarity where
  /-- Positive lobe magnitude (scaled). -/
  chi_plus : Nat
  /-- Negative lobe magnitude (scaled). -/
  chi_minus : Nat
  /-- Positive lobe is nonzero. -/
  plus_pos : chi_plus > 0
  /-- Negative lobe is nonzero. -/
  minus_pos : chi_minus > 0
  deriving Repr
```
