---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Sectors.CouplingFormulas",
  "permalink": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Sectors.CouplingFormulas`.",
  "module_name": "TauLib.BookIV.Sectors.CouplingFormulas",
  "module_slug": "book-iv-sectors-coupling-formulas",
  "book": "BookIV",
  "family": "Sectors",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Sectors/CouplingFormulas.lean",
  "sha256": "03e07bfd551088e180647336d30065ef7a938bc2a24aa8e2ea2636bbe9164748",
  "imports": [
    "TauLib.BookIV.Sectors.SectorParameters"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Arena.FiveSectors",
    "TauLib.BookIV.Calibration.DimensionlessCouplings",
    "TauLib.BookIV.Physics.MassEnergy",
    "TauLib.BookIV.Physics.Thermodynamics",
    "TauLib.BookIV.Sectors.FineStructure",
    "TauLib.BookV.Gravity.EinsteinEquation"
  ],
  "registry_ids": [
    "IV.D07",
    "IV.P01",
    "IV.P03",
    "IV.T01",
    "IV.T02"
  ],
  "declaration_counts": {
    "structure": 1,
    "def": 13,
    "theorem": 12,
    "eval": 13
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "CouplingFormula",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/coupling-formula/",
      "source_line_start": 61,
      "source_line_end": 72,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D07"
      ]
    },
    {
      "kind": "def",
      "name": "CouplingFormula.toFloat",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/to-float/",
      "source_line_start": 75,
      "source_line_end": 89,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "iotaD_pos",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/iota-d-pos/",
      "source_line_start": 92,
      "source_line_end": 92,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "iota_pos",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/iota-pos/",
      "source_line_start": 93,
      "source_line_end": 93,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "oneMinusIota_pos",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/one-minus-iota-pos/",
      "source_line_start": 94,
      "source_line_end": 95,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "onePlusIota_pos",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/one-plus-iota-pos/",
      "source_line_start": 96,
      "source_line_end": 97,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "kappa_DD",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/kappa-dd/",
      "source_line_start": 104,
      "source_line_end": 109,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "kappa_AA",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/kappa-aa/",
      "source_line_start": 112,
      "source_line_end": 117,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "kappa_BB",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/kappa-bb/",
      "source_line_start": 120,
      "source_line_end": 125,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "kappa_CC",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/kappa-cc/",
      "source_line_start": 128,
      "source_line_end": 133,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "kappa_AB",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/kappa-ab/",
      "source_line_start": 136,
      "source_line_end": 141,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "kappa_AC",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/kappa-ac/",
      "source_line_start": 144,
      "source_line_end": 149,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "kappa_AD",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/kappa-ad/",
      "source_line_start": 152,
      "source_line_end": 157,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "kappa_BC",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/kappa-bc/",
      "source_line_start": 160,
      "source_line_end": 165,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "kappa_BD",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/kappa-bd/",
      "source_line_start": 168,
      "source_line_end": 173,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "kappa_CD",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/kappa-cd/",
      "source_line_start": 176,
      "source_line_end": 181,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "all_coupling_formulas",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/all-coupling-formulas/",
      "source_line_start": 184,
      "source_line_end": 187,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "temporal_complement",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/temporal-complement/",
      "source_line_start": 197,
      "source_line_end": 200,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T01"
      ]
    },
    {
      "kind": "theorem",
      "name": "temporal_complement_denom",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/temporal-complement-denom/",
      "source_line_start": 203,
      "source_line_end": 205,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "temporal_multiplicative",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/temporal-multiplicative/",
      "source_line_start": 216,
      "source_line_end": 220,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T02"
      ]
    },
    {
      "kind": "theorem",
      "name": "em_is_weak_squared",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/em-is-weak-squared/",
      "source_line_start": 228,
      "source_line_end": 231,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "weak_strong_is_multiplicative",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/weak-strong-is-multiplicative/",
      "source_line_start": 235,
      "source_line_end": 239,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "all_formulas_positive",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/all-formulas-positive/",
      "source_line_start": 248,
      "source_line_end": 257,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P01"
      ]
    },
    {
      "kind": "theorem",
      "name": "coupling_ledger_count",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/coupling-ledger-count/",
      "source_line_start": 260,
      "source_line_end": 261,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "coupling_formula",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/coupling-formula-l269/",
      "source_line_start": 269,
      "source_line_end": 287,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "self_coupling_order",
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/self-coupling-order/",
      "source_line_start": 295,
      "source_line_end": 301,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l308/",
      "source_line_start": 308,
      "source_line_end": 308,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l309/",
      "source_line_start": 309,
      "source_line_end": 309,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l310/",
      "source_line_start": 310,
      "source_line_end": 310,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l311/",
      "source_line_start": 311,
      "source_line_end": 311,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l314/",
      "source_line_start": 314,
      "source_line_end": 314,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l315/",
      "source_line_start": 315,
      "source_line_end": 315,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l316/",
      "source_line_start": 316,
      "source_line_end": 316,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l317/",
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
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l318/",
      "source_line_start": 318,
      "source_line_end": 318,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l319/",
      "source_line_start": 319,
      "source_line_end": 319,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l322/",
      "source_line_start": 322,
      "source_line_end": 322,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l323/",
      "source_line_start": 323,
      "source_line_end": 323,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l326/",
      "source_line_start": 326,
      "source_line_end": 328,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean",
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
- Source path: [`TauLib/BookIV/Sectors/CouplingFormulas.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Sectors/CouplingFormulas.lean`
- SHA-256: `03e07bfd551088e180647336d30065ef7a938bc2a24aa8e2ea2636bbe9164748`

## Registry Links

- `IV.D07` — Coupling Formula Map
- `IV.P01` — All Couplings Positive
- `IV.P03` — Power Hierarchy
- `IV.T01` — Temporal Complement
- `IV.T02` — Temporal Multiplicative Closure

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Sectors.SectorParameters`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Arena.FiveSectors`
- `TauLib.BookIV.Calibration.DimensionlessCouplings`
- `TauLib.BookIV.Physics.MassEnergy`
- `TauLib.BookIV.Physics.Thermodynamics`
- `TauLib.BookIV.Sectors.FineStructure`
- `TauLib.BookV.Gravity.EinsteinEquation`

## Declaration Counts

- `def`: 13
- `eval`: 13
- `structure`: 1
- `theorem`: 12

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [CouplingFormula](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/coupling-formula/) | L61-L72 | type/data schema | type/data schema | `IV.D07` |
| `def` | [CouplingFormula.toFloat](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/to-float/) | L75-L89 | data/computed value | data/computed value | — |
| `theorem` | [iotaD_pos](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/iota-d-pos/) | L92-L92 | proof obligation | formal proof obligation checked | — |
| `theorem` | [iota_pos](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/iota-pos/) | L93-L93 | proof obligation | formal proof obligation checked | — |
| `theorem` | [oneMinusIota_pos](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/one-minus-iota-pos/) | L94-L95 | proof obligation | formal proof obligation checked | — |
| `theorem` | [onePlusIota_pos](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/one-plus-iota-pos/) | L96-L97 | proof obligation | formal proof obligation checked | — |
| `def` | [kappa_DD](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/kappa-dd/) | L104-L109 | definition | definition | — |
| `def` | [kappa_AA](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/kappa-aa/) | L112-L117 | definition | definition | — |
| `def` | [kappa_BB](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/kappa-bb/) | L120-L125 | definition | definition | — |
| `def` | [kappa_CC](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/kappa-cc/) | L128-L133 | definition | definition | — |
| `def` | [kappa_AB](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/kappa-ab/) | L136-L141 | definition | definition | — |
| `def` | [kappa_AC](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/kappa-ac/) | L144-L149 | definition | definition | — |
| `def` | [kappa_AD](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/kappa-ad/) | L152-L157 | definition | definition | — |
| `def` | [kappa_BC](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/kappa-bc/) | L160-L165 | definition | definition | — |
| `def` | [kappa_BD](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/kappa-bd/) | L168-L173 | definition | definition | — |
| `def` | [kappa_CD](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/kappa-cd/) | L176-L181 | definition | definition | — |
| `def` | [all_coupling_formulas](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/all-coupling-formulas/) | L184-L187 | data/computed value | data/computed value | — |
| `theorem` | [temporal_complement](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/temporal-complement/) | L197-L200 | proof obligation | formal proof obligation checked | `IV.T01` |
| `theorem` | [temporal_complement_denom](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/temporal-complement-denom/) | L203-L205 | proof obligation | formal proof obligation checked | — |
| `theorem` | [temporal_multiplicative](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/temporal-multiplicative/) | L216-L220 | proof obligation | formal proof obligation checked | `IV.T02` |
| `theorem` | [em_is_weak_squared](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/em-is-weak-squared/) | L228-L231 | proof obligation | formal proof obligation checked | — |
| `theorem` | [weak_strong_is_multiplicative](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/weak-strong-is-multiplicative/) | L235-L239 | proof obligation | formal proof obligation checked | — |
| `theorem` | [all_formulas_positive](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/all-formulas-positive/) | L248-L257 | proof obligation | formal proof obligation checked | `IV.P01` |
| `theorem` | [coupling_ledger_count](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/coupling-ledger-count/) | L260-L261 | proof obligation | formal proof obligation checked | — |
| `def` | [coupling_formula](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/coupling-formula-l269/) | L269-L287 | definition | definition | — |
| `theorem` | [self_coupling_order](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/self-coupling-order/) | L295-L301 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L308](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l308/) | L308-L308 | computed check | computed check | — |
| `eval` | [#eval L309](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l309/) | L309-L309 | computed check | computed check | — |
| `eval` | [#eval L310](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l310/) | L310-L310 | computed check | computed check | — |
| `eval` | [#eval L311](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l311/) | L311-L311 | computed check | computed check | — |
| `eval` | [#eval L314](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l314/) | L314-L314 | computed check | computed check | — |
| `eval` | [#eval L315](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l315/) | L315-L315 | computed check | computed check | — |
| `eval` | [#eval L316](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l316/) | L316-L316 | computed check | computed check | — |
| `eval` | [#eval L317](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l317/) | L317-L317 | computed check | computed check | — |
| `eval` | [#eval L318](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l318/) | L318-L318 | computed check | computed check | — |
| `eval` | [#eval L319](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l319/) | L319-L319 | computed check | computed check | — |
| `eval` | [#eval L322](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l322/) | L322-L322 | computed check | computed check | — |
| `eval` | [#eval L323](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l323/) | L323-L323 | computed check | computed check | — |
| `eval` | [#eval L326](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/eval-l326/) | L326-L328 | computed check | computed check | — |
