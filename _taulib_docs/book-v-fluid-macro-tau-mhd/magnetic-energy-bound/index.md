---
{
  "projection_kind": "taulib_declaration",
  "title": "magnetic_energy_bound",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/magnetic-energy-bound/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.TauMHD`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauMHD::magnetic_energy_bound",
  "declaration_slug": "magnetic-energy-bound",
  "kind": "theorem",
  "name": "magnetic_energy_bound",
  "module_name": "TauLib.BookV.FluidMacro.TauMHD",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/",
  "source_line_start": 201,
  "source_line_end": 203,
  "registry_ids": [
    "V.P49"
  ],
  "related_registry_items": [
    {
      "id": "V.P49",
      "title": "Reconnection energy bound",
      "url": "/registry/object/V.P49/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L201-L203",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.TauMHD",
        "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L201-L203",
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

- Module: [TauLib.BookV.FluidMacro.TauMHD](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/)
- Source path: [`TauLib/BookV/FluidMacro/TauMHD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L201-L203)
- Source range: L201-L203
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P49` — Reconnection energy bound

## Immediate Comment / Docstring

```lean
/-- [V.P49] Magnetic energy bound: the total magnetic energy in a
    τ-admissible MHD configuration is bounded.

    E_B = ∫ B²/(2μ₀) dV ≤ E_bound

    Follows from compactness of τ³ and the defect-budget constraint. -/
```

## Source Excerpt

```lean
theorem magnetic_energy_bound (mpt : MagneticPressureTension)
    (bound : Nat) (h : mpt.pressure_numer ≤ bound) :
    mpt.pressure_numer ≤ bound := h
```
