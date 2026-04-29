---
{
  "projection_kind": "taulib_declaration",
  "title": "PulsarData",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-compact-objects/pulsar-data/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.CompactObjects`.",
  "declaration_id": "TauLib.BookV.Astrophysics.CompactObjects::PulsarData",
  "declaration_slug": "pulsar-data",
  "kind": "structure",
  "name": "PulsarData",
  "module_name": "TauLib.BookV.Astrophysics.CompactObjects",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/",
  "source_line_start": 166,
  "source_line_end": 179,
  "registry_ids": [
    "V.D125"
  ],
  "related_registry_items": [
    {
      "id": "V.D125",
      "title": "Black Hole as Maximal Topological Defect --- V.D58",
      "url": "/registry/object/V.D125/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L166-L179",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.CompactObjects",
        "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L166-L179",
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

- Module: [TauLib.BookV.Astrophysics.CompactObjects](/verify/taulib/docs/book-v-astrophysics-compact-objects/)
- Source path: [`TauLib/BookV/Astrophysics/CompactObjects.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L166-L179)
- Source range: L166-L179
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D125` — Black Hole as Maximal Topological Defect --- V.D58

## Immediate Comment / Docstring

```lean
/-- [V.D125] Pulsar data: a rotating neutron star emitting beamed
    radiation from its magnetic poles.

    The timing stability of millisecond pulsars (Δt/t ~ 10⁻²¹)
    makes them the most precise gravitational clocks. -/
```

## Source Excerpt

```lean
structure PulsarData where
  /-- Underlying compact object. -/
  star : CompactObjectData
  /-- Pulsar type. -/
  pulsar_type : PulsarType
  /-- Period (scaled, microseconds). -/
  period_microseconds : Nat
  /-- Period positive. -/
  period_pos : period_microseconds > 0
  /-- Period derivative (dimensionless, scaled × 10^20). -/
  period_dot_scaled : Nat
  /-- Must be a neutron star. -/
  is_ns : star.obj_type = .NeutronStar
  deriving Repr
```
