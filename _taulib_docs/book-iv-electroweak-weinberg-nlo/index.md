---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Electroweak.WeinbergNLO",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Electroweak.WeinbergNLO`.",
  "module_name": "TauLib.BookIV.Electroweak.WeinbergNLO",
  "module_slug": "book-iv-electroweak-weinberg-nlo",
  "book": "BookIV",
  "family": "Electroweak",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Electroweak/WeinbergNLO.lean",
  "sha256": "8b47e1a57864c18c2f6b676f94e2c3f866522cc0dbf0879f353a7c5a4ecd46ed",
  "imports": [
    "TauLib.BookI.CF.WindowAlgebra",
    "TauLib.BookIV.Electroweak.EWMixing",
    "TauLib.BookIV.Electroweak.EWProjection"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.Meta.PrintAxioms"
  ],
  "registry_ids": [
    "IV.D334",
    "IV.D337",
    "IV.D338",
    "IV.D339",
    "IV.P180",
    "IV.P181",
    "IV.R389",
    "IV.R390",
    "IV.R391",
    "IV.R393",
    "IV.T134",
    "IV.T135",
    "IV.T139",
    "IV.T140"
  ],
  "declaration_counts": {
    "structure": 2,
    "def": 7,
    "theorem": 19
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "WeinbergNLO",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/weinberg-nlo/",
      "source_line_start": 50,
      "source_line_end": 56,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D334"
      ]
    },
    {
      "kind": "def",
      "name": "weinbergNLO",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/weinberg-nlo-l59/",
      "source_line_start": 59,
      "source_line_end": 60,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nlo_from_windows",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/nlo-from-windows/",
      "source_line_start": 69,
      "source_line_end": 73,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T134"
      ]
    },
    {
      "kind": "theorem",
      "name": "exponent_width_coincidence",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/exponent-width-coincidence/",
      "source_line_start": 85,
      "source_line_end": 88,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P180"
      ]
    },
    {
      "kind": "theorem",
      "name": "mw_ratio_values",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/mw-ratio-values/",
      "source_line_start": 96,
      "source_line_end": 98,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "window_gap",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/window-gap/",
      "source_line_start": 101,
      "source_line_end": 102,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "remark_scale_consistency",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/remark-scale-consistency/",
      "source_line_start": 111,
      "source_line_end": 112,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "IV.R389"
      ]
    },
    {
      "kind": "structure",
      "name": "FermiFormIngredients",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/fermi-form-ingredients/",
      "source_line_start": 126,
      "source_line_end": 138,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T135"
      ]
    },
    {
      "kind": "def",
      "name": "fermiForm",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/fermi-form/",
      "source_line_start": 141,
      "source_line_end": 147,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "fermi_form_w_independent",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/fermi-form-w-independent/",
      "source_line_start": 152,
      "source_line_end": 159,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T135"
      ]
    },
    {
      "kind": "theorem",
      "name": "mode_interpretation_17",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/mode-interpretation-17/",
      "source_line_start": 168,
      "source_line_end": 168,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P181"
      ]
    },
    {
      "kind": "theorem",
      "name": "mode_interpretation_5",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/mode-interpretation-5/",
      "source_line_start": 172,
      "source_line_end": 172,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P181"
      ]
    },
    {
      "kind": "theorem",
      "name": "mode_interpretation_7",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/mode-interpretation-7/",
      "source_line_start": 176,
      "source_line_end": 176,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mode_cf_consistency",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/mode-cf-consistency/",
      "source_line_start": 180,
      "source_line_end": 183,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "remark_oq_a3_resolved",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/remark-oq-a3-resolved/",
      "source_line_start": 196,
      "source_line_end": 197,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "IV.R390"
      ]
    },
    {
      "kind": "def",
      "name": "remark_oq_b2_status",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/remark-oq-b2-status/",
      "source_line_start": 205,
      "source_line_end": 206,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "IV.R391"
      ]
    },
    {
      "kind": "theorem",
      "name": "nlo_from_ew_projection",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/nlo-from-ew-projection/",
      "source_line_start": 211,
      "source_line_end": 214,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T139"
      ]
    },
    {
      "kind": "def",
      "name": "weinberg_nnlo_coeffs",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/weinberg-nnlo-coeffs/",
      "source_line_start": 223,
      "source_line_end": 224,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "IV.D337"
      ]
    },
    {
      "kind": "theorem",
      "name": "nnlo_nlo_num_is_w3_4",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/nnlo-nlo-num-is-w3-4/",
      "source_line_start": 227,
      "source_line_end": 228,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nnlo_nnlo_den_is_w4_3",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/nnlo-nnlo-den-is-w4-3/",
      "source_line_start": 231,
      "source_line_end": 232,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nnlo_window_extends_nlo",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/nnlo-window-extends-nlo/",
      "source_line_start": 236,
      "source_line_end": 238,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mw_nlo_coefficient",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/mw-nlo-coefficient/",
      "source_line_start": 245,
      "source_line_end": 248,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.D338"
      ]
    },
    {
      "kind": "theorem",
      "name": "mw_nlo_numerator_equals_sin2w_nlo_numerator",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/mw-nlo-numerator-equals-sin2w-nlo-numerator/",
      "source_line_start": 251,
      "source_line_end": 253,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_s_nlo_denominator",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/alpha-s-nlo-denominator/",
      "source_line_start": 262,
      "source_line_end": 263,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.D339"
      ]
    },
    {
      "kind": "theorem",
      "name": "window_universality",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/window-universality/",
      "source_line_start": 274,
      "source_line_end": 277,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T140"
      ]
    },
    {
      "kind": "def",
      "name": "remark_nnlo_precision",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/remark-nnlo-precision/",
      "source_line_start": 282,
      "source_line_end": 284,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "IV.R393"
      ]
    },
    {
      "kind": "theorem",
      "name": "nnlo_window_strictly_larger",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/nnlo-window-strictly-larger/",
      "source_line_start": 288,
      "source_line_end": 289,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "consecutive_window_integers",
      "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/consecutive-window-integers/",
      "source_line_start": 292,
      "source_line_end": 298,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean",
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
- Source path: [`TauLib/BookIV/Electroweak/WeinbergNLO.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Electroweak/WeinbergNLO.lean`
- SHA-256: `8b47e1a57864c18c2f6b676f94e2c3f866522cc0dbf0879f353a7c5a4ecd46ed`

## Registry Links

- `IV.D334` — NLO Weinberg Correction
- `IV.D337` — sin²θ_W NNLO Formula
- `IV.D338` — M_W NLO Formula
- `IV.D339` — alpha_s NLO Formula
- `IV.P180` — Exponent-Width Coincidence
- `IV.P181` — Mode Interpretation of EW Coefficients
- `IV.R389` — Scale Consistency
- `IV.R390` — OQ-A3 Resolution Status
- `IV.R391` — OQ-B2 Partial Resolution Status
- `IV.R393` — NNLO Precision Summary
- `IV.T134` — Window Algebra Origin
- `IV.T135` — Fermi Form w-Independence
- `IV.T139` — NLO from EW Projection
- `IV.T140` — Window Universality — W₃(4)=5

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.CF.WindowAlgebra`
- `TauLib.BookIV.Electroweak.EWMixing`
- `TauLib.BookIV.Electroweak.EWProjection`

## Imported By

- `TauLib.BookIV`
- `TauLib.Meta.PrintAxioms`

## Declaration Counts

- `def`: 7
- `structure`: 2
- `theorem`: 19

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [WeinbergNLO](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/weinberg-nlo/) | L50-L56 | type/data schema | type/data schema | `IV.D334` |
| `def` | [weinbergNLO](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/weinberg-nlo-l59/) | L59-L60 | definition | definition | — |
| `theorem` | [nlo_from_windows](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/nlo-from-windows/) | L69-L73 | proof obligation | formal proof obligation checked | `IV.T134` |
| `theorem` | [exponent_width_coincidence](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/exponent-width-coincidence/) | L85-L88 | proof obligation | formal proof obligation checked | `IV.P180` |
| `theorem` | [mw_ratio_values](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/mw-ratio-values/) | L96-L98 | proof obligation | formal proof obligation checked | — |
| `theorem` | [window_gap](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/window-gap/) | L101-L102 | proof obligation | formal proof obligation checked | — |
| `def` | [remark_scale_consistency](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/remark-scale-consistency/) | L111-L112 | docstring/data record | docstring/data record | `IV.R389` |
| `structure` | [FermiFormIngredients](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/fermi-form-ingredients/) | L126-L138 | type/data schema | type/data schema | `IV.T135` |
| `def` | [fermiForm](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/fermi-form/) | L141-L147 | definition | definition | — |
| `theorem` | [fermi_form_w_independent](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/fermi-form-w-independent/) | L152-L159 | proof obligation | formal proof obligation checked | `IV.T135` |
| `theorem` | [mode_interpretation_17](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/mode-interpretation-17/) | L168-L168 | proof obligation | formal proof obligation checked | `IV.P181` |
| `theorem` | [mode_interpretation_5](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/mode-interpretation-5/) | L172-L172 | proof obligation | formal proof obligation checked | `IV.P181` |
| `theorem` | [mode_interpretation_7](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/mode-interpretation-7/) | L176-L176 | proof obligation | formal proof obligation checked | — |
| `theorem` | [mode_cf_consistency](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/mode-cf-consistency/) | L180-L183 | proof obligation | formal proof obligation checked | — |
| `def` | [remark_oq_a3_resolved](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/remark-oq-a3-resolved/) | L196-L197 | docstring/data record | docstring/data record | `IV.R390` |
| `def` | [remark_oq_b2_status](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/remark-oq-b2-status/) | L205-L206 | docstring/data record | docstring/data record | `IV.R391` |
| `theorem` | [nlo_from_ew_projection](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/nlo-from-ew-projection/) | L211-L214 | proof obligation | formal proof obligation checked | `IV.T139` |
| `def` | [weinberg_nnlo_coeffs](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/weinberg-nnlo-coeffs/) | L223-L224 | data/computed value | data/computed value | `IV.D337` |
| `theorem` | [nnlo_nlo_num_is_w3_4](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/nnlo-nlo-num-is-w3-4/) | L227-L228 | proof obligation | formal proof obligation checked | — |
| `theorem` | [nnlo_nnlo_den_is_w4_3](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/nnlo-nnlo-den-is-w4-3/) | L231-L232 | proof obligation | formal proof obligation checked | — |
| `theorem` | [nnlo_window_extends_nlo](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/nnlo-window-extends-nlo/) | L236-L238 | proof obligation | formal proof obligation checked | — |
| `theorem` | [mw_nlo_coefficient](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/mw-nlo-coefficient/) | L245-L248 | proof obligation | formal proof obligation checked | `IV.D338` |
| `theorem` | [mw_nlo_numerator_equals_sin2w_nlo_numerator](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/mw-nlo-numerator-equals-sin2w-nlo-numerator/) | L251-L253 | proof obligation | formal proof obligation checked | — |
| `theorem` | [alpha_s_nlo_denominator](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/alpha-s-nlo-denominator/) | L262-L263 | proof obligation | formal proof obligation checked | `IV.D339` |
| `theorem` | [window_universality](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/window-universality/) | L274-L277 | proof obligation | formal proof obligation checked | `IV.T140` |
| `def` | [remark_nnlo_precision](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/remark-nnlo-precision/) | L282-L284 | docstring/data record | docstring/data record | `IV.R393` |
| `theorem` | [nnlo_window_strictly_larger](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/nnlo-window-strictly-larger/) | L288-L289 | proof obligation | formal proof obligation checked | — |
| `theorem` | [consecutive_window_integers](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/consecutive-window-integers/) | L292-L298 | proof obligation | formal proof obligation checked | — |
