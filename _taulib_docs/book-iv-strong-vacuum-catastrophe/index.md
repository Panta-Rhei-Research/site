---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Strong.VacuumCatastrophe",
  "permalink": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Strong.VacuumCatastrophe`.",
  "module_name": "TauLib.BookIV.Strong.VacuumCatastrophe",
  "module_slug": "book-iv-strong-vacuum-catastrophe",
  "book": "BookIV",
  "family": "Strong",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Strong/VacuumCatastrophe.lean",
  "sha256": "7b41c9d40c2e20f27ac291968db92e927d3486fece4f82de58b2743fc9f1e99e",
  "imports": [
    "TauLib.BookIV.Strong.QuarksGluons"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.ManyBody.DefectFunctionalExt",
    "TauLib.BookIV.Particles.SectorAtlas"
  ],
  "registry_ids": [
    "IV.D192",
    "IV.D193",
    "IV.P119",
    "IV.P120",
    "IV.T78",
    "IV.T79"
  ],
  "declaration_counts": {
    "structure": 7,
    "def": 9,
    "theorem": 14,
    "inductive": 1,
    "eval": 11
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "BoundaryFirstNorm",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/boundary-first-norm/",
      "source_line_start": 54,
      "source_line_end": 63,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D192"
      ]
    },
    {
      "kind": "def",
      "name": "boundary_first_norm",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/boundary-first-norm-l65/",
      "source_line_start": 65,
      "source_line_end": 65,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NoUncountable",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/no-uncountable/",
      "source_line_start": 80,
      "source_line_end": 89,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P119"
      ]
    },
    {
      "kind": "def",
      "name": "no_uncountable",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/no-uncountable-l91/",
      "source_line_start": 91,
      "source_line_end": 91,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CanonicalVacuumUniqueness",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/canonical-vacuum-uniqueness/",
      "source_line_start": 105,
      "source_line_end": 112,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P120"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_vacuum_uniqueness",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/canonical-vacuum-uniqueness-l114/",
      "source_line_start": 114,
      "source_line_end": 114,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "four_sector_vacua",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/four-sector-vacua/",
      "source_line_start": 117,
      "source_line_end": 118,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "ModeCountType",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/mode-count-type/",
      "source_line_start": 133,
      "source_line_end": 138,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D193"
      ]
    },
    {
      "kind": "structure",
      "name": "EarnedModeCount",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/earned-mode-count/",
      "source_line_start": 141,
      "source_line_end": 148,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "tau_mode_count",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/tau-mode-count/",
      "source_line_start": 151,
      "source_line_end": 154,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "orthodox_mode_count",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/orthodox-mode-count/",
      "source_line_start": 157,
      "source_line_end": 160,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_is_earned",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/tau-is-earned/",
      "source_line_start": 162,
      "source_line_end": 162,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "orthodox_is_unearned",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/orthodox-is-unearned/",
      "source_line_start": 163,
      "source_line_end": 163,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "earned_does_not_diverge",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/earned-does-not-diverge/",
      "source_line_start": 165,
      "source_line_end": 165,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "unearned_diverges",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/unearned-diverges/",
      "source_line_start": 166,
      "source_line_end": 166,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NoVacuumCatastrophe",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/no-vacuum-catastrophe/",
      "source_line_start": 182,
      "source_line_end": 195,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T78"
      ]
    },
    {
      "kind": "def",
      "name": "no_vacuum_catastrophe",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/no-vacuum-catastrophe-l197/",
      "source_line_start": 197,
      "source_line_end": 197,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "vacuum_is_finite",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/vacuum-is-finite/",
      "source_line_start": 199,
      "source_line_end": 200,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "vacuum_parameter_free",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/vacuum-parameter-free/",
      "source_line_start": 202,
      "source_line_end": 203,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "vacuum_scale_independent",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/vacuum-scale-independent/",
      "source_line_start": 205,
      "source_line_end": 206,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "four_sectors_summed",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/four-sectors-summed/",
      "source_line_start": 208,
      "source_line_end": 209,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TailStabilization",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/tail-stabilization/",
      "source_line_start": 224,
      "source_line_end": 235,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T79"
      ]
    },
    {
      "kind": "def",
      "name": "tail_stabilization",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/tail-stabilization-l237/",
      "source_line_start": 237,
      "source_line_end": 237,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "stabilization_exists",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/stabilization-exists/",
      "source_line_start": 239,
      "source_line_end": 240,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "VacuumEnergyComparison",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/vacuum-energy-comparison/",
      "source_line_start": 247,
      "source_line_end": 258,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "tau_vacuum_energy",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/tau-vacuum-energy/",
      "source_line_start": 260,
      "source_line_end": 265,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "orthodox_vacuum_energy",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/orthodox-vacuum-energy/",
      "source_line_start": 267,
      "source_line_end": 272,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_no_cc_problem",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/tau-no-cc-problem/",
      "source_line_start": 274,
      "source_line_end": 274,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "orthodox_has_cc_problem",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/orthodox-has-cc-problem/",
      "source_line_start": 275,
      "source_line_end": 275,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_no_divergence",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/tau-no-divergence/",
      "source_line_start": 277,
      "source_line_end": 277,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "orthodox_diverges",
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/orthodox-diverges/",
      "source_line_start": 278,
      "source_line_end": 278,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l284/",
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
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l285/",
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
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l286/",
      "source_line_start": 286,
      "source_line_end": 286,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l287/",
      "source_line_start": 287,
      "source_line_end": 287,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l288/",
      "source_line_start": 288,
      "source_line_end": 288,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l289/",
      "source_line_start": 289,
      "source_line_end": 289,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l290/",
      "source_line_start": 290,
      "source_line_end": 290,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l291/",
      "source_line_start": 291,
      "source_line_end": 291,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l292/",
      "source_line_start": 292,
      "source_line_end": 292,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l293/",
      "source_line_start": 293,
      "source_line_end": 293,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l294/",
      "source_line_start": 294,
      "source_line_end": 296,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean",
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
- Source path: [`TauLib/BookIV/Strong/VacuumCatastrophe.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Strong/VacuumCatastrophe.lean`
- SHA-256: `7b41c9d40c2e20f27ac291968db92e927d3486fece4f82de58b2743fc9f1e99e`

## Registry Links

- `IV.D192` — Boundary-first normalization
- `IV.D193` — Earned vs.\ unearned mode count
- `IV.P119` — No uncountable factorization
- `IV.P120` — Canonical vacuum uniqueness
- `IV.T78` — No vacuum catastrophe in τ
- `IV.T79` — Tail stabilization of vacuum energy

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Strong.QuarksGluons`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.ManyBody.DefectFunctionalExt`
- `TauLib.BookIV.Particles.SectorAtlas`

## Declaration Counts

- `def`: 9
- `eval`: 11
- `inductive`: 1
- `structure`: 7
- `theorem`: 14

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [BoundaryFirstNorm](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/boundary-first-norm/) | L54-L63 | type/data schema | type/data schema | `IV.D192` |
| `def` | [boundary_first_norm](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/boundary-first-norm-l65/) | L65-L65 | definition | definition | — |
| `structure` | [NoUncountable](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/no-uncountable/) | L80-L89 | type/data schema | type/data schema | `IV.P119` |
| `def` | [no_uncountable](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/no-uncountable-l91/) | L91-L91 | definition | definition | — |
| `structure` | [CanonicalVacuumUniqueness](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/canonical-vacuum-uniqueness/) | L105-L112 | type/data schema | type/data schema | `IV.P120` |
| `def` | [canonical_vacuum_uniqueness](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/canonical-vacuum-uniqueness-l114/) | L114-L114 | definition | definition | — |
| `theorem` | [four_sector_vacua](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/four-sector-vacua/) | L117-L118 | proof obligation | formal proof obligation checked | — |
| `inductive` | [ModeCountType](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/mode-count-type/) | L133-L138 | type/data schema | type/data schema | `IV.D193` |
| `structure` | [EarnedModeCount](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/earned-mode-count/) | L141-L148 | type/data schema | type/data schema | — |
| `def` | [tau_mode_count](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/tau-mode-count/) | L151-L154 | definition | definition | — |
| `def` | [orthodox_mode_count](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/orthodox-mode-count/) | L157-L160 | definition | definition | — |
| `theorem` | [tau_is_earned](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/tau-is-earned/) | L162-L162 | proof obligation | formal proof obligation checked | — |
| `theorem` | [orthodox_is_unearned](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/orthodox-is-unearned/) | L163-L163 | proof obligation | formal proof obligation checked | — |
| `theorem` | [earned_does_not_diverge](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/earned-does-not-diverge/) | L165-L165 | proof obligation | formal proof obligation checked | — |
| `theorem` | [unearned_diverges](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/unearned-diverges/) | L166-L166 | proof obligation | formal proof obligation checked | — |
| `structure` | [NoVacuumCatastrophe](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/no-vacuum-catastrophe/) | L182-L195 | type/data schema | type/data schema | `IV.T78` |
| `def` | [no_vacuum_catastrophe](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/no-vacuum-catastrophe-l197/) | L197-L197 | definition | definition | — |
| `theorem` | [vacuum_is_finite](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/vacuum-is-finite/) | L199-L200 | proof obligation | formal proof obligation checked | — |
| `theorem` | [vacuum_parameter_free](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/vacuum-parameter-free/) | L202-L203 | proof obligation | formal proof obligation checked | — |
| `theorem` | [vacuum_scale_independent](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/vacuum-scale-independent/) | L205-L206 | proof obligation | formal proof obligation checked | — |
| `theorem` | [four_sectors_summed](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/four-sectors-summed/) | L208-L209 | proof obligation | formal proof obligation checked | — |
| `structure` | [TailStabilization](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/tail-stabilization/) | L224-L235 | type/data schema | type/data schema | `IV.T79` |
| `def` | [tail_stabilization](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/tail-stabilization-l237/) | L237-L237 | definition | definition | — |
| `theorem` | [stabilization_exists](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/stabilization-exists/) | L239-L240 | proof obligation | formal proof obligation checked | — |
| `structure` | [VacuumEnergyComparison](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/vacuum-energy-comparison/) | L247-L258 | type/data schema | type/data schema | — |
| `def` | [tau_vacuum_energy](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/tau-vacuum-energy/) | L260-L265 | definition | definition | — |
| `def` | [orthodox_vacuum_energy](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/orthodox-vacuum-energy/) | L267-L272 | definition | definition | — |
| `theorem` | [tau_no_cc_problem](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/tau-no-cc-problem/) | L274-L274 | proof obligation | formal proof obligation checked | — |
| `theorem` | [orthodox_has_cc_problem](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/orthodox-has-cc-problem/) | L275-L275 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_no_divergence](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/tau-no-divergence/) | L277-L277 | proof obligation | formal proof obligation checked | — |
| `theorem` | [orthodox_diverges](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/orthodox-diverges/) | L278-L278 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L284](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l284/) | L284-L284 | computed check | computed check | — |
| `eval` | [#eval L285](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l285/) | L285-L285 | computed check | computed check | — |
| `eval` | [#eval L286](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l286/) | L286-L286 | computed check | computed check | — |
| `eval` | [#eval L287](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l287/) | L287-L287 | computed check | computed check | — |
| `eval` | [#eval L288](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l288/) | L288-L288 | computed check | computed check | — |
| `eval` | [#eval L289](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l289/) | L289-L289 | computed check | computed check | — |
| `eval` | [#eval L290](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l290/) | L290-L290 | computed check | computed check | — |
| `eval` | [#eval L291](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l291/) | L291-L291 | computed check | computed check | — |
| `eval` | [#eval L292](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l292/) | L292-L292 | computed check | computed check | — |
| `eval` | [#eval L293](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l293/) | L293-L293 | computed check | computed check | — |
| `eval` | [#eval L294](/corpus/taulib/docs/book-iv-strong-vacuum-catastrophe/eval-l294/) | L294-L296 | computed check | computed check | — |
