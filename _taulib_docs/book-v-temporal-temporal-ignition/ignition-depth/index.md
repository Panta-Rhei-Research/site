---
{
  "projection_kind": "taulib_declaration",
  "title": "IgnitionDepth",
  "permalink": "/verify/taulib/docs/book-v-temporal-temporal-ignition/ignition-depth/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.TemporalIgnition`.",
  "declaration_id": "TauLib.BookV.Temporal.TemporalIgnition::IgnitionDepth",
  "declaration_slug": "ignition-depth",
  "kind": "structure",
  "name": "IgnitionDepth",
  "module_name": "TauLib.BookV.Temporal.TemporalIgnition",
  "module_url": "/verify/taulib/docs/book-v-temporal-temporal-ignition/",
  "source_line_start": 90,
  "source_line_end": 99,
  "registry_ids": [
    "V.D21"
  ],
  "related_registry_items": [
    {
      "id": "V.D21",
      "title": "Ignition Depth",
      "url": "/registry/object/V.D21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L90-L99",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.TemporalIgnition",
        "url": "/verify/taulib/docs/book-v-temporal-temporal-ignition/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L90-L99",
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

- Module: [TauLib.BookV.Temporal.TemporalIgnition](/verify/taulib/docs/book-v-temporal-temporal-ignition/)
- Source path: [`TauLib/BookV/Temporal/TemporalIgnition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L90-L99)
- Source range: L90-L99
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D21` — Ignition Depth

## Immediate Comment / Docstring

```lean
/-- [V.D21] Ignition depth: the smallest depth n_ign at which all 5
    sector spectral labels are present in the boundary holonomy algebra.

    Below n_ign, not all sectors are differentiated: the boundary
    holonomy algebra lacks full sector structure. -/
```

## Source Excerpt

```lean
structure IgnitionDepth where
  /-- The ignition depth n_ign. -/
  n_ign : Nat
  /-- Ignition depth is positive (some pre-temporal epochs exist). -/
  n_ign_pos : n_ign > 0
  /-- Number of sectors activated at n_ign (must be 5). -/
  sectors_at_ignition : Nat
  /-- All 5 sectors present at ignition. -/
  full_spectrum : sectors_at_ignition = 5
  deriving Repr
```
