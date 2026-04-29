---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookVI.Source.Epigenetics",
  "permalink": "/verify/taulib/docs/book-vi-source-epigenetics/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookVI.Source.Epigenetics`.",
  "module_name": "TauLib.BookVI.Source.Epigenetics",
  "module_slug": "book-vi-source-epigenetics",
  "book": "BookVI",
  "family": "Source",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookVI/Source/Epigenetics.lean",
  "sha256": "ab267c9b55463532e78b52e40058644d775bfd553e0b105dcf4d43ae59389cb7",
  "imports": [
    "TauLib.BookVI.Source.GeneticCode"
  ],
  "imported_by": [
    "TauLib.BookVI"
  ],
  "registry_ids": [
    "VI.D78",
    "VI.D79",
    "VI.D80",
    "VI.D81",
    "VI.D82",
    "VI.D83",
    "VI.D84",
    "VI.D85",
    "VI.P22",
    "VI.T47",
    "VI.T48",
    "VI.T49"
  ],
  "declaration_counts": {
    "structure": 12,
    "def": 12,
    "theorem": 12
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "ChromatinPartition",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/chromatin-partition/",
      "source_line_start": 52,
      "source_line_end": 61,
      "formal_status": "defined",
      "registry_ids": [
        "VI.D78"
      ]
    },
    {
      "kind": "def",
      "name": "chromatin_partition",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/chromatin-partition-l63/",
      "source_line_start": 63,
      "source_line_end": 63,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chromatin_partition_clopen",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/chromatin-partition-clopen/",
      "source_line_start": 65,
      "source_line_end": 67,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EpigeneticState",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/epigenetic-state/",
      "source_line_start": 79,
      "source_line_end": 88,
      "formal_status": "defined",
      "registry_ids": [
        "VI.D79"
      ]
    },
    {
      "kind": "def",
      "name": "totipotent_state",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/totipotent-state/",
      "source_line_start": 90,
      "source_line_end": 92,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "totipotent_is_level_zero",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/totipotent-is-level-zero/",
      "source_line_start": 94,
      "source_line_end": 96,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GeneExpressionProfile",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/gene-expression-profile/",
      "source_line_start": 107,
      "source_line_end": 116,
      "formal_status": "defined",
      "registry_ids": [
        "VI.D80"
      ]
    },
    {
      "kind": "def",
      "name": "typical_somatic_profile",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/typical-somatic-profile/",
      "source_line_start": 118,
      "source_line_end": 121,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "expression_is_restricted",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/expression-is-restricted/",
      "source_line_start": 123,
      "source_line_end": 125,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "PotencyRestriction",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/potency-restriction/",
      "source_line_start": 137,
      "source_line_end": 146,
      "formal_status": "defined",
      "registry_ids": [
        "VI.D81"
      ]
    },
    {
      "kind": "def",
      "name": "potency_hierarchy",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/potency-hierarchy/",
      "source_line_start": 148,
      "source_line_end": 150,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "potency_has_five_levels",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/potency-has-five-levels/",
      "source_line_start": 152,
      "source_line_end": 154,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "IntergenerationalTransfer",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/intergenerational-transfer/",
      "source_line_start": 166,
      "source_line_end": 175,
      "formal_status": "defined",
      "registry_ids": [
        "VI.D82"
      ]
    },
    {
      "kind": "def",
      "name": "epigenetic_transfer",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/epigenetic-transfer/",
      "source_line_start": 177,
      "source_line_end": 177,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "transfer_is_lossy",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/transfer-is-lossy/",
      "source_line_start": 179,
      "source_line_end": 181,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "WaddingtonLandscape",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/waddington-landscape/",
      "source_line_start": 193,
      "source_line_end": 202,
      "formal_status": "defined",
      "registry_ids": [
        "VI.D83"
      ]
    },
    {
      "kind": "def",
      "name": "waddington",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/waddington/",
      "source_line_start": 204,
      "source_line_end": 204,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "waddington_descends",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/waddington-descends/",
      "source_line_start": 206,
      "source_line_end": 208,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CellFate",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/cell-fate/",
      "source_line_start": 220,
      "source_line_end": 229,
      "formal_status": "defined",
      "registry_ids": [
        "VI.D84"
      ]
    },
    {
      "kind": "def",
      "name": "terminal_fate",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/terminal-fate/",
      "source_line_start": 231,
      "source_line_end": 231,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "terminal_is_fixed",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/terminal-is-fixed/",
      "source_line_start": 233,
      "source_line_end": 235,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DifferentiationIrreversible",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/differentiation-irreversible/",
      "source_line_start": 247,
      "source_line_end": 256,
      "formal_status": "defined",
      "registry_ids": [
        "VI.T47"
      ]
    },
    {
      "kind": "def",
      "name": "diff_irrev",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/diff-irrev/",
      "source_line_start": 258,
      "source_line_end": 258,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "differentiation_irreversible",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/differentiation-irreversible-l260/",
      "source_line_start": 260,
      "source_line_end": 264,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ReprogrammingReversal",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/reprogramming-reversal/",
      "source_line_start": 276,
      "source_line_end": 285,
      "formal_status": "defined",
      "registry_ids": [
        "VI.T48"
      ]
    },
    {
      "kind": "def",
      "name": "reprog",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/reprog/",
      "source_line_start": 287,
      "source_line_end": 287,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "reprogramming_refinement_reversal",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/reprogramming-refinement-reversal/",
      "source_line_start": 289,
      "source_line_end": 293,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CellFateFixedPoint",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/cell-fate-fixed-point/",
      "source_line_start": 305,
      "source_line_end": 314,
      "formal_status": "defined",
      "registry_ids": [
        "VI.P22"
      ]
    },
    {
      "kind": "def",
      "name": "fate_fp",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/fate-fp/",
      "source_line_start": 316,
      "source_line_end": 316,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cell_fate_fixed_point",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/cell-fate-fixed-point-l318/",
      "source_line_start": 318,
      "source_line_end": 322,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EpigeneticDrift",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/epigenetic-drift/",
      "source_line_start": 334,
      "source_line_end": 343,
      "formal_status": "defined",
      "registry_ids": [
        "VI.D85"
      ]
    },
    {
      "kind": "def",
      "name": "epi_drift",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/epi-drift/",
      "source_line_start": 345,
      "source_line_end": 345,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "drift_is_aging_instance",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/drift-is-aging-instance/",
      "source_line_start": 347,
      "source_line_end": 349,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DriftBoundedByRepair",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/drift-bounded-by-repair/",
      "source_line_start": 361,
      "source_line_end": 370,
      "formal_status": "defined",
      "registry_ids": [
        "VI.T49"
      ]
    },
    {
      "kind": "def",
      "name": "drift_repair",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/drift-repair/",
      "source_line_start": 372,
      "source_line_end": 372,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "drift_bounded_by_repair",
      "url": "/verify/taulib/docs/book-vi-source-epigenetics/drift-bounded-by-repair-l374/",
      "source_line_start": 374,
      "source_line_end": 380,
      "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean",
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
- Source path: [`TauLib/BookVI/Source/Epigenetics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookVI/Source/Epigenetics.lean`
- SHA-256: `ab267c9b55463532e78b52e40058644d775bfd553e0b105dcf4d43ae59389cb7`

## Registry Links

- `VI.D78` — Chromatin Partition
- `VI.D79` — Epigenetic State
- `VI.D80` — Gene Expression Profile
- `VI.D81` — Potency Restriction
- `VI.D82` — Intergenerational Transfer
- `VI.D83` — Waddington Landscape
- `VI.D84` — Cell Fate
- `VI.D85` — Epigenetic Drift
- `VI.P22` — Cell Fate as Fixed Point
- `VI.T47` — Differentiation Is Irreversible
- `VI.T48` — Reprogramming as Refinement Reversal
- `VI.T49` — Drift Bounded by Repair

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookVI.Source.GeneticCode`

## Imported By

- `TauLib.BookVI`

## Declaration Counts

- `def`: 12
- `structure`: 12
- `theorem`: 12

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [ChromatinPartition](/verify/taulib/docs/book-vi-source-epigenetics/chromatin-partition/) | L52-L61 | defined | `VI.D78` |
| `def` | [chromatin_partition](/verify/taulib/docs/book-vi-source-epigenetics/chromatin-partition-l63/) | L63-L63 | defined | — |
| `theorem` | [chromatin_partition_clopen](/verify/taulib/docs/book-vi-source-epigenetics/chromatin-partition-clopen/) | L65-L67 | formalized | — |
| `structure` | [EpigeneticState](/verify/taulib/docs/book-vi-source-epigenetics/epigenetic-state/) | L79-L88 | defined | `VI.D79` |
| `def` | [totipotent_state](/verify/taulib/docs/book-vi-source-epigenetics/totipotent-state/) | L90-L92 | defined | — |
| `theorem` | [totipotent_is_level_zero](/verify/taulib/docs/book-vi-source-epigenetics/totipotent-is-level-zero/) | L94-L96 | formalized | — |
| `structure` | [GeneExpressionProfile](/verify/taulib/docs/book-vi-source-epigenetics/gene-expression-profile/) | L107-L116 | defined | `VI.D80` |
| `def` | [typical_somatic_profile](/verify/taulib/docs/book-vi-source-epigenetics/typical-somatic-profile/) | L118-L121 | defined | — |
| `theorem` | [expression_is_restricted](/verify/taulib/docs/book-vi-source-epigenetics/expression-is-restricted/) | L123-L125 | formalized | — |
| `structure` | [PotencyRestriction](/verify/taulib/docs/book-vi-source-epigenetics/potency-restriction/) | L137-L146 | defined | `VI.D81` |
| `def` | [potency_hierarchy](/verify/taulib/docs/book-vi-source-epigenetics/potency-hierarchy/) | L148-L150 | defined | — |
| `theorem` | [potency_has_five_levels](/verify/taulib/docs/book-vi-source-epigenetics/potency-has-five-levels/) | L152-L154 | formalized | — |
| `structure` | [IntergenerationalTransfer](/verify/taulib/docs/book-vi-source-epigenetics/intergenerational-transfer/) | L166-L175 | defined | `VI.D82` |
| `def` | [epigenetic_transfer](/verify/taulib/docs/book-vi-source-epigenetics/epigenetic-transfer/) | L177-L177 | defined | — |
| `theorem` | [transfer_is_lossy](/verify/taulib/docs/book-vi-source-epigenetics/transfer-is-lossy/) | L179-L181 | formalized | — |
| `structure` | [WaddingtonLandscape](/verify/taulib/docs/book-vi-source-epigenetics/waddington-landscape/) | L193-L202 | defined | `VI.D83` |
| `def` | [waddington](/verify/taulib/docs/book-vi-source-epigenetics/waddington/) | L204-L204 | defined | — |
| `theorem` | [waddington_descends](/verify/taulib/docs/book-vi-source-epigenetics/waddington-descends/) | L206-L208 | formalized | — |
| `structure` | [CellFate](/verify/taulib/docs/book-vi-source-epigenetics/cell-fate/) | L220-L229 | defined | `VI.D84` |
| `def` | [terminal_fate](/verify/taulib/docs/book-vi-source-epigenetics/terminal-fate/) | L231-L231 | defined | — |
| `theorem` | [terminal_is_fixed](/verify/taulib/docs/book-vi-source-epigenetics/terminal-is-fixed/) | L233-L235 | formalized | — |
| `structure` | [DifferentiationIrreversible](/verify/taulib/docs/book-vi-source-epigenetics/differentiation-irreversible/) | L247-L256 | defined | `VI.T47` |
| `def` | [diff_irrev](/verify/taulib/docs/book-vi-source-epigenetics/diff-irrev/) | L258-L258 | defined | — |
| `theorem` | [differentiation_irreversible](/verify/taulib/docs/book-vi-source-epigenetics/differentiation-irreversible-l260/) | L260-L264 | formalized | — |
| `structure` | [ReprogrammingReversal](/verify/taulib/docs/book-vi-source-epigenetics/reprogramming-reversal/) | L276-L285 | defined | `VI.T48` |
| `def` | [reprog](/verify/taulib/docs/book-vi-source-epigenetics/reprog/) | L287-L287 | defined | — |
| `theorem` | [reprogramming_refinement_reversal](/verify/taulib/docs/book-vi-source-epigenetics/reprogramming-refinement-reversal/) | L289-L293 | formalized | — |
| `structure` | [CellFateFixedPoint](/verify/taulib/docs/book-vi-source-epigenetics/cell-fate-fixed-point/) | L305-L314 | defined | `VI.P22` |
| `def` | [fate_fp](/verify/taulib/docs/book-vi-source-epigenetics/fate-fp/) | L316-L316 | defined | — |
| `theorem` | [cell_fate_fixed_point](/verify/taulib/docs/book-vi-source-epigenetics/cell-fate-fixed-point-l318/) | L318-L322 | formalized | — |
| `structure` | [EpigeneticDrift](/verify/taulib/docs/book-vi-source-epigenetics/epigenetic-drift/) | L334-L343 | defined | `VI.D85` |
| `def` | [epi_drift](/verify/taulib/docs/book-vi-source-epigenetics/epi-drift/) | L345-L345 | defined | — |
| `theorem` | [drift_is_aging_instance](/verify/taulib/docs/book-vi-source-epigenetics/drift-is-aging-instance/) | L347-L349 | formalized | — |
| `structure` | [DriftBoundedByRepair](/verify/taulib/docs/book-vi-source-epigenetics/drift-bounded-by-repair/) | L361-L370 | defined | `VI.T49` |
| `def` | [drift_repair](/verify/taulib/docs/book-vi-source-epigenetics/drift-repair/) | L372-L372 | defined | — |
| `theorem` | [drift_bounded_by_repair](/verify/taulib/docs/book-vi-source-epigenetics/drift-bounded-by-repair-l374/) | L374-L380 | formalized | — |
