---
{
  "projection_kind": "taulib_declaration",
  "title": "CoronalFluxConsistency",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/coronal-flux-consistency/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauAlfven`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauAlfven::CoronalFluxConsistency",
  "declaration_slug": "coronal-flux-consistency",
  "kind": "structure",
  "name": "CoronalFluxConsistency",
  "module_name": "TauLib.BookV.FluidMacro.TauAlfven",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/",
  "source_line_start": 319,
  "source_line_end": 324,
  "registry_ids": [
    "V.P173"
  ],
  "related_registry_items": [
    {
      "id": "V.P173",
      "title": "Coronal Flux Consistency",
      "url": "/registry/object/V.P173/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L319-L324",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L319-L324",
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
- Source path: [`TauLib/BookV/FluidMacro/TauAlfven.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L319-L324)
- Source range: L319-L324
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P173` — Coronal Flux Consistency

## Immediate Comment / Docstring

```lean
/-- [V.P173] Coronal flux consistency.

    Prediction: F_τ ≈ 2.1 × 10⁵ erg cm⁻² s⁻¹.
    Required: ≈ 3 × 10⁵ (active regions).
    Ratio: F_τ/F_req ≈ 0.7 (within factor 1.5).
    Consistent given order-of-magnitude uncertainties in
    photospheric parameters (ρ, v_A, v_conv). -/
```

## Source Excerpt

```lean
structure CoronalFluxConsistency where
  /-- Predicted / required ratio × 100. -/
  ratio_x100 : Nat := 70
  /-- Within factor 2. -/
  within_factor_2 : ratio_x100 ≥ 50 := by omega
  deriving Repr
```
