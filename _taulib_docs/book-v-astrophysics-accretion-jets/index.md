---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Astrophysics.AccretionJets",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Astrophysics.AccretionJets`.",
  "module_name": "TauLib.BookV.Astrophysics.AccretionJets",
  "module_slug": "book-v-astrophysics-accretion-jets",
  "book": "BookV",
  "family": "Astrophysics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Astrophysics/AccretionJets.lean",
  "sha256": "289a035030d527078230c0e16240392af4ae211a436e54183ba49ee5c0ecff11",
  "imports": [
    "TauLib.BookV.Astrophysics.Supernovae"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Astrophysics.BinaryMergersGW"
  ],
  "registry_ids": [
    "V.D129",
    "V.D130",
    "V.D131",
    "V.D132",
    "V.D285",
    "V.D286",
    "V.D289",
    "V.D290",
    "V.P153",
    "V.P77",
    "V.P78",
    "V.P79",
    "V.R185",
    "V.R186",
    "V.R187",
    "V.R188",
    "V.R189",
    "V.R190",
    "V.R191",
    "V.T228",
    "V.T231",
    "V.T232",
    "V.T90",
    "V.T91",
    "V.T92"
  ],
  "declaration_counts": {
    "theorem": 10,
    "inductive": 2,
    "structure": 8,
    "def": 6,
    "eval": 6
  },
  "declarations": [
    {
      "kind": "theorem",
      "name": "accretion_as_defect_infall",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/accretion-as-defect-infall/",
      "source_line_start": 79,
      "source_line_end": 81,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P77"
      ]
    },
    {
      "kind": "inductive",
      "name": "DiskModel",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/disk-model/",
      "source_line_start": 88,
      "source_line_end": 95,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AccretionDiskStructure",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/accretion-disk-structure/",
      "source_line_start": 102,
      "source_line_end": 115,
      "formal_status": "defined",
      "registry_ids": [
        "V.D129"
      ]
    },
    {
      "kind": "structure",
      "name": "EddingtonLimitData",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/eddington-limit-data/",
      "source_line_start": 125,
      "source_line_end": 134,
      "formal_status": "defined",
      "registry_ids": [
        "V.D130"
      ]
    },
    {
      "kind": "theorem",
      "name": "eddington_sector_balance",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/eddington-sector-balance/",
      "source_line_start": 142,
      "source_line_end": 144,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P78"
      ]
    },
    {
      "kind": "theorem",
      "name": "bipolar_jet_theorem",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/bipolar-jet-theorem/",
      "source_line_start": 159,
      "source_line_end": 161,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T90"
      ]
    },
    {
      "kind": "theorem",
      "name": "jet_power_from_spin",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/jet-power-from-spin/",
      "source_line_start": 177,
      "source_line_end": 179,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T91"
      ]
    },
    {
      "kind": "structure",
      "name": "JetCollimationData",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/jet-collimation-data/",
      "source_line_start": 188,
      "source_line_end": 199,
      "formal_status": "defined",
      "registry_ids": [
        "V.D131"
      ]
    },
    {
      "kind": "inductive",
      "name": "AGNType",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/agntype/",
      "source_line_start": 211,
      "source_line_end": 224,
      "formal_status": "defined",
      "registry_ids": [
        "V.D132"
      ]
    },
    {
      "kind": "theorem",
      "name": "quasar_luminosity",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/quasar-luminosity/",
      "source_line_start": 235,
      "source_line_end": 237,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P79"
      ]
    },
    {
      "kind": "def",
      "name": "nuclear_efficiency",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/nuclear-efficiency/",
      "source_line_start": 244,
      "source_line_end": 244,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "max_accretion_efficiency",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/max-accretion-efficiency/",
      "source_line_start": 246,
      "source_line_end": 246,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "accretion_efficiency_bound",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/accretion-efficiency-bound/",
      "source_line_start": 255,
      "source_line_end": 256,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T92"
      ]
    },
    {
      "kind": "def",
      "name": "stellar_bh_disk",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/stellar-bh-disk/",
      "source_line_start": 300,
      "source_line_end": 306,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "m87_jet",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/m87-jet/",
      "source_line_start": 309,
      "source_line_end": 314,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/eval-l316/",
      "source_line_start": 316,
      "source_line_end": 316,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/eval-l317/",
      "source_line_start": 317,
      "source_line_end": 317,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/eval-l318/",
      "source_line_start": 318,
      "source_line_end": 318,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/eval-l319/",
      "source_line_start": 319,
      "source_line_end": 319,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ToroidalFluxIntegral",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/toroidal-flux-integral/",
      "source_line_start": 327,
      "source_line_end": 334,
      "formal_status": "defined",
      "registry_ids": [
        "V.D285"
      ]
    },
    {
      "kind": "structure",
      "name": "PoloidalFluxIntegral",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/poloidal-flux-integral/",
      "source_line_start": 338,
      "source_line_end": 345,
      "formal_status": "defined",
      "registry_ids": [
        "V.D286"
      ]
    },
    {
      "kind": "theorem",
      "name": "flux_threading_theorem",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/flux-threading-theorem/",
      "source_line_start": 350,
      "source_line_end": 352,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T228"
      ]
    },
    {
      "kind": "theorem",
      "name": "homology_rank_t2_vs_s2",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/homology-rank-t2-vs-s2/",
      "source_line_start": 355,
      "source_line_end": 355,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "FluxRatio",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/flux-ratio/",
      "source_line_start": 358,
      "source_line_end": 367,
      "formal_status": "defined",
      "registry_ids": [
        "V.P153"
      ]
    },
    {
      "kind": "structure",
      "name": "JetPoloidalField",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/jet-poloidal-field/",
      "source_line_start": 375,
      "source_line_end": 386,
      "formal_status": "defined",
      "registry_ids": [
        "V.D289"
      ]
    },
    {
      "kind": "structure",
      "name": "JetHelicity",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/jet-helicity/",
      "source_line_start": 389,
      "source_line_end": 398,
      "formal_status": "defined",
      "registry_ids": [
        "V.D290"
      ]
    },
    {
      "kind": "theorem",
      "name": "jet_helicity_conserved",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/jet-helicity-conserved/",
      "source_line_start": 402,
      "source_line_end": 404,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T231"
      ]
    },
    {
      "kind": "theorem",
      "name": "jet_collimation_from_hoop_stress",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/jet-collimation-from-hoop-stress/",
      "source_line_start": 408,
      "source_line_end": 410,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T232"
      ]
    },
    {
      "kind": "def",
      "name": "m87_jet_magnetic",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/m87-jet-magnetic/",
      "source_line_start": 413,
      "source_line_end": 414,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "m87_jet_helicity",
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/m87-jet-helicity/",
      "source_line_start": 417,
      "source_line_end": 418,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/eval-l420/",
      "source_line_start": 420,
      "source_line_end": 420,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/eval-l421/",
      "source_line_start": 421,
      "source_line_end": 423,
      "formal_status": "computed",
      "registry_ids": []
    }
  ],
  "right_rail": {
    "related": [
      {
        "title": "TauLib Overview",
        "url": "/verify/taulib/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Module",
      "source": "Corpus projection",
      "commit": "cb5e8301"
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
  "type": "TauLib Module"
}
---

## Corpus TauLib Projection

This page is generated directly from the pinned TauLib Lean source snapshot in `corpus/taulib-sources/project`. It is a Corpus-native module view designed for cross-linking Registry, Construction Spine, Results, and Verify surfaces.

## Source Provenance

- Source repository: `Panta-Rhei-Research/taulib`
- Source commit: [`cb5e8301`](https://github.com/Panta-Rhei-Research/taulib/commit/cb5e83015b54dd72eba560953fe2461820078757)
- Source path: [`TauLib/BookV/Astrophysics/AccretionJets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Astrophysics/AccretionJets.lean`
- SHA-256: `289a035030d527078230c0e16240392af4ae211a436e54183ba49ee5c0ecff11`

## Registry Links

- `V.D129` — Accretion Funnel (tau-geodesic)
- `V.D130` — Jet Axis (Topological Channel)
- `V.D131` — Synchrotron Readout
- `V.D132` — AGN Lifecycle Phase
- `V.D285` — Toroidal Flux Integral
- `V.D286` — Poloidal Flux Integral
- `V.D289` — Jet Poloidal Field
- `V.D290` — Jet Magnetic Helicity
- `V.P153` — Flux Ratio
- `V.P77` — Equatorial focusing
- `V.P78` — Jet-Torus Alignment
- `V.P79` — Neutrino Emission Channel
- `V.R185` — The alpha-viscosity re-read
- `V.R186` — Observational comparison
- `V.R187` — Eddington Limit Re-Read
- `V.R188` — The ubiquitous sqrt3
- `V.R189` — IceCube neutrinos from AGN
- `V.R190` — Quasar Redshift Distribution
- `V.R191` — Why the exponent is sim 4
- `V.T228` — Flux Threading Theorem
- `V.T231` — Jet Helicity Conservation
- `V.T232` — Jet Collimation from Hoop Stress
- `V.T90` — Jet Collimation Theorem
- `V.T91` — Accretion Luminosity Bound
- `V.T92` — AGN Unification Theorem

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Astrophysics.Supernovae`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Astrophysics.BinaryMergersGW`

## Declaration Counts

- `def`: 6
- `eval`: 6
- `inductive`: 2
- `structure`: 8
- `theorem`: 10

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `theorem` | [accretion_as_defect_infall](/verify/taulib/docs/book-v-astrophysics-accretion-jets/accretion-as-defect-infall/) | L79-L81 | formalized | `V.P77` |
| `inductive` | [DiskModel](/verify/taulib/docs/book-v-astrophysics-accretion-jets/disk-model/) | L88-L95 | defined | — |
| `structure` | [AccretionDiskStructure](/verify/taulib/docs/book-v-astrophysics-accretion-jets/accretion-disk-structure/) | L102-L115 | defined | `V.D129` |
| `structure` | [EddingtonLimitData](/verify/taulib/docs/book-v-astrophysics-accretion-jets/eddington-limit-data/) | L125-L134 | defined | `V.D130` |
| `theorem` | [eddington_sector_balance](/verify/taulib/docs/book-v-astrophysics-accretion-jets/eddington-sector-balance/) | L142-L144 | formalized | `V.P78` |
| `theorem` | [bipolar_jet_theorem](/verify/taulib/docs/book-v-astrophysics-accretion-jets/bipolar-jet-theorem/) | L159-L161 | formalized | `V.T90` |
| `theorem` | [jet_power_from_spin](/verify/taulib/docs/book-v-astrophysics-accretion-jets/jet-power-from-spin/) | L177-L179 | formalized | `V.T91` |
| `structure` | [JetCollimationData](/verify/taulib/docs/book-v-astrophysics-accretion-jets/jet-collimation-data/) | L188-L199 | defined | `V.D131` |
| `inductive` | [AGNType](/verify/taulib/docs/book-v-astrophysics-accretion-jets/agntype/) | L211-L224 | defined | `V.D132` |
| `theorem` | [quasar_luminosity](/verify/taulib/docs/book-v-astrophysics-accretion-jets/quasar-luminosity/) | L235-L237 | formalized | `V.P79` |
| `def` | [nuclear_efficiency](/verify/taulib/docs/book-v-astrophysics-accretion-jets/nuclear-efficiency/) | L244-L244 | defined | — |
| `def` | [max_accretion_efficiency](/verify/taulib/docs/book-v-astrophysics-accretion-jets/max-accretion-efficiency/) | L246-L246 | defined | — |
| `theorem` | [accretion_efficiency_bound](/verify/taulib/docs/book-v-astrophysics-accretion-jets/accretion-efficiency-bound/) | L255-L256 | formalized | `V.T92` |
| `def` | [stellar_bh_disk](/verify/taulib/docs/book-v-astrophysics-accretion-jets/stellar-bh-disk/) | L300-L306 | defined | — |
| `def` | [m87_jet](/verify/taulib/docs/book-v-astrophysics-accretion-jets/m87-jet/) | L309-L314 | defined | — |
| `eval` | [#eval L316](/verify/taulib/docs/book-v-astrophysics-accretion-jets/eval-l316/) | L316-L316 | computed | — |
| `eval` | [#eval L317](/verify/taulib/docs/book-v-astrophysics-accretion-jets/eval-l317/) | L317-L317 | computed | — |
| `eval` | [#eval L318](/verify/taulib/docs/book-v-astrophysics-accretion-jets/eval-l318/) | L318-L318 | computed | — |
| `eval` | [#eval L319](/verify/taulib/docs/book-v-astrophysics-accretion-jets/eval-l319/) | L319-L319 | computed | — |
| `structure` | [ToroidalFluxIntegral](/verify/taulib/docs/book-v-astrophysics-accretion-jets/toroidal-flux-integral/) | L327-L334 | defined | `V.D285` |
| `structure` | [PoloidalFluxIntegral](/verify/taulib/docs/book-v-astrophysics-accretion-jets/poloidal-flux-integral/) | L338-L345 | defined | `V.D286` |
| `theorem` | [flux_threading_theorem](/verify/taulib/docs/book-v-astrophysics-accretion-jets/flux-threading-theorem/) | L350-L352 | formalized | `V.T228` |
| `theorem` | [homology_rank_t2_vs_s2](/verify/taulib/docs/book-v-astrophysics-accretion-jets/homology-rank-t2-vs-s2/) | L355-L355 | formalized | — |
| `structure` | [FluxRatio](/verify/taulib/docs/book-v-astrophysics-accretion-jets/flux-ratio/) | L358-L367 | defined | `V.P153` |
| `structure` | [JetPoloidalField](/verify/taulib/docs/book-v-astrophysics-accretion-jets/jet-poloidal-field/) | L375-L386 | defined | `V.D289` |
| `structure` | [JetHelicity](/verify/taulib/docs/book-v-astrophysics-accretion-jets/jet-helicity/) | L389-L398 | defined | `V.D290` |
| `theorem` | [jet_helicity_conserved](/verify/taulib/docs/book-v-astrophysics-accretion-jets/jet-helicity-conserved/) | L402-L404 | formalized | `V.T231` |
| `theorem` | [jet_collimation_from_hoop_stress](/verify/taulib/docs/book-v-astrophysics-accretion-jets/jet-collimation-from-hoop-stress/) | L408-L410 | formalized | `V.T232` |
| `def` | [m87_jet_magnetic](/verify/taulib/docs/book-v-astrophysics-accretion-jets/m87-jet-magnetic/) | L413-L414 | defined | — |
| `def` | [m87_jet_helicity](/verify/taulib/docs/book-v-astrophysics-accretion-jets/m87-jet-helicity/) | L417-L418 | defined | — |
| `eval` | [#eval L420](/verify/taulib/docs/book-v-astrophysics-accretion-jets/eval-l420/) | L420-L420 | computed | — |
| `eval` | [#eval L421](/verify/taulib/docs/book-v-astrophysics-accretion-jets/eval-l421/) | L421-L423 | computed | — |
