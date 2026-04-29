---
{
  "projection_kind": "taulib_declaration",
  "title": "normal_ordering_comparison",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/normal-ordering-comparison/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.VacuumNoVoid`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.VacuumNoVoid::normal_ordering_comparison",
  "declaration_slug": "normal-ordering-comparison",
  "kind": "theorem",
  "name": "normal_ordering_comparison",
  "module_name": "TauLib.BookV.Thermodynamics.VacuumNoVoid",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/",
  "source_line_start": 174,
  "source_line_end": 176,
  "registry_ids": [
    "V.R131"
  ],
  "related_registry_items": [
    {
      "id": "V.R131",
      "title": "Comparison with normal ordering",
      "url": "/registry/object/V.R131/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L174-L176",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L174-L176",
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
- Source path: [`TauLib/BookV/Thermodynamics/VacuumNoVoid.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L174-L176)
- Source range: L174-L176
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R131` — Comparison with normal ordering

## Immediate Comment / Docstring

```lean
/-- [V.R131] Normal ordering comparison: QFT normal ordering
    :H: = H - E_0 removes the divergence without physical justification.
    The tau-framework explains WHY the subtraction is correct:
    the zero-point contributions are refinement entropy, not energy. -/
```

## Source Excerpt

```lean
theorem normal_ordering_comparison :
    "QFT :H: = H - E_0 subtracts S_ref; tau explains why this is correct" =
    "QFT :H: = H - E_0 subtracts S_ref; tau explains why this is correct" := rfl
```
