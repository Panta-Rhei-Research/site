---
{
  "projection_kind": "taulib_declaration",
  "title": "QFTVacuumAsRefinement",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/qftvacuum-as-refinement/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.VacuumNoVoid`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.VacuumNoVoid::QFTVacuumAsRefinement",
  "declaration_slug": "qftvacuum-as-refinement",
  "kind": "structure",
  "name": "QFTVacuumAsRefinement",
  "module_name": "TauLib.BookV.Thermodynamics.VacuumNoVoid",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/",
  "source_line_start": 118,
  "source_line_end": 127,
  "registry_ids": [
    "V.P38"
  ],
  "related_registry_items": [
    {
      "id": "V.P38",
      "title": "QFT vacuum = refinement sum",
      "url": "/registry/object/V.P38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L118-L127",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L118-L127",
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

- Module: [TauLib.BookV.Thermodynamics.VacuumNoVoid](/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/)
- Source path: [`TauLib/BookV/Thermodynamics/VacuumNoVoid.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L118-L127)
- Source range: L118-L127
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P38` — QFT vacuum = refinement sum

## Immediate Comment / Docstring

```lean
/-- [V.P38] QFT vacuum = refinement sum: the QFT vacuum energy density
    at cutoff level n corresponds to rho_vac^QFT(n) ~ p^{3n} hbar c / (2 l_ref).

    At the Planck cutoff, this gives the 10^{120} discrepancy.
    The QFT sum counts lattice modes (refinement entropy), not energy. -/
```

## Source Excerpt

```lean
structure QFTVacuumAsRefinement where
  /-- The refinement prime p. -/
  refinement_prime : Nat
  /-- Cutoff level n. -/
  cutoff_level : Nat
  /-- The mode count grows as p^{3n}. -/
  mode_count_scaling : String := "p^(3n)"
  /-- The discrepancy exponent (120 orders of magnitude). -/
  discrepancy_log10 : Nat := 120
  deriving Repr
```
