---
{
  "projection_kind": "taulib_declaration",
  "title": "FermiFormIngredients",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/fermi-form-ingredients/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeinbergNLO`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeinbergNLO::FermiFormIngredients",
  "declaration_slug": "fermi-form-ingredients",
  "kind": "structure",
  "name": "FermiFormIngredients",
  "module_name": "TauLib.BookIV.Electroweak.WeinbergNLO",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/",
  "source_line_start": 126,
  "source_line_end": 138,
  "registry_ids": [
    "IV.T135"
  ],
  "related_registry_items": [
    {
      "id": "IV.T135",
      "title": "Fermi Form w-Independence",
      "url": "/registry/object/IV.T135/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L126-L138",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeinbergNLO",
        "url": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L126-L138",
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

- Module: [TauLib.BookIV.Electroweak.WeinbergNLO](/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/)
- Source path: [`TauLib/BookIV/Electroweak/WeinbergNLO.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L126-L138)
- Source range: L126-L138
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T135` — Fermi Form w-Independence

## Immediate Comment / Docstring

```lean
/-- [IV.T135] The Fermi form for neutron lifetime uses G_F directly:
    τ_n⁻¹ = G_F² · m_n⁵/(2π³) · V_ud² · (1+3g_A²) · f · (1+δ_R).
    The ratio w = M_W/m_n does NOT appear. Formally: the Fermi form
    is a function of 5 ingredients (G_F, m_n, V_ud, g_A, f, δ_R),
    none of which is w.

    The 250 ppm gap in w = (17/5)·ι⁻³ is therefore a tree-level
    Sirlin remainder that does not propagate to physical observables. -/
```

## Source Excerpt

```lean
structure FermiFormIngredients where
  /-- Fermi coupling constant G_F (from muon decay, not from M_W). -/
  g_fermi : String
  /-- Neutron mass m_n (single empirical anchor). -/
  m_neutron : String
  /-- CKM matrix element V_ud. -/
  v_ud : String
  /-- Axial coupling g_A. -/
  g_axial : String
  /-- Phase space factor f. -/
  phase_space : String
  /-- Radiative correction δ_R. -/
  delta_r : String
```
