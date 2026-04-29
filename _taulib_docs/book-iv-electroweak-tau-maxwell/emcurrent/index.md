---
{
  "projection_kind": "taulib_declaration",
  "title": "EMCurrent",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/emcurrent/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauMaxwell`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauMaxwell::EMCurrent",
  "declaration_slug": "emcurrent",
  "kind": "structure",
  "name": "EMCurrent",
  "module_name": "TauLib.BookIV.Electroweak.TauMaxwell",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/",
  "source_line_start": 194,
  "source_line_end": 203,
  "registry_ids": [
    "IV.D103"
  ],
  "related_registry_items": [
    {
      "id": "IV.D103",
      "title": "Electromagnetic Current 4-Vector",
      "url": "/registry/object/IV.D103/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L194-L203",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauMaxwell",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L194-L203",
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

- Module: [TauLib.BookIV.Electroweak.TauMaxwell](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/)
- Source path: [`TauLib/BookIV/Electroweak/TauMaxwell.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L194-L203)
- Source range: L194-L203
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D103` — Electromagnetic Current 4-Vector

## Immediate Comment / Docstring

```lean
/-- [IV.D103] EM current 4-vector J^μ = (ρ, J).
    ρ = charge density (winding numbers per volume),
    J = current density (transport of charged defects). -/
```

## Source Excerpt

```lean
structure EMCurrent where
  /-- Spacetime components. -/
  components : Nat
  comp_eq : components = 4
  /-- Charge density (time component). -/
  has_charge_density : Bool := true
  /-- Spatial current density (3 spatial components). -/
  spatial_components : Nat
  spatial_eq : spatial_components = 3
  deriving Repr
```
