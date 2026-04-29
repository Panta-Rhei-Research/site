---
{
  "projection_kind": "taulib_declaration",
  "title": "alpha_spectral_denom",
  "permalink": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-spectral-denom/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Sectors.FineStructure`.",
  "declaration_id": "TauLib.BookIV.Sectors.FineStructure::alpha_spectral_denom",
  "declaration_slug": "alpha-spectral-denom",
  "kind": "def",
  "name": "alpha_spectral_denom",
  "module_name": "TauLib.BookIV.Sectors.FineStructure",
  "module_url": "/verify/taulib/docs/book-iv-sectors-fine-structure/",
  "source_line_start": 94,
  "source_line_end": 94,
  "registry_ids": [
    "IV.D08"
  ],
  "related_registry_items": [
    {
      "id": "IV.D08",
      "title": "Spectral Fine Structure",
      "url": "/registry/object/IV.D08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L94-L94",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L94-L94",
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

- Module: [TauLib.BookIV.Sectors.FineStructure](/verify/taulib/docs/book-iv-sectors-fine-structure/)
- Source path: [`TauLib/BookIV/Sectors/FineStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L94-L94)
- Source range: L94-L94
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D08` — Spectral Fine Structure

## Immediate Comment / Docstring

```lean
/-- [IV.D08] α_spectral denominator: 15 · (10⁶)⁴ = 15 · 10²⁴. -/
```

## Source Excerpt

```lean
def alpha_spectral_denom : Nat := 15 * iota_fourth_denom
```
