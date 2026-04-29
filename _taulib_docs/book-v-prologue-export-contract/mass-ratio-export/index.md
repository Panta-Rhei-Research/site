---
{
  "projection_kind": "taulib_declaration",
  "title": "mass_ratio_export",
  "permalink": "/verify/taulib/docs/book-v-prologue-export-contract/mass-ratio-export/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Prologue.ExportContract`.",
  "declaration_id": "TauLib.BookV.Prologue.ExportContract::mass_ratio_export",
  "declaration_slug": "mass-ratio-export",
  "kind": "theorem",
  "name": "mass_ratio_export",
  "module_name": "TauLib.BookV.Prologue.ExportContract",
  "module_url": "/verify/taulib/docs/book-v-prologue-export-contract/",
  "source_line_start": 157,
  "source_line_end": 164,
  "registry_ids": [
    "V.T07"
  ],
  "related_registry_items": [
    {
      "id": "V.T07",
      "title": "Mass Ratio --- IV.T30",
      "url": "/registry/object/V.T07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L157-L164",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Prologue.ExportContract",
        "url": "/verify/taulib/docs/book-v-prologue-export-contract/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L157-L164",
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

- Module: [TauLib.BookV.Prologue.ExportContract](/verify/taulib/docs/book-v-prologue-export-contract/)
- Source path: [`TauLib/BookV/Prologue/ExportContract.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L157-L164)
- Source range: L157-L164
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T07` — Mass Ratio --- IV.T30

## Immediate Comment / Docstring

```lean
/-- [V.T07] Mass ratio R = ι_τ^(-7) − (√3 + π³α²)·ι_τ^(-2), 0.025 ppm.

    The 10-link derivation chain has zero conjectural ingredients.
    Wraps the Level 0 range proof from MassRatioFormula (at 6-digit
    precision, R₀ is in (1837, 1840); at exact ι_τ, R₁ ≈ 1838.684). -/
```

## Source Excerpt

```lean
theorem mass_ratio_export :
    -- R₀ > 1837 (at 6-digit ι_τ)
    bulk_numer * correction0_denom >
    correction0_numer * bulk_denom + 1837 * bulk_denom * correction0_denom ∧
    -- R₀ < 1840 (at 6-digit ι_τ)
    bulk_numer * correction0_denom <
    correction0_numer * bulk_denom + 1840 * bulk_denom * correction0_denom :=
  r0_in_range
```
