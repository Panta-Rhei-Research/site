---
{
  "projection_kind": "taulib_declaration",
  "title": "MHDRegime",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/mhdregime/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt2`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt2::MHDRegime",
  "declaration_slug": "mhdregime",
  "kind": "structure",
  "name": "MHDRegime",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/",
  "source_line_start": 139,
  "source_line_end": 148,
  "registry_ids": [
    "IV.D224"
  ],
  "related_registry_items": [
    {
      "id": "IV.D224",
      "title": "MHD regime",
      "url": "/registry/object/IV.D224/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L139-L148",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
        "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L139-L148",
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

- Module: [TauLib.BookIV.ManyBody.DefectFunctionalExt2](/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/)
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L139-L148)
- Source range: L139-L148
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D224` — MHD regime

## Immediate Comment / Docstring

```lean
/-- [IV.D224] The MHD (magnetohydrodynamic) regime: nu >> mu and kappa is
    coupled to the B-sector. The system exhibits frozen-flux behavior
    (Alfven modes) where magnetic field lines move with the fluid.

    EM holonomy is coupled to fluid transport. -/
```

## Source Excerpt

```lean
structure MHDRegime where
  /-- Vorticity dominates mobility. -/
  vorticity_dominant : Bool := true
  /-- B-sector coupled (EM holonomy). -/
  em_coupled : Bool := true
  /-- Frozen-flux behavior. -/
  frozen_flux : Bool := true
  /-- Alfven modes present. -/
  alfven_modes : Bool := true
  deriving Repr
```
