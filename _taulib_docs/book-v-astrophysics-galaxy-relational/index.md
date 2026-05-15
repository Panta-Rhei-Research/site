---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Astrophysics.GalaxyRelational",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Astrophysics.GalaxyRelational`.",
  "module_name": "TauLib.BookV.Astrophysics.GalaxyRelational",
  "module_slug": "book-v-astrophysics-galaxy-relational",
  "book": "BookV",
  "family": "Astrophysics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Astrophysics/GalaxyRelational.lean",
  "sha256": "40ce7a316e3b9fd29702625ea6e6b1bdef169f3902f5c3898e82da955b406aac",
  "imports": [
    "TauLib.BookV.Astrophysics.KeplerSolarSystem"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Astrophysics.RotationCurves"
  ],
  "registry_ids": [
    "V.D120",
    "V.D121",
    "V.D122",
    "V.D299",
    "V.P163",
    "V.P164",
    "V.P63",
    "V.P64",
    "V.P65",
    "V.P66",
    "V.R169",
    "V.R170",
    "V.R171",
    "V.R172",
    "V.R173",
    "V.R422",
    "V.T239"
  ],
  "declaration_counts": {
    "inductive": 2,
    "structure": 5,
    "def": 3,
    "theorem": 6,
    "eval": 7
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "GalaxyMorphology",
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/galaxy-morphology/",
      "source_line_start": 62,
      "source_line_end": 73,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GalacticDefectBundle",
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/galactic-defect-bundle/",
      "source_line_start": 81,
      "source_line_end": 94,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D120"
      ]
    },
    {
      "kind": "def",
      "name": "milky_way",
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/milky-way/",
      "source_line_start": 97,
      "source_line_end": 103,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "morphology_from_topology",
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/morphology-from-topology/",
      "source_line_start": 116,
      "source_line_end": 118,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P63"
      ]
    },
    {
      "kind": "theorem",
      "name": "spiral_arms_density_waves",
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/spiral-arms-density-waves/",
      "source_line_start": 127,
      "source_line_end": 130,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P64"
      ]
    },
    {
      "kind": "inductive",
      "name": "RotationRegime",
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/rotation-regime/",
      "source_line_start": 137,
      "source_line_end": 144,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GalacticRotationProfile",
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/galactic-rotation-profile/",
      "source_line_start": 152,
      "source_line_end": 163,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D121"
      ]
    },
    {
      "kind": "theorem",
      "name": "tully_fisher_scaling",
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/tully-fisher-scaling/",
      "source_line_start": 176,
      "source_line_end": 178,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P65"
      ]
    },
    {
      "kind": "structure",
      "name": "GalaxyClusterData",
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/galaxy-cluster-data/",
      "source_line_start": 187,
      "source_line_end": 200,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D122"
      ]
    },
    {
      "kind": "theorem",
      "name": "virial_discrepancy",
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/virial-discrepancy/",
      "source_line_start": 210,
      "source_line_end": 211,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P66"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/eval-l243/",
      "source_line_start": 243,
      "source_line_end": 243,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": [
        "V.R169",
        "V.R170",
        "V.R171",
        "V.R172",
        "V.R173"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/eval-l244/",
      "source_line_start": 244,
      "source_line_end": 244,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/eval-l245/",
      "source_line_start": 245,
      "source_line_end": 245,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/eval-l246/",
      "source_line_start": 246,
      "source_line_end": 246,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HighZAccelerationEnhancement",
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/high-zacceleration-enhancement/",
      "source_line_start": 256,
      "source_line_end": 267,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D299"
      ]
    },
    {
      "kind": "structure",
      "name": "JWSTEnhancementTheorem",
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/jwstenhancement-theorem/",
      "source_line_start": 272,
      "source_line_end": 285,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.T239"
      ]
    },
    {
      "kind": "def",
      "name": "gnz11_enhancement",
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/gnz11-enhancement/",
      "source_line_start": 288,
      "source_line_end": 294,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "jades_z13_enhancement",
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/jades-z13-enhancement/",
      "source_line_start": 297,
      "source_line_end": 303,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sfe_enhancement_at_z10",
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/sfe-enhancement-at-z10/",
      "source_line_start": 306,
      "source_line_end": 307,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P163"
      ]
    },
    {
      "kind": "theorem",
      "name": "uv_lf_excess_jades",
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/uv-lf-excess-jades/",
      "source_line_start": 311,
      "source_line_end": 312,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P164"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/eval-l316/",
      "source_line_start": 316,
      "source_line_end": 316,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": [
        "V.R422"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/eval-l317/",
      "source_line_start": 317,
      "source_line_end": 317,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/eval-l318/",
      "source_line_start": 318,
      "source_line_end": 320,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean",
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
- Source path: [`TauLib/BookV/Astrophysics/GalaxyRelational.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Astrophysics/GalaxyRelational.lean`
- SHA-256: `40ce7a316e3b9fd29702625ea6e6b1bdef169f3902f5c3898e82da955b406aac`

## Registry Links

- `V.D120` — Galaxy as Relational Coherence --- V.D53
- `V.D121` — Cosmic Web as Capacity Skeleton --- V.D54
- `V.D122` — Morphological Capacity Profile --- V.D55
- `V.D299` — High-z Acceleration Enhancement
- `V.P163` — SFE Enhancement Factor
- `V.P164` — UV Luminosity Function Excess
- `V.P63` — Modified Jeans Scale --- V.P27
- `V.P64` — Galaxy Formation Sequence --- V.P28
- `V.P65` — Web Determines Galaxy Locations --- V.P29
- `V.P66` — Galactic Virial Theorem --- V.P30
- `V.R169` — No void between galaxies
- `V.R170` — Conjectural scope
- `V.R171` — Filaments are not gravitational wakes
- `V.R172` — Morphology is not destiny
- `V.R173` — Satellite planes and the missing satellite problem
- `V.R422` — JWST Comparison Table
- `V.T239` — JWST Enhancement Theorem

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Astrophysics.KeplerSolarSystem`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Astrophysics.RotationCurves`

## Declaration Counts

- `def`: 3
- `eval`: 7
- `inductive`: 2
- `structure`: 5
- `theorem`: 6

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [GalaxyMorphology](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/galaxy-morphology/) | L62-L73 | type/data schema | type/data schema | — |
| `structure` | [GalacticDefectBundle](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/galactic-defect-bundle/) | L81-L94 | type/data schema | type/data schema | `V.D120` |
| `def` | [milky_way](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/milky-way/) | L97-L103 | definition | definition | — |
| `theorem` | [morphology_from_topology](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/morphology-from-topology/) | L116-L118 | proof obligation | formal proof obligation checked | `V.P63` |
| `theorem` | [spiral_arms_density_waves](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/spiral-arms-density-waves/) | L127-L130 | proof obligation | formal proof obligation checked | `V.P64` |
| `inductive` | [RotationRegime](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/rotation-regime/) | L137-L144 | type/data schema | type/data schema | — |
| `structure` | [GalacticRotationProfile](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/galactic-rotation-profile/) | L152-L163 | type/data schema | type/data schema | `V.D121` |
| `theorem` | [tully_fisher_scaling](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/tully-fisher-scaling/) | L176-L178 | proof obligation | formal proof obligation checked | `V.P65` |
| `structure` | [GalaxyClusterData](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/galaxy-cluster-data/) | L187-L200 | type/data schema | type/data schema | `V.D122` |
| `theorem` | [virial_discrepancy](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/virial-discrepancy/) | L210-L211 | proof obligation | formal proof obligation checked | `V.P66` |
| `eval` | [#eval L243](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/eval-l243/) | L243-L243 | computed check | computed check | `V.R169`, `V.R170`, `V.R171`, `V.R172`, `V.R173` |
| `eval` | [#eval L244](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/eval-l244/) | L244-L244 | computed check | computed check | — |
| `eval` | [#eval L245](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/eval-l245/) | L245-L245 | computed check | computed check | — |
| `eval` | [#eval L246](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/eval-l246/) | L246-L246 | computed check | computed check | — |
| `structure` | [HighZAccelerationEnhancement](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/high-zacceleration-enhancement/) | L256-L267 | type/data schema | type/data schema | `V.D299` |
| `structure` | [JWSTEnhancementTheorem](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/jwstenhancement-theorem/) | L272-L285 | type/data schema | type/data schema | `V.T239` |
| `def` | [gnz11_enhancement](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/gnz11-enhancement/) | L288-L294 | definition | definition | — |
| `def` | [jades_z13_enhancement](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/jades-z13-enhancement/) | L297-L303 | definition | definition | — |
| `theorem` | [sfe_enhancement_at_z10](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/sfe-enhancement-at-z10/) | L306-L307 | proof obligation | formal proof obligation checked | `V.P163` |
| `theorem` | [uv_lf_excess_jades](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/uv-lf-excess-jades/) | L311-L312 | proof obligation | formal proof obligation checked | `V.P164` |
| `eval` | [#eval L316](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/eval-l316/) | L316-L316 | computed check | computed check | `V.R422` |
| `eval` | [#eval L317](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/eval-l317/) | L317-L317 | computed check | computed check | — |
| `eval` | [#eval L318](/corpus/taulib/docs/book-v-astrophysics-galaxy-relational/eval-l318/) | L318-L320 | computed check | computed check | — |
