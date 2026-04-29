---
{
  "projection_kind": "taulib_declaration",
  "title": "NeutrinoBackgroundOrigin",
  "permalink": "/verify/taulib/docs/book-v-cosmology-neutrino-background/neutrino-background-origin/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.NeutrinoBackground`.",
  "declaration_id": "TauLib.BookV.Cosmology.NeutrinoBackground::NeutrinoBackgroundOrigin",
  "declaration_slug": "neutrino-background-origin",
  "kind": "structure",
  "name": "NeutrinoBackgroundOrigin",
  "module_name": "TauLib.BookV.Cosmology.NeutrinoBackground",
  "module_url": "/verify/taulib/docs/book-v-cosmology-neutrino-background/",
  "source_line_start": 46,
  "source_line_end": 59,
  "registry_ids": [
    "V.P114"
  ],
  "related_registry_items": [
    {
      "id": "V.P114",
      "title": "Neutrino Background Origin",
      "url": "/registry/object/V.P114/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L46-L59",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.NeutrinoBackground",
        "url": "/verify/taulib/docs/book-v-cosmology-neutrino-background/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L46-L59",
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

- Module: [TauLib.BookV.Cosmology.NeutrinoBackground](/verify/taulib/docs/book-v-cosmology-neutrino-background/)
- Source path: [`TauLib/BookV/Cosmology/NeutrinoBackground.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L46-L59)
- Source range: L46-L59
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P114` — Neutrino Background Origin

## Immediate Comment / Docstring

```lean
/-- [V.P114] Neutrino background origin: CνB originates from neutrino
    decoupling at T_dec ≈ 1.37 MeV.

    - Decoupling governed by A-sector coupling κ(A;1) = ι_τ
    - 3 neutrino species (from N_eff = 3, sector exhaustion V.T151)
    - T_CνB = (4/11)^{1/3} · T_CMB = 1.945 K (established)
    - Number density: 336 ν/cm³ (112 per flavor) -/
```

## Source Excerpt

```lean
structure NeutrinoBackgroundOrigin where
  /-- Number of neutrino species. -/
  n_species : Nat
  /-- Exactly 3 species. -/
  species_eq : n_species = 3
  /-- Number density per flavor (ν/cm³). -/
  density_per_flavor : Nat := 112
  /-- Total number density (ν/cm³). -/
  total_density : Nat := 336
  /-- Decoupling is A-sector governed. -/
  a_sector_governed : Bool := true
  /-- Background is thermal relic. -/
  thermal_relic : Bool := true
  deriving Repr
```
