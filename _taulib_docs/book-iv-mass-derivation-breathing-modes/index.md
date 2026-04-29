---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.MassDerivation.BreathingModes",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.MassDerivation.BreathingModes`.",
  "module_name": "TauLib.BookIV.MassDerivation.BreathingModes",
  "module_slug": "book-iv-mass-derivation-breathing-modes",
  "book": "BookIV",
  "family": "MassDerivation",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/MassDerivation/BreathingModes.lean",
  "sha256": "e9960036c3f02b3146e9eea0b30e47e8ca1d093a7b4c26176015a645aa6d49a2",
  "imports": [
    "TauLib.BookIV.QuantumMechanics.EnergyEntropy",
    "TauLib.BookIV.Calibration.EpsteinZeta",
    "TauLib.BookIV.Physics.LemniscateCapacity"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.MassDerivation.HolonomyDetail"
  ],
  "registry_ids": [
    "IV.D309",
    "IV.D310",
    "IV.D311",
    "IV.D312",
    "IV.D313",
    "IV.P171",
    "IV.R336",
    "IV.R337",
    "IV.R338",
    "IV.T114",
    "IV.T115"
  ],
  "declaration_counts": {
    "structure": 5,
    "def": 6,
    "theorem": 11,
    "eval": 7
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "MassHierarchy",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/mass-hierarchy/",
      "source_line_start": 42,
      "source_line_end": 48,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R336"
      ]
    },
    {
      "kind": "def",
      "name": "mass_hierarchy",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/mass-hierarchy-l50/",
      "source_line_start": 50,
      "source_line_end": 52,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BreathingOperator",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/breathing-operator/",
      "source_line_start": 59,
      "source_line_end": 64,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D309"
      ]
    },
    {
      "kind": "def",
      "name": "breathing_operator",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/breathing-operator-l66/",
      "source_line_start": 66,
      "source_line_end": 69,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "breathing_is_inverse_iota_sq",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/breathing-is-inverse-iota-sq/",
      "source_line_start": 71,
      "source_line_end": 74,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BreathingSpectrum",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/breathing-spectrum/",
      "source_line_start": 81,
      "source_line_end": 87,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P171"
      ]
    },
    {
      "kind": "def",
      "name": "breathing_spectrum",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/breathing-spectrum-l89/",
      "source_line_start": 89,
      "source_line_end": 92,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "breathing_spectrum_discrete",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/breathing-spectrum-discrete/",
      "source_line_start": 94,
      "source_line_end": 95,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EpsteinZetaOnT2",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/epstein-zeta-on-t2/",
      "source_line_start": 102,
      "source_line_end": 105,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D310"
      ]
    },
    {
      "kind": "def",
      "name": "epstein_on_T2",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/epstein-on-t2/",
      "source_line_start": 107,
      "source_line_end": 108,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "epstein_shape_is_iota",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/epstein-shape-is-iota/",
      "source_line_start": 110,
      "source_line_end": 113,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "toroidal_dominance",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/toroidal-dominance/",
      "source_line_start": 120,
      "source_line_end": 122,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.R337"
      ]
    },
    {
      "kind": "def",
      "name": "chowla_selberg_data",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/chowla-selberg-data/",
      "source_line_start": 125,
      "source_line_end": 125,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D311"
      ]
    },
    {
      "kind": "theorem",
      "name": "leading_exponent_seven",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/leading-exponent-seven/",
      "source_line_start": 128,
      "source_line_end": 130,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T114"
      ]
    },
    {
      "kind": "theorem",
      "name": "s4_forced",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/s4-forced/",
      "source_line_start": 133,
      "source_line_end": 135,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.R338"
      ]
    },
    {
      "kind": "structure",
      "name": "ThreeFoldLemniscate",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/three-fold-lemniscate/",
      "source_line_start": 142,
      "source_line_end": 147,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D312"
      ]
    },
    {
      "kind": "def",
      "name": "three_fold_lemniscate",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/three-fold-lemniscate-l149/",
      "source_line_start": 149,
      "source_line_end": 150,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "three_supports",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/three-supports/",
      "source_line_start": 152,
      "source_line_end": 154,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "spectral_distance_sq",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/spectral-distance-sq/",
      "source_line_start": 157,
      "source_line_end": 158,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.D313"
      ]
    },
    {
      "kind": "theorem",
      "name": "adjacent_distance_sq_is_3",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/adjacent-distance-sq-is-3/",
      "source_line_start": 161,
      "source_line_end": 163,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T115"
      ]
    },
    {
      "kind": "theorem",
      "name": "bulk_dominates_surface",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/bulk-dominates-surface/",
      "source_line_start": 169,
      "source_line_end": 171,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "surface_dominates_coupling",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/surface-dominates-coupling/",
      "source_line_start": 173,
      "source_line_end": 175,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/eval-l181/",
      "source_line_start": 181,
      "source_line_end": 181,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/eval-l182/",
      "source_line_start": 182,
      "source_line_end": 182,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/eval-l183/",
      "source_line_start": 183,
      "source_line_end": 183,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/eval-l184/",
      "source_line_start": 184,
      "source_line_end": 184,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/eval-l185/",
      "source_line_start": 185,
      "source_line_end": 185,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/eval-l186/",
      "source_line_start": 186,
      "source_line_end": 186,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/eval-l187/",
      "source_line_start": 187,
      "source_line_end": 189,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean",
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
- Source path: [`TauLib/BookIV/MassDerivation/BreathingModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/MassDerivation/BreathingModes.lean`
- SHA-256: `e9960036c3f02b3146e9eea0b30e47e8ca1d093a7b4c26176015a645aa6d49a2`

## Registry Links

- `IV.D309` — Breathing operator
- `IV.D310` — Epstein zeta structure
- `IV.D311` — Chowla--Selberg decomposition
- `IV.D312` — Lemniscate three-fold
- `IV.D313` — Spectral distance sqrt3
- `IV.P171` — Breathing spectrum
- `IV.R336` — Ten orders of magnitude from one constant
- `IV.R337` — Toroidal dominance
- `IV.R338` — Structural origin of the exponent 7
- `IV.T114` — Leading exponent -7
- `IV.T115` — Three-fold distance squared

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.QuantumMechanics.EnergyEntropy`
- `TauLib.BookIV.Calibration.EpsteinZeta`
- `TauLib.BookIV.Physics.LemniscateCapacity`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.MassDerivation.HolonomyDetail`

## Declaration Counts

- `def`: 6
- `eval`: 7
- `structure`: 5
- `theorem`: 11

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [MassHierarchy](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/mass-hierarchy/) | L42-L48 | defined | `IV.R336` |
| `def` | [mass_hierarchy](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/mass-hierarchy-l50/) | L50-L52 | defined | — |
| `structure` | [BreathingOperator](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/breathing-operator/) | L59-L64 | defined | `IV.D309` |
| `def` | [breathing_operator](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/breathing-operator-l66/) | L66-L69 | defined | — |
| `theorem` | [breathing_is_inverse_iota_sq](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/breathing-is-inverse-iota-sq/) | L71-L74 | formalized | — |
| `structure` | [BreathingSpectrum](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/breathing-spectrum/) | L81-L87 | defined | `IV.P171` |
| `def` | [breathing_spectrum](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/breathing-spectrum-l89/) | L89-L92 | defined | — |
| `theorem` | [breathing_spectrum_discrete](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/breathing-spectrum-discrete/) | L94-L95 | formalized | — |
| `structure` | [EpsteinZetaOnT2](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/epstein-zeta-on-t2/) | L102-L105 | defined | `IV.D310` |
| `def` | [epstein_on_T2](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/epstein-on-t2/) | L107-L108 | defined | — |
| `theorem` | [epstein_shape_is_iota](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/epstein-shape-is-iota/) | L110-L113 | formalized | — |
| `theorem` | [toroidal_dominance](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/toroidal-dominance/) | L120-L122 | formalized | `IV.R337` |
| `def` | [chowla_selberg_data](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/chowla-selberg-data/) | L125-L125 | defined | `IV.D311` |
| `theorem` | [leading_exponent_seven](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/leading-exponent-seven/) | L128-L130 | formalized | `IV.T114` |
| `theorem` | [s4_forced](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/s4-forced/) | L133-L135 | formalized | `IV.R338` |
| `structure` | [ThreeFoldLemniscate](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/three-fold-lemniscate/) | L142-L147 | defined | `IV.D312` |
| `def` | [three_fold_lemniscate](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/three-fold-lemniscate-l149/) | L149-L150 | defined | — |
| `theorem` | [three_supports](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/three-supports/) | L152-L154 | formalized | — |
| `theorem` | [spectral_distance_sq](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/spectral-distance-sq/) | L157-L158 | formalized | `IV.D313` |
| `theorem` | [adjacent_distance_sq_is_3](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/adjacent-distance-sq-is-3/) | L161-L163 | formalized | `IV.T115` |
| `theorem` | [bulk_dominates_surface](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/bulk-dominates-surface/) | L169-L171 | formalized | — |
| `theorem` | [surface_dominates_coupling](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/surface-dominates-coupling/) | L173-L175 | formalized | — |
| `eval` | [#eval L181](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/eval-l181/) | L181-L181 | computed | — |
| `eval` | [#eval L182](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/eval-l182/) | L182-L182 | computed | — |
| `eval` | [#eval L183](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/eval-l183/) | L183-L183 | computed | — |
| `eval` | [#eval L184](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/eval-l184/) | L184-L184 | computed | — |
| `eval` | [#eval L185](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/eval-l185/) | L185-L185 | computed | — |
| `eval` | [#eval L186](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/eval-l186/) | L186-L186 | computed | — |
| `eval` | [#eval L187](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/eval-l187/) | L187-L189 | computed | — |
