---
{
  "projection_kind": "taulib_declaration",
  "title": "vacuum_energy_is_boundary",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/vacuum-energy-is-boundary/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.VacuumNoVoid`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.VacuumNoVoid::vacuum_energy_is_boundary",
  "declaration_slug": "vacuum-energy-is-boundary",
  "kind": "theorem",
  "name": "vacuum_energy_is_boundary",
  "module_name": "TauLib.BookV.Thermodynamics.VacuumNoVoid",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/",
  "source_line_start": 105,
  "source_line_end": 107,
  "registry_ids": [
    "V.T65"
  ],
  "related_registry_items": [
    {
      "id": "V.T65",
      "title": "Vacuum energy is boundary energy",
      "url": "/registry/object/V.T65/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L105-L107",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.VacuumNoVoid",
        "url": "/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L105-L107",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookV.Thermodynamics.VacuumNoVoid](/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/)
- Source path: [`TauLib/BookV/Thermodynamics/VacuumNoVoid.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L105-L107)
- Source range: L105-L107
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T65` — Vacuum energy is boundary energy

## Immediate Comment / Docstring

```lean
/-- [V.T65] Vacuum energy is boundary energy:
    E_vac = E_bdry = integral over L of |H_partial[omega_0]|^2 d-sigma.

    The vacuum energy is a finite integral over the compact
    boundary L = S^1 v S^1. No momentum integral, no UV cutoff,
    no renormalization needed. -/
```

## Source Excerpt

```lean
theorem vacuum_energy_is_boundary :
    "E_vac = E_bdry = integral_L |H_partial[omega_0]|^2 d-sigma, finite" =
    "E_vac = E_bdry = integral_L |H_partial[omega_0]|^2 d-sigma, finite" := rfl
```
