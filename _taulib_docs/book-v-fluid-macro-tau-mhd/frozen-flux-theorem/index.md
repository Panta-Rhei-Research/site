---
{
  "projection_kind": "taulib_declaration",
  "title": "FrozenFluxTheorem",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/frozen-flux-theorem/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauMHD`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauMHD::FrozenFluxTheorem",
  "declaration_slug": "frozen-flux-theorem",
  "kind": "structure",
  "name": "FrozenFluxTheorem",
  "module_name": "TauLib.BookV.FluidMacro.TauMHD",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/",
  "source_line_start": 142,
  "source_line_end": 149,
  "registry_ids": [
    "V.T75"
  ],
  "related_registry_items": [
    {
      "id": "V.T75",
      "title": "Frozen-flux invariant",
      "url": "/registry/object/V.T75/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L142-L149",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L142-L149",
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
- Source path: [`TauLib/BookV/FluidMacro/TauMHD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L142-L149)
- Source range: L142-L149
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T75` — Frozen-flux invariant

## Immediate Comment / Docstring

```lean
/-- [V.T75] Frozen flux theorem: in ideal MHD, the magnetic flux
    through any surface moving with the fluid is constant.

    dΦ_B/dt = 0

    This is the topological preservation of B-sector holonomy by
    the fluid flow. Only holds in ideal MHD (η = 0). -/
```

## Source Excerpt

```lean
structure FrozenFluxTheorem where
  /-- The MHD system. -/
  system : TauMHDSystem
  /-- System is ideal. -/
  is_ideal : system.approx = .Ideal
  /-- Flux is conserved. -/
  flux_conserved : Bool := true
  deriving Repr
```
