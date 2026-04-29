---
{
  "projection_kind": "taulib_declaration",
  "title": "AstroPhenomenon",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/astro-phenomenon/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Astrophysics.SectorExhaustion`.",
  "declaration_id": "TauLib.BookV.Astrophysics.SectorExhaustion::AstroPhenomenon",
  "declaration_slug": "astro-phenomenon",
  "kind": "inductive",
  "name": "AstroPhenomenon",
  "module_name": "TauLib.BookV.Astrophysics.SectorExhaustion",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/",
  "source_line_start": 71,
  "source_line_end": 96,
  "registry_ids": [
    "V.D144"
  ],
  "related_registry_items": [
    {
      "id": "V.D144",
      "title": "Sector Budget",
      "url": "/registry/object/V.D144/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L71-L96",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.SectorExhaustion",
        "url": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L71-L96",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookV.Astrophysics.SectorExhaustion](/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/)
- Source path: [`TauLib/BookV/Astrophysics/SectorExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L71-L96)
- Source range: L71-L96
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `V.D144` — Sector Budget

## Immediate Comment / Docstring

```lean
/-- [V.D144] Astrophysical phenomenon catalog: the major categories
    of astrophysical phenomena, all accounted for by the 5 sectors. -/
```

## Source Excerpt

```lean
inductive AstroPhenomenon where
  /-- Stellar structure and evolution. -/
  | StellarEvolution
  /-- Gravitational dynamics (orbits, clusters, LSS). -/
  | GravitationalDynamics
  /-- Nuclear reactions (fusion, r-process). -/
  | NuclearReactions
  /-- Electromagnetic radiation (thermal, synchrotron, etc.). -/
  | EMRadiation
  /-- Neutrino emission and interaction. -/
  | NeutrinoPhysics
  /-- Compact objects (WD, NS, BH). -/
  | CompactObjectPhysics
  /-- Accretion and jets. -/
  | AccretionJets
  /-- Gravitational waves. -/
  | GravitationalWaves
  /-- Cosmic expansion. -/
  | CosmicExpansion
  /-- Cosmic microwave background. -/
  | CMBPhysics
  /-- Large-scale structure. -/
  | LargeScaleStructure
  /-- Primordial nucleosynthesis (BBN). -/
  | BBN
  deriving Repr, DecidableEq, BEq
```
