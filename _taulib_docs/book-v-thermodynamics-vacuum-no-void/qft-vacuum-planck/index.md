---
{
  "projection_kind": "taulib_declaration",
  "title": "qft_vacuum_planck",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/qft-vacuum-planck/",
  "summary_short": "`def` declaration in `TauLib.BookV.Thermodynamics.VacuumNoVoid`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.VacuumNoVoid::qft_vacuum_planck",
  "declaration_slug": "qft-vacuum-planck",
  "kind": "def",
  "name": "qft_vacuum_planck",
  "module_name": "TauLib.BookV.Thermodynamics.VacuumNoVoid",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/",
  "source_line_start": 130,
  "source_line_end": 132,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L130-L132",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L130-L132",
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

- Module: [TauLib.BookV.Thermodynamics.VacuumNoVoid](/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/)
- Source path: [`TauLib/BookV/Thermodynamics/VacuumNoVoid.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L130-L132)
- Source range: L130-L132
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The discrepancy is 120 orders of magnitude. -/
```

## Source Excerpt

```lean
def qft_vacuum_planck : QFTVacuumAsRefinement where
  refinement_prime := 2
  cutoff_level := 0
```
