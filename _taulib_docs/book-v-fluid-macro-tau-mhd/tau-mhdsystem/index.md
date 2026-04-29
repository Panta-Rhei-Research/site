---
{
  "projection_kind": "taulib_declaration",
  "title": "TauMHDSystem",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/tau-mhdsystem/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauMHD`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauMHD::TauMHDSystem",
  "declaration_slug": "tau-mhdsystem",
  "kind": "structure",
  "name": "TauMHDSystem",
  "module_name": "TauLib.BookV.FluidMacro.TauMHD",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/",
  "source_line_start": 85,
  "source_line_end": 98,
  "registry_ids": [
    "V.D107"
  ],
  "related_registry_items": [
    {
      "id": "V.D107",
      "title": "tau-MHD system",
      "url": "/registry/object/V.D107/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L85-L98",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L85-L98",
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
- Source path: [`TauLib/BookV/FluidMacro/TauMHD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L85-L98)
- Source range: L85-L98
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D107` — tau-MHD system

## Immediate Comment / Docstring

```lean
/-- [V.D107] τ-MHD system: macro defect-transport coupled to the
    B-sector holonomy constraint.

    The conducting fluid carries magnetic flux; the approximation type
    determines whether flux is frozen (ideal) or diffuses (resistive). -/
```

## Source Excerpt

```lean
structure TauMHDSystem where
  /-- Underlying plasma state. -/
  plasma : TauPlasmaState
  /-- MHD approximation. -/
  approx : MHDApprox
  /-- Magnetic Reynolds number (Re_m, scaled). -/
  mag_reynolds_numer : Nat
  /-- Magnetic Reynolds denominator. -/
  mag_reynolds_denom : Nat
  /-- Denominator positive. -/
  mag_reynolds_denom_pos : mag_reynolds_denom > 0
  /-- Whether the system is in the MHD limit. -/
  in_mhd_limit : Bool := true
  deriving Repr
```
