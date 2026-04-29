---
{
  "projection_kind": "taulib_declaration",
  "title": "silent_modes_are_gravity_plus_Z0",
  "permalink": "/verify/taulib/docs/book-iv-sectors-mode-census/silent-modes-are-gravity-plus-z0/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Sectors.ModeCensus`.",
  "declaration_id": "TauLib.BookIV.Sectors.ModeCensus::silent_modes_are_gravity_plus_Z0",
  "declaration_slug": "silent-modes-are-gravity-plus-z0",
  "kind": "theorem",
  "name": "silent_modes_are_gravity_plus_Z0",
  "module_name": "TauLib.BookIV.Sectors.ModeCensus",
  "module_url": "/verify/taulib/docs/book-iv-sectors-mode-census/",
  "source_line_start": 132,
  "source_line_end": 137,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/ModeCensus.lean#L132-L137",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.ModeCensus",
        "url": "/verify/taulib/docs/book-iv-sectors-mode-census/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/ModeCensus.lean#L132-L137",
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

- Module: [TauLib.BookIV.Sectors.ModeCensus](/verify/taulib/docs/book-iv-sectors-mode-census/)
- Source path: [`TauLib/BookIV/Sectors/ModeCensus.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/ModeCensus.lean#L132-L137)
- Source range: L132-L137
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The 4 silent modes are exactly: α×3 configs + π×crossing. -/
```

## Source Excerpt

```lean
theorem silent_modes_are_gravity_plus_Z0 :
    (⟨.alpha, .lobePos⟩ : BoundaryMode).emActive = false ∧
    (⟨.alpha, .lobeNeg⟩ : BoundaryMode).emActive = false ∧
    (⟨.alpha, .crossing⟩ : BoundaryMode).emActive = false ∧
    (⟨.pi_, .crossing⟩ : BoundaryMode).emActive = false := by
  exact ⟨rfl, rfl, rfl, rfl⟩
```
