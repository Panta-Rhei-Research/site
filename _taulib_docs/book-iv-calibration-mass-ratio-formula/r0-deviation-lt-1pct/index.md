---
{
  "projection_kind": "taulib_declaration",
  "title": "r0_deviation_lt_1pct",
  "permalink": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/r0-deviation-lt-1pct/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.MassRatioFormula`.",
  "declaration_id": "TauLib.BookIV.Calibration.MassRatioFormula::r0_deviation_lt_1pct",
  "declaration_slug": "r0-deviation-lt-1pct",
  "kind": "theorem",
  "name": "r0_deviation_lt_1pct",
  "module_name": "TauLib.BookIV.Calibration.MassRatioFormula",
  "module_url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/",
  "source_line_start": 227,
  "source_line_end": 254,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L227-L254",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.MassRatioFormula",
        "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L227-L254",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookIV.Calibration.MassRatioFormula](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/)
- Source path: [`TauLib/BookIV/Calibration/MassRatioFormula.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L227-L254)
- Source range: L227-L254
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- R₀ deviation from CODATA is less than 1%.

    |R₀ − R_CODATA| / R_CODATA < 0.01

    At 6-digit precision, R₀ ≈ 1838.7 vs R_CODATA ≈ 1838.68, so deviation ≈ 0.001%.

    Cross-multiplied to avoid division:
    |bulk/bulk_denom − correction/correction_denom − R_CODATA| × 100 < R_CODATA

    Since R₀ < R_CODATA (undershoots), the absolute value is:
    R_CODATA − R₀ = (R_CODATA + correction) − bulk

    We prove: 100 × (CODATA + correction − bulk) < CODATA.
    Cross-multiplied on all three fractions' denominators. -/
```

## Source Excerpt

```lean
theorem r0_deviation_lt_1pct :
    -- (R_CODATA − R₀) × 100 < R_CODATA
    -- (R_CODATA + √3·ι_τ^(-2) − ι_τ^(-7)) × 100 < R_CODATA
    -- Since all are positive rationals with different denominators,
    -- cross-multiply to get a Nat comparison:
    --
    -- 100 × (si_mass_ratio.numer × bulk_denom × correction0_denom
    --        + correction0_numer × si_mass_ratio.denom × bulk_denom
    --        − bulk_numer × si_mass_ratio.denom × correction0_denom)
    -- < si_mass_ratio.numer × bulk_denom × correction0_denom
    --
    -- Rearranged to avoid subtraction:
    -- 100 × (CODATA_cross + correction_cross) < 101 × CODATA_cross + 100 × bulk_cross
    -- i.e.: 100 × correction_cross < CODATA_cross + 100 × bulk_cross
    --
    -- Where: CODATA_cross = si_mass_ratio.numer × bulk_denom × correction0_denom
    --        correction_cross = correction0_numer × si_mass_ratio.denom × bulk_denom
    --        bulk_cross = bulk_numer × si_mass_ratio.denom × correction0_denom
    --
    -- Formulation: bulk_cross + CODATA_cross > 100 × correction_cross
    -- i.e.: bulk ≈ 1848, CODATA ≈ 1839 (both >> correction ≈ 14.9)
    -- so bulk_cross + CODATA_cross ≈ 3692 × common_scale
    -- and 100 × correction_cross ≈ 1487 × common_scale
    -- 3692 > 1487 ✓
    bulk_numer * si_mass_ratio.denom * correction0_denom +
    si_mass_ratio.numer * bulk_denom * correction0_denom >
    100 * correction0_numer * si_mass_ratio.denom * bulk_denom := by
  native_decide
```
