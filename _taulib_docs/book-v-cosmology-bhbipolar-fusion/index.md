---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Cosmology.BHBipolarFusion",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Cosmology.BHBipolarFusion`.",
  "module_name": "TauLib.BookV.Cosmology.BHBipolarFusion",
  "module_slug": "book-v-cosmology-bhbipolar-fusion",
  "book": "BookV",
  "family": "Cosmology",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Cosmology/BHBipolarFusion.lean",
  "sha256": "e70cc8f6bb3d1623c511a96e8b8d9a3a28f29d0f1d454f0358ae4fbc62fda8ef",
  "imports": [
    "TauLib.BookV.Cosmology.BHBirthTopology"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Cosmology.NoShrinkExtended"
  ],
  "registry_ids": [
    "V.D168",
    "V.D169",
    "V.D170",
    "V.D171",
    "V.D172",
    "V.P94",
    "V.R223",
    "V.R224",
    "V.R225",
    "V.T111",
    "V.T112"
  ],
  "declaration_counts": {
    "structure": 7,
    "theorem": 7,
    "def": 8,
    "eval": 7
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "BHBipolarity",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/bhbipolarity/",
      "source_line_start": 61,
      "source_line_end": 70,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D168"
      ]
    },
    {
      "kind": "theorem",
      "name": "necessary_bipolarity",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/necessary-bipolarity/",
      "source_line_start": 82,
      "source_line_end": 83,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T111"
      ]
    },
    {
      "kind": "structure",
      "name": "PolarityImbalance",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/polarity-imbalance/",
      "source_line_start": 96,
      "source_line_end": 103,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D169"
      ]
    },
    {
      "kind": "def",
      "name": "BHBipolarity.imbalance",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/imbalance/",
      "source_line_start": 106,
      "source_line_end": 109,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "PolarityFixedPoint",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/polarity-fixed-point/",
      "source_line_start": 122,
      "source_line_end": 131,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P94"
      ]
    },
    {
      "kind": "def",
      "name": "polarity_fixed_point",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/polarity-fixed-point-l134/",
      "source_line_start": 134,
      "source_line_end": 138,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "polarity_convergence",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/polarity-convergence/",
      "source_line_start": 141,
      "source_line_end": 144,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BHBlueprint",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/bhblueprint/",
      "source_line_start": 154,
      "source_line_end": 161,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D170"
      ]
    },
    {
      "kind": "def",
      "name": "BlueprintFusion",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/blueprint-fusion/",
      "source_line_start": 173,
      "source_line_end": 181,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "V.D171"
      ]
    },
    {
      "kind": "structure",
      "name": "BlueprintMonoid",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/blueprint-monoid/",
      "source_line_start": 194,
      "source_line_end": 201,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D172"
      ]
    },
    {
      "kind": "theorem",
      "name": "blueprint_monoid_closure",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/blueprint-monoid-closure/",
      "source_line_start": 212,
      "source_line_end": 217,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T112"
      ]
    },
    {
      "kind": "theorem",
      "name": "fusion_mass_additive",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/fusion-mass-additive/",
      "source_line_start": 220,
      "source_line_end": 221,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BHEntropyRemark",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/bhentropy-remark/",
      "source_line_start": 231,
      "source_line_end": 240,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.R224"
      ]
    },
    {
      "kind": "def",
      "name": "bh_entropy_data",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/bh-entropy-data/",
      "source_line_start": 243,
      "source_line_end": 247,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "bh1",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/bh1/",
      "source_line_start": 267,
      "source_line_end": 271,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "bh2",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/bh2/",
      "source_line_start": 274,
      "source_line_end": 278,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "bh_fused",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/bh-fused/",
      "source_line_start": 281,
      "source_line_end": 281,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/eval-l283/",
      "source_line_start": 283,
      "source_line_end": 283,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/eval-l284/",
      "source_line_start": 284,
      "source_line_end": 284,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/eval-l285/",
      "source_line_start": 285,
      "source_line_end": 285,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/eval-l286/",
      "source_line_start": 286,
      "source_line_end": 286,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "PolarityContractionMap",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/polarity-contraction-map/",
      "source_line_start": 308,
      "source_line_end": 321,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "polarity_contraction",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/polarity-contraction/",
      "source_line_start": 323,
      "source_line_end": 323,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "polarity_contraction_strict",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/polarity-contraction-strict/",
      "source_line_start": 326,
      "source_line_end": 329,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "polarity_fixed_point_unique",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/polarity-fixed-point-unique/",
      "source_line_start": 332,
      "source_line_end": 336,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "polarity_fixed_point_consistent",
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/polarity-fixed-point-consistent/",
      "source_line_start": 340,
      "source_line_end": 343,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/eval-l346/",
      "source_line_start": 346,
      "source_line_end": 346,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/eval-l347/",
      "source_line_start": 347,
      "source_line_end": 347,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/eval-l348/",
      "source_line_start": 348,
      "source_line_end": 350,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean",
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
- Source path: [`TauLib/BookV/Cosmology/BHBipolarFusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Cosmology/BHBipolarFusion.lean`
- SHA-256: `e70cc8f6bb3d1623c511a96e8b8d9a3a28f29d0f1d454f0358ae4fbc62fda8ef`

## Registry Links

- `V.D168` — BH Bipolarity
- `V.D169` — Polarity Imbalance
- `V.D170` — Blueprint
- `V.D171` — Blueprint fusion mathrmFuse
- `V.D172` — Blueprint Monoid
- `V.P94` — Polarity Convergence
- `V.R223` — Irreversibility of mergers
- `V.R224` — BH Entropy Formula Interpretation
- `V.R225` — Export to Book VI
- `V.T111` — Necessary Bipolarity
- `V.T112` — Blueprint Monoid Closure

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Cosmology.BHBirthTopology`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Cosmology.NoShrinkExtended`

## Declaration Counts

- `def`: 8
- `eval`: 7
- `structure`: 7
- `theorem`: 7

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [BHBipolarity](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/bhbipolarity/) | L61-L70 | type/data schema | type/data schema | `V.D168` |
| `theorem` | [necessary_bipolarity](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/necessary-bipolarity/) | L82-L83 | proof obligation | formal proof obligation checked | `V.T111` |
| `structure` | [PolarityImbalance](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/polarity-imbalance/) | L96-L103 | type/data schema | type/data schema | `V.D169` |
| `def` | [BHBipolarity.imbalance](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/imbalance/) | L106-L109 | definition | definition | — |
| `structure` | [PolarityFixedPoint](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/polarity-fixed-point/) | L122-L131 | type/data schema | type/data schema | `V.P94` |
| `def` | [polarity_fixed_point](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/polarity-fixed-point-l134/) | L134-L138 | definition | definition | — |
| `theorem` | [polarity_convergence](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/polarity-convergence/) | L141-L144 | proof obligation | formal proof obligation checked | — |
| `structure` | [BHBlueprint](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/bhblueprint/) | L154-L161 | type/data schema | type/data schema | `V.D170` |
| `def` | [BlueprintFusion](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/blueprint-fusion/) | L173-L181 | definition | definition | `V.D171` |
| `structure` | [BlueprintMonoid](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/blueprint-monoid/) | L194-L201 | type/data schema | type/data schema | `V.D172` |
| `theorem` | [blueprint_monoid_closure](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/blueprint-monoid-closure/) | L212-L217 | proof obligation | formal proof obligation checked | `V.T112` |
| `theorem` | [fusion_mass_additive](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/fusion-mass-additive/) | L220-L221 | proof obligation | formal proof obligation checked | — |
| `structure` | [BHEntropyRemark](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/bhentropy-remark/) | L231-L240 | type/data schema | type/data schema | `V.R224` |
| `def` | [bh_entropy_data](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/bh-entropy-data/) | L243-L247 | definition | definition | — |
| `def` | [bh1](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/bh1/) | L267-L271 | definition | definition | — |
| `def` | [bh2](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/bh2/) | L274-L278 | definition | definition | — |
| `def` | [bh_fused](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/bh-fused/) | L281-L281 | definition | definition | — |
| `eval` | [#eval L283](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/eval-l283/) | L283-L283 | computed check | computed check | — |
| `eval` | [#eval L284](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/eval-l284/) | L284-L284 | computed check | computed check | — |
| `eval` | [#eval L285](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/eval-l285/) | L285-L285 | computed check | computed check | — |
| `eval` | [#eval L286](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/eval-l286/) | L286-L286 | computed check | computed check | — |
| `structure` | [PolarityContractionMap](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/polarity-contraction-map/) | L308-L321 | type/data schema | type/data schema | — |
| `def` | [polarity_contraction](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/polarity-contraction/) | L323-L323 | definition | definition | — |
| `theorem` | [polarity_contraction_strict](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/polarity-contraction-strict/) | L326-L329 | proof obligation | formal proof obligation checked | — |
| `theorem` | [polarity_fixed_point_unique](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/polarity-fixed-point-unique/) | L332-L336 | proof obligation | formal proof obligation checked | — |
| `theorem` | [polarity_fixed_point_consistent](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/polarity-fixed-point-consistent/) | L340-L343 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L346](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/eval-l346/) | L346-L346 | computed check | computed check | — |
| `eval` | [#eval L347](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/eval-l347/) | L347-L347 | computed check | computed check | — |
| `eval` | [#eval L348](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/eval-l348/) | L348-L350 | computed check | computed check | — |
