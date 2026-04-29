---
{
  "projection_kind": "taulib_declaration",
  "title": "no_running_em",
  "permalink": "/verify/taulib/docs/book-iv-physics-thermodynamics/no-running-em/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Physics.Thermodynamics`.",
  "declaration_id": "TauLib.BookIV.Physics.Thermodynamics::no_running_em",
  "declaration_slug": "no-running-em",
  "kind": "def",
  "name": "no_running_em",
  "module_name": "TauLib.BookIV.Physics.Thermodynamics",
  "module_url": "/verify/taulib/docs/book-iv-physics-thermodynamics/",
  "source_line_start": 158,
  "source_line_end": 162,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L158-L162",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L158-L162",
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
- Source path: [`TauLib/BookIV/Physics/Thermodynamics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L158-L162)
- Source range: L158-L162
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- No-Running for EM sector: α_EM is fixed at ι_τ². -/
```

## Source Excerpt

```lean
def no_running_em : NoRunningPrinciple where
  sector := .B
  ontic_coupling_numer := iota_sq_numer
  ontic_coupling_denom := iota_sq_denom
  denom_pos := by simp [iota_sq_denom, iotaD, iota_tau_denom]
```
