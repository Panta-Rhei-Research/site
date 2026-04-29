---
{
  "projection_kind": "taulib_declaration",
  "title": "MHDDynamo",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/mhddynamo/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauMHD`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauMHD::MHDDynamo",
  "declaration_slug": "mhddynamo",
  "kind": "structure",
  "name": "MHDDynamo",
  "module_name": "TauLib.BookV.FluidMacro.TauMHD",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/",
  "source_line_start": 174,
  "source_line_end": 183,
  "registry_ids": [
    "V.D109"
  ],
  "related_registry_items": [
    {
      "id": "V.D109",
      "title": "tau-reconnection event",
      "url": "/registry/object/V.D109/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L174-L183",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L174-L183",
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
- Source path: [`TauLib/BookV/FluidMacro/TauMHD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L174-L183)
- Source range: L174-L183
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D109` — tau-reconnection event

## Immediate Comment / Docstring

```lean
/-- [V.D109] MHD dynamo: self-sustained magnetic field generation by
    fluid motions.

    Requires: breaking axial symmetry (Cowling's theorem) and
    Re_m >> 1 (magnetic Reynolds number much larger than 1). -/
```

## Source Excerpt

```lean
structure MHDDynamo where
  /-- Dynamo type. -/
  dynamo_type : DynamoType
  /-- Magnetic Reynolds number is large (Re_m > critical). -/
  rem_large : Bool := true
  /-- Axial symmetry is broken. -/
  symmetry_broken : Bool := true
  /-- Whether the dynamo is self-sustaining. -/
  is_self_sustaining : Bool := true
  deriving Repr
```
