---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.Cyclotomic",
  "permalink": "/verify/taulib/docs/book-i-boundary-cyclotomic/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.Cyclotomic`.",
  "module_name": "TauLib.BookI.Boundary.Cyclotomic",
  "module_slug": "book-i-boundary-cyclotomic",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/Cyclotomic.lean",
  "sha256": "263c1201c8412549ed0263bd8749c875c25ab2264de6dc66cd64a9d397dc91f6",
  "imports": [
    "TauLib.BookI.Boundary.NumberTower",
    "TauLib.BookI.Polarity.CRTBasis",
    "Mathlib.Tactic.Ring",
    "Mathlib.Tactic.NormNum"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Boundary.Galois"
  ],
  "registry_ids": [
    "I.D88",
    "I.R23",
    "I.T45"
  ],
  "declaration_counts": {
    "def": 4,
    "theorem": 12,
    "example": 8
  },
  "declarations": [
    {
      "kind": "def",
      "name": "IsRootOfUnity",
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/is-root-of-unity/",
      "source_line_start": 41,
      "source_line_end": 46,
      "formal_status": "defined",
      "registry_ids": [
        "I.D88"
      ]
    },
    {
      "kind": "def",
      "name": "IsPrimitiveRoot",
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/is-primitive-root/",
      "source_line_start": 50,
      "source_line_end": 51,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "root_of_unity_one",
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/root-of-unity-one/",
      "source_line_start": 58,
      "source_line_end": 59,
      "formal_status": "formalized",
      "registry_ids": [
        "I.T45"
      ]
    },
    {
      "kind": "theorem",
      "name": "root_of_unity_pow",
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/root-of-unity-pow/",
      "source_line_start": 62,
      "source_line_end": 68,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "CyclotomicRoot",
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/cyclotomic-root/",
      "source_line_start": 73,
      "source_line_end": 74,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "root_divides_power",
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/root-divides-power/",
      "source_line_start": 77,
      "source_line_end": 80,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "root_of_unity_factor_left",
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/root-of-unity-factor-left/",
      "source_line_start": 87,
      "source_line_end": 97,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "root_of_unity_factor_right",
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/root-of-unity-factor-right/",
      "source_line_start": 100,
      "source_line_end": 103,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "euler_totient",
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/euler-totient/",
      "source_line_start": 110,
      "source_line_end": 111,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "euler_totient_one",
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/euler-totient-one/",
      "source_line_start": 114,
      "source_line_end": 114,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "euler_totient_two",
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/euler-totient-two/",
      "source_line_start": 117,
      "source_line_end": 117,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "euler_totient_three",
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/euler-totient-three/",
      "source_line_start": 120,
      "source_line_end": 120,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "euler_totient_five",
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/euler-totient-five/",
      "source_line_start": 121,
      "source_line_end": 121,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "euler_totient_seven",
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/euler-totient-seven/",
      "source_line_start": 122,
      "source_line_end": 122,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "galois_action",
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/galois-action/",
      "source_line_start": 131,
      "source_line_end": 137,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "galois_action_comp",
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/galois-action-comp/",
      "source_line_start": 140,
      "source_line_end": 143,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/example-l153/",
      "source_line_start": 153,
      "source_line_end": 153,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/example-l156/",
      "source_line_start": 156,
      "source_line_end": 161,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/example-l164/",
      "source_line_start": 164,
      "source_line_end": 164,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/example-l167/",
      "source_line_start": 167,
      "source_line_end": 167,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/example-l168/",
      "source_line_start": 168,
      "source_line_end": 168,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/example-l169/",
      "source_line_start": 169,
      "source_line_end": 169,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/example-l172/",
      "source_line_start": 172,
      "source_line_end": 172,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/example-l173/",
      "source_line_start": 173,
      "source_line_end": 189,
      "formal_status": "example",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Cyclotomic.lean",
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
- Source path: [`TauLib/BookI/Boundary/Cyclotomic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Cyclotomic.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/Cyclotomic.lean`
- SHA-256: `263c1201c8412549ed0263bd8749c875c25ab2264de6dc66cd64a9d397dc91f6`

## Registry Links

- `I.D88` — Cyclotomic Fields
- `I.R23` — Galois Theory Preview
- `I.T45` — Roots of Unity CRT Decomposition

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.NumberTower`
- `TauLib.BookI.Polarity.CRTBasis`
- `Mathlib.Tactic.Ring`
- `Mathlib.Tactic.NormNum`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Boundary.Galois`

## Declaration Counts

- `def`: 4
- `example`: 8
- `theorem`: 12

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [IsRootOfUnity](/verify/taulib/docs/book-i-boundary-cyclotomic/is-root-of-unity/) | L41-L46 | defined | `I.D88` |
| `def` | [IsPrimitiveRoot](/verify/taulib/docs/book-i-boundary-cyclotomic/is-primitive-root/) | L50-L51 | defined | — |
| `theorem` | [root_of_unity_one](/verify/taulib/docs/book-i-boundary-cyclotomic/root-of-unity-one/) | L58-L59 | formalized | `I.T45` |
| `theorem` | [root_of_unity_pow](/verify/taulib/docs/book-i-boundary-cyclotomic/root-of-unity-pow/) | L62-L68 | formalized | — |
| `def` | [CyclotomicRoot](/verify/taulib/docs/book-i-boundary-cyclotomic/cyclotomic-root/) | L73-L74 | defined | — |
| `theorem` | [root_divides_power](/verify/taulib/docs/book-i-boundary-cyclotomic/root-divides-power/) | L77-L80 | formalized | — |
| `theorem` | [root_of_unity_factor_left](/verify/taulib/docs/book-i-boundary-cyclotomic/root-of-unity-factor-left/) | L87-L97 | formalized | — |
| `theorem` | [root_of_unity_factor_right](/verify/taulib/docs/book-i-boundary-cyclotomic/root-of-unity-factor-right/) | L100-L103 | formalized | — |
| `def` | [euler_totient](/verify/taulib/docs/book-i-boundary-cyclotomic/euler-totient/) | L110-L111 | defined | — |
| `theorem` | [euler_totient_one](/verify/taulib/docs/book-i-boundary-cyclotomic/euler-totient-one/) | L114-L114 | formalized | — |
| `theorem` | [euler_totient_two](/verify/taulib/docs/book-i-boundary-cyclotomic/euler-totient-two/) | L117-L117 | formalized | — |
| `theorem` | [euler_totient_three](/verify/taulib/docs/book-i-boundary-cyclotomic/euler-totient-three/) | L120-L120 | formalized | — |
| `theorem` | [euler_totient_five](/verify/taulib/docs/book-i-boundary-cyclotomic/euler-totient-five/) | L121-L121 | formalized | — |
| `theorem` | [euler_totient_seven](/verify/taulib/docs/book-i-boundary-cyclotomic/euler-totient-seven/) | L122-L122 | formalized | — |
| `theorem` | [galois_action](/verify/taulib/docs/book-i-boundary-cyclotomic/galois-action/) | L131-L137 | formalized | — |
| `theorem` | [galois_action_comp](/verify/taulib/docs/book-i-boundary-cyclotomic/galois-action-comp/) | L140-L143 | formalized | — |
| `example` | [#eval L153](/verify/taulib/docs/book-i-boundary-cyclotomic/example-l153/) | L153-L153 | example | — |
| `example` | [#eval L156](/verify/taulib/docs/book-i-boundary-cyclotomic/example-l156/) | L156-L161 | example | — |
| `example` | [#eval L164](/verify/taulib/docs/book-i-boundary-cyclotomic/example-l164/) | L164-L164 | example | — |
| `example` | [#eval L167](/verify/taulib/docs/book-i-boundary-cyclotomic/example-l167/) | L167-L167 | example | — |
| `example` | [#eval L168](/verify/taulib/docs/book-i-boundary-cyclotomic/example-l168/) | L168-L168 | example | — |
| `example` | [#eval L169](/verify/taulib/docs/book-i-boundary-cyclotomic/example-l169/) | L169-L169 | example | — |
| `example` | [#eval L172](/verify/taulib/docs/book-i-boundary-cyclotomic/example-l172/) | L172-L172 | example | — |
| `example` | [#eval L173](/verify/taulib/docs/book-i-boundary-cyclotomic/example-l173/) | L173-L189 | example | — |
