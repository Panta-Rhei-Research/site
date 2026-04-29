---
{
  "projection_kind": "taulib_declaration",
  "title": "CPAsymmetryFromPolarity",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/cpasymmetry-from-polarity/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BBNBaryogenesis`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNBaryogenesis::CPAsymmetryFromPolarity",
  "declaration_slug": "cpasymmetry-from-polarity",
  "kind": "structure",
  "name": "CPAsymmetryFromPolarity",
  "module_name": "TauLib.BookV.Cosmology.BBNBaryogenesis",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/",
  "source_line_start": 473,
  "source_line_end": 484,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L473-L484",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BBNBaryogenesis",
        "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L473-L484",
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

- Module: [TauLib.BookV.Cosmology.BBNBaryogenesis](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/)
- Source path: [`TauLib/BookV/Cosmology/BBNBaryogenesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L473-L484)
- Source range: L473-L484
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- CP asymmetry from A-sector (π-generator) polarity structure.

    The A-sector polarity matrix [[1, ι_τ],[ι_τ, 1]] gives
    B-violation asymmetry ε = ι_τ per generator cycle.

    Over the full 5-generator orbit × dim(τ³):
    ε_total ∝ ι_τ¹⁵ (matching SA-i mod-5 suppression)

    ε_CP = κ(A;1) = ι_τ: the A-sector self-coupling is
    the CP asymmetry scale.

    This connects baryogenesis CP violation to the same A-sector
    polarity that drives PMNS mixing angles (Campaign A). -/
```

## Source Excerpt

```lean
structure CPAsymmetryFromPolarity where
  /-- CP asymmetry scale = ι_τ = κ(A;1). -/
  cp_scale_is_iota : Bool := true
  /-- A-sector polarity matrix [[1,ι_τ],[ι_τ,1]]. -/
  polarity_matrix_form : Bool := true
  /-- Per-generator asymmetry = ι_τ. -/
  per_generator_asymmetry : Bool := true
  /-- Total = ι_τ¹⁵ from 5-gen × dim 3. -/
  total_matches_sai_mod5 : Bool := true
  /-- Connects to PMNS (Campaign A). -/
  connects_to_pmns : Bool := true
  deriving Repr
```
