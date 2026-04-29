---
{
  "projection_kind": "taulib_declaration",
  "title": "no_running_gravity",
  "permalink": "/verify/taulib/docs/book-iv-physics-thermodynamics/no-running-gravity/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Physics.Thermodynamics`.",
  "declaration_id": "TauLib.BookIV.Physics.Thermodynamics::no_running_gravity",
  "declaration_slug": "no-running-gravity",
  "kind": "def",
  "name": "no_running_gravity",
  "module_name": "TauLib.BookIV.Physics.Thermodynamics",
  "module_url": "/verify/taulib/docs/book-iv-physics-thermodynamics/",
  "source_line_start": 179,
  "source_line_end": 183,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L179-L183",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.Thermodynamics",
        "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L179-L183",
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

- Module: [TauLib.BookIV.Physics.Thermodynamics](/verify/taulib/docs/book-iv-physics-thermodynamics/)
- Source path: [`TauLib/BookIV/Physics/Thermodynamics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L179-L183)
- Source range: L179-L183
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- No-Running for Gravity sector: κ_GR is fixed at 1−ι_τ. -/
```

## Source Excerpt

```lean
def no_running_gravity : NoRunningPrinciple where
  sector := .D
  ontic_coupling_numer := iotaD - iota
  ontic_coupling_denom := iotaD
  denom_pos := by simp [iotaD, iota_tau_denom]
```
