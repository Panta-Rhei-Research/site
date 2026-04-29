---
{
  "projection_kind": "taulib_declaration",
  "title": "CriticalMobilityThreshold",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/critical-mobility-threshold/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt::CriticalMobilityThreshold",
  "declaration_slug": "critical-mobility-threshold",
  "kind": "structure",
  "name": "CriticalMobilityThreshold",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/",
  "source_line_start": 390,
  "source_line_end": 399,
  "registry_ids": [
    "IV.D219"
  ],
  "related_registry_items": [
    {
      "id": "IV.D219",
      "title": "Critical mobility threshold",
      "url": "/registry/object/IV.D219/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L390-L399",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
        "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L390-L399",
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

- Module: [TauLib.BookIV.ManyBody.DefectFunctionalExt](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/)
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L390-L399)
- Source range: L390-L399
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D219` — Critical mobility threshold

## Immediate Comment / Docstring

```lean
/-- [IV.D219] The critical mobility threshold mu_crit is the macroscopic
    mobility value at which the Euler budget ceases to hold.
    Below mu_crit: Euler regime (inviscid, budget-conserving).
    Above mu_crit: Navier-Stokes regime (viscous, dissipative). -/
```

## Source Excerpt

```lean
structure CriticalMobilityThreshold where
  /-- Separates Euler from NS regime. -/
  separates_euler_ns : Bool := true
  /-- Below: Euler (inviscid). -/
  below_is_euler : Bool := true
  /-- Above: NS (viscous). -/
  above_is_ns : Bool := true
  /-- Determined by sector geometry (not free parameter). -/
  not_free_param : Bool := true
  deriving Repr
```
