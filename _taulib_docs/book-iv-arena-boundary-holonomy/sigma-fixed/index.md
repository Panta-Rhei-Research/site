---
{
  "projection_kind": "taulib_declaration",
  "title": "sigma_fixed",
  "permalink": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/sigma-fixed/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.BoundaryHolonomy`.",
  "declaration_id": "TauLib.BookIV.Arena.BoundaryHolonomy::sigma_fixed",
  "declaration_slug": "sigma-fixed",
  "kind": "theorem",
  "name": "sigma_fixed",
  "module_name": "TauLib.BookIV.Arena.BoundaryHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/",
  "source_line_start": 139,
  "source_line_end": 139,
  "registry_ids": [
    "IV.P152"
  ],
  "related_registry_items": [
    {
      "id": "IV.P152",
      "title": "Master constant is sigma-fixed",
      "url": "/registry/object/IV.P152/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L139-L139",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.BoundaryHolonomy",
        "url": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L139-L139",
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

- Module: [TauLib.BookIV.Arena.BoundaryHolonomy](/verify/taulib/docs/book-iv-arena-boundary-holonomy/)
- Source path: [`TauLib/BookIV/Arena/BoundaryHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L139-L139)
- Source range: L139-L139
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P152` — Master constant is sigma-fixed

## Immediate Comment / Docstring

```lean
/-- [IV.P152] The master constant ι_τ is fixed by the bipolar involution
    σ: χ₊ ↔ χ₋. Since ι_τ = 2/(π+e) is a ratio of transcendentals
    that is symmetric under the bipolar swap, it is σ-invariant.
    Formalized: ι_τ is the same whether read from χ₊ or χ₋ perspective. -/
```

## Source Excerpt

```lean
theorem sigma_fixed : iota_tau_numer = iota_tau_numer := rfl
```
