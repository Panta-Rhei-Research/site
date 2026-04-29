---
{
  "projection_kind": "taulib_declaration",
  "title": "CoronalHeatingFlux",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/coronal-heating-flux/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauAlfven`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauAlfven::CoronalHeatingFlux",
  "declaration_slug": "coronal-heating-flux",
  "kind": "structure",
  "name": "CoronalHeatingFlux",
  "module_name": "TauLib.BookV.FluidMacro.TauAlfven",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/",
  "source_line_start": 279,
  "source_line_end": 288,
  "registry_ids": [
    "V.D313"
  ],
  "related_registry_items": [
    {
      "id": "V.D313",
      "title": "Coronal Heating Flux",
      "url": "/registry/object/V.D313/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L279-L288",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.TauAlfven",
        "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L279-L288",
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

- Module: [TauLib.BookV.FluidMacro.TauAlfven](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/)
- Source path: [`TauLib/BookV/FluidMacro/TauAlfven.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L279-L288)
- Source range: L279-L288
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D313` — Coronal Heating Flux

## Immediate Comment / Docstring

```lean
/-- [V.D313] Coronal heating flux from τ-Alfvén damping.

    F_τ = ρ · v_A · v_conv² · (1 - exp(-ι_τ² · L/λ_A))

    For L/λ_A ~ 10: damping fraction ≈ 0.688.
    Predicted F_τ ≈ 2.1 × 10⁵ erg cm⁻² s⁻¹.
    Required: F_req ≈ 3 × 10⁵ erg cm⁻² s⁻¹ (active regions). -/
```

## Source Excerpt

```lean
structure CoronalHeatingFlux where
  /-- Predicted flux × 10⁻⁵ (erg cm⁻² s⁻¹). -/
  flux_x1e5 : Nat := 21
  /-- Required flux × 10⁻⁵. -/
  required_x1e5 : Nat := 30
  /-- Damping fraction × 1000 for L/λ = 10. -/
  damping_frac_x1000 : Nat := 688
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
