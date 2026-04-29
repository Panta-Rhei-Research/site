---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookII.Enrichment.EnrichmentLadder",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookII.Enrichment.EnrichmentLadder`.",
  "module_name": "TauLib.BookII.Enrichment.EnrichmentLadder",
  "module_slug": "book-ii-enrichment-enrichment-ladder",
  "book": "BookII",
  "family": "Enrichment",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookII/Enrichment/EnrichmentLadder.lean",
  "sha256": "5f3662ad75dc44cb294aedc7b7d152878ba5b34db7cc21bec45c910a9d56b5e8",
  "imports": [
    "TauLib.BookII.Enrichment.SelfDescribing"
  ],
  "imported_by": [
    "TauLib.BookII",
    "TauLib.BookII.CentralTheorem.BoundaryCharacters",
    "TauLib.BookII.Closure.DiffGeoAgenda",
    "TauLib.BookII.Mirror.SignClassification"
  ],
  "registry_ids": [
    "II.D58"
  ],
  "declaration_counts": {
    "inductive": 1,
    "def": 9,
    "theorem": 12,
    "eval": 12
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "EnrichmentLevel",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/enrichment-level/",
      "source_line_start": 54,
      "source_line_end": 57,
      "formal_status": "defined",
      "registry_ids": [
        "II.D58"
      ]
    },
    {
      "kind": "def",
      "name": "e0_check_id_compat",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e0-check-id-compat/",
      "source_line_start": 68,
      "source_line_end": 77,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "e0_check_zero_compat",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e0-check-zero-compat/",
      "source_line_start": 82,
      "source_line_end": 83,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "e0_external_hom_check",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e0-external-hom-check/",
      "source_line_start": 96,
      "source_line_end": 107,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "count_rc_endomorphisms_k1",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/count-rc-endomorphisms-k1/",
      "source_line_start": 115,
      "source_line_end": 115,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "verify_k1_count",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/verify-k1-count/",
      "source_line_start": 119,
      "source_line_end": 137,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "e1_internal_hom_check",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e1-internal-hom-check/",
      "source_line_start": 155,
      "source_line_end": 180,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "e0_e1_transition_check",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e0-e1-transition-check/",
      "source_line_start": 194,
      "source_line_end": 198,
      "formal_status": "defined",
      "registry_ids": [
        "II.D58"
      ]
    },
    {
      "kind": "def",
      "name": "enrichment_gap_check",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/enrichment-gap-check/",
      "source_line_start": 215,
      "source_line_end": 220,
      "formal_status": "defined",
      "registry_ids": [
        "II.D58"
      ]
    },
    {
      "kind": "def",
      "name": "full_enrichment_ladder_check",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/full-enrichment-ladder-check/",
      "source_line_start": 232,
      "source_line_end": 235,
      "formal_status": "defined",
      "registry_ids": [
        "II.D58"
      ]
    },
    {
      "kind": "theorem",
      "name": "id_restriction",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/id-restriction/",
      "source_line_start": 244,
      "source_line_end": 247,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "zero_restriction",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/zero-restriction/",
      "source_line_start": 251,
      "source_line_end": 253,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "e0_recoverable_from_e1",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e0-recoverable-from-e1/",
      "source_line_start": 258,
      "source_line_end": 260,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tower_coherence_transitive",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/tower-coherence-transitive/",
      "source_line_start": 266,
      "source_line_end": 268,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "e0_ne_e1",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e0-ne-e1/",
      "source_line_start": 271,
      "source_line_end": 273,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l280/",
      "source_line_start": 280,
      "source_line_end": 280,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l283/",
      "source_line_start": 283,
      "source_line_end": 283,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l286/",
      "source_line_start": 286,
      "source_line_end": 286,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l287/",
      "source_line_start": 287,
      "source_line_end": 287,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l290/",
      "source_line_start": 290,
      "source_line_end": 290,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l293/",
      "source_line_start": 293,
      "source_line_end": 293,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l296/",
      "source_line_start": 296,
      "source_line_end": 296,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l299/",
      "source_line_start": 299,
      "source_line_end": 299,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l300/",
      "source_line_start": 300,
      "source_line_end": 300,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l303/",
      "source_line_start": 303,
      "source_line_end": 303,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l304/",
      "source_line_start": 304,
      "source_line_end": 304,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l305/",
      "source_line_start": 305,
      "source_line_end": 305,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "e0_hom_3",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e0-hom-3/",
      "source_line_start": 312,
      "source_line_end": 313,
      "formal_status": "formalized",
      "registry_ids": [
        "II.D58"
      ]
    },
    {
      "kind": "theorem",
      "name": "e1_hom_3",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e1-hom-3/",
      "source_line_start": 316,
      "source_line_end": 317,
      "formal_status": "formalized",
      "registry_ids": [
        "II.D58"
      ]
    },
    {
      "kind": "theorem",
      "name": "k1_count_4",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/k1-count-4/",
      "source_line_start": 320,
      "source_line_end": 321,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "k1_verify",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/k1-verify/",
      "source_line_start": 323,
      "source_line_end": 324,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "transition_3",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/transition-3/",
      "source_line_start": 327,
      "source_line_end": 328,
      "formal_status": "formalized",
      "registry_ids": [
        "II.D58"
      ]
    },
    {
      "kind": "theorem",
      "name": "gap_10_3_3",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/gap-10-3-3/",
      "source_line_start": 331,
      "source_line_end": 332,
      "formal_status": "formalized",
      "registry_ids": [
        "II.D58"
      ]
    },
    {
      "kind": "theorem",
      "name": "full_ladder_10_3_3",
      "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/full-ladder-10-3-3/",
      "source_line_start": 335,
      "source_line_end": 338,
      "formal_status": "formalized",
      "registry_ids": [
        "II.D58"
      ]
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean",
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
- Source path: [`TauLib/BookII/Enrichment/EnrichmentLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookII/Enrichment/EnrichmentLadder.lean`
- SHA-256: `5f3662ad75dc44cb294aedc7b7d152878ba5b34db7cc21bec45c910a9d56b5e8`

## Registry Links

- `II.D58` — E0/E1 Transition

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookII.Enrichment.SelfDescribing`

## Imported By

- `TauLib.BookII`
- `TauLib.BookII.CentralTheorem.BoundaryCharacters`
- `TauLib.BookII.Closure.DiffGeoAgenda`
- `TauLib.BookII.Mirror.SignClassification`

## Declaration Counts

- `def`: 9
- `eval`: 12
- `inductive`: 1
- `theorem`: 12

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [EnrichmentLevel](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/enrichment-level/) | L54-L57 | defined | `II.D58` |
| `def` | [e0_check_id_compat](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e0-check-id-compat/) | L68-L77 | defined | — |
| `def` | [e0_check_zero_compat](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e0-check-zero-compat/) | L82-L83 | defined | — |
| `def` | [e0_external_hom_check](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e0-external-hom-check/) | L96-L107 | defined | — |
| `def` | [count_rc_endomorphisms_k1](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/count-rc-endomorphisms-k1/) | L115-L115 | defined | — |
| `def` | [verify_k1_count](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/verify-k1-count/) | L119-L137 | defined | — |
| `def` | [e1_internal_hom_check](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e1-internal-hom-check/) | L155-L180 | defined | — |
| `def` | [e0_e1_transition_check](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e0-e1-transition-check/) | L194-L198 | defined | `II.D58` |
| `def` | [enrichment_gap_check](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/enrichment-gap-check/) | L215-L220 | defined | `II.D58` |
| `def` | [full_enrichment_ladder_check](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/full-enrichment-ladder-check/) | L232-L235 | defined | `II.D58` |
| `theorem` | [id_restriction](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/id-restriction/) | L244-L247 | formalized | — |
| `theorem` | [zero_restriction](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/zero-restriction/) | L251-L253 | formalized | — |
| `theorem` | [e0_recoverable_from_e1](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e0-recoverable-from-e1/) | L258-L260 | formalized | — |
| `theorem` | [tower_coherence_transitive](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/tower-coherence-transitive/) | L266-L268 | formalized | — |
| `theorem` | [e0_ne_e1](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e0-ne-e1/) | L271-L273 | formalized | — |
| `eval` | [#eval L280](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l280/) | L280-L280 | computed | — |
| `eval` | [#eval L283](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l283/) | L283-L283 | computed | — |
| `eval` | [#eval L286](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l286/) | L286-L286 | computed | — |
| `eval` | [#eval L287](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l287/) | L287-L287 | computed | — |
| `eval` | [#eval L290](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l290/) | L290-L290 | computed | — |
| `eval` | [#eval L293](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l293/) | L293-L293 | computed | — |
| `eval` | [#eval L296](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l296/) | L296-L296 | computed | — |
| `eval` | [#eval L299](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l299/) | L299-L299 | computed | — |
| `eval` | [#eval L300](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l300/) | L300-L300 | computed | — |
| `eval` | [#eval L303](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l303/) | L303-L303 | computed | — |
| `eval` | [#eval L304](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l304/) | L304-L304 | computed | — |
| `eval` | [#eval L305](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/eval-l305/) | L305-L305 | computed | — |
| `theorem` | [e0_hom_3](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e0-hom-3/) | L312-L313 | formalized | `II.D58` |
| `theorem` | [e1_hom_3](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e1-hom-3/) | L316-L317 | formalized | `II.D58` |
| `theorem` | [k1_count_4](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/k1-count-4/) | L320-L321 | formalized | — |
| `theorem` | [k1_verify](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/k1-verify/) | L323-L324 | formalized | — |
| `theorem` | [transition_3](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/transition-3/) | L327-L328 | formalized | `II.D58` |
| `theorem` | [gap_10_3_3](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/gap-10-3-3/) | L331-L332 | formalized | `II.D58` |
| `theorem` | [full_ladder_10_3_3](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/full-ladder-10-3-3/) | L335-L338 | formalized | `II.D58` |
