---
{
  "projection_kind": "taulib_declaration",
  "title": "BaryonDensityFromIota",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/baryon-density-from-iota/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::BaryonDensityFromIota",
  "declaration_slug": "baryon-density-from-iota",
  "kind": "structure",
  "name": "BaryonDensityFromIota",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 103,
  "source_line_end": 110,
  "registry_ids": [
    "V.T190"
  ],
  "related_registry_items": [
    {
      "id": "V.T190",
      "title": "Baryon Density from Master Constant",
      "url": "/registry/object/V.T190/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L103-L110",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L103-L110",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L103-L110)
- Source range: L103-L110
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T190` — Baryon Density from Master Constant

## Immediate Comment / Docstring

```lean
/-- [V.T190] Baryon Density from Master Constant.
    ι_τ → α_τ → η_B → ω_b = 0.02209. Zero free parameters.
    Chain: ι_τ → α_τ = (121/225)·ι_τ⁴ → η_B = α·ι_τ¹⁵·(5/6) →
    ρ_b = m_p·η_B·n_γ → ω_b = ρ_b/ρ_crit. -/
```

## Source Excerpt

```lean
structure BaryonDensityFromIota where
  /-- Number of chain links. -/
  chain_links : Nat
  /-- Five links in chain. -/
  links_eq : chain_links = 5
  /-- Number of free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
