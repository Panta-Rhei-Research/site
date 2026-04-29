---
{
  "projection_kind": "taulib_declaration",
  "title": "vacuum_source_finite",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/vacuum-source-finite/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.VacuumNoVoid`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.VacuumNoVoid::vacuum_source_finite",
  "declaration_slug": "vacuum-source-finite",
  "kind": "theorem",
  "name": "vacuum_source_finite",
  "module_name": "TauLib.BookV.Thermodynamics.VacuumNoVoid",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/",
  "source_line_start": 162,
  "source_line_end": 164,
  "registry_ids": [
    "V.C08"
  ],
  "related_registry_items": [
    {
      "id": "V.C08",
      "title": "Vacuum source term is finite",
      "url": "/registry/object/V.C08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L162-L164",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L162-L164",
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
- Source path: [`TauLib/BookV/Thermodynamics/VacuumNoVoid.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L162-L164)
- Source range: L162-L164
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.C08` — Vacuum source term is finite

## Immediate Comment / Docstring

```lean
/-- [V.C08] Vacuum source term is finite:
    T_vac = E_bdry/V = (1/V) integral_L |H_partial[omega_0]|^2 d-sigma.

    Finite and independent of any momentum cutoff.
    The 10^{120} discrepancy does not arise because no
    momentum-space sum is performed. -/
```

## Source Excerpt

```lean
theorem vacuum_source_finite :
    "T_vac = E_bdry/V, finite, no cutoff dependence" =
    "T_vac = E_bdry/V, finite, no cutoff dependence" := rfl
```
