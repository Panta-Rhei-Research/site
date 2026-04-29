---
{
  "projection_kind": "taulib_declaration",
  "title": "CoreCollapseMechanism",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-supernovae/core-collapse-mechanism/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.Supernovae`.",
  "declaration_id": "TauLib.BookV.Astrophysics.Supernovae::CoreCollapseMechanism",
  "declaration_slug": "core-collapse-mechanism",
  "kind": "structure",
  "name": "CoreCollapseMechanism",
  "module_name": "TauLib.BookV.Astrophysics.Supernovae",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-supernovae/",
  "source_line_start": 129,
  "source_line_end": 142,
  "registry_ids": [
    "V.D127"
  ],
  "related_registry_items": [
    {
      "id": "V.D127",
      "title": "Channel Reversal --- V.D60",
      "url": "/registry/object/V.D127/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L129-L142",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.Supernovae",
        "url": "/verify/taulib/docs/book-v-astrophysics-supernovae/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L129-L142",
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

- Module: [TauLib.BookV.Astrophysics.Supernovae](/verify/taulib/docs/book-v-astrophysics-supernovae/)
- Source path: [`TauLib/BookV/Astrophysics/Supernovae.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L129-L142)
- Source range: L129-L142
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D127` — Channel Reversal --- V.D60

## Immediate Comment / Docstring

```lean
/-- [V.D127] Core collapse mechanism: the sequence of events in a
    core-collapse supernova, modeled as a defect cascade in the
    τ-framework. -/
```

## Source Excerpt

```lean
structure CoreCollapseMechanism where
  /-- Progenitor mass (tenths of solar mass). -/
  progenitor_mass : Nat
  /-- Progenitor is massive enough (> 8 M_☉). -/
  massive_enough : progenitor_mass > 80
  /-- Iron core mass at collapse (tenths of solar mass). -/
  core_mass : Nat
  /-- Core exceeds Chandrasekhar. -/
  exceeds_chandrasekhar : core_mass ≥ chandrasekhar_mass_limit
  /-- Remnant type. -/
  remnant : CompactObjectType
  /-- Energy released (10⁵¹ erg, scaled × 10). -/
  energy_released : Nat
  deriving Repr
```
