---
{
  "projection_kind": "taulib_declaration",
  "title": "ThresholdRegimeBoundary",
  "permalink": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/threshold-regime-boundary/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.ThresholdLadder`.",
  "declaration_id": "TauLib.BookV.Cosmology.ThresholdLadder::ThresholdRegimeBoundary",
  "declaration_slug": "threshold-regime-boundary",
  "kind": "structure",
  "name": "ThresholdRegimeBoundary",
  "module_name": "TauLib.BookV.Cosmology.ThresholdLadder",
  "module_url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/",
  "source_line_start": 84,
  "source_line_end": 95,
  "registry_ids": [
    "V.D158"
  ],
  "related_registry_items": [
    {
      "id": "V.D158",
      "title": "Threshold (Regime Boundary)",
      "url": "/registry/object/V.D158/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L84-L95",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.ThresholdLadder",
        "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L84-L95",
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

- Module: [TauLib.BookV.Cosmology.ThresholdLadder](/verify/taulib/docs/book-v-cosmology-threshold-ladder/)
- Source path: [`TauLib/BookV/Cosmology/ThresholdLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L84-L95)
- Source range: L84-L95
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D158` — Threshold (Regime Boundary)

## Immediate Comment / Docstring

```lean
/-- [V.D158] Threshold (regime boundary): a critical depth where a
    qualitative change occurs in the regime boundary character.

    At threshold n_*, one or more sector couplings cross a critical
    value, causing a regime transition. -/
```

## Source Excerpt

```lean
structure ThresholdRegimeBoundary where
  /-- Threshold type. -/
  kind : ThresholdType
  /-- Refinement depth at threshold (ordinal index). -/
  depth_index : Nat
  /-- Depth is positive. -/
  depth_pos : depth_index > 0
  /-- Which sector crosses. -/
  sector_name : String
  /-- Scope. -/
  scope : String := "tau-effective"
  deriving Repr
```
