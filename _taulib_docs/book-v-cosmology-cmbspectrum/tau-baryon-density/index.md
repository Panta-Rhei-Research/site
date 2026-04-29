---
{
  "projection_kind": "taulib_declaration",
  "title": "TauBaryonDensity",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/tau-baryon-density/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::TauBaryonDensity",
  "declaration_slug": "tau-baryon-density",
  "kind": "structure",
  "name": "TauBaryonDensity",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 60,
  "source_line_end": 67,
  "registry_ids": [
    "V.D247"
  ],
  "related_registry_items": [
    {
      "id": "V.D247",
      "title": "τ-Native Baryon Density ω_b from η_B",
      "url": "/registry/object/V.D247/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L60-L67",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L60-L67",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L60-L67)
- Source range: L60-L67
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D247` — τ-Native Baryon Density ω_b from η_B

## Immediate Comment / Docstring

```lean
/-- [V.D247] τ-Native Baryon Density ω_b from η_B.
    ω_b = m_p·η_B·n_γ/ρ_crit = 0.02209.
    At −12334 ppm (−1.2%) from Planck 0.02237±0.00015. -/
```

## Source Excerpt

```lean
structure TauBaryonDensity where
  /-- Source: 1 = from η_B chain. -/
  chain_source : Nat := 1
  /-- Number of free parameters. -/
  free_params : Nat := 0
  /-- σ deviation ×100 (1.2σ → 120). -/
  sigma_deviation_x100 : Nat := 120
  deriving Repr
```
