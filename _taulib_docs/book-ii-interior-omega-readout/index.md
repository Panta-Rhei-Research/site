---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookII.Interior.OmegaReadout",
  "permalink": "/corpus/taulib/docs/book-ii-interior-omega-readout/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookII.Interior.OmegaReadout`.",
  "module_name": "TauLib.BookII.Interior.OmegaReadout",
  "module_slug": "book-ii-interior-omega-readout",
  "book": "BookII",
  "family": "Interior",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookII/Interior/OmegaReadout.lean",
  "sha256": "5c1757aced41fac2f665ac96510c69cb0eaa337dd0a9d63db04b47ea095dcae6",
  "imports": [
    "TauLib.BookII.Interior.TauAdmissible",
    "TauLib.BookI.Polarity.BipolarAlgebra"
  ],
  "imported_by": [
    "TauLib.BookII",
    "TauLib.BookII.Interior.BipolarDecomposition"
  ],
  "registry_ids": [
    "II.D04",
    "II.P01",
    "II.T02"
  ],
  "declaration_counts": {
    "inductive": 1,
    "def": 9,
    "eval": 11,
    "theorem": 3
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "FiberDominance",
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/fiber-dominance/",
      "source_line_start": 40,
      "source_line_end": 44,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "II.D04"
      ]
    },
    {
      "kind": "def",
      "name": "classify_dominance",
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/classify-dominance/",
      "source_line_start": 47,
      "source_line_end": 50,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauAdmissiblePoint.fiber_dominance",
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/fiber-dominance-l53/",
      "source_line_start": 53,
      "source_line_end": 54,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "omega_readout",
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/omega-readout/",
      "source_line_start": 63,
      "source_line_end": 65,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "II.D04"
      ]
    },
    {
      "kind": "def",
      "name": "dominance_to_sector",
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/dominance-to-sector/",
      "source_line_start": 69,
      "source_line_end": 73,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "primorial_fiber_check",
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/primorial-fiber-check/",
      "source_line_start": 81,
      "source_line_end": 82,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.T02"
      ]
    },
    {
      "kind": "def",
      "name": "primorial_base_diverges",
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/primorial-base-diverges/",
      "source_line_start": 85,
      "source_line_end": 92,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.T02"
      ]
    },
    {
      "kind": "def",
      "name": "tower_path_check",
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/tower-path-check/",
      "source_line_start": 95,
      "source_line_end": 97,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.T02"
      ]
    },
    {
      "kind": "def",
      "name": "base_collapse_check",
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/base-collapse-check/",
      "source_line_start": 100,
      "source_line_end": 107,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "lemniscate_sector_idem_check",
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/lemniscate-sector-idem-check/",
      "source_line_start": 120,
      "source_line_end": 132,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "II.P01"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l139/",
      "source_line_start": 139,
      "source_line_end": 139,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l140/",
      "source_line_start": 140,
      "source_line_end": 140,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l141/",
      "source_line_start": 141,
      "source_line_end": 141,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l142/",
      "source_line_start": 142,
      "source_line_end": 142,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l145/",
      "source_line_start": 145,
      "source_line_end": 145,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l148/",
      "source_line_start": 148,
      "source_line_end": 148,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l149/",
      "source_line_start": 149,
      "source_line_end": 149,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l152/",
      "source_line_start": 152,
      "source_line_end": 152,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l155/",
      "source_line_start": 155,
      "source_line_end": 155,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l158/",
      "source_line_start": 158,
      "source_line_end": 158,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l159/",
      "source_line_start": 159,
      "source_line_end": 159,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "primorial_balanced",
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/primorial-balanced/",
      "source_line_start": 162,
      "source_line_end": 162,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "base_diverges",
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/base-diverges/",
      "source_line_start": 163,
      "source_line_end": 163,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "lemniscate_compat",
      "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/lemniscate-compat/",
      "source_line_start": 164,
      "source_line_end": 166,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean",
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
- Source path: [`TauLib/BookII/Interior/OmegaReadout.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookII/Interior/OmegaReadout.lean`
- SHA-256: `5c1757aced41fac2f665ac96510c69cb0eaa337dd0a9d63db04b47ea095dcae6`

## Registry Links

- `II.D04` — Omega Readout
- `II.P01` — Lemniscate as Coordinate Limit
- `II.T02` — Fiber Degeneration at Omega

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookII.Interior.TauAdmissible`
- `TauLib.BookI.Polarity.BipolarAlgebra`

## Imported By

- `TauLib.BookII`
- `TauLib.BookII.Interior.BipolarDecomposition`

## Declaration Counts

- `def`: 9
- `eval`: 11
- `inductive`: 1
- `theorem`: 3

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [FiberDominance](/corpus/taulib/docs/book-ii-interior-omega-readout/fiber-dominance/) | L40-L44 | type/data schema | type/data schema | `II.D04` |
| `def` | [classify_dominance](/corpus/taulib/docs/book-ii-interior-omega-readout/classify-dominance/) | L47-L50 | definition | definition | — |
| `def` | [TauAdmissiblePoint.fiber_dominance](/corpus/taulib/docs/book-ii-interior-omega-readout/fiber-dominance-l53/) | L53-L54 | definition | definition | — |
| `def` | [omega_readout](/corpus/taulib/docs/book-ii-interior-omega-readout/omega-readout/) | L63-L65 | definition | definition | `II.D04` |
| `def` | [dominance_to_sector](/corpus/taulib/docs/book-ii-interior-omega-readout/dominance-to-sector/) | L69-L73 | definition | definition | — |
| `def` | [primorial_fiber_check](/corpus/taulib/docs/book-ii-interior-omega-readout/primorial-fiber-check/) | L81-L82 | data/computed value | data/computed value | `II.T02` |
| `def` | [primorial_base_diverges](/corpus/taulib/docs/book-ii-interior-omega-readout/primorial-base-diverges/) | L85-L92 | data/computed value | data/computed value | `II.T02` |
| `def` | [tower_path_check](/corpus/taulib/docs/book-ii-interior-omega-readout/tower-path-check/) | L95-L97 | data/computed value | data/computed value | `II.T02` |
| `def` | [base_collapse_check](/corpus/taulib/docs/book-ii-interior-omega-readout/base-collapse-check/) | L100-L107 | data/computed value | data/computed value | — |
| `def` | [lemniscate_sector_idem_check](/corpus/taulib/docs/book-ii-interior-omega-readout/lemniscate-sector-idem-check/) | L120-L132 | data/computed value | data/computed value | `II.P01` |
| `eval` | [#eval L139](/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l139/) | L139-L139 | computed check | computed check | — |
| `eval` | [#eval L140](/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l140/) | L140-L140 | computed check | computed check | — |
| `eval` | [#eval L141](/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l141/) | L141-L141 | computed check | computed check | — |
| `eval` | [#eval L142](/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l142/) | L142-L142 | computed check | computed check | — |
| `eval` | [#eval L145](/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l145/) | L145-L145 | computed check | computed check | — |
| `eval` | [#eval L148](/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l148/) | L148-L148 | computed check | computed check | — |
| `eval` | [#eval L149](/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l149/) | L149-L149 | computed check | computed check | — |
| `eval` | [#eval L152](/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l152/) | L152-L152 | computed check | computed check | — |
| `eval` | [#eval L155](/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l155/) | L155-L155 | computed check | computed check | — |
| `eval` | [#eval L158](/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l158/) | L158-L158 | computed check | computed check | — |
| `eval` | [#eval L159](/corpus/taulib/docs/book-ii-interior-omega-readout/eval-l159/) | L159-L159 | computed check | computed check | — |
| `theorem` | [primorial_balanced](/corpus/taulib/docs/book-ii-interior-omega-readout/primorial-balanced/) | L162-L162 | proof obligation | formal proof obligation checked | — |
| `theorem` | [base_diverges](/corpus/taulib/docs/book-ii-interior-omega-readout/base-diverges/) | L163-L163 | proof obligation | formal proof obligation checked | — |
| `theorem` | [lemniscate_compat](/corpus/taulib/docs/book-ii-interior-omega-readout/lemniscate-compat/) | L164-L166 | proof obligation | formal proof obligation checked | — |
