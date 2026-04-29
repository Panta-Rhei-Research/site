---
{
  "projection_kind": "taulib_declaration",
  "title": "CanonicalGenerator",
  "permalink": "/verify/taulib/docs/book-iv-particles-sector-atlas/canonical-generator/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.SectorAtlas`.",
  "declaration_id": "TauLib.BookIV.Particles.SectorAtlas::CanonicalGenerator",
  "declaration_slug": "canonical-generator",
  "kind": "structure",
  "name": "CanonicalGenerator",
  "module_name": "TauLib.BookIV.Particles.SectorAtlas",
  "module_url": "/verify/taulib/docs/book-iv-particles-sector-atlas/",
  "source_line_start": 128,
  "source_line_end": 135,
  "registry_ids": [
    "IV.D194"
  ],
  "related_registry_items": [
    {
      "id": "IV.D194",
      "title": "9-element canonical generator set",
      "url": "/registry/object/IV.D194/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L128-L135",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.SectorAtlas",
        "url": "/verify/taulib/docs/book-iv-particles-sector-atlas/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L128-L135",
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

- Module: [TauLib.BookIV.Particles.SectorAtlas](/verify/taulib/docs/book-iv-particles-sector-atlas/)
- Source path: [`TauLib/BookIV/Particles/SectorAtlas.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L128-L135)
- Source range: L128-L135
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D194` — 9-element canonical generator set

## Immediate Comment / Docstring

```lean
/-- [IV.D194] A canonical generator of the boundary holonomy algebra.
    The 9 generators come in three groups:
    - 4 sector vacuum idempotents
    - 4 gap quanta (one per sector)
    - 1 crossing generator ι_τ coupling χ₊ and χ₋ -/
```

## Source Excerpt

```lean
structure CanonicalGenerator where
  /-- Generator label. -/
  label : String
  /-- Group classification. -/
  group : GeneratorGroup
  /-- Associated sector (if applicable). -/
  sector : Option Sector
  deriving Repr
```
