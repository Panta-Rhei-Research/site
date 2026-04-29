---
{
  "projection_kind": "taulib_declaration",
  "title": "AlfvenDampingRate",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping-rate/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauAlfven`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauAlfven::AlfvenDampingRate",
  "declaration_slug": "alfven-damping-rate",
  "kind": "structure",
  "name": "AlfvenDampingRate",
  "module_name": "TauLib.BookV.FluidMacro.TauAlfven",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/",
  "source_line_start": 256,
  "source_line_end": 263,
  "registry_ids": [
    "V.D312"
  ],
  "related_registry_items": [
    {
      "id": "V.D312",
      "title": "Alfvén Damping Rate",
      "url": "/registry/object/V.D312/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L256-L263",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L256-L263",
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
- Source path: [`TauLib/BookV/FluidMacro/TauAlfven.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L256-L263)
- Source range: L256-L263
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D312` — Alfvén Damping Rate

## Immediate Comment / Docstring

```lean
/-- [V.D312] Alfvén damping rate from B-sector coupling.

    γ_A = κ(B;2) · ω_A = ι_τ² · v_A k

    The B-sector coupling governs Alfvén wave dissipation.
    Damping length: L_d = v_A / γ_A = 1/(ι_τ² k). -/
```

## Source Excerpt

```lean
structure AlfvenDampingRate where
  /-- ι_τ² × 100000 (≈ 11649). -/
  iota_sq_x100000 : Nat := 11649
  /-- Coupling sector (B = 2). -/
  sector : Nat := 2
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
