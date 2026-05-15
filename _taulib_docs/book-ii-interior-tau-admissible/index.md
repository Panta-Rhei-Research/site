---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookII.Interior.TauAdmissible",
  "permalink": "/corpus/taulib/docs/book-ii-interior-tau-admissible/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookII.Interior.TauAdmissible`.",
  "module_name": "TauLib.BookII.Interior.TauAdmissible",
  "module_slug": "book-ii-interior-tau-admissible",
  "book": "BookII",
  "family": "Interior",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookII/Interior/TauAdmissible.lean",
  "sha256": "06c3c8cd817e54396051cb08fc2f897ea94c0803109ee9d869d60dcc992d9e68",
  "imports": [
    "TauLib.BookI.Coordinates.ABCD",
    "TauLib.BookI.Coordinates.Primes"
  ],
  "imported_by": [
    "TauLib.BookII",
    "TauLib.BookII.Interior.OmegaReadout",
    "TauLib.BookII.Interior.Tau3Fibration",
    "TauLib.BookII.Topology.DimensionFour"
  ],
  "registry_ids": [
    "II.D02",
    "II.D03",
    "II.T01"
  ],
  "declaration_counts": {
    "def": 17,
    "structure": 1,
    "eval": 25,
    "theorem": 1
  },
  "declarations": [
    {
      "kind": "def",
      "name": "constraint_C1",
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/constraint-c1/",
      "source_line_start": 39,
      "source_line_end": 40,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "largest_prime_factor_aux",
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/largest-prime-factor-aux/",
      "source_line_start": 44,
      "source_line_end": 52,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "largest_prime_factor",
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/largest-prime-factor/",
      "source_line_start": 55,
      "source_line_end": 57,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "constraint_C3",
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/constraint-c3/",
      "source_line_start": 60,
      "source_line_end": 61,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "constraint_C4",
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/constraint-c4/",
      "source_line_start": 64,
      "source_line_end": 65,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "constraint_C5",
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/constraint-c5/",
      "source_line_start": 68,
      "source_line_end": 73,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "is_tau_admissible",
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/is-tau-admissible/",
      "source_line_start": 76,
      "source_line_end": 77,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.D03"
      ]
    },
    {
      "kind": "structure",
      "name": "TauAdmissiblePoint",
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/tau-admissible-point/",
      "source_line_start": 86,
      "source_line_end": 91,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "II.D02"
      ]
    },
    {
      "kind": "def",
      "name": "from_tau_idx",
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/from-tau-idx/",
      "source_line_start": 94,
      "source_line_end": 96,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "to_tau_idx",
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/to-tau-idx/",
      "source_line_start": 99,
      "source_line_end": 100,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauAdmissiblePoint.valid",
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/valid/",
      "source_line_start": 103,
      "source_line_end": 104,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "round_trip_check",
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/round-trip-check/",
      "source_line_start": 112,
      "source_line_end": 113,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "admissible_check",
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/admissible-check/",
      "source_line_start": 117,
      "source_line_end": 118,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "batch_verify",
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/batch-verify/",
      "source_line_start": 121,
      "source_line_end": 128,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "primorial_witness",
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/primorial-witness/",
      "source_line_start": 135,
      "source_line_end": 141,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "primorial_b_eq_one",
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/primorial-b-eq-one/",
      "source_line_start": 144,
      "source_line_end": 145,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "primorial_c_eq_one",
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/primorial-c-eq-one/",
      "source_line_start": 147,
      "source_line_end": 148,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "primorial_a_increasing",
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/primorial-a-increasing/",
      "source_line_start": 151,
      "source_line_end": 153,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l160/",
      "source_line_start": 160,
      "source_line_end": 160,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l161/",
      "source_line_start": 161,
      "source_line_end": 161,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l162/",
      "source_line_start": 162,
      "source_line_end": 162,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l164/",
      "source_line_start": 164,
      "source_line_end": 164,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l165/",
      "source_line_start": 165,
      "source_line_end": 165,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l166/",
      "source_line_start": 166,
      "source_line_end": 166,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l167/",
      "source_line_start": 167,
      "source_line_end": 167,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l169/",
      "source_line_start": 169,
      "source_line_end": 169,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l170/",
      "source_line_start": 170,
      "source_line_end": 170,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l171/",
      "source_line_start": 171,
      "source_line_end": 171,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l174/",
      "source_line_start": 174,
      "source_line_end": 174,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l175/",
      "source_line_start": 175,
      "source_line_end": 175,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l176/",
      "source_line_start": 176,
      "source_line_end": 176,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l178/",
      "source_line_start": 178,
      "source_line_end": 178,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l179/",
      "source_line_start": 179,
      "source_line_end": 179,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l180/",
      "source_line_start": 180,
      "source_line_end": 180,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l183/",
      "source_line_start": 183,
      "source_line_end": 183,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l184/",
      "source_line_start": 184,
      "source_line_end": 184,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l185/",
      "source_line_start": 185,
      "source_line_end": 185,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l186/",
      "source_line_start": 186,
      "source_line_end": 186,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l189/",
      "source_line_start": 189,
      "source_line_end": 189,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l192/",
      "source_line_start": 192,
      "source_line_end": 192,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l193/",
      "source_line_start": 193,
      "source_line_end": 193,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l194/",
      "source_line_start": 194,
      "source_line_end": 194,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l195/",
      "source_line_start": 195,
      "source_line_end": 195,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "admissible_2_to_20",
      "url": "/corpus/taulib/docs/book-ii-interior-tau-admissible/admissible-2-to-20/",
      "source_line_start": 198,
      "source_line_end": 200,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/TauAdmissible.lean",
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
- Source path: [`TauLib/BookII/Interior/TauAdmissible.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/TauAdmissible.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookII/Interior/TauAdmissible.lean`
- SHA-256: `06c3c8cd817e54396051cb08fc2f897ea94c0803109ee9d869d60dcc992d9e68`

## Registry Links

- `II.D02` — Tau-Admissible Point
- `II.D03` — Constraint Lattice
- `II.T01` — Point Set Well-Defined

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Coordinates.ABCD`
- `TauLib.BookI.Coordinates.Primes`

## Imported By

- `TauLib.BookII`
- `TauLib.BookII.Interior.OmegaReadout`
- `TauLib.BookII.Interior.Tau3Fibration`
- `TauLib.BookII.Topology.DimensionFour`

## Declaration Counts

- `def`: 17
- `eval`: 25
- `structure`: 1
- `theorem`: 1

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [constraint_C1](/corpus/taulib/docs/book-ii-interior-tau-admissible/constraint-c1/) | L39-L40 | data/computed value | data/computed value | — |
| `def` | [largest_prime_factor_aux](/corpus/taulib/docs/book-ii-interior-tau-admissible/largest-prime-factor-aux/) | L44-L52 | data/computed value | data/computed value | — |
| `def` | [largest_prime_factor](/corpus/taulib/docs/book-ii-interior-tau-admissible/largest-prime-factor/) | L55-L57 | definition | definition | — |
| `def` | [constraint_C3](/corpus/taulib/docs/book-ii-interior-tau-admissible/constraint-c3/) | L60-L61 | data/computed value | data/computed value | — |
| `def` | [constraint_C4](/corpus/taulib/docs/book-ii-interior-tau-admissible/constraint-c4/) | L64-L65 | data/computed value | data/computed value | — |
| `def` | [constraint_C5](/corpus/taulib/docs/book-ii-interior-tau-admissible/constraint-c5/) | L68-L73 | data/computed value | data/computed value | — |
| `def` | [is_tau_admissible](/corpus/taulib/docs/book-ii-interior-tau-admissible/is-tau-admissible/) | L76-L77 | data/computed value | data/computed value | `II.D03` |
| `structure` | [TauAdmissiblePoint](/corpus/taulib/docs/book-ii-interior-tau-admissible/tau-admissible-point/) | L86-L91 | type/data schema | type/data schema | `II.D02` |
| `def` | [from_tau_idx](/corpus/taulib/docs/book-ii-interior-tau-admissible/from-tau-idx/) | L94-L96 | definition | definition | — |
| `def` | [to_tau_idx](/corpus/taulib/docs/book-ii-interior-tau-admissible/to-tau-idx/) | L99-L100 | definition | definition | — |
| `def` | [TauAdmissiblePoint.valid](/corpus/taulib/docs/book-ii-interior-tau-admissible/valid/) | L103-L104 | data/computed value | data/computed value | — |
| `def` | [round_trip_check](/corpus/taulib/docs/book-ii-interior-tau-admissible/round-trip-check/) | L112-L113 | data/computed value | data/computed value | — |
| `def` | [admissible_check](/corpus/taulib/docs/book-ii-interior-tau-admissible/admissible-check/) | L117-L118 | data/computed value | data/computed value | — |
| `def` | [batch_verify](/corpus/taulib/docs/book-ii-interior-tau-admissible/batch-verify/) | L121-L128 | data/computed value | data/computed value | — |
| `def` | [primorial_witness](/corpus/taulib/docs/book-ii-interior-tau-admissible/primorial-witness/) | L135-L141 | data/computed value | data/computed value | — |
| `def` | [primorial_b_eq_one](/corpus/taulib/docs/book-ii-interior-tau-admissible/primorial-b-eq-one/) | L144-L145 | data/computed value | data/computed value | — |
| `def` | [primorial_c_eq_one](/corpus/taulib/docs/book-ii-interior-tau-admissible/primorial-c-eq-one/) | L147-L148 | data/computed value | data/computed value | — |
| `def` | [primorial_a_increasing](/corpus/taulib/docs/book-ii-interior-tau-admissible/primorial-a-increasing/) | L151-L153 | data/computed value | data/computed value | — |
| `eval` | [#eval L160](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l160/) | L160-L160 | computed check | computed check | — |
| `eval` | [#eval L161](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l161/) | L161-L161 | computed check | computed check | — |
| `eval` | [#eval L162](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l162/) | L162-L162 | computed check | computed check | — |
| `eval` | [#eval L164](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l164/) | L164-L164 | computed check | computed check | — |
| `eval` | [#eval L165](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l165/) | L165-L165 | computed check | computed check | — |
| `eval` | [#eval L166](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l166/) | L166-L166 | computed check | computed check | — |
| `eval` | [#eval L167](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l167/) | L167-L167 | computed check | computed check | — |
| `eval` | [#eval L169](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l169/) | L169-L169 | computed check | computed check | — |
| `eval` | [#eval L170](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l170/) | L170-L170 | computed check | computed check | — |
| `eval` | [#eval L171](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l171/) | L171-L171 | computed check | computed check | — |
| `eval` | [#eval L174](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l174/) | L174-L174 | computed check | computed check | — |
| `eval` | [#eval L175](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l175/) | L175-L175 | computed check | computed check | — |
| `eval` | [#eval L176](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l176/) | L176-L176 | computed check | computed check | — |
| `eval` | [#eval L178](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l178/) | L178-L178 | computed check | computed check | — |
| `eval` | [#eval L179](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l179/) | L179-L179 | computed check | computed check | — |
| `eval` | [#eval L180](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l180/) | L180-L180 | computed check | computed check | — |
| `eval` | [#eval L183](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l183/) | L183-L183 | computed check | computed check | — |
| `eval` | [#eval L184](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l184/) | L184-L184 | computed check | computed check | — |
| `eval` | [#eval L185](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l185/) | L185-L185 | computed check | computed check | — |
| `eval` | [#eval L186](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l186/) | L186-L186 | computed check | computed check | — |
| `eval` | [#eval L189](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l189/) | L189-L189 | computed check | computed check | — |
| `eval` | [#eval L192](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l192/) | L192-L192 | computed check | computed check | — |
| `eval` | [#eval L193](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l193/) | L193-L193 | computed check | computed check | — |
| `eval` | [#eval L194](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l194/) | L194-L194 | computed check | computed check | — |
| `eval` | [#eval L195](/corpus/taulib/docs/book-ii-interior-tau-admissible/eval-l195/) | L195-L195 | computed check | computed check | — |
| `theorem` | [admissible_2_to_20](/corpus/taulib/docs/book-ii-interior-tau-admissible/admissible-2-to-20/) | L198-L200 | proof obligation | formal proof obligation checked | — |
