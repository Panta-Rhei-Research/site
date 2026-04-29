---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_alfven_damping_rate",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/tau-alfven-damping-rate/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.TauAlfven`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauAlfven::tau_alfven_damping_rate",
  "declaration_slug": "tau-alfven-damping-rate",
  "kind": "theorem",
  "name": "tau_alfven_damping_rate",
  "module_name": "TauLib.BookV.FluidMacro.TauAlfven",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/",
  "source_line_start": 303,
  "source_line_end": 306,
  "registry_ids": [
    "V.T253"
  ],
  "related_registry_items": [
    {
      "id": "V.T253",
      "title": "τ-Alfvén Damping = ι_τ² ω",
      "url": "/registry/object/V.T253/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L303-L306",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L303-L306",
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

- Module: [TauLib.BookV.FluidMacro.TauAlfven](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/)
- Source path: [`TauLib/BookV/FluidMacro/TauAlfven.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L303-L306)
- Source range: L303-L306
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T253` — τ-Alfvén Damping = ι_τ² ω

## Immediate Comment / Docstring

```lean
/-- [V.T253] τ-Alfvén damping rate is ι_τ² · ω_A.

    The Alfvén damping rate is controlled by the B-sector coupling
    κ(B;2) = ι_τ². As waves propagate along the base τ¹, the T²
    fiber introduces dissipation proportional to ι_τ².
    Zero free parameters. -/
```

## Source Excerpt

```lean
theorem tau_alfven_damping_rate :
    alfven_damping_rate_tau.free_params = 0 ∧
    alfven_damping_rate_tau.sector = 2 := by
  exact ⟨by native_decide, by native_decide⟩
```
