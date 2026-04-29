---
{
  "projection_kind": "taulib_declaration",
  "title": "HolonomyFormula",
  "permalink": "/verify/taulib/docs/book-iv-sectors-fine-structure/holonomy-formula/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Sectors.FineStructure`.",
  "declaration_id": "TauLib.BookIV.Sectors.FineStructure::HolonomyFormula",
  "declaration_slug": "holonomy-formula",
  "kind": "structure",
  "name": "HolonomyFormula",
  "module_name": "TauLib.BookIV.Sectors.FineStructure",
  "module_url": "/verify/taulib/docs/book-iv-sectors-fine-structure/",
  "source_line_start": 298,
  "source_line_end": 306,
  "registry_ids": [
    "IV.R01"
  ],
  "related_registry_items": [
    {
      "id": "IV.R01",
      "title": "Holonomy vs Spectral",
      "url": "/registry/object/IV.R01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L298-L306",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.FineStructure",
        "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L298-L306",
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

- Module: [TauLib.BookIV.Sectors.FineStructure](/verify/taulib/docs/book-iv-sectors-fine-structure/)
- Source path: [`TauLib/BookIV/Sectors/FineStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L298-L306)
- Source range: L298-L306
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R01` — Holonomy vs Spectral

## Immediate Comment / Docstring

```lean
/-- [IV.R01] The holonomy formula for α involves four calibration
    parameters Q, M, H, L (all determined by ι_τ via the neutron
    anchoring cascade, Book IV Part VII). At this stage we record
    the structural relationship:

    α_holonomy = (π³/16) · Q⁴/(M² H³ L⁶)

    For the holonomy formula to match the spectral formula, we need:
    (π³/16) · Q⁴/(M² H³ L⁶) = (8/15) · ι_τ⁴ · R(ι_τ)

    where R(ι_τ) ≈ 1.0065... is the calibration correction factor.

    This structure records that the holonomy formula EXISTS and
    has the correct form; the numerical evaluation requires the
    calibration cascade. -/
```

## Source Excerpt

```lean
structure HolonomyFormula where
  /-- Geometric prefactor: π³/16. -/
  geom_numer : Nat := 31  -- π³ ≈ 31.006
  geom_denom : Nat := 16
  /-- The calibration exponents: Q⁴, M⁻², H⁻³, L⁻⁶. -/
  Q_exp : Int := 4
  M_exp : Int := -2
  H_exp : Int := -3
  L_exp : Int := -6
```
