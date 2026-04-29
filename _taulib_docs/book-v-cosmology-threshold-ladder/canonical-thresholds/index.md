---
{
  "projection_kind": "taulib_declaration",
  "title": "CanonicalThresholds",
  "permalink": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/canonical-thresholds/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.ThresholdLadder`.",
  "declaration_id": "TauLib.BookV.Cosmology.ThresholdLadder::CanonicalThresholds",
  "declaration_slug": "canonical-thresholds",
  "kind": "structure",
  "name": "CanonicalThresholds",
  "module_name": "TauLib.BookV.Cosmology.ThresholdLadder",
  "module_url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/",
  "source_line_start": 103,
  "source_line_end": 122,
  "registry_ids": [
    "V.D159"
  ],
  "related_registry_items": [
    {
      "id": "V.D159",
      "title": "Canonical Thresholds",
      "url": "/registry/object/V.D159/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L103-L122",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L103-L122",
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
- Source path: [`TauLib/BookV/Cosmology/ThresholdLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L103-L122)
- Source range: L103-L122
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D159` — Canonical Thresholds

## Immediate Comment / Docstring

```lean
/-- [V.D159] Canonical thresholds: the six regime transitions in
    monotone order. Depths are ordinal indices (1 = earliest). -/
```

## Source Excerpt

```lean
structure CanonicalThresholds where
  /-- Electroweak. -/
  ew : ThresholdRegimeBoundary
  /-- Baryogenesis. -/
  baryogenesis : ThresholdRegimeBoundary
  /-- Neutron. -/
  neutron : ThresholdRegimeBoundary
  /-- Nucleosynthesis. -/
  nucleosynthesis : ThresholdRegimeBoundary
  /-- Hydrogen recombination. -/
  hydrogen : ThresholdRegimeBoundary
  /-- Photon decoupling. -/
  photon_decoupling : ThresholdRegimeBoundary
  /-- Monotone ordering. -/
  monotone : ew.depth_index < baryogenesis.depth_index ∧
             baryogenesis.depth_index < neutron.depth_index ∧
             neutron.depth_index < nucleosynthesis.depth_index ∧
             nucleosynthesis.depth_index < hydrogen.depth_index ∧
             hydrogen.depth_index < photon_decoupling.depth_index
  deriving Repr
```
