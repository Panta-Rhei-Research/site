---
{
  "projection_kind": "taulib_declaration",
  "title": "alpha_tower_inverse_tight",
  "permalink": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-tower-inverse-tight/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Sectors.FineStructure`.",
  "declaration_id": "TauLib.BookIV.Sectors.FineStructure::alpha_tower_inverse_tight",
  "declaration_slug": "alpha-tower-inverse-tight",
  "kind": "theorem",
  "name": "alpha_tower_inverse_tight",
  "module_name": "TauLib.BookIV.Sectors.FineStructure",
  "module_url": "/verify/taulib/docs/book-iv-sectors-fine-structure/",
  "source_line_start": 233,
  "source_line_end": 238,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L233-L238",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L233-L238",
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
- Source path: [`TauLib/BookIV/Sectors/FineStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L233-L238)
- Source range: L233-L238
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- 1/α_tower is between 137.0 and 137.1 (much tighter than spectral 135-139).
    Cross-multiplied: 1370 · numer < 10 · denom < 1371 · numer. -/
```

## Source Excerpt

```lean
theorem alpha_tower_inverse_tight :
    1370 * alpha_tower_numer < 10 * alpha_tower_denom ∧
    10 * alpha_tower_denom < 1371 * alpha_tower_numer := by
  simp [alpha_tower_numer, alpha_tower_denom,
        iota_fourth_numer, iota_fourth_denom,
        iota, iotaD, iota_tau_numer, iota_tau_denom]
```
