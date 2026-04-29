---
{
  "projection_kind": "taulib_declaration",
  "title": "ReconnectionRate",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/reconnection-rate/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauMHD`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauMHD::ReconnectionRate",
  "declaration_slug": "reconnection-rate",
  "kind": "structure",
  "name": "ReconnectionRate",
  "module_name": "TauLib.BookV.FluidMacro.TauMHD",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/",
  "source_line_start": 235,
  "source_line_end": 240,
  "registry_ids": [
    "V.P50"
  ],
  "related_registry_items": [
    {
      "id": "V.P50",
      "title": "Alfv'en wave dispersion",
      "url": "/registry/object/V.P50/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L235-L240",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L235-L240",
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
- Source path: [`TauLib/BookV/FluidMacro/TauMHD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L235-L240)
- Source range: L235-L240
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P50` — Alfv'en wave dispersion

## Immediate Comment / Docstring

```lean
/-- [V.P50] Reconnection rate: the rate of magnetic flux destruction
    at the reconnection site.

    Sweet-Parker: v_in/v_A ~ Re_m^{-1/2} (slow)
    Petschek: v_in/v_A ~ 1/(ln Re_m) (fast)

    In the τ-framework, reconnection is the controlled destruction
    of B-sector holonomy in a resistive layer. -/
```

## Source Excerpt

```lean
structure ReconnectionRate where
  /-- Alfven Mach number of inflow (scaled by 1000). -/
  mach_inflow_scaled : Nat
  /-- Whether this is fast (Petschek) or slow (Sweet-Parker). -/
  is_fast : Bool
  deriving Repr
```
