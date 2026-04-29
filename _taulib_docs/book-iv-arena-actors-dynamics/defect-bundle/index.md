---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectBundle",
  "permalink": "/verify/taulib/docs/book-iv-arena-actors-dynamics/defect-bundle/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.ActorsDynamics`.",
  "declaration_id": "TauLib.BookIV.Arena.ActorsDynamics::DefectBundle",
  "declaration_slug": "defect-bundle",
  "kind": "structure",
  "name": "DefectBundle",
  "module_name": "TauLib.BookIV.Arena.ActorsDynamics",
  "module_url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/",
  "source_line_start": 47,
  "source_line_end": 54,
  "registry_ids": [
    "IV.D267"
  ],
  "related_registry_items": [
    {
      "id": "IV.D267",
      "title": "Defect bundle (ontic particle)",
      "url": "/registry/object/IV.D267/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L47-L54",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L47-L54",
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
- Source path: [`TauLib/BookIV/Arena/ActorsDynamics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L47-L54)
- Source range: L47-L54
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D267` — Defect bundle (ontic particle)

## Immediate Comment / Docstring

```lean
/-- [IV.D267] A defect bundle (ontic particle): a localized defect in
    the τ³ refinement tower. Carries mass (fiber stiffness), charge
    (sector coupling), and spin (holonomy winding). -/
```

## Source Excerpt

```lean
structure DefectBundle where
  /-- Carrier type: fiber, base, or crossing. -/
  carrier : CarrierType
  /-- Sector affinity. -/
  sector : Tau.BookIII.Sectors.Sector
  /-- Has positive mass (fiber component). -/
  massive : Bool
  deriving Repr
```
