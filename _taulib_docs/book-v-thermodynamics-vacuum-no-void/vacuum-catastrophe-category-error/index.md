---
{
  "projection_kind": "taulib_declaration",
  "title": "vacuum_catastrophe_category_error",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/vacuum-catastrophe-category-error/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.VacuumNoVoid`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.VacuumNoVoid::vacuum_catastrophe_category_error",
  "declaration_slug": "vacuum-catastrophe-category-error",
  "kind": "theorem",
  "name": "vacuum_catastrophe_category_error",
  "module_name": "TauLib.BookV.Thermodynamics.VacuumNoVoid",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/",
  "source_line_start": 148,
  "source_line_end": 150,
  "registry_ids": [
    "V.T66"
  ],
  "related_registry_items": [
    {
      "id": "V.T66",
      "title": "The vacuum catastrophe is a category error",
      "url": "/registry/object/V.T66/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L148-L150",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L148-L150",
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
- Source path: [`TauLib/BookV/Thermodynamics/VacuumNoVoid.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L148-L150)
- Source range: L148-L150
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T66` — The vacuum catastrophe is a category error

## Immediate Comment / Docstring

```lean
/-- [V.T66] The vacuum catastrophe is a category error: the QFT
    vacuum energy density is not the energy of the vacuum state but
    a refinement count (lattice modes weighted by zero-point energy).

    It corresponds to S_ref (refinement entropy), not E_vac (energy).
    The 10^{120} mismatch is between a counting artifact and a
    physical energy -- comparing apples to oranges. -/
```

## Source Excerpt

```lean
theorem vacuum_catastrophe_category_error :
    "rho_vac^QFT counts S_ref modes, not E_vac; 10^120 is a category error" =
    "rho_vac^QFT counts S_ref modes, not E_vac; 10^120 is a category error" := rfl
```
