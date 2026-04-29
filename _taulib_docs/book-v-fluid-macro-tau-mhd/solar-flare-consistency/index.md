---
{
  "projection_kind": "taulib_declaration",
  "title": "SolarFlareConsistency",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/solar-flare-consistency/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauMHD`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauMHD::SolarFlareConsistency",
  "declaration_slug": "solar-flare-consistency",
  "kind": "structure",
  "name": "SolarFlareConsistency",
  "module_name": "TauLib.BookV.FluidMacro.TauMHD",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/",
  "source_line_start": 322,
  "source_line_end": 331,
  "registry_ids": [
    "V.P172"
  ],
  "related_registry_items": [
    {
      "id": "V.P172",
      "title": "Solar Flare Consistency",
      "url": "/registry/object/V.P172/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L322-L331",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L322-L331",
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
- Source path: [`TauLib/BookV/FluidMacro/TauMHD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L322-L331)
- Source range: L322-L331
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P172` — Solar Flare Consistency

## Immediate Comment / Docstring

```lean
/-- [V.P172] Solar flare consistency.

    Prediction: 0.117 v_A.
    Observed: (0.1 ± 0.03) v_A (Priest & Forbes 2000, Ji et al. 2004).
    Deviation: +17% (~0.6σ). -/
```

## Source Excerpt

```lean
structure SolarFlareConsistency where
  /-- Prediction × 1000. -/
  pred_x1000 : Nat := 117
  /-- Observed central × 1000. -/
  obs_x1000 : Nat := 100
  /-- Observed ± × 1000. -/
  unc_x1000 : Nat := 30
  /-- Within 1σ. -/
  within_1sigma : pred_x1000 ≤ obs_x1000 + unc_x1000 := by omega
  deriving Repr
```
