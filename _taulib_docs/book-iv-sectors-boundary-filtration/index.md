---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Sectors.BoundaryFiltration",
  "permalink": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Sectors.BoundaryFiltration`.",
  "module_name": "TauLib.BookIV.Sectors.BoundaryFiltration",
  "module_slug": "book-iv-sectors-boundary-filtration",
  "book": "BookIV",
  "family": "Sectors",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Sectors/BoundaryFiltration.lean",
  "sha256": "8cb4300b21d74de6a779a0566dce1b03c781321d61b723c6ccde0492f9c97d42",
  "imports": [
    "TauLib.BookIV.Sectors.ModeCensus",
    "TauLib.BookIV.Sectors.SectorParameters"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Electroweak.EWProjection",
    "TauLib.BookIV.Sectors.SpectralPage"
  ],
  "registry_ids": [
    "IV.D328",
    "IV.D329",
    "IV.D330",
    "IV.D60",
    "IV.D61",
    "IV.D62",
    "IV.P09",
    "IV.P178",
    "IV.R387",
    "IV.T130",
    "IV.T131",
    "IV.T132",
    "IV.T17"
  ],
  "declaration_counts": {
    "inductive": 1,
    "def": 5,
    "theorem": 15,
    "eval": 3
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "GenCarrier",
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/gen-carrier/",
      "source_line_start": 70,
      "source_line_end": 73,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "genCarrier",
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/gen-carrier-l82/",
      "source_line_start": 82,
      "source_line_end": 87,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "IV.D328"
      ]
    },
    {
      "kind": "def",
      "name": "genPolarity",
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/gen-polarity/",
      "source_line_start": 99,
      "source_line_end": 104,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "IV.D329"
      ]
    },
    {
      "kind": "def",
      "name": "emActiveStructural",
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/em-active-structural/",
      "source_line_start": 121,
      "source_line_end": 124,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "IV.D330"
      ]
    },
    {
      "kind": "def",
      "name": "activeModesStructural",
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/active-modes-structural/",
      "source_line_start": 131,
      "source_line_end": 132,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "silentModesStructural",
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/silent-modes-structural/",
      "source_line_start": 135,
      "source_line_end": 136,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "structural_agrees_with_physics",
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/structural-agrees-with-physics/",
      "source_line_start": 148,
      "source_line_end": 152,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T130"
      ]
    },
    {
      "kind": "theorem",
      "name": "census_structural",
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/census-structural/",
      "source_line_start": 160,
      "source_line_end": 160,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P178"
      ]
    },
    {
      "kind": "theorem",
      "name": "silent_structural",
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/silent-structural/",
      "source_line_start": 163,
      "source_line_end": 163,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "structural_census_consistent",
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/structural-census-consistent/",
      "source_line_start": 166,
      "source_line_end": 167,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "rule1_silences_alpha",
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/rule1-silences-alpha/",
      "source_line_start": 174,
      "source_line_end": 178,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "rule2_silences_pi_crossing",
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/rule2-silences-pi-crossing/",
      "source_line_start": 181,
      "source_line_end": 185,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "fiber_generators_fully_active",
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/fiber-generators-fully-active/",
      "source_line_start": 188,
      "source_line_end": 198,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "twin_prime_residue",
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/twin-prime-residue/",
      "source_line_start": 218,
      "source_line_end": 220,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T131"
      ]
    },
    {
      "kind": "theorem",
      "name": "sieve_correction_decomposition",
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/sieve-correction-decomposition/",
      "source_line_start": 225,
      "source_line_end": 226,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "twin_prime_core_identity",
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/twin-prime-core-identity/",
      "source_line_start": 231,
      "source_line_end": 232,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T132"
      ]
    },
    {
      "kind": "theorem",
      "name": "twin_prime_vanishing",
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/twin-prime-vanishing/",
      "source_line_start": 236,
      "source_line_end": 237,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "active_count_unit_mod_sn",
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/active-count-unit-mod-sn/",
      "source_line_start": 240,
      "source_line_end": 241,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "silent_count_structural",
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/silent-count-structural/",
      "source_line_start": 244,
      "source_line_end": 245,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sn_equals_factorial",
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/sn-equals-factorial/",
      "source_line_start": 248,
      "source_line_end": 249,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "e1_page_arithmetic",
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/e1-page-arithmetic/",
      "source_line_start": 252,
      "source_line_end": 254,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/eval-l260/",
      "source_line_start": 260,
      "source_line_end": 260,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/eval-l261/",
      "source_line_start": 261,
      "source_line_end": 261,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-boundary-filtration/eval-l264/",
      "source_line_start": 264,
      "source_line_end": 266,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean",
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
- Source path: [`TauLib/BookIV/Sectors/BoundaryFiltration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Sectors/BoundaryFiltration.lean`
- SHA-256: `8cb4300b21d74de6a779a0566dce1b03c781321d61b723c6ccde0492f9c97d42`

## Registry Links

- `IV.D328` — Generator Carrier Assignment
- `IV.D329` — Generator Polarity Assignment
- `IV.D330` — Structural EM Activity
- `IV.D60` — Space of CR-Functions
- `IV.D61` — Canonical Inner Product
- `IV.D62` — Holomorphic Hilbert Space
- `IV.P09` — Integrability of τ³ CR-Structure
- `IV.P178` — SM-Independent Census
- `IV.R387` — OQ.11 Resolution Status
- `IV.T130` — Structural–Physics Census Equivalence
- `IV.T17` — Emergence of Spin-1/2

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Sectors.ModeCensus`
- `TauLib.BookIV.Sectors.SectorParameters`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Electroweak.EWProjection`
- `TauLib.BookIV.Sectors.SpectralPage`

## Declaration Counts

- `def`: 5
- `eval`: 3
- `inductive`: 1
- `theorem`: 15

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [GenCarrier](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/gen-carrier/) | L70-L73 | type/data schema | type/data schema | — |
| `def` | [genCarrier](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/gen-carrier-l82/) | L82-L87 | definition | definition | `IV.D328` |
| `def` | [genPolarity](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/gen-polarity/) | L99-L104 | definition | definition | `IV.D329` |
| `def` | [emActiveStructural](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/em-active-structural/) | L121-L124 | definition | definition | `IV.D330` |
| `def` | [activeModesStructural](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/active-modes-structural/) | L131-L132 | data/computed value | data/computed value | — |
| `def` | [silentModesStructural](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/silent-modes-structural/) | L135-L136 | data/computed value | data/computed value | — |
| `theorem` | [structural_agrees_with_physics](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/structural-agrees-with-physics/) | L148-L152 | proof obligation | formal proof obligation checked | `IV.T130` |
| `theorem` | [census_structural](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/census-structural/) | L160-L160 | proof obligation | formal proof obligation checked | `IV.P178` |
| `theorem` | [silent_structural](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/silent-structural/) | L163-L163 | proof obligation | formal proof obligation checked | — |
| `theorem` | [structural_census_consistent](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/structural-census-consistent/) | L166-L167 | proof obligation | formal proof obligation checked | — |
| `theorem` | [rule1_silences_alpha](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/rule1-silences-alpha/) | L174-L178 | proof obligation | formal proof obligation checked | — |
| `theorem` | [rule2_silences_pi_crossing](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/rule2-silences-pi-crossing/) | L181-L185 | proof obligation | formal proof obligation checked | — |
| `theorem` | [fiber_generators_fully_active](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/fiber-generators-fully-active/) | L188-L198 | proof obligation | formal proof obligation checked | — |
| `theorem` | [twin_prime_residue](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/twin-prime-residue/) | L218-L220 | proof obligation | formal proof obligation checked | `IV.T131` |
| `theorem` | [sieve_correction_decomposition](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/sieve-correction-decomposition/) | L225-L226 | proof obligation | formal proof obligation checked | — |
| `theorem` | [twin_prime_core_identity](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/twin-prime-core-identity/) | L231-L232 | proof obligation | formal proof obligation checked | `IV.T132` |
| `theorem` | [twin_prime_vanishing](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/twin-prime-vanishing/) | L236-L237 | proof obligation | formal proof obligation checked | — |
| `theorem` | [active_count_unit_mod_sn](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/active-count-unit-mod-sn/) | L240-L241 | proof obligation | formal proof obligation checked | — |
| `theorem` | [silent_count_structural](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/silent-count-structural/) | L244-L245 | proof obligation | formal proof obligation checked | — |
| `theorem` | [sn_equals_factorial](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/sn-equals-factorial/) | L248-L249 | proof obligation | formal proof obligation checked | — |
| `theorem` | [e1_page_arithmetic](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/e1-page-arithmetic/) | L252-L254 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L260](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/eval-l260/) | L260-L260 | computed check | computed check | — |
| `eval` | [#eval L261](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/eval-l261/) | L261-L261 | computed check | computed check | — |
| `eval` | [#eval L264](/corpus/taulib/docs/book-iv-sectors-boundary-filtration/eval-l264/) | L264-L266 | computed check | computed check | — |
