---
{
  "projection_kind": "taulib_declaration",
  "title": "DomainWall",
  "permalink": "/verify/taulib/docs/book-iv-many-body-magnetism/domain-wall/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.Magnetism`.",
  "declaration_id": "TauLib.BookIV.ManyBody.Magnetism::DomainWall",
  "declaration_slug": "domain-wall",
  "kind": "structure",
  "name": "DomainWall",
  "module_name": "TauLib.BookIV.ManyBody.Magnetism",
  "module_url": "/verify/taulib/docs/book-iv-many-body-magnetism/",
  "source_line_start": 162,
  "source_line_end": 171,
  "registry_ids": [
    "IV.D389"
  ],
  "related_registry_items": [
    {
      "id": "IV.D389",
      "title": "Magnetic Domain Wall on T²",
      "url": "/registry/object/IV.D389/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L162-L171",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.Magnetism",
        "url": "/verify/taulib/docs/book-iv-many-body-magnetism/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L162-L171",
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

- Module: [TauLib.BookIV.ManyBody.Magnetism](/verify/taulib/docs/book-iv-many-body-magnetism/)
- Source path: [`TauLib/BookIV/ManyBody/Magnetism.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L162-L171)
- Source range: L162-L171
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D389` — Magnetic Domain Wall on T²

## Immediate Comment / Docstring

```lean
/-- [IV.D389] Magnetic domain wall: codimension-1 defect in the spin-alignment
    field on T². Curve γ ⊂ T² across which spin orientation changes
    discontinuously (Bloch wall) or rotates (Néel wall). In defect-tuple
    language, a locus where d₄ has winding discontinuity. -/
```

## Source Excerpt

```lean
structure DomainWall where
  /-- Codimension-1 defect. -/
  codimension : Nat := 1
  /-- Bloch wall: discontinuous normal. -/
  bloch_type : Bool := true
  /-- Néel wall: rotation in wall plane. -/
  neel_type : Bool := true
  /-- d₄ winding discontinuity. -/
  d4_discontinuity : Bool := true
  deriving Repr
```
