---
{
  "projection_kind": "taulib_declaration",
  "title": "MassFiberStiffness",
  "permalink": "/verify/taulib/docs/book-iv-arena-actors-dynamics/mass-fiber-stiffness/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.ActorsDynamics`.",
  "declaration_id": "TauLib.BookIV.Arena.ActorsDynamics::MassFiberStiffness",
  "declaration_slug": "mass-fiber-stiffness",
  "kind": "structure",
  "name": "MassFiberStiffness",
  "module_name": "TauLib.BookIV.Arena.ActorsDynamics",
  "module_url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/",
  "source_line_start": 130,
  "source_line_end": 136,
  "registry_ids": [
    "IV.D271"
  ],
  "related_registry_items": [
    {
      "id": "IV.D271",
      "title": "Mass as fiber stiffness",
      "url": "/registry/object/IV.D271/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L130-L136",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.ActorsDynamics",
        "url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L130-L136",
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

- Module: [TauLib.BookIV.Arena.ActorsDynamics](/verify/taulib/docs/book-iv-arena-actors-dynamics/)
- Source path: [`TauLib/BookIV/Arena/ActorsDynamics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L130-L136)
- Source range: L130-L136
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D271` — Mass as fiber stiffness

## Immediate Comment / Docstring

```lean
/-- [IV.D271] Mass as fiber stiffness: mass = resistance of fiber T²
    to deformation. Massless modes (radiation) have zero fiber component.
    Massive modes (defect bundles) have positive fiber stiffness. -/
```

## Source Excerpt

```lean
structure MassFiberStiffness where
  /-- Carrier type determines mass. -/
  carrier : CarrierType
  /-- Fiber or crossing → massive; base → massless. -/
  is_massive : Bool
  mass_rule : is_massive = (carrier != .Base)
  deriving Repr
```
