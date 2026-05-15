---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Sectors.SpectralPage",
  "permalink": "/corpus/taulib/docs/book-iv-sectors-spectral-page/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Sectors.SpectralPage`.",
  "module_name": "TauLib.BookIV.Sectors.SpectralPage",
  "module_slug": "book-iv-sectors-spectral-page",
  "book": "BookIV",
  "family": "Sectors",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Sectors/SpectralPage.lean",
  "sha256": "eb936beb6d526b04dfe8de769120483a41c491db26cd0b53fe3227bd46c48ec2",
  "imports": [
    "TauLib.BookIV.Sectors.BoundaryFiltration",
    "TauLib.BookIV.Sectors.ModeCensus"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookV.GravityField.ExponentDerivation"
  ],
  "registry_ids": [
    "IV.D331",
    "IV.P179",
    "IV.R388",
    "IV.T133"
  ],
  "declaration_counts": {
    "def": 3,
    "theorem": 8,
    "eval": 3
  },
  "declarations": [
    {
      "kind": "def",
      "name": "tensorModes",
      "url": "/corpus/taulib/docs/book-iv-sectors-spectral-page/tensor-modes/",
      "source_line_start": 50,
      "source_line_end": 51,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "IV.D331"
      ]
    },
    {
      "kind": "def",
      "name": "emTensorActive",
      "url": "/corpus/taulib/docs/book-iv-sectors-spectral-page/em-tensor-active/",
      "source_line_start": 54,
      "source_line_end": 55,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "emTensorSilent",
      "url": "/corpus/taulib/docs/book-iv-sectors-spectral-page/em-tensor-silent/",
      "source_line_start": 58,
      "source_line_end": 59,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "em_tensor_total",
      "url": "/corpus/taulib/docs/book-iv-sectors-spectral-page/em-tensor-total/",
      "source_line_start": 66,
      "source_line_end": 66,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T133"
      ]
    },
    {
      "kind": "theorem",
      "name": "em_tensor_active_count",
      "url": "/corpus/taulib/docs/book-iv-sectors-spectral-page/em-tensor-active-count/",
      "source_line_start": 69,
      "source_line_end": 69,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T133"
      ]
    },
    {
      "kind": "theorem",
      "name": "em_tensor_silent_count",
      "url": "/corpus/taulib/docs/book-iv-sectors-spectral-page/em-tensor-silent-count/",
      "source_line_start": 72,
      "source_line_end": 72,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tensor_partition",
      "url": "/corpus/taulib/docs/book-iv-sectors-spectral-page/tensor-partition/",
      "source_line_start": 75,
      "source_line_end": 76,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "density_is_square",
      "url": "/corpus/taulib/docs/book-iv-sectors-spectral-page/density-is-square/",
      "source_line_start": 83,
      "source_line_end": 83,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "density_equals_square",
      "url": "/corpus/taulib/docs/book-iv-sectors-spectral-page/density-equals-square/",
      "source_line_start": 86,
      "source_line_end": 87,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tensor_equals_sieve_times_correction",
      "url": "/corpus/taulib/docs/book-iv-sectors-spectral-page/tensor-equals-sieve-times-correction/",
      "source_line_start": 92,
      "source_line_end": 93,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P179"
      ]
    },
    {
      "kind": "theorem",
      "name": "correction_cross_mult",
      "url": "/corpus/taulib/docs/book-iv-sectors-spectral-page/correction-cross-mult/",
      "source_line_start": 97,
      "source_line_end": 98,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-spectral-page/eval-l104/",
      "source_line_start": 104,
      "source_line_end": 104,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-spectral-page/eval-l105/",
      "source_line_start": 105,
      "source_line_end": 105,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-spectral-page/eval-l106/",
      "source_line_start": 106,
      "source_line_end": 108,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SpectralPage.lean",
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
- Source path: [`TauLib/BookIV/Sectors/SpectralPage.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SpectralPage.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Sectors/SpectralPage.lean`
- SHA-256: `eb936beb6d526b04dfe8de769120483a41c491db26cd0b53fe3227bd46c48ec2`

## Registry Links

- `IV.D331` — Tensor-Square Character Algebra
- `IV.P179` — E₁ Page Derivation of α-Coefficient
- `IV.R388` — OQ-A1 Status: RESOLVED
- `IV.T133` — EM Tensor Density Theorem

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Sectors.BoundaryFiltration`
- `TauLib.BookIV.Sectors.ModeCensus`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookV.GravityField.ExponentDerivation`

## Declaration Counts

- `def`: 3
- `eval`: 3
- `theorem`: 8

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [tensorModes](/corpus/taulib/docs/book-iv-sectors-spectral-page/tensor-modes/) | L50-L51 | data/computed value | data/computed value | `IV.D331` |
| `def` | [emTensorActive](/corpus/taulib/docs/book-iv-sectors-spectral-page/em-tensor-active/) | L54-L55 | data/computed value | data/computed value | — |
| `def` | [emTensorSilent](/corpus/taulib/docs/book-iv-sectors-spectral-page/em-tensor-silent/) | L58-L59 | data/computed value | data/computed value | — |
| `theorem` | [em_tensor_total](/corpus/taulib/docs/book-iv-sectors-spectral-page/em-tensor-total/) | L66-L66 | proof obligation | formal proof obligation checked | `IV.T133` |
| `theorem` | [em_tensor_active_count](/corpus/taulib/docs/book-iv-sectors-spectral-page/em-tensor-active-count/) | L69-L69 | proof obligation | formal proof obligation checked | `IV.T133` |
| `theorem` | [em_tensor_silent_count](/corpus/taulib/docs/book-iv-sectors-spectral-page/em-tensor-silent-count/) | L72-L72 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tensor_partition](/corpus/taulib/docs/book-iv-sectors-spectral-page/tensor-partition/) | L75-L76 | proof obligation | formal proof obligation checked | — |
| `theorem` | [density_is_square](/corpus/taulib/docs/book-iv-sectors-spectral-page/density-is-square/) | L83-L83 | proof obligation | formal proof obligation checked | — |
| `theorem` | [density_equals_square](/corpus/taulib/docs/book-iv-sectors-spectral-page/density-equals-square/) | L86-L87 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tensor_equals_sieve_times_correction](/corpus/taulib/docs/book-iv-sectors-spectral-page/tensor-equals-sieve-times-correction/) | L92-L93 | proof obligation | formal proof obligation checked | `IV.P179` |
| `theorem` | [correction_cross_mult](/corpus/taulib/docs/book-iv-sectors-spectral-page/correction-cross-mult/) | L97-L98 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L104](/corpus/taulib/docs/book-iv-sectors-spectral-page/eval-l104/) | L104-L104 | computed check | computed check | — |
| `eval` | [#eval L105](/corpus/taulib/docs/book-iv-sectors-spectral-page/eval-l105/) | L105-L105 | computed check | computed check | — |
| `eval` | [#eval L106](/corpus/taulib/docs/book-iv-sectors-spectral-page/eval-l106/) | L106-L108 | computed check | computed check | — |
