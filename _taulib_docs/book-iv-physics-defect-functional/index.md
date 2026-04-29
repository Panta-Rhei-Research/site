---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Physics.DefectFunctional",
  "permalink": "/verify/taulib/docs/book-iv-physics-defect-functional/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Physics.DefectFunctional`.",
  "module_name": "TauLib.BookIV.Physics.DefectFunctional",
  "module_slug": "book-iv-physics-defect-functional",
  "book": "BookIV",
  "family": "Physics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Physics/DefectFunctional.lean",
  "sha256": "5e04ea090f238c24766753acae81fca270a074f5603dde7d9a4eea1d6f6e9d3f",
  "imports": [
    "TauLib.BookIV.Physics.QuantityFramework"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Arena.ActorsDynamics",
    "TauLib.BookIV.Physics.Thermodynamics",
    "TauLib.BookV.Prologue.ExportContract"
  ],
  "registry_ids": [
    "IV.D16",
    "IV.D17",
    "IV.D18",
    "IV.D19"
  ],
  "declaration_counts": {
    "inductive": 2,
    "structure": 2,
    "def": 11,
    "theorem": 12,
    "eval": 6
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "DefectComponent",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/defect-component/",
      "source_line_start": 59,
      "source_line_end": 68,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D16"
      ]
    },
    {
      "kind": "structure",
      "name": "DefectTuple",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/defect-tuple/",
      "source_line_start": 79,
      "source_line_end": 88,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D17"
      ]
    },
    {
      "kind": "def",
      "name": "DefectTuple.total",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/total/",
      "source_line_start": 91,
      "source_line_end": 92,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "FluidRegime",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/fluid-regime/",
      "source_line_start": 103,
      "source_line_end": 128,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D18"
      ]
    },
    {
      "kind": "structure",
      "name": "RegimeSignature",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/regime-signature/",
      "source_line_start": 139,
      "source_line_end": 154,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D19"
      ]
    },
    {
      "kind": "def",
      "name": "crystal_signature",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/crystal-signature/",
      "source_line_start": 161,
      "source_line_end": 168,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "glass_signature",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/glass-signature/",
      "source_line_start": 171,
      "source_line_end": 178,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "euler_signature",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/euler-signature/",
      "source_line_start": 181,
      "source_line_end": 188,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ns_signature",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/ns-signature/",
      "source_line_start": 191,
      "source_line_end": 198,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "mhd_signature",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/mhd-signature/",
      "source_line_start": 201,
      "source_line_end": 208,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "plasma_signature",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/plasma-signature/",
      "source_line_start": 211,
      "source_line_end": 218,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "superfluid_signature",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/superfluid-signature/",
      "source_line_start": 221,
      "source_line_end": 228,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "superconductor_signature",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/superconductor-signature/",
      "source_line_start": 231,
      "source_line_end": 238,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "all_regime_signatures",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/all-regime-signatures/",
      "source_line_start": 241,
      "source_line_end": 243,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "regime_signature",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/regime-signature-l246/",
      "source_line_start": 246,
      "source_line_end": 255,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "four_components_exhaust",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/four-components-exhaust/",
      "source_line_start": 262,
      "source_line_end": 264,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "eight_regimes_exhaust",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/eight-regimes-exhaust/",
      "source_line_start": 267,
      "source_line_end": 270,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "euler_no_dissipation",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/euler-no-dissipation/",
      "source_line_start": 273,
      "source_line_end": 274,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "euler_kelvin_invariant",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/euler-kelvin-invariant/",
      "source_line_start": 277,
      "source_line_end": 278,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ns_has_dissipation",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/ns-has-dissipation/",
      "source_line_start": 281,
      "source_line_end": 282,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "superfluid_quantized",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/superfluid-quantized/",
      "source_line_start": 285,
      "source_line_end": 286,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "superfluid_no_dissipation",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/superfluid-no-dissipation/",
      "source_line_start": 289,
      "source_line_end": 290,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "superconductor_em_coupled",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/superconductor-em-coupled/",
      "source_line_start": 293,
      "source_line_end": 294,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "crystal_arrested",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/crystal-arrested/",
      "source_line_start": 297,
      "source_line_end": 298,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mhd_em_coupled",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/mhd-em-coupled/",
      "source_line_start": 301,
      "source_line_end": 302,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "defect_total_sum",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/defect-total-sum/",
      "source_line_start": 305,
      "source_line_end": 306,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "all_signatures_count",
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/all-signatures-count/",
      "source_line_start": 309,
      "source_line_end": 309,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/eval-l315/",
      "source_line_start": 315,
      "source_line_end": 315,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/eval-l316/",
      "source_line_start": 316,
      "source_line_end": 316,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/eval-l317/",
      "source_line_start": 317,
      "source_line_end": 317,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/eval-l318/",
      "source_line_start": 318,
      "source_line_end": 318,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/eval-l319/",
      "source_line_start": 319,
      "source_line_end": 319,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-defect-functional/eval-l322/",
      "source_line_start": 322,
      "source_line_end": 324,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/DefectFunctional.lean",
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
- Source path: [`TauLib/BookIV/Physics/DefectFunctional.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/DefectFunctional.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Physics/DefectFunctional.lean`
- SHA-256: `5e04ea090f238c24766753acae81fca270a074f5603dde7d9a4eea1d6f6e9d3f`

## Registry Links

- `IV.D16` — Defect Component
- `IV.D17` — Defect Tuple
- `IV.D18` — Fluid Regime
- `IV.D19` — Regime Signature

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Physics.QuantityFramework`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Arena.ActorsDynamics`
- `TauLib.BookIV.Physics.Thermodynamics`
- `TauLib.BookV.Prologue.ExportContract`

## Declaration Counts

- `def`: 11
- `eval`: 6
- `inductive`: 2
- `structure`: 2
- `theorem`: 12

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [DefectComponent](/verify/taulib/docs/book-iv-physics-defect-functional/defect-component/) | L59-L68 | defined | `IV.D16` |
| `structure` | [DefectTuple](/verify/taulib/docs/book-iv-physics-defect-functional/defect-tuple/) | L79-L88 | defined | `IV.D17` |
| `def` | [DefectTuple.total](/verify/taulib/docs/book-iv-physics-defect-functional/total/) | L91-L92 | defined | — |
| `inductive` | [FluidRegime](/verify/taulib/docs/book-iv-physics-defect-functional/fluid-regime/) | L103-L128 | defined | `IV.D18` |
| `structure` | [RegimeSignature](/verify/taulib/docs/book-iv-physics-defect-functional/regime-signature/) | L139-L154 | defined | `IV.D19` |
| `def` | [crystal_signature](/verify/taulib/docs/book-iv-physics-defect-functional/crystal-signature/) | L161-L168 | defined | — |
| `def` | [glass_signature](/verify/taulib/docs/book-iv-physics-defect-functional/glass-signature/) | L171-L178 | defined | — |
| `def` | [euler_signature](/verify/taulib/docs/book-iv-physics-defect-functional/euler-signature/) | L181-L188 | defined | — |
| `def` | [ns_signature](/verify/taulib/docs/book-iv-physics-defect-functional/ns-signature/) | L191-L198 | defined | — |
| `def` | [mhd_signature](/verify/taulib/docs/book-iv-physics-defect-functional/mhd-signature/) | L201-L208 | defined | — |
| `def` | [plasma_signature](/verify/taulib/docs/book-iv-physics-defect-functional/plasma-signature/) | L211-L218 | defined | — |
| `def` | [superfluid_signature](/verify/taulib/docs/book-iv-physics-defect-functional/superfluid-signature/) | L221-L228 | defined | — |
| `def` | [superconductor_signature](/verify/taulib/docs/book-iv-physics-defect-functional/superconductor-signature/) | L231-L238 | defined | — |
| `def` | [all_regime_signatures](/verify/taulib/docs/book-iv-physics-defect-functional/all-regime-signatures/) | L241-L243 | defined | — |
| `def` | [regime_signature](/verify/taulib/docs/book-iv-physics-defect-functional/regime-signature-l246/) | L246-L255 | defined | — |
| `theorem` | [four_components_exhaust](/verify/taulib/docs/book-iv-physics-defect-functional/four-components-exhaust/) | L262-L264 | formalized | — |
| `theorem` | [eight_regimes_exhaust](/verify/taulib/docs/book-iv-physics-defect-functional/eight-regimes-exhaust/) | L267-L270 | formalized | — |
| `theorem` | [euler_no_dissipation](/verify/taulib/docs/book-iv-physics-defect-functional/euler-no-dissipation/) | L273-L274 | formalized | — |
| `theorem` | [euler_kelvin_invariant](/verify/taulib/docs/book-iv-physics-defect-functional/euler-kelvin-invariant/) | L277-L278 | formalized | — |
| `theorem` | [ns_has_dissipation](/verify/taulib/docs/book-iv-physics-defect-functional/ns-has-dissipation/) | L281-L282 | formalized | — |
| `theorem` | [superfluid_quantized](/verify/taulib/docs/book-iv-physics-defect-functional/superfluid-quantized/) | L285-L286 | formalized | — |
| `theorem` | [superfluid_no_dissipation](/verify/taulib/docs/book-iv-physics-defect-functional/superfluid-no-dissipation/) | L289-L290 | formalized | — |
| `theorem` | [superconductor_em_coupled](/verify/taulib/docs/book-iv-physics-defect-functional/superconductor-em-coupled/) | L293-L294 | formalized | — |
| `theorem` | [crystal_arrested](/verify/taulib/docs/book-iv-physics-defect-functional/crystal-arrested/) | L297-L298 | formalized | — |
| `theorem` | [mhd_em_coupled](/verify/taulib/docs/book-iv-physics-defect-functional/mhd-em-coupled/) | L301-L302 | formalized | — |
| `theorem` | [defect_total_sum](/verify/taulib/docs/book-iv-physics-defect-functional/defect-total-sum/) | L305-L306 | formalized | — |
| `theorem` | [all_signatures_count](/verify/taulib/docs/book-iv-physics-defect-functional/all-signatures-count/) | L309-L309 | formalized | — |
| `eval` | [#eval L315](/verify/taulib/docs/book-iv-physics-defect-functional/eval-l315/) | L315-L315 | computed | — |
| `eval` | [#eval L316](/verify/taulib/docs/book-iv-physics-defect-functional/eval-l316/) | L316-L316 | computed | — |
| `eval` | [#eval L317](/verify/taulib/docs/book-iv-physics-defect-functional/eval-l317/) | L317-L317 | computed | — |
| `eval` | [#eval L318](/verify/taulib/docs/book-iv-physics-defect-functional/eval-l318/) | L318-L318 | computed | — |
| `eval` | [#eval L319](/verify/taulib/docs/book-iv-physics-defect-functional/eval-l319/) | L319-L319 | computed | — |
| `eval` | [#eval L322](/verify/taulib/docs/book-iv-physics-defect-functional/eval-l322/) | L322-L324 | computed | — |
