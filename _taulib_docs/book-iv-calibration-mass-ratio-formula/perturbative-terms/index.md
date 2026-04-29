---
{
  "projection_kind": "taulib_declaration",
  "title": "perturbative_terms",
  "permalink": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/perturbative-terms/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.MassRatioFormula`.",
  "declaration_id": "TauLib.BookIV.Calibration.MassRatioFormula::perturbative_terms",
  "declaration_slug": "perturbative-terms",
  "kind": "def",
  "name": "perturbative_terms",
  "module_name": "TauLib.BookIV.Calibration.MassRatioFormula",
  "module_url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/",
  "source_line_start": 295,
  "source_line_end": 299,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L295-L299",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L295-L299",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIV.Calibration.MassRatioFormula](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/)
- Source path: [`TauLib/BookIV/Calibration/MassRatioFormula.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L295-L299)
- Source range: L295-L299
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Perturbative hierarchy: π³α² << √3 << ι_τ^(-7).

    Term magnitudes (at exact ι_τ):
    T0 = ι_τ^(-7) ≈ 1854
    T1 = √3·ι_τ^(-2) ≈ 14.9
    T2 = π³α²·ι_τ^(-2) ≈ 0.014
    T3 = residual ≈ 0.000046

    Ratio: T0/T1 ≈ 124, T1/T2 ≈ 1050, T2/T3 ≈ 300 -/
```

## Source Excerpt

```lean
def perturbative_terms : List String :=
  ["T0: ι_τ^(-7) ≈ 1854",
   "T1: √3·ι_τ^(-2) ≈ 14.9",
   "T2: π³α²·ι_τ^(-2) ≈ 0.014",
   "T3: residual ≈ 0.000046"]
```
