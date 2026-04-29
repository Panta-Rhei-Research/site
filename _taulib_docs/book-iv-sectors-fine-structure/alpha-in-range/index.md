---
{
  "projection_kind": "taulib_declaration",
  "title": "alpha_in_range",
  "permalink": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-in-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Sectors.FineStructure`.",
  "declaration_id": "TauLib.BookIV.Sectors.FineStructure::alpha_in_range",
  "declaration_slug": "alpha-in-range",
  "kind": "theorem",
  "name": "alpha_in_range",
  "module_name": "TauLib.BookIV.Sectors.FineStructure",
  "module_url": "/verify/taulib/docs/book-iv-sectors-fine-structure/",
  "source_line_start": 119,
  "source_line_end": 124,
  "registry_ids": [
    "IV.P02"
  ],
  "related_registry_items": [
    {
      "id": "IV.P02",
      "title": "α Numerical Range",
      "url": "/registry/object/IV.P02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L119-L124",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.FineStructure",
        "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L119-L124",
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

- Module: [TauLib.BookIV.Sectors.FineStructure](/verify/taulib/docs/book-iv-sectors-fine-structure/)
- Source path: [`TauLib/BookIV/Sectors/FineStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L119-L124)
- Source range: L119-L124
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P02` — α Numerical Range

## Immediate Comment / Docstring

```lean
/-- [IV.P02] α_spectral is in the range (7200, 7400) / 10⁶.
    Experimental value: α ≈ 7297.35 / 10⁶.
    Spectral approximation: α ≈ 7247 / 10⁶ (within range). -/
```

## Source Excerpt

```lean
theorem alpha_in_range :
    alpha_spectral_numer * 1000000 > 7200 * alpha_spectral_denom ∧
    alpha_spectral_numer * 1000000 < 7400 * alpha_spectral_denom := by
  simp [alpha_spectral_numer, alpha_spectral_denom,
        iota_fourth_numer, iota_fourth_denom,
        iota, iotaD, iota_tau_numer, iota_tau_denom]
```
