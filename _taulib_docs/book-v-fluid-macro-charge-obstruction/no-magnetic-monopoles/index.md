---
{
  "projection_kind": "taulib_declaration",
  "title": "no_magnetic_monopoles",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/no-magnetic-monopoles/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.ChargeObstruction`.",
  "declaration_id": "TauLib.BookV.FluidMacro.ChargeObstruction::no_magnetic_monopoles",
  "declaration_slug": "no-magnetic-monopoles",
  "kind": "theorem",
  "name": "no_magnetic_monopoles",
  "module_name": "TauLib.BookV.FluidMacro.ChargeObstruction",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/",
  "source_line_start": 157,
  "source_line_end": 158,
  "registry_ids": [
    "V.C11"
  ],
  "related_registry_items": [
    {
      "id": "V.C11",
      "title": "No magnetic monopoles",
      "url": "/registry/object/V.C11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L157-L158",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.ChargeObstruction",
        "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L157-L158",
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

- Module: [TauLib.BookV.FluidMacro.ChargeObstruction](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/)
- Source path: [`TauLib/BookV/FluidMacro/ChargeObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L157-L158)
- Source range: L157-L158
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.C11` — No magnetic monopoles

## Immediate Comment / Docstring

```lean
/-- [V.C11] No magnetic monopoles: no τ-admissible configuration
    carries a net magnetic charge.

    ∫_Σ B · dΣ = 0 for every closed surface Σ. The magnetic holonomy
    is trivial by the same boundary structure forcing electric neutrality. -/
```

## Source Excerpt

```lean
theorem no_magnetic_monopoles (m : MagneticCharge) :
    m.value = 0 := m.is_zero
```
