---
{
  "projection_kind": "taulib_declaration",
  "title": "ReconnectionEvent",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/reconnection-event/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauMHD`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauMHD::ReconnectionEvent",
  "declaration_slug": "reconnection-event",
  "kind": "structure",
  "name": "ReconnectionEvent",
  "module_name": "TauLib.BookV.FluidMacro.TauMHD",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/",
  "source_line_start": 214,
  "source_line_end": 221,
  "registry_ids": [
    "V.D110"
  ],
  "related_registry_items": [
    {
      "id": "V.D110",
      "title": "MHD instability condition",
      "url": "/registry/object/V.D110/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L214-L221",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L214-L221",
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
- Source path: [`TauLib/BookV/FluidMacro/TauMHD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L214-L221)
- Source range: L214-L221
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D110` — MHD instability condition

## Immediate Comment / Docstring

```lean
/-- [V.D110] Reconnection event: topological change of magnetic field
    line connectivity.

    Reconnection releases stored magnetic energy and converts it to
    kinetic energy and heating. Occurs in resistive MHD regions. -/
```

## Source Excerpt

```lean
structure ReconnectionEvent where
  /-- Energy released (scaled). -/
  energy_released : Nat
  /-- Whether it is fast reconnection (Sweet-Parker vs Petschek). -/
  is_fast : Bool
  /-- Whether the event changes global topology. -/
  topology_change : Bool := true
  deriving Repr
```
