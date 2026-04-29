---
{
  "projection_kind": "taulib_declaration",
  "title": "FastReconnectionRate",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/fast-reconnection-rate/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauMHD`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauMHD::FastReconnectionRate",
  "declaration_slug": "fast-reconnection-rate",
  "kind": "structure",
  "name": "FastReconnectionRate",
  "module_name": "TauLib.BookV.FluidMacro.TauMHD",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/",
  "source_line_start": 283,
  "source_line_end": 296,
  "registry_ids": [
    "V.D311"
  ],
  "related_registry_items": [
    {
      "id": "V.D311",
      "title": "Fast Reconnection Rate",
      "url": "/registry/object/V.D311/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L283-L296",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L283-L296",
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

- Module: [TauLib.BookV.FluidMacro.TauMHD](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/)
- Source path: [`TauLib/BookV/FluidMacro/TauMHD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L283-L296)
- Source range: L283-L296
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D311` — Fast Reconnection Rate

## Immediate Comment / Docstring

```lean
/-- [V.D311] Fast reconnection rate from B-sector coupling.

    v_rec = κ(B;2) · v_A = ι_τ² · v_A ≈ 0.117 v_A

    The rate is governed by the B-sector self-coupling κ(B;2) = ι_τ².
    Reconnection is a topological transition in which θ_B changes
    discretely; the rate is set by the sector coupling, not by
    diffusivity. Zero free parameters. -/
```

## Source Excerpt

```lean
structure FastReconnectionRate where
  /-- ι_τ² × 100000 (≈ 11649). -/
  iota_sq_x100000 : Nat := 11649
  /-- v_rec / v_A × 1000 (≈ 117). -/
  rate_x1000 : Nat := 117
  /-- Observed rate × 1000 (≈ 100 ± 30). -/
  observed_x1000 : Nat := 100
  /-- Observed uncertainty × 1000 (±30). -/
  observed_unc_x1000 : Nat := 30
  /-- Free parameters. -/
  free_params : Nat := 0
  /-- Deviation in ppm from central value: +17%. -/
  deviation_pct_x10 : Nat := 170
  deriving Repr
```
