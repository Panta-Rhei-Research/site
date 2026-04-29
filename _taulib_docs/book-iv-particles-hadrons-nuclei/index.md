---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Particles.HadronsNuclei",
  "permalink": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Particles.HadronsNuclei`.",
  "module_name": "TauLib.BookIV.Particles.HadronsNuclei",
  "module_slug": "book-iv-particles-hadrons-nuclei",
  "book": "BookIV",
  "family": "Particles",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Particles/HadronsNuclei.lean",
  "sha256": "25457c9569572bea93783463eac1a343a51030fe5de3a0924ef0fadd5b9d2492",
  "imports": [
    "TauLib.BookIV.Particles.BetaDecay"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Particles.PeriodicTable"
  ],
  "registry_ids": [
    "IV.D200",
    "IV.D201",
    "IV.D202",
    "IV.P128",
    "IV.P129",
    "IV.P130",
    "IV.P131",
    "IV.P132",
    "IV.R128",
    "IV.R129",
    "IV.R130",
    "IV.R131",
    "IV.R132",
    "IV.R133",
    "IV.R134",
    "IV.R135",
    "IV.R136",
    "IV.R137",
    "IV.R138",
    "IV.R139"
  ],
  "declaration_counts": {
    "inductive": 1,
    "structure": 13,
    "def": 19,
    "theorem": 8,
    "eval": 10
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "BaryonNumber",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/baryon-number/",
      "source_line_start": 56,
      "source_line_end": 61,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MesonClassification",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/meson-classification/",
      "source_line_start": 70,
      "source_line_end": 81,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D200"
      ]
    },
    {
      "kind": "def",
      "name": "pion_plus",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/pion-plus/",
      "source_line_start": 84,
      "source_line_end": 85,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "kaon_plus",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/kaon-plus/",
      "source_line_start": 87,
      "source_line_end": 88,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "rho_meson",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/rho-meson/",
      "source_line_start": 90,
      "source_line_end": 91,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EtaEtaPrime",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eta-eta-prime/",
      "source_line_start": 100,
      "source_line_end": 107,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R128"
      ]
    },
    {
      "kind": "def",
      "name": "eta_eta_prime",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eta-eta-prime-l109/",
      "source_line_start": 109,
      "source_line_end": 109,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GlueballDef",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/glueball-def/",
      "source_line_start": 120,
      "source_line_end": 129,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D201"
      ]
    },
    {
      "kind": "def",
      "name": "glueball_def",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/glueball-def-l131/",
      "source_line_start": 131,
      "source_line_end": 131,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "glueball_no_quarks",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/glueball-no-quarks/",
      "source_line_start": 133,
      "source_line_end": 133,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "glueballs_mass_gap",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/glueballs-mass-gap/",
      "source_line_start": 142,
      "source_line_end": 143,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R129"
      ]
    },
    {
      "kind": "structure",
      "name": "NucleonMassDecomp",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nucleon-mass-decomp/",
      "source_line_start": 157,
      "source_line_end": 170,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P128"
      ]
    },
    {
      "kind": "def",
      "name": "nucleon_mass_decomposition",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nucleon-mass-decomposition/",
      "source_line_start": 172,
      "source_line_end": 172,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nucleon_99pct_nonquark",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nucleon-99pct-nonquark/",
      "source_line_start": 174,
      "source_line_end": 175,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nucleon_decomp_sums",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nucleon-decomp-sums/",
      "source_line_start": 178,
      "source_line_end": 183,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "IsospinSplitting",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/isospin-splitting/",
      "source_line_start": 192,
      "source_line_end": 201,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R131"
      ]
    },
    {
      "kind": "def",
      "name": "isospin_splitting",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/isospin-splitting-l203/",
      "source_line_start": 203,
      "source_line_end": 203,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NuclearForce",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-force/",
      "source_line_start": 213,
      "source_line_end": 220,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D202"
      ]
    },
    {
      "kind": "def",
      "name": "nuclear_force",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-force-l222/",
      "source_line_start": 222,
      "source_line_end": 222,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DeuteronBinding",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/deuteron-binding/",
      "source_line_start": 231,
      "source_line_end": 238,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R133"
      ]
    },
    {
      "kind": "def",
      "name": "deuteron_binding",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/deuteron-binding-l240/",
      "source_line_start": 240,
      "source_line_end": 240,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NuclearSaturation",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-saturation/",
      "source_line_start": 249,
      "source_line_end": 256,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P129"
      ]
    },
    {
      "kind": "def",
      "name": "nuclear_force_saturation",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-force-saturation/",
      "source_line_start": 258,
      "source_line_end": 258,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NuclearShellStructure",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-shell-structure/",
      "source_line_start": 267,
      "source_line_end": 272,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P130"
      ]
    },
    {
      "kind": "def",
      "name": "nuclear_shell_structure",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-shell-structure-l274/",
      "source_line_start": 274,
      "source_line_end": 274,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "seven_magic_numbers",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/seven-magic-numbers/",
      "source_line_start": 276,
      "source_line_end": 277,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "Helium4Bound",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/helium4-bound/",
      "source_line_start": 286,
      "source_line_end": 297,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R135"
      ]
    },
    {
      "kind": "def",
      "name": "helium4_tightly_bound",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/helium4-tightly-bound/",
      "source_line_start": 299,
      "source_line_end": 299,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "helium4_doubly_magic",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/helium4-doubly-magic/",
      "source_line_start": 301,
      "source_line_end": 302,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "IronPeak",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/iron-peak/",
      "source_line_start": 314,
      "source_line_end": 323,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P131"
      ]
    },
    {
      "kind": "def",
      "name": "iron_peak",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/iron-peak-l325/",
      "source_line_start": 325,
      "source_line_end": 325,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "iron_at_56",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/iron-at-56/",
      "source_line_start": 327,
      "source_line_end": 327,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "nucleosynthesis_forward",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nucleosynthesis-forward/",
      "source_line_start": 336,
      "source_line_end": 337,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R136"
      ]
    },
    {
      "kind": "def",
      "name": "alpha_decay_mode",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/alpha-decay-mode/",
      "source_line_start": 346,
      "source_line_end": 347,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R137"
      ]
    },
    {
      "kind": "structure",
      "name": "NeutronStabilityNuclear",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/neutron-stability-nuclear/",
      "source_line_start": 356,
      "source_line_end": 363,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R138"
      ]
    },
    {
      "kind": "def",
      "name": "neutron_stability_nuclear",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/neutron-stability-nuclear-l365/",
      "source_line_start": 365,
      "source_line_end": 365,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "gamma_decay_mode",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/gamma-decay-mode/",
      "source_line_start": 374,
      "source_line_end": 375,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R139"
      ]
    },
    {
      "kind": "structure",
      "name": "DecayChannels",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/decay-channels/",
      "source_line_start": 388,
      "source_line_end": 395,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P132"
      ]
    },
    {
      "kind": "def",
      "name": "decay_channels",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/decay-channels-l397/",
      "source_line_start": 397,
      "source_line_end": 397,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "three_decay_types",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/three-decay-types/",
      "source_line_start": 399,
      "source_line_end": 399,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "four_conservation_laws",
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/four-conservation-laws/",
      "source_line_start": 400,
      "source_line_end": 400,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l406/",
      "source_line_start": 406,
      "source_line_end": 406,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l407/",
      "source_line_start": 407,
      "source_line_end": 407,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l408/",
      "source_line_start": 408,
      "source_line_end": 408,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l409/",
      "source_line_start": 409,
      "source_line_end": 409,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l410/",
      "source_line_start": 410,
      "source_line_end": 410,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l411/",
      "source_line_start": 411,
      "source_line_end": 411,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l412/",
      "source_line_start": 412,
      "source_line_end": 412,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l413/",
      "source_line_start": 413,
      "source_line_end": 413,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l414/",
      "source_line_start": 414,
      "source_line_end": 414,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l415/",
      "source_line_start": 415,
      "source_line_end": 417,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean",
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
- Source path: [`TauLib/BookIV/Particles/HadronsNuclei.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Particles/HadronsNuclei.lean`
- SHA-256: `25457c9569572bea93783463eac1a343a51030fe5de3a0924ef0fadd5b9d2492`

## Registry Links

- `IV.D200` — Meson classification
- `IV.D201` — Glueball
- `IV.D202` — Nuclear force
- `IV.P128` — Nucleon mass decomposition
- `IV.P129` — Nuclear force saturation
- `IV.P130` — Nuclear shell structure
- `IV.P131` — Iron peak from competing sectors
- `IV.P132` — Decay channels from sector admissibility
- `IV.R128` — Eta-eta prime splitting
- `IV.R129` — Glueballs and the mass gap
- `IV.R130` — Mass from nothing
- `IV.R131` — Isospin splitting from polarity
- `IV.R132` — Proton lighter but ontologically later
- `IV.R133` — Deuteron binding in tau-language
- `IV.R134` — Spin-orbit from omega-sector
- `IV.R135` — Why He-4 is tightly bound
- `IV.R136` — Nucleosynthesis forward to Book V
- `IV.R137` — Alpha-decay as mode cluster ejection
- `IV.R138` — Neutron stability inside nuclei
- `IV.R139` — Gamma-decay as mode transition

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Particles.BetaDecay`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Particles.PeriodicTable`

## Declaration Counts

- `def`: 19
- `eval`: 10
- `inductive`: 1
- `structure`: 13
- `theorem`: 8

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [BaryonNumber](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/baryon-number/) | L56-L61 | defined | — |
| `structure` | [MesonClassification](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/meson-classification/) | L70-L81 | defined | `IV.D200` |
| `def` | [pion_plus](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/pion-plus/) | L84-L85 | defined | — |
| `def` | [kaon_plus](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/kaon-plus/) | L87-L88 | defined | — |
| `def` | [rho_meson](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/rho-meson/) | L90-L91 | defined | — |
| `structure` | [EtaEtaPrime](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eta-eta-prime/) | L100-L107 | defined | `IV.R128` |
| `def` | [eta_eta_prime](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eta-eta-prime-l109/) | L109-L109 | defined | — |
| `structure` | [GlueballDef](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/glueball-def/) | L120-L129 | defined | `IV.D201` |
| `def` | [glueball_def](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/glueball-def-l131/) | L131-L131 | defined | — |
| `theorem` | [glueball_no_quarks](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/glueball-no-quarks/) | L133-L133 | formalized | — |
| `def` | [glueballs_mass_gap](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/glueballs-mass-gap/) | L142-L143 | defined | `IV.R129` |
| `structure` | [NucleonMassDecomp](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nucleon-mass-decomp/) | L157-L170 | defined | `IV.P128` |
| `def` | [nucleon_mass_decomposition](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nucleon-mass-decomposition/) | L172-L172 | defined | — |
| `theorem` | [nucleon_99pct_nonquark](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nucleon-99pct-nonquark/) | L174-L175 | formalized | — |
| `theorem` | [nucleon_decomp_sums](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nucleon-decomp-sums/) | L178-L183 | formalized | — |
| `structure` | [IsospinSplitting](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/isospin-splitting/) | L192-L201 | defined | `IV.R131` |
| `def` | [isospin_splitting](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/isospin-splitting-l203/) | L203-L203 | defined | — |
| `structure` | [NuclearForce](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-force/) | L213-L220 | defined | `IV.D202` |
| `def` | [nuclear_force](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-force-l222/) | L222-L222 | defined | — |
| `structure` | [DeuteronBinding](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/deuteron-binding/) | L231-L238 | defined | `IV.R133` |
| `def` | [deuteron_binding](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/deuteron-binding-l240/) | L240-L240 | defined | — |
| `structure` | [NuclearSaturation](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-saturation/) | L249-L256 | defined | `IV.P129` |
| `def` | [nuclear_force_saturation](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-force-saturation/) | L258-L258 | defined | — |
| `structure` | [NuclearShellStructure](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-shell-structure/) | L267-L272 | defined | `IV.P130` |
| `def` | [nuclear_shell_structure](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-shell-structure-l274/) | L274-L274 | defined | — |
| `theorem` | [seven_magic_numbers](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/seven-magic-numbers/) | L276-L277 | formalized | — |
| `structure` | [Helium4Bound](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/helium4-bound/) | L286-L297 | defined | `IV.R135` |
| `def` | [helium4_tightly_bound](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/helium4-tightly-bound/) | L299-L299 | defined | — |
| `theorem` | [helium4_doubly_magic](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/helium4-doubly-magic/) | L301-L302 | formalized | — |
| `structure` | [IronPeak](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/iron-peak/) | L314-L323 | defined | `IV.P131` |
| `def` | [iron_peak](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/iron-peak-l325/) | L325-L325 | defined | — |
| `theorem` | [iron_at_56](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/iron-at-56/) | L327-L327 | formalized | — |
| `def` | [nucleosynthesis_forward](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nucleosynthesis-forward/) | L336-L337 | defined | `IV.R136` |
| `def` | [alpha_decay_mode](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/alpha-decay-mode/) | L346-L347 | defined | `IV.R137` |
| `structure` | [NeutronStabilityNuclear](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/neutron-stability-nuclear/) | L356-L363 | defined | `IV.R138` |
| `def` | [neutron_stability_nuclear](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/neutron-stability-nuclear-l365/) | L365-L365 | defined | — |
| `def` | [gamma_decay_mode](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/gamma-decay-mode/) | L374-L375 | defined | `IV.R139` |
| `structure` | [DecayChannels](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/decay-channels/) | L388-L395 | defined | `IV.P132` |
| `def` | [decay_channels](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/decay-channels-l397/) | L397-L397 | defined | — |
| `theorem` | [three_decay_types](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/three-decay-types/) | L399-L399 | formalized | — |
| `theorem` | [four_conservation_laws](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/four-conservation-laws/) | L400-L400 | formalized | — |
| `eval` | [#eval L406](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l406/) | L406-L406 | computed | — |
| `eval` | [#eval L407](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l407/) | L407-L407 | computed | — |
| `eval` | [#eval L408](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l408/) | L408-L408 | computed | — |
| `eval` | [#eval L409](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l409/) | L409-L409 | computed | — |
| `eval` | [#eval L410](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l410/) | L410-L410 | computed | — |
| `eval` | [#eval L411](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l411/) | L411-L411 | computed | — |
| `eval` | [#eval L412](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l412/) | L412-L412 | computed | — |
| `eval` | [#eval L413](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l413/) | L413-L413 | computed | — |
| `eval` | [#eval L414](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l414/) | L414-L414 | computed | — |
| `eval` | [#eval L415](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l415/) | L415-L417 | computed | — |
