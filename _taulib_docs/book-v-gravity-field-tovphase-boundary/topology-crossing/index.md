---
{
  "projection_kind": "taulib_declaration",
  "title": "TopologyCrossing",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/topology-crossing/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TOVPhaseBoundary`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVPhaseBoundary::TopologyCrossing",
  "declaration_slug": "topology-crossing",
  "kind": "structure",
  "name": "TopologyCrossing",
  "module_name": "TauLib.BookV.GravityField.TOVPhaseBoundary",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/",
  "source_line_start": 130,
  "source_line_end": 137,
  "registry_ids": [
    "V.D77"
  ],
  "related_registry_items": [
    {
      "id": "V.D77",
      "title": "Topology Crossing Event",
      "url": "/registry/object/V.D77/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L130-L137",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TOVPhaseBoundary",
        "url": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L130-L137",
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

- Module: [TauLib.BookV.GravityField.TOVPhaseBoundary](/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/)
- Source path: [`TauLib/BookV/GravityField/TOVPhaseBoundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L130-L137)
- Source range: L130-L137
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D77` — Topology Crossing Event

## Immediate Comment / Docstring

```lean
/-- [V.D77] Topology crossing event: the moment at which the
    defect bundle topology transitions from S^2 to T^2.

    The crossing is smooth (no singularity) and occurs at
    M = M_n*. The topology of the stable configuration changes
    but the boundary character varies continuously. -/
```

## Source Excerpt

```lean
structure TopologyCrossing where
  /-- The coherence horizon at which crossing occurs. -/
  horizon : CoherenceHorizon
  /-- Whether the crossing is smooth (no singularity). -/
  is_smooth : Bool := true
  /-- Whether boundary character is continuous across crossing. -/
  is_continuous : Bool := true
  deriving Repr
```
