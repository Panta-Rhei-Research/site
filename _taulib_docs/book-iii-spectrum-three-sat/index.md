---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIII.Spectrum.ThreeSAT",
  "permalink": "/verify/taulib/docs/book-iii-spectrum-three-sat/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIII.Spectrum.ThreeSAT`.",
  "module_name": "TauLib.BookIII.Spectrum.ThreeSAT",
  "module_slug": "book-iii-spectrum-three-sat",
  "book": "BookIII",
  "family": "Spectrum",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIII/Spectrum/ThreeSAT.lean",
  "sha256": "869faf2047d267e263f34b57643b7f48d416e1ffb63838af1daf82d710bf0a72",
  "imports": [
    "TauLib.BookI.Holomorphy.SpectralCoefficients",
    "TauLib.BookI.Polarity.NthPrime"
  ],
  "imported_by": [
    "TauLib.BookIII",
    "TauLib.BookIII.Spectrum.KernelHinge"
  ],
  "registry_ids": [
    "I.D73",
    "I.P31",
    "I.P32"
  ],
  "declaration_counts": {
    "structure": 3,
    "def": 12,
    "theorem": 5,
    "example": 1,
    "eval": 6
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "Literal",
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/literal/",
      "source_line_start": 38,
      "source_line_end": 43,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "Clause",
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/clause/",
      "source_line_start": 46,
      "source_line_end": 53,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CNF",
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/cnf/",
      "source_line_start": 56,
      "source_line_end": 68,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Literal.eval",
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/eval/",
      "source_line_start": 71,
      "source_line_end": 72,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Clause.eval",
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/eval-l75/",
      "source_line_start": 75,
      "source_line_end": 76,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "CNF.eval",
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/eval-l79/",
      "source_line_start": 79,
      "source_line_end": 80,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "CNF.satisfiable",
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/satisfiable/",
      "source_line_start": 83,
      "source_line_end": 84,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "crt_residue",
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/crt-residue/",
      "source_line_start": 92,
      "source_line_end": 94,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "spectral_var_true",
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/spectral-var-true/",
      "source_line_start": 100,
      "source_line_end": 101,
      "formal_status": "defined",
      "registry_ids": [
        "I.D73"
      ]
    },
    {
      "kind": "def",
      "name": "spectral_literal",
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/spectral-literal/",
      "source_line_start": 104,
      "source_line_end": 106,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "spectral_clause",
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/spectral-clause/",
      "source_line_start": 109,
      "source_line_end": 110,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "spectral_cnf",
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/spectral-cnf/",
      "source_line_start": 114,
      "source_line_end": 115,
      "formal_status": "defined",
      "registry_ids": [
        "I.D73"
      ]
    },
    {
      "kind": "def",
      "name": "SpectralSatisfiable",
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/spectral-satisfiable/",
      "source_line_start": 119,
      "source_line_end": 120,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "spectral_decidable",
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/spectral-decidable/",
      "source_line_start": 129,
      "source_line_end": 131,
      "formal_status": "formalized",
      "registry_ids": [
        "I.P31"
      ]
    },
    {
      "kind": "theorem",
      "name": "empty_cnf_sat",
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/empty-cnf-sat/",
      "source_line_start": 134,
      "source_line_end": 135,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bool_sat_decidable",
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/bool-sat-decidable/",
      "source_line_start": 138,
      "source_line_end": 140,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_complexity_bridge_concrete",
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/tau-complexity-bridge-concrete/",
      "source_line_start": 151,
      "source_line_end": 157,
      "formal_status": "formalized",
      "registry_ids": [
        "I.P32"
      ]
    },
    {
      "kind": "theorem",
      "name": "single_var_spectral",
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/single-var-spectral/",
      "source_line_start": 160,
      "source_line_end": 162,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_clause",
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/example-clause/",
      "source_line_start": 169,
      "source_line_end": 170,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/example-l173/",
      "source_line_start": 173,
      "source_line_end": 173,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_cnf",
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/example-cnf/",
      "source_line_start": 176,
      "source_line_end": 177,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/eval-l184/",
      "source_line_start": 184,
      "source_line_end": 184,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/eval-l185/",
      "source_line_start": 185,
      "source_line_end": 185,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/eval-l188/",
      "source_line_start": 188,
      "source_line_end": 188,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/eval-l191/",
      "source_line_start": 191,
      "source_line_end": 191,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/eval-l194/",
      "source_line_start": 194,
      "source_line_end": 194,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/eval-l195/",
      "source_line_start": 195,
      "source_line_end": 197,
      "formal_status": "computed",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/ThreeSAT.lean",
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
- Source path: [`TauLib/BookIII/Spectrum/ThreeSAT.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/ThreeSAT.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIII/Spectrum/ThreeSAT.lean`
- SHA-256: `869faf2047d267e263f34b57643b7f48d416e1ffb63838af1daf82d710bf0a72`

## Registry Links

- No Registry IDs were detected in this module.

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Holomorphy.SpectralCoefficients`
- `TauLib.BookI.Polarity.NthPrime`

## Imported By

- `TauLib.BookIII`
- `TauLib.BookIII.Spectrum.KernelHinge`

## Declaration Counts

- `def`: 12
- `eval`: 6
- `example`: 1
- `structure`: 3
- `theorem`: 5

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [Literal](/verify/taulib/docs/book-iii-spectrum-three-sat/literal/) | L38-L43 | defined | — |
| `structure` | [Clause](/verify/taulib/docs/book-iii-spectrum-three-sat/clause/) | L46-L53 | defined | — |
| `structure` | [CNF](/verify/taulib/docs/book-iii-spectrum-three-sat/cnf/) | L56-L68 | defined | — |
| `def` | [Literal.eval](/verify/taulib/docs/book-iii-spectrum-three-sat/eval/) | L71-L72 | defined | — |
| `def` | [Clause.eval](/verify/taulib/docs/book-iii-spectrum-three-sat/eval-l75/) | L75-L76 | defined | — |
| `def` | [CNF.eval](/verify/taulib/docs/book-iii-spectrum-three-sat/eval-l79/) | L79-L80 | defined | — |
| `def` | [CNF.satisfiable](/verify/taulib/docs/book-iii-spectrum-three-sat/satisfiable/) | L83-L84 | defined | — |
| `def` | [crt_residue](/verify/taulib/docs/book-iii-spectrum-three-sat/crt-residue/) | L92-L94 | defined | — |
| `def` | [spectral_var_true](/verify/taulib/docs/book-iii-spectrum-three-sat/spectral-var-true/) | L100-L101 | defined | `I.D73` |
| `def` | [spectral_literal](/verify/taulib/docs/book-iii-spectrum-three-sat/spectral-literal/) | L104-L106 | defined | — |
| `def` | [spectral_clause](/verify/taulib/docs/book-iii-spectrum-three-sat/spectral-clause/) | L109-L110 | defined | — |
| `def` | [spectral_cnf](/verify/taulib/docs/book-iii-spectrum-three-sat/spectral-cnf/) | L114-L115 | defined | `I.D73` |
| `def` | [SpectralSatisfiable](/verify/taulib/docs/book-iii-spectrum-three-sat/spectral-satisfiable/) | L119-L120 | defined | — |
| `theorem` | [spectral_decidable](/verify/taulib/docs/book-iii-spectrum-three-sat/spectral-decidable/) | L129-L131 | formalized | `I.P31` |
| `theorem` | [empty_cnf_sat](/verify/taulib/docs/book-iii-spectrum-three-sat/empty-cnf-sat/) | L134-L135 | formalized | — |
| `theorem` | [bool_sat_decidable](/verify/taulib/docs/book-iii-spectrum-three-sat/bool-sat-decidable/) | L138-L140 | formalized | — |
| `theorem` | [tau_complexity_bridge_concrete](/verify/taulib/docs/book-iii-spectrum-three-sat/tau-complexity-bridge-concrete/) | L151-L157 | formalized | `I.P32` |
| `theorem` | [single_var_spectral](/verify/taulib/docs/book-iii-spectrum-three-sat/single-var-spectral/) | L160-L162 | formalized | — |
| `def` | [example_clause](/verify/taulib/docs/book-iii-spectrum-three-sat/example-clause/) | L169-L170 | defined | — |
| `example` | [#eval L173](/verify/taulib/docs/book-iii-spectrum-three-sat/example-l173/) | L173-L173 | example | — |
| `def` | [example_cnf](/verify/taulib/docs/book-iii-spectrum-three-sat/example-cnf/) | L176-L177 | defined | — |
| `eval` | [#eval L184](/verify/taulib/docs/book-iii-spectrum-three-sat/eval-l184/) | L184-L184 | computed | — |
| `eval` | [#eval L185](/verify/taulib/docs/book-iii-spectrum-three-sat/eval-l185/) | L185-L185 | computed | — |
| `eval` | [#eval L188](/verify/taulib/docs/book-iii-spectrum-three-sat/eval-l188/) | L188-L188 | computed | — |
| `eval` | [#eval L191](/verify/taulib/docs/book-iii-spectrum-three-sat/eval-l191/) | L191-L191 | computed | — |
| `eval` | [#eval L194](/verify/taulib/docs/book-iii-spectrum-three-sat/eval-l194/) | L194-L194 | computed | — |
| `eval` | [#eval L195](/verify/taulib/docs/book-iii-spectrum-three-sat/eval-l195/) | L195-L197 | computed | — |
