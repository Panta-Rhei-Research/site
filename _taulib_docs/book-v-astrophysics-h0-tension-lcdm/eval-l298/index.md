---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L298",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l298/",
  "summary_short": "`eval` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::#eval:298",
  "declaration_slug": "eval-l298",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 298,
  "source_line_end": 298,
  "registry_ids": [
    "V.R205",
    "V.R206",
    "V.R207",
    "V.R208"
  ],
  "related_registry_items": [
    {
      "id": "V.R205",
      "title": "Both Measurements Correct",
      "url": "/registry/object/V.R205/"
    },
    {
      "id": "V.R206",
      "title": "Correct Parameters Wrong Ontology",
      "url": "/registry/object/V.R206/"
    },
    {
      "id": "V.R207",
      "title": "What Would Reopen the Case",
      "url": "/registry/object/V.R207/"
    },
    {
      "id": "V.R208",
      "title": "From Part V to Part VI",
      "url": "/registry/object/V.R208/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L298-L298",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.H0TensionLCDM",
        "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L298-L298",
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

- Module: [TauLib.BookV.Astrophysics.H0TensionLCDM](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/)
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L298-L298)
- Source range: L298-L298
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `V.R205` — Both Measurements Correct
- `V.R206` — Correct Parameters Wrong Ontology
- `V.R207` — What Would Reopen the Case
- `V.R208` — From Part V to Part VI

## Immediate Comment / Docstring

```lean
-- ============================================================
-- REMARKS (comment-only)
-- ============================================================

-- [V.R205] 5σ Tension Current Status: as of 2024-2025, the H₀
-- tension persists at >5σ between Planck (67.4) and SH0ES (73.0).
-- TRGB measurements give intermediate values (~69-72).
-- DESI BAO results (2024) are consistent with Planck.

-- [V.R206] LCDM as Depth-1 Approximation: ΛCDM is the depth-1
-- readout of the τ-framework. It works remarkably well because
-- depth-1 captures >95% of the physics. The remaining ~5% (tensions,
-- DM/DE, etc.) are depth-2+ corrections that ΛCDM cannot access.

-- [V.R207] 120 Orders of Magnitude Problem Dissolved: the "worst
-- prediction in physics" (Λ_QFT/Λ_obs ~ 10¹²²) is dissolved because
-- it compares incommensurable quantities. The bulk vacuum energy
-- (QFT) and the cosmological constant (boundary readout) are
-- different objects at different levels of the τ-framework.

-- [V.R208] Future Tests from CMB-S4 and DESI: next-generation
-- surveys (CMB-S4, DESI, Euclid, Roman) will measure H₀ at
-- multiple redshifts and scales, directly testing the τ-prediction
-- that H₀ is scale-dependent.

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval planck_h0.h0_scaled          -- 674
```
