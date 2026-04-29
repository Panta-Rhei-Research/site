---
{
  "projection_kind": "taulib_declaration",
  "title": "CylinderDomain",
  "permalink": "/verify/taulib/docs/book-ii-domains-cylinders/cylinder-domain/",
  "summary_short": "`inductive` declaration in `TauLib.BookII.Domains.Cylinders`.",
  "declaration_id": "TauLib.BookII.Domains.Cylinders::CylinderDomain",
  "declaration_slug": "cylinder-domain",
  "kind": "inductive",
  "name": "CylinderDomain",
  "module_name": "TauLib.BookII.Domains.Cylinders",
  "module_url": "/verify/taulib/docs/book-ii-domains-cylinders/",
  "source_line_start": 54,
  "source_line_end": 58,
  "registry_ids": [
    "II.D10"
  ],
  "related_registry_items": [
    {
      "id": "II.D10",
      "title": "Stage-k Cylinder",
      "url": "/registry/object/II.D10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean#L54-L58",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Domains.Cylinders",
        "url": "/verify/taulib/docs/book-ii-domains-cylinders/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean#L54-L58",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookII.Domains.Cylinders](/verify/taulib/docs/book-ii-domains-cylinders/)
- Source path: [`TauLib/BookII/Domains/Cylinders.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean#L54-L58)
- Source range: L54-L58
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `II.D10` — Stage-k Cylinder

## Immediate Comment / Docstring

```lean
/-- [II.D10] Cylinder domain: finite Boolean combination of cylinders. -/
```

## Source Excerpt

```lean
inductive CylinderDomain where
  | basic : TauIdx → TauIdx → CylinderDomain
  | inter : CylinderDomain → CylinderDomain → CylinderDomain
  | union : CylinderDomain → CylinderDomain → CylinderDomain
  | compl : CylinderDomain → CylinderDomain
```
