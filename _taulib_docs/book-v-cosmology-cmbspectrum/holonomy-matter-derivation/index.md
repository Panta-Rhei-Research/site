---
{
  "projection_kind": "taulib_declaration",
  "title": "HolonomyMatterDerivation",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/holonomy-matter-derivation/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::HolonomyMatterDerivation",
  "declaration_slug": "holonomy-matter-derivation",
  "kind": "structure",
  "name": "HolonomyMatterDerivation",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 479,
  "source_line_end": 490,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L479-L490",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.CMBSpectrum",
        "url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L479-L490",
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

- Module: [TauLib.BookV.Cosmology.CMBSpectrum](/verify/taulib/docs/book-v-cosmology-cmbspectrum/)
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L479-L490)
- Source range: L479-L490
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.T192 upgrade] Holonomy matter fraction derivation.

    The boundary holonomy mass M_∂ contributes to the Friedmann
    energy budget in ratio κ_D/κ_B to baryonic matter:

    ρ = ρ_baryon + ρ_holonomy
    ρ_holonomy/ρ_baryon = κ_D/κ_B = (1−ι_τ)/ι_τ² ≈ 5.655

    Physical basis:
    - Baryons couple through EM (κ_B = ι_τ²)
    - Holonomy mass couples through gravity (κ_D = 1−ι_τ)
    - The ratio is the "holonomy-to-baryon" ratio

    Therefore ω_m/ω_b = 1 + κ_D/κ_B = 1 + (1−ι_τ)/ι_τ² = 6.655. -/
```

## Source Excerpt

```lean
structure HolonomyMatterDerivation where
  /-- Number of baryon coupling channels (EM: κ_B). -/
  n_baryon_coupling : Nat := 1
  /-- Number of holonomy coupling channels (gravity: κ_D). -/
  n_holonomy_coupling : Nat := 1
  /-- Number of ratio terms (κ_D and κ_B). -/
  n_ratio_terms : Nat := 2
  /-- Number of free parameters. -/
  free_params : Nat := 0
  /-- Number of Friedmann budget terms (ρ_baryon + ρ_holonomy). -/
  n_budget_terms : Nat := 2
  deriving Repr
```
