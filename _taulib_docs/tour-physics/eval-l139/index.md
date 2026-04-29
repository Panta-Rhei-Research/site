---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L139",
  "permalink": "/verify/taulib/docs/tour-physics/eval-l139/",
  "summary_short": "`eval` declaration in `TauLib.Tour.Physics`.",
  "declaration_id": "TauLib.Tour.Physics::#eval:139",
  "declaration_slug": "eval-l139",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.Physics",
  "module_url": "/verify/taulib/docs/tour-physics/",
  "source_line_start": 139,
  "source_line_end": 150,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Physics.lean#L139-L150",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.Tour.Physics",
        "url": "/verify/taulib/docs/tour-physics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Physics.lean#L139-L150",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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

- Module: [TauLib.Tour.Physics](/verify/taulib/docs/tour-physics/)
- Source path: [`TauLib/Tour/Physics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Physics.lean#L139-L150)
- Source range: L139-L150
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- No axion needed. No Peccei-Quinn symmetry. No new fields.
-- Prediction: ADMX and CASPEr should find null results.
```

## Source Excerpt

```lean
#eval no_axion_required             -- "SA-i is the τ-native Peccei-Quinn mechanism: ..."

-- ================================================================
-- PART 5: CMB FIRST PEAK (Book V, Chapter 45)
-- ================================================================

-- The CMB first acoustic peak at ℓ₁ ≈ 220 is derived from
-- the holonomy matter fraction ω_m/ω_b = 1 + κ_D/κ_B ≈ 6.655.
-- No dark matter particles — boundary holonomy mass gravitates
-- like CDM but is topological in origin.

#check first_peak_holonomy_thm     -- free_params = 0 ∧ deviation_ppm = 2840 ∧ ...
```
