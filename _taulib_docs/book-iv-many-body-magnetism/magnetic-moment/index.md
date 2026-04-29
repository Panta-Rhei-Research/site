---
{
  "projection_kind": "taulib_declaration",
  "title": "MagneticMoment",
  "permalink": "/verify/taulib/docs/book-iv-many-body-magnetism/magnetic-moment/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.Magnetism`.",
  "declaration_id": "TauLib.BookIV.ManyBody.Magnetism::MagneticMoment",
  "declaration_slug": "magnetic-moment",
  "kind": "structure",
  "name": "MagneticMoment",
  "module_name": "TauLib.BookIV.ManyBody.Magnetism",
  "module_url": "/verify/taulib/docs/book-iv-many-body-magnetism/",
  "source_line_start": 54,
  "source_line_end": 61,
  "registry_ids": [
    "IV.D387"
  ],
  "related_registry_items": [
    {
      "id": "IV.D387",
      "title": "Magnetic Moment on T²",
      "url": "/registry/object/IV.D387/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L54-L61",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L54-L61",
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
- Source path: [`TauLib/BookIV/ManyBody/Magnetism.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L54-L61)
- Source range: L54-L61
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D387` — Magnetic Moment on T²

## Immediate Comment / Docstring

```lean
/-- [IV.D387] Magnetic moment of a defect bundle with spin quantum number s
    on T². The magnetization M is the average magnetic moment per unit volume
    over the statistical ensemble. -/
```

## Source Excerpt

```lean
structure MagneticMoment where
  /-- Magnetic moment proportional to spin. -/
  moment_from_spin : Bool := true
  /-- Magnetization is collective property. -/
  magnetization_collective : Bool := true
  /-- d₄ component governs alignment pattern. -/
  d4_governs_alignment : Bool := true
  deriving Repr
```
