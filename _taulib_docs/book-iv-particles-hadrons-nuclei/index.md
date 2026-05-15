---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Particles.HadronsNuclei",
  "permalink": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/",
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
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/baryon-number/",
      "source_line_start": 56,
      "source_line_end": 61,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MesonClassification",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/meson-classification/",
      "source_line_start": 70,
      "source_line_end": 81,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D200"
      ]
    },
    {
      "kind": "def",
      "name": "pion_plus",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/pion-plus/",
      "source_line_start": 84,
      "source_line_end": 85,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "kaon_plus",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/kaon-plus/",
      "source_line_start": 87,
      "source_line_end": 88,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "rho_meson",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/rho-meson/",
      "source_line_start": 90,
      "source_line_end": 91,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EtaEtaPrime",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eta-eta-prime/",
      "source_line_start": 100,
      "source_line_end": 107,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.R128"
      ]
    },
    {
      "kind": "def",
      "name": "eta_eta_prime",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eta-eta-prime-l109/",
      "source_line_start": 109,
      "source_line_end": 109,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GlueballDef",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/glueball-def/",
      "source_line_start": 120,
      "source_line_end": 129,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D201"
      ]
    },
    {
      "kind": "def",
      "name": "glueball_def",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/glueball-def-l131/",
      "source_line_start": 131,
      "source_line_end": 131,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "glueball_no_quarks",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/glueball-no-quarks/",
      "source_line_start": 133,
      "source_line_end": 133,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "glueballs_mass_gap",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/glueballs-mass-gap/",
      "source_line_start": 142,
      "source_line_end": 143,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "IV.R129"
      ]
    },
    {
      "kind": "structure",
      "name": "NucleonMassDecomp",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nucleon-mass-decomp/",
      "source_line_start": 157,
      "source_line_end": 170,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P128"
      ]
    },
    {
      "kind": "def",
      "name": "nucleon_mass_decomposition",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nucleon-mass-decomposition/",
      "source_line_start": 172,
      "source_line_end": 172,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nucleon_99pct_nonquark",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nucleon-99pct-nonquark/",
      "source_line_start": 174,
      "source_line_end": 175,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nucleon_decomp_sums",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nucleon-decomp-sums/",
      "source_line_start": 178,
      "source_line_end": 183,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "IsospinSplitting",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/isospin-splitting/",
      "source_line_start": 192,
      "source_line_end": 201,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.R131"
      ]
    },
    {
      "kind": "def",
      "name": "isospin_splitting",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/isospin-splitting-l203/",
      "source_line_start": 203,
      "source_line_end": 203,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NuclearForce",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-force/",
      "source_line_start": 213,
      "source_line_end": 220,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D202"
      ]
    },
    {
      "kind": "def",
      "name": "nuclear_force",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-force-l222/",
      "source_line_start": 222,
      "source_line_end": 222,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DeuteronBinding",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/deuteron-binding/",
      "source_line_start": 231,
      "source_line_end": 238,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.R133"
      ]
    },
    {
      "kind": "def",
      "name": "deuteron_binding",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/deuteron-binding-l240/",
      "source_line_start": 240,
      "source_line_end": 240,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NuclearSaturation",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-saturation/",
      "source_line_start": 249,
      "source_line_end": 256,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P129"
      ]
    },
    {
      "kind": "def",
      "name": "nuclear_force_saturation",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-force-saturation/",
      "source_line_start": 258,
      "source_line_end": 258,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NuclearShellStructure",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-shell-structure/",
      "source_line_start": 267,
      "source_line_end": 272,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P130"
      ]
    },
    {
      "kind": "def",
      "name": "nuclear_shell_structure",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-shell-structure-l274/",
      "source_line_start": 274,
      "source_line_end": 274,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "seven_magic_numbers",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/seven-magic-numbers/",
      "source_line_start": 276,
      "source_line_end": 277,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "Helium4Bound",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/helium4-bound/",
      "source_line_start": 286,
      "source_line_end": 297,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.R135"
      ]
    },
    {
      "kind": "def",
      "name": "helium4_tightly_bound",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/helium4-tightly-bound/",
      "source_line_start": 299,
      "source_line_end": 299,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "helium4_doubly_magic",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/helium4-doubly-magic/",
      "source_line_start": 301,
      "source_line_end": 302,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "IronPeak",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/iron-peak/",
      "source_line_start": 314,
      "source_line_end": 323,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P131"
      ]
    },
    {
      "kind": "def",
      "name": "iron_peak",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/iron-peak-l325/",
      "source_line_start": 325,
      "source_line_end": 325,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "iron_at_56",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/iron-at-56/",
      "source_line_start": 327,
      "source_line_end": 327,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "nucleosynthesis_forward",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nucleosynthesis-forward/",
      "source_line_start": 336,
      "source_line_end": 337,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "IV.R136"
      ]
    },
    {
      "kind": "def",
      "name": "alpha_decay_mode",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/alpha-decay-mode/",
      "source_line_start": 346,
      "source_line_end": 347,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "IV.R137"
      ]
    },
    {
      "kind": "structure",
      "name": "NeutronStabilityNuclear",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/neutron-stability-nuclear/",
      "source_line_start": 356,
      "source_line_end": 363,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.R138"
      ]
    },
    {
      "kind": "def",
      "name": "neutron_stability_nuclear",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/neutron-stability-nuclear-l365/",
      "source_line_start": 365,
      "source_line_end": 365,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "gamma_decay_mode",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/gamma-decay-mode/",
      "source_line_start": 374,
      "source_line_end": 375,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "IV.R139"
      ]
    },
    {
      "kind": "structure",
      "name": "DecayChannels",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/decay-channels/",
      "source_line_start": 388,
      "source_line_end": 395,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P132"
      ]
    },
    {
      "kind": "def",
      "name": "decay_channels",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/decay-channels-l397/",
      "source_line_start": 397,
      "source_line_end": 397,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "three_decay_types",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/three-decay-types/",
      "source_line_start": 399,
      "source_line_end": 399,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "four_conservation_laws",
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/four-conservation-laws/",
      "source_line_start": 400,
      "source_line_end": 400,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l406/",
      "source_line_start": 406,
      "source_line_end": 406,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l407/",
      "source_line_start": 407,
      "source_line_end": 407,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l408/",
      "source_line_start": 408,
      "source_line_end": 408,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l409/",
      "source_line_start": 409,
      "source_line_end": 409,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l410/",
      "source_line_start": 410,
      "source_line_end": 410,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l411/",
      "source_line_start": 411,
      "source_line_end": 411,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l412/",
      "source_line_start": 412,
      "source_line_end": 412,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l413/",
      "source_line_start": 413,
      "source_line_end": 413,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l414/",
      "source_line_start": 414,
      "source_line_end": 414,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l415/",
      "source_line_start": 415,
      "source_line_end": 417,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
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
        "url": "/corpus/taulib/docs/"
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

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [BaryonNumber](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/baryon-number/) | L56-L61 | type/data schema | type/data schema | — |
| `structure` | [MesonClassification](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/meson-classification/) | L70-L81 | type/data schema | type/data schema | `IV.D200` |
| `def` | [pion_plus](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/pion-plus/) | L84-L85 | definition | definition | — |
| `def` | [kaon_plus](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/kaon-plus/) | L87-L88 | definition | definition | — |
| `def` | [rho_meson](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/rho-meson/) | L90-L91 | definition | definition | — |
| `structure` | [EtaEtaPrime](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eta-eta-prime/) | L100-L107 | type/data schema | type/data schema | `IV.R128` |
| `def` | [eta_eta_prime](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eta-eta-prime-l109/) | L109-L109 | definition | definition | — |
| `structure` | [GlueballDef](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/glueball-def/) | L120-L129 | type/data schema | type/data schema | `IV.D201` |
| `def` | [glueball_def](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/glueball-def-l131/) | L131-L131 | definition | definition | — |
| `theorem` | [glueball_no_quarks](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/glueball-no-quarks/) | L133-L133 | proof obligation | formal proof obligation checked | — |
| `def` | [glueballs_mass_gap](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/glueballs-mass-gap/) | L142-L143 | docstring/data record | docstring/data record | `IV.R129` |
| `structure` | [NucleonMassDecomp](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nucleon-mass-decomp/) | L157-L170 | type/data schema | type/data schema | `IV.P128` |
| `def` | [nucleon_mass_decomposition](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nucleon-mass-decomposition/) | L172-L172 | definition | definition | — |
| `theorem` | [nucleon_99pct_nonquark](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nucleon-99pct-nonquark/) | L174-L175 | proof obligation | formal proof obligation checked | — |
| `theorem` | [nucleon_decomp_sums](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nucleon-decomp-sums/) | L178-L183 | proof obligation | formal proof obligation checked | — |
| `structure` | [IsospinSplitting](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/isospin-splitting/) | L192-L201 | type/data schema | type/data schema | `IV.R131` |
| `def` | [isospin_splitting](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/isospin-splitting-l203/) | L203-L203 | definition | definition | — |
| `structure` | [NuclearForce](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-force/) | L213-L220 | type/data schema | type/data schema | `IV.D202` |
| `def` | [nuclear_force](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-force-l222/) | L222-L222 | definition | definition | — |
| `structure` | [DeuteronBinding](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/deuteron-binding/) | L231-L238 | type/data schema | type/data schema | `IV.R133` |
| `def` | [deuteron_binding](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/deuteron-binding-l240/) | L240-L240 | definition | definition | — |
| `structure` | [NuclearSaturation](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-saturation/) | L249-L256 | type/data schema | type/data schema | `IV.P129` |
| `def` | [nuclear_force_saturation](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-force-saturation/) | L258-L258 | definition | definition | — |
| `structure` | [NuclearShellStructure](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-shell-structure/) | L267-L272 | type/data schema | type/data schema | `IV.P130` |
| `def` | [nuclear_shell_structure](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-shell-structure-l274/) | L274-L274 | definition | definition | — |
| `theorem` | [seven_magic_numbers](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/seven-magic-numbers/) | L276-L277 | proof obligation | formal proof obligation checked | — |
| `structure` | [Helium4Bound](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/helium4-bound/) | L286-L297 | type/data schema | type/data schema | `IV.R135` |
| `def` | [helium4_tightly_bound](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/helium4-tightly-bound/) | L299-L299 | definition | definition | — |
| `theorem` | [helium4_doubly_magic](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/helium4-doubly-magic/) | L301-L302 | proof obligation | formal proof obligation checked | — |
| `structure` | [IronPeak](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/iron-peak/) | L314-L323 | type/data schema | type/data schema | `IV.P131` |
| `def` | [iron_peak](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/iron-peak-l325/) | L325-L325 | definition | definition | — |
| `theorem` | [iron_at_56](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/iron-at-56/) | L327-L327 | proof obligation | formal proof obligation checked | — |
| `def` | [nucleosynthesis_forward](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/nucleosynthesis-forward/) | L336-L337 | docstring/data record | docstring/data record | `IV.R136` |
| `def` | [alpha_decay_mode](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/alpha-decay-mode/) | L346-L347 | docstring/data record | docstring/data record | `IV.R137` |
| `structure` | [NeutronStabilityNuclear](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/neutron-stability-nuclear/) | L356-L363 | type/data schema | type/data schema | `IV.R138` |
| `def` | [neutron_stability_nuclear](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/neutron-stability-nuclear-l365/) | L365-L365 | definition | definition | — |
| `def` | [gamma_decay_mode](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/gamma-decay-mode/) | L374-L375 | docstring/data record | docstring/data record | `IV.R139` |
| `structure` | [DecayChannels](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/decay-channels/) | L388-L395 | type/data schema | type/data schema | `IV.P132` |
| `def` | [decay_channels](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/decay-channels-l397/) | L397-L397 | definition | definition | — |
| `theorem` | [three_decay_types](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/three-decay-types/) | L399-L399 | proof obligation | formal proof obligation checked | — |
| `theorem` | [four_conservation_laws](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/four-conservation-laws/) | L400-L400 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L406](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l406/) | L406-L406 | computed check | computed check | — |
| `eval` | [#eval L407](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l407/) | L407-L407 | computed check | computed check | — |
| `eval` | [#eval L408](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l408/) | L408-L408 | computed check | computed check | — |
| `eval` | [#eval L409](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l409/) | L409-L409 | computed check | computed check | — |
| `eval` | [#eval L410](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l410/) | L410-L410 | computed check | computed check | — |
| `eval` | [#eval L411](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l411/) | L411-L411 | computed check | computed check | — |
| `eval` | [#eval L412](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l412/) | L412-L412 | computed check | computed check | — |
| `eval` | [#eval L413](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l413/) | L413-L413 | computed check | computed check | — |
| `eval` | [#eval L414](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l414/) | L414-L414 | computed check | computed check | — |
| `eval` | [#eval L415](/corpus/taulib/docs/book-iv-particles-hadrons-nuclei/eval-l415/) | L415-L417 | computed check | computed check | — |
