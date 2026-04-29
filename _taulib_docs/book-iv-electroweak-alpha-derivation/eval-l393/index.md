---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L393",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/eval-l393/",
  "summary_short": "`eval` declaration in `TauLib.BookIV.Electroweak.AlphaDerivation`.",
  "declaration_id": "TauLib.BookIV.Electroweak.AlphaDerivation::#eval:393",
  "declaration_slug": "eval-l393",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookIV.Electroweak.AlphaDerivation",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/",
  "source_line_start": 393,
  "source_line_end": 393,
  "registry_ids": [
    "IV.R27",
    "IV.R365",
    "IV.R366",
    "IV.R367",
    "IV.R368",
    "IV.R369",
    "IV.R370",
    "IV.R371",
    "IV.R372",
    "IV.R373"
  ],
  "related_registry_items": [
    {
      "id": "IV.R27",
      "title": "sqrt(3) Triad",
      "url": "/registry/object/IV.R27/"
    },
    {
      "id": "IV.R365",
      "title": "Why alpha_mathrmem",
      "url": "/registry/object/IV.R365/"
    },
    {
      "id": "IV.R366",
      "title": "Measuring alpha_mathrmem",
      "url": "/registry/object/IV.R366/"
    },
    {
      "id": "IV.R367",
      "title": "No external input",
      "url": "/registry/object/IV.R367/"
    },
    {
      "id": "IV.R368",
      "title": "Why (1,0) winding",
      "url": "/registry/object/IV.R368/"
    },
    {
      "id": "IV.R369",
      "title": "Compactness is essential",
      "url": "/registry/object/IV.R369/"
    },
    {
      "id": "IV.R370",
      "title": "The iota_tau^2 cancellation",
      "url": "/registry/object/IV.R370/"
    },
    {
      "id": "IV.R371",
      "title": "The meaning of 0.6%",
      "url": "/registry/object/IV.R371/"
    },
    {
      "id": "IV.R372",
      "title": "Lean verification",
      "url": "/registry/object/IV.R372/"
    },
    {
      "id": "IV.R373",
      "title": "pi^3 approx 31: not a Mersenne prime",
      "url": "/registry/object/IV.R373/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L393-L393",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.AlphaDerivation",
        "url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L393-L393",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookIV.Electroweak.AlphaDerivation](/verify/taulib/docs/book-iv-electroweak-alpha-derivation/)
- Source path: [`TauLib/BookIV/Electroweak/AlphaDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L393-L393)
- Source range: L393-L393
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `IV.R27` — sqrt(3) Triad
- `IV.R365` — Why alpha_mathrmem
- `IV.R366` — Measuring alpha_mathrmem
- `IV.R367` — No external input
- `IV.R368` — Why (1,0) winding
- `IV.R369` — Compactness is essential
- `IV.R370` — The iota_tau^2 cancellation
- `IV.R371` — The meaning of 0.6%
- `IV.R372` — Lean verification
- `IV.R373` — pi^3 approx 31: not a Mersenne prime

## Immediate Comment / Docstring

```lean
-- [IV.R27] The spectral formula α = (8/15)·ι_τ⁴ captures the
-- leading-order dependence; the holonomy formula is exact.

-- [IV.R365] The exponent 4 in ι_τ⁴ means α couples TWO τ²-surface
-- modes, each contributing ι_τ² to the coupling.

-- [IV.R366] The factor 8/15 = 2³/(3·5) comes from the primorial
-- structure of the τ-orbit counting function.

-- [IV.R367] The factor π³/16 in the holonomy formula decomposes as
-- π³ (three circles in τ³) divided by 16 = 2⁴ (normalizations).

-- [IV.R368] The correction factor R ≈ 1.0065 is small because the
-- spectral formula already captures the dominant scaling.

-- [IV.R369] The five relational units (M,L,H,Q,R) collapse to
-- 1 anchor (m_n) + 1 constant (ι_τ): from 7 SI base units to 2.

-- [IV.R370] α ≈ 1/137 is not a coincidence or fine-tuning:
-- it is a structural consequence of ι_τ ≈ 0.341 and the factor 8/15.

-- [IV.R371] The AB holonomy lemma connects gauge theory (connection)
-- to sector physics (coupling constant) — two facets of one structure.

-- [IV.R372] Charge quantization + α determination together show
-- that QED is fully derived from K0-K6 with zero free parameters.

-- [IV.R373] The graviton null transport mode (D-sector) parallels
-- the photon (B-sector); gravity is the D-sector gauge theory.

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval alpha_tau_float                       -- ≈ 0.00725 (spectral)
```
