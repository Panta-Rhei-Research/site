---
{
  "projection_kind": "taulib_declaration",
  "title": "NormalizationRemark",
  "permalink": "/verify/taulib/docs/book-iv-calibration-epstein-zeta/normalization-remark/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.EpsteinZeta`.",
  "declaration_id": "TauLib.BookIV.Calibration.EpsteinZeta::NormalizationRemark",
  "declaration_slug": "normalization-remark",
  "kind": "structure",
  "name": "NormalizationRemark",
  "module_name": "TauLib.BookIV.Calibration.EpsteinZeta",
  "module_url": "/verify/taulib/docs/book-iv-calibration-epstein-zeta/",
  "source_line_start": 186,
  "source_line_end": 193,
  "registry_ids": [
    "IV.R10"
  ],
  "related_registry_items": [
    {
      "id": "IV.R10",
      "title": "Normalization",
      "url": "/registry/object/IV.R10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/EpsteinZeta.lean#L186-L193",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.EpsteinZeta",
        "url": "/verify/taulib/docs/book-iv-calibration-epstein-zeta/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/EpsteinZeta.lean#L186-L193",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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

- Module: [TauLib.BookIV.Calibration.EpsteinZeta](/verify/taulib/docs/book-iv-calibration-epstein-zeta/)
- Source path: [`TauLib/BookIV/Calibration/EpsteinZeta.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/EpsteinZeta.lean#L186-L193)
- Source range: L186-L193
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R10` — Normalization

## Immediate Comment / Docstring

```lean
/-- [IV.R10] The normalization N = Z(4; iι_τ)/R ≈ 5.935 is NOT algebraic.

    Z(4; iι_τ) ≈ 10912  (total zeta value)
    R ≈ 1838.68          (mass ratio)
    N = Z(4)/R ≈ 5.935   (not a simple ratio)

    The mass ratio R is the bulk-to-surface breathing ratio
    of the Hodge Laplacian on T², NOT Z(4) divided by an
    integer or simple algebraic constant.

    This is a structural observation — the "normalization problem"
    is dissolved once we recognize R as the ratio of Hilbert-space
    norms, not as Z(4) divided by something. -/
```

## Source Excerpt

```lean
structure NormalizationRemark where
  /-- Z(4; iι_τ) approximate value (scaled ×1000). -/
  z4_approx_scaled : Nat := 10912000
  /-- R approximate value (scaled ×1000). -/
  r_approx_scaled : Nat := 1838684
  /-- The ratio is not a simple integer. -/
  not_algebraic : String := "N ≈ 5.935 is NOT an integer or simple algebraic number"
  deriving Repr
```
