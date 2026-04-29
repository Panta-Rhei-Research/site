---
{
  "projection_kind": "taulib_declaration",
  "title": "OrbitStepsVsTime",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-inversion/orbit-steps-vs-time/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.Inversion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.Inversion::OrbitStepsVsTime",
  "declaration_slug": "orbit-steps-vs-time",
  "kind": "structure",
  "name": "OrbitStepsVsTime",
  "module_name": "TauLib.BookV.Thermodynamics.Inversion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-inversion/",
  "source_line_start": 269,
  "source_line_end": 274,
  "registry_ids": [
    "V.R118"
  ],
  "related_registry_items": [
    {
      "id": "V.R118",
      "title": "Orbit steps versus physical time",
      "url": "/registry/object/V.R118/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L269-L274",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.Inversion",
        "url": "/verify/taulib/docs/book-v-thermodynamics-inversion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L269-L274",
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

- Module: [TauLib.BookV.Thermodynamics.Inversion](/verify/taulib/docs/book-v-thermodynamics-inversion/)
- Source path: [`TauLib/BookV/Thermodynamics/Inversion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L269-L274)
- Source range: L269-L274
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.R118` — Orbit steps versus physical time

## Immediate Comment / Docstring

```lean
/-- [V.R118] Orbit steps versus physical time.

    n_coh ~ 661 is in orbit steps, not physical time.
    One orbit step may span Planck-scale or cosmological durations.
    The finiteness of n_coh is regime-independent; the physical
    duration is calibration-dependent. -/
```

## Source Excerpt

```lean
structure OrbitStepsVsTime where
  /-- Orbit-step bound. -/
  orbit_bound : Nat
  /-- Whether the mapping to physical time is calibration-dependent. -/
  calibration_dependent : Bool := true
  deriving Repr
```
