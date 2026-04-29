---
{
  "projection_kind": "taulib_declaration",
  "title": "leray_limit_recovery",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/leray-limit-recovery/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.NavierStokesMacro`.",
  "declaration_id": "TauLib.BookV.FluidMacro.NavierStokesMacro::leray_limit_recovery",
  "declaration_slug": "leray-limit-recovery",
  "kind": "theorem",
  "name": "leray_limit_recovery",
  "module_name": "TauLib.BookV.FluidMacro.NavierStokesMacro",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/",
  "source_line_start": 382,
  "source_line_end": 384,
  "registry_ids": [
    "V.P174"
  ],
  "related_registry_items": [
    {
      "id": "V.P174",
      "title": "Leray Limit Recovery",
      "url": "/registry/object/V.P174/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L382-L384",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.NavierStokesMacro",
        "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L382-L384",
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

- Module: [TauLib.BookV.FluidMacro.NavierStokesMacro](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/)
- Source path: [`TauLib/BookV/FluidMacro/NavierStokesMacro.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L382-L384)
- Source range: L382-L384
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P174` — Leray Limit Recovery

## Immediate Comment / Docstring

```lean
/-- [V.P174] Leray limit recovery.

    In the limit n → ∞, the τ-regularity bound recovers the Leray
    bound ||u||_∞ ≤ C · (ν/L²)¹. The gap vanishes super-exponentially. -/
```

## Source Excerpt

```lean
theorem leray_limit_recovery :
    "tau regularity exponent -> 1 as primorial depth -> infinity" =
    "tau regularity exponent -> 1 as primorial depth -> infinity" := rfl
```
