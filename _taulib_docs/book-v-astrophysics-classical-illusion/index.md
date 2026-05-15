---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Astrophysics.ClassicalIllusion",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Astrophysics.ClassicalIllusion`.",
  "module_name": "TauLib.BookV.Astrophysics.ClassicalIllusion",
  "module_slug": "book-v-astrophysics-classical-illusion",
  "book": "BookV",
  "family": "Astrophysics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Astrophysics/ClassicalIllusion.lean",
  "sha256": "0bc93f8d69a0ddbfa843dddf0a757a5611ef5141f4a19fc1f346ec5f79a329f0",
  "imports": [
    "TauLib.BookV.FluidMacro.PhaseTransitions"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Astrophysics.KeplerSolarSystem",
    "TauLib.BookV.Cosmology.BigBangRegime"
  ],
  "registry_ids": [
    "V.D117",
    "V.P56",
    "V.P57",
    "V.P58",
    "V.R161",
    "V.R162",
    "V.R163",
    "V.R164",
    "V.T78",
    "V.T79",
    "V.T80"
  ],
  "declaration_counts": {
    "inductive": 3,
    "structure": 1,
    "def": 2,
    "theorem": 6,
    "eval": 4
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "ReadoutRegime",
      "url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/readout-regime/",
      "source_line_start": 70,
      "source_line_end": 79,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ClassicalReadoutMap",
      "url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/classical-readout-map/",
      "source_line_start": 87,
      "source_line_end": 98,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D117"
      ]
    },
    {
      "kind": "def",
      "name": "newtonian_readout",
      "url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/newtonian-readout/",
      "source_line_start": 101,
      "source_line_end": 104,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "post_newtonian_readout",
      "url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/post-newtonian-readout/",
      "source_line_start": 107,
      "source_line_end": 110,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "classical_limit_theorem",
      "url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/classical-limit-theorem/",
      "source_line_start": 123,
      "source_line_end": 125,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T78"
      ]
    },
    {
      "kind": "inductive",
      "name": "ApparentForce",
      "url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/apparent-force/",
      "source_line_start": 132,
      "source_line_end": 143,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "force_free_ontology",
      "url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/force-free-ontology/",
      "source_line_start": 147,
      "source_line_end": 149,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P56"
      ]
    },
    {
      "kind": "theorem",
      "name": "euler_lagrange_recovery",
      "url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/euler-lagrange-recovery/",
      "source_line_start": 161,
      "source_line_end": 163,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T79"
      ]
    },
    {
      "kind": "theorem",
      "name": "action_from_defect",
      "url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/action-from-defect/",
      "source_line_start": 175,
      "source_line_end": 177,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P57"
      ]
    },
    {
      "kind": "inductive",
      "name": "ConservationLaw",
      "url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/conservation-law/",
      "source_line_start": 184,
      "source_line_end": 191,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "conservation_from_sectors",
      "url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/conservation-from-sectors/",
      "source_line_start": 200,
      "source_line_end": 202,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P58"
      ]
    },
    {
      "kind": "theorem",
      "name": "classical_completeness",
      "url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/classical-completeness/",
      "source_line_start": 213,
      "source_line_end": 215,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T80"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/eval-l247/",
      "source_line_start": 247,
      "source_line_end": 247,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": [
        "V.R161",
        "V.R162",
        "V.R163",
        "V.R164"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/eval-l248/",
      "source_line_start": 248,
      "source_line_end": 248,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/eval-l249/",
      "source_line_start": 249,
      "source_line_end": 249,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/eval-l250/",
      "source_line_start": 250,
      "source_line_end": 252,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean",
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
- Source path: [`TauLib/BookV/Astrophysics/ClassicalIllusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Astrophysics/ClassicalIllusion.lean`
- SHA-256: `0bc93f8d69a0ddbfa843dddf0a757a5611ef5141f4a19fc1f346ec5f79a329f0`

## Registry Links

- `V.D117` — Classical Validity Scale --- V.D50
- `V.P56` — Capacity Gradient as Apparent Dark Matter --- V.P20
- `V.P57` — Bertrand as Readout Constraint --- V.P21
- `V.P58` — Newton's First Law as Limit --- V.P22
- `V.R161` — The three conditions quantified
- `V.R162` — The MOND scale as proxy
- `V.R163` — No free parameters
- `V.R164` — The dark matter debate is a projection artifact
- `V.T78` — Newtonian Limit --- V.T30
- `V.T79` — Two-Regime Readout --- V.T31
- `V.T80` — Correspondence Tower --- V.T32

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.FluidMacro.PhaseTransitions`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Astrophysics.KeplerSolarSystem`
- `TauLib.BookV.Cosmology.BigBangRegime`

## Declaration Counts

- `def`: 2
- `eval`: 4
- `inductive`: 3
- `structure`: 1
- `theorem`: 6

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [ReadoutRegime](/corpus/taulib/docs/book-v-astrophysics-classical-illusion/readout-regime/) | L70-L79 | type/data schema | type/data schema | — |
| `structure` | [ClassicalReadoutMap](/corpus/taulib/docs/book-v-astrophysics-classical-illusion/classical-readout-map/) | L87-L98 | type/data schema | type/data schema | `V.D117` |
| `def` | [newtonian_readout](/corpus/taulib/docs/book-v-astrophysics-classical-illusion/newtonian-readout/) | L101-L104 | definition | definition | — |
| `def` | [post_newtonian_readout](/corpus/taulib/docs/book-v-astrophysics-classical-illusion/post-newtonian-readout/) | L107-L110 | definition | definition | — |
| `theorem` | [classical_limit_theorem](/corpus/taulib/docs/book-v-astrophysics-classical-illusion/classical-limit-theorem/) | L123-L125 | proof obligation | formal proof obligation checked | `V.T78` |
| `inductive` | [ApparentForce](/corpus/taulib/docs/book-v-astrophysics-classical-illusion/apparent-force/) | L132-L143 | type/data schema | type/data schema | — |
| `theorem` | [force_free_ontology](/corpus/taulib/docs/book-v-astrophysics-classical-illusion/force-free-ontology/) | L147-L149 | proof obligation | formal proof obligation checked | `V.P56` |
| `theorem` | [euler_lagrange_recovery](/corpus/taulib/docs/book-v-astrophysics-classical-illusion/euler-lagrange-recovery/) | L161-L163 | proof obligation | formal proof obligation checked | `V.T79` |
| `theorem` | [action_from_defect](/corpus/taulib/docs/book-v-astrophysics-classical-illusion/action-from-defect/) | L175-L177 | proof obligation | formal proof obligation checked | `V.P57` |
| `inductive` | [ConservationLaw](/corpus/taulib/docs/book-v-astrophysics-classical-illusion/conservation-law/) | L184-L191 | type/data schema | type/data schema | — |
| `theorem` | [conservation_from_sectors](/corpus/taulib/docs/book-v-astrophysics-classical-illusion/conservation-from-sectors/) | L200-L202 | proof obligation | formal proof obligation checked | `V.P58` |
| `theorem` | [classical_completeness](/corpus/taulib/docs/book-v-astrophysics-classical-illusion/classical-completeness/) | L213-L215 | proof obligation | formal proof obligation checked | `V.T80` |
| `eval` | [#eval L247](/corpus/taulib/docs/book-v-astrophysics-classical-illusion/eval-l247/) | L247-L247 | computed check | computed check | `V.R161`, `V.R162`, `V.R163`, `V.R164` |
| `eval` | [#eval L248](/corpus/taulib/docs/book-v-astrophysics-classical-illusion/eval-l248/) | L248-L248 | computed check | computed check | — |
| `eval` | [#eval L249](/corpus/taulib/docs/book-v-astrophysics-classical-illusion/eval-l249/) | L249-L249 | computed check | computed check | — |
| `eval` | [#eval L250](/corpus/taulib/docs/book-v-astrophysics-classical-illusion/eval-l250/) | L250-L252 | computed check | computed check | — |
