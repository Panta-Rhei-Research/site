---
{
  "projection_kind": "taulib_declaration",
  "title": "canonical_ladder",
  "permalink": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/canonical-ladder/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.ThresholdLadder`.",
  "declaration_id": "TauLib.BookV.Cosmology.ThresholdLadder::canonical_ladder",
  "declaration_slug": "canonical-ladder",
  "kind": "def",
  "name": "canonical_ladder",
  "module_name": "TauLib.BookV.Cosmology.ThresholdLadder",
  "module_url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/",
  "source_line_start": 125,
  "source_line_end": 138,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L125-L138",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L125-L138",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookV/Cosmology/ThresholdLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L125-L138)
- Source range: L125-L138
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The canonical threshold ladder instance. -/
```

## Source Excerpt

```lean
def canonical_ladder : CanonicalThresholds where
  ew := { kind := .EW, depth_index := 1, depth_pos := by omega,
           sector_name := "omega (B cap C)" }
  baryogenesis := { kind := .Baryogenesis, depth_index := 2,
                    depth_pos := by omega, sector_name := "A (Weak)" }
  neutron := { kind := .Neutron, depth_index := 3, depth_pos := by omega,
               sector_name := "C (Strong)" }
  nucleosynthesis := { kind := .Nucleosynthesis, depth_index := 4,
                       depth_pos := by omega, sector_name := "C (Strong)" }
  hydrogen := { kind := .Hydrogen, depth_index := 5, depth_pos := by omega,
                sector_name := "B (EM)" }
  photon_decoupling := { kind := .PhotonDecoupling, depth_index := 6,
                         depth_pos := by omega, sector_name := "B (EM)" }
  monotone := ⟨by native_decide, by native_decide, by native_decide, by native_decide, by native_decide⟩
```
