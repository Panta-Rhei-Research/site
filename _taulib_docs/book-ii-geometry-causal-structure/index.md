---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookII.Geometry.CausalStructure",
  "permalink": "/corpus/taulib/docs/book-ii-geometry-causal-structure/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookII.Geometry.CausalStructure`.",
  "module_name": "TauLib.BookII.Geometry.CausalStructure",
  "module_slug": "book-ii-geometry-causal-structure",
  "book": "BookII",
  "family": "Geometry",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookII/Geometry/CausalStructure.lean",
  "sha256": "b74db434ebc9ec9d43ecc7109ae05378e14abdbf8ef4c04e0564fa0a645fc8e2",
  "imports": [
    "TauLib.BookII.Geometry.Congruence",
    "TauLib.BookI.Polarity.BipolarAlgebra",
    "TauLib.BookI.Boundary.SplitComplex"
  ],
  "imported_by": [
    "TauLib.BookII"
  ],
  "registry_ids": [
    "II.D21",
    "II.D22",
    "II.T19"
  ],
  "declaration_counts": {
    "def": 12,
    "theorem": 7,
    "inductive": 1,
    "eval": 11
  },
  "declarations": [
    {
      "kind": "def",
      "name": "wave_char_roots",
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/wave-char-roots/",
      "source_line_start": 47,
      "source_line_end": 48,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.D21"
      ]
    },
    {
      "kind": "def",
      "name": "wave_discriminant_positive",
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/wave-discriminant-positive/",
      "source_line_start": 53,
      "source_line_end": 57,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "j_squared_plus_one",
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/j-squared-plus-one/",
      "source_line_start": 60,
      "source_line_end": 62,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "char_xi",
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/char-xi/",
      "source_line_start": 71,
      "source_line_end": 71,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "char_zeta",
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/char-zeta/",
      "source_line_start": 74,
      "source_line_end": 74,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "char_recover_check",
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/char-recover-check/",
      "source_line_start": 78,
      "source_line_end": 83,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "CausalClass",
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/causal-class/",
      "source_line_start": 94,
      "source_line_end": 98,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "II.D22"
      ]
    },
    {
      "kind": "def",
      "name": "classify_causal",
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/classify-causal/",
      "source_line_start": 101,
      "source_line_end": 105,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "null_cone_check",
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/null-cone-check/",
      "source_line_start": 108,
      "source_line_end": 112,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "e_plus_null",
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/e-plus-null/",
      "source_line_start": 116,
      "source_line_end": 117,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "e_minus_null",
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/e-minus-null/",
      "source_line_start": 121,
      "source_line_end": 122,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "static_limit_check",
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/static-limit-check/",
      "source_line_start": 136,
      "source_line_end": 142,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.T19"
      ]
    },
    {
      "kind": "def",
      "name": "indefinite_signature_check",
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/indefinite-signature-check/",
      "source_line_start": 146,
      "source_line_end": 150,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sector_causal_correspondence",
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/sector-causal-correspondence/",
      "source_line_start": 160,
      "source_line_end": 166,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l172/",
      "source_line_start": 172,
      "source_line_end": 172,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l173/",
      "source_line_start": 173,
      "source_line_end": 173,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l174/",
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
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l175/",
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
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l176/",
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
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l177/",
      "source_line_start": 177,
      "source_line_end": 177,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l178/",
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
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l179/",
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
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l181/",
      "source_line_start": 181,
      "source_line_end": 181,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l182/",
      "source_line_start": 182,
      "source_line_end": 182,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l183/",
      "source_line_start": 183,
      "source_line_end": 183,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "wave_disc",
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/wave-disc/",
      "source_line_start": 186,
      "source_line_end": 186,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "char_recover",
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/char-recover/",
      "source_line_start": 187,
      "source_line_end": 187,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "null_cone",
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/null-cone/",
      "source_line_start": 188,
      "source_line_end": 188,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "static_lim",
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/static-lim/",
      "source_line_start": 189,
      "source_line_end": 189,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "indef_sig",
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/indef-sig/",
      "source_line_start": 190,
      "source_line_end": 190,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sector_causal",
      "url": "/corpus/taulib/docs/book-ii-geometry-causal-structure/sector-causal/",
      "source_line_start": 191,
      "source_line_end": 193,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/CausalStructure.lean",
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
- Source path: [`TauLib/BookII/Geometry/CausalStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/CausalStructure.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookII/Geometry/CausalStructure.lean`
- SHA-256: `b74db434ebc9ec9d43ecc7109ae05378e14abdbf8ef4c04e0564fa0a645fc8e2`

## Registry Links

- `II.D21` — Wave-Type PDE
- `II.D22` — Causal Structure
- `II.T19` — Euclidean as Static Limit

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookII.Geometry.Congruence`
- `TauLib.BookI.Polarity.BipolarAlgebra`
- `TauLib.BookI.Boundary.SplitComplex`

## Imported By

- `TauLib.BookII`

## Declaration Counts

- `def`: 12
- `eval`: 11
- `inductive`: 1
- `theorem`: 7

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [wave_char_roots](/corpus/taulib/docs/book-ii-geometry-causal-structure/wave-char-roots/) | L47-L48 | data/computed value | data/computed value | `II.D21` |
| `def` | [wave_discriminant_positive](/corpus/taulib/docs/book-ii-geometry-causal-structure/wave-discriminant-positive/) | L53-L57 | data/computed value | data/computed value | — |
| `theorem` | [j_squared_plus_one](/corpus/taulib/docs/book-ii-geometry-causal-structure/j-squared-plus-one/) | L60-L62 | proof obligation | formal proof obligation checked | — |
| `def` | [char_xi](/corpus/taulib/docs/book-ii-geometry-causal-structure/char-xi/) | L71-L71 | data/computed value | data/computed value | — |
| `def` | [char_zeta](/corpus/taulib/docs/book-ii-geometry-causal-structure/char-zeta/) | L74-L74 | data/computed value | data/computed value | — |
| `def` | [char_recover_check](/corpus/taulib/docs/book-ii-geometry-causal-structure/char-recover-check/) | L78-L83 | data/computed value | data/computed value | — |
| `inductive` | [CausalClass](/corpus/taulib/docs/book-ii-geometry-causal-structure/causal-class/) | L94-L98 | type/data schema | type/data schema | `II.D22` |
| `def` | [classify_causal](/corpus/taulib/docs/book-ii-geometry-causal-structure/classify-causal/) | L101-L105 | data/computed value | data/computed value | — |
| `def` | [null_cone_check](/corpus/taulib/docs/book-ii-geometry-causal-structure/null-cone-check/) | L108-L112 | data/computed value | data/computed value | — |
| `def` | [e_plus_null](/corpus/taulib/docs/book-ii-geometry-causal-structure/e-plus-null/) | L116-L117 | data/computed value | data/computed value | — |
| `def` | [e_minus_null](/corpus/taulib/docs/book-ii-geometry-causal-structure/e-minus-null/) | L121-L122 | data/computed value | data/computed value | — |
| `def` | [static_limit_check](/corpus/taulib/docs/book-ii-geometry-causal-structure/static-limit-check/) | L136-L142 | data/computed value | data/computed value | `II.T19` |
| `def` | [indefinite_signature_check](/corpus/taulib/docs/book-ii-geometry-causal-structure/indefinite-signature-check/) | L146-L150 | data/computed value | data/computed value | — |
| `def` | [sector_causal_correspondence](/corpus/taulib/docs/book-ii-geometry-causal-structure/sector-causal-correspondence/) | L160-L166 | data/computed value | data/computed value | — |
| `eval` | [#eval L172](/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l172/) | L172-L172 | computed check | computed check | — |
| `eval` | [#eval L173](/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l173/) | L173-L173 | computed check | computed check | — |
| `eval` | [#eval L174](/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l174/) | L174-L174 | computed check | computed check | — |
| `eval` | [#eval L175](/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l175/) | L175-L175 | computed check | computed check | — |
| `eval` | [#eval L176](/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l176/) | L176-L176 | computed check | computed check | — |
| `eval` | [#eval L177](/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l177/) | L177-L177 | computed check | computed check | — |
| `eval` | [#eval L178](/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l178/) | L178-L178 | computed check | computed check | — |
| `eval` | [#eval L179](/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l179/) | L179-L179 | computed check | computed check | — |
| `eval` | [#eval L181](/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l181/) | L181-L181 | computed check | computed check | — |
| `eval` | [#eval L182](/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l182/) | L182-L182 | computed check | computed check | — |
| `eval` | [#eval L183](/corpus/taulib/docs/book-ii-geometry-causal-structure/eval-l183/) | L183-L183 | computed check | computed check | — |
| `theorem` | [wave_disc](/corpus/taulib/docs/book-ii-geometry-causal-structure/wave-disc/) | L186-L186 | proof obligation | formal proof obligation checked | — |
| `theorem` | [char_recover](/corpus/taulib/docs/book-ii-geometry-causal-structure/char-recover/) | L187-L187 | proof obligation | formal proof obligation checked | — |
| `theorem` | [null_cone](/corpus/taulib/docs/book-ii-geometry-causal-structure/null-cone/) | L188-L188 | proof obligation | formal proof obligation checked | — |
| `theorem` | [static_lim](/corpus/taulib/docs/book-ii-geometry-causal-structure/static-lim/) | L189-L189 | proof obligation | formal proof obligation checked | — |
| `theorem` | [indef_sig](/corpus/taulib/docs/book-ii-geometry-causal-structure/indef-sig/) | L190-L190 | proof obligation | formal proof obligation checked | — |
| `theorem` | [sector_causal](/corpus/taulib/docs/book-ii-geometry-causal-structure/sector-causal/) | L191-L193 | proof obligation | formal proof obligation checked | — |
