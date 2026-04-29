---
{
  "projection_kind": "taulib_declaration",
  "title": "ParallelTransport",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/parallel-transport/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance::ParallelTransport",
  "declaration_slug": "parallel-transport",
  "kind": "structure",
  "name": "ParallelTransport",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/",
  "source_line_start": 185,
  "source_line_end": 192,
  "registry_ids": [
    "IV.D91"
  ],
  "related_registry_items": [
    {
      "id": "IV.D91",
      "title": "Parallel Transport",
      "url": "/registry/object/IV.D91/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L185-L192",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.GaugeInvariance",
        "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L185-L192",
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

- Module: [TauLib.BookIV.Electroweak.GaugeInvariance](/verify/taulib/docs/book-iv-electroweak-gauge-invariance/)
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L185-L192)
- Source range: L185-L192
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D91` — Parallel Transport

## Immediate Comment / Docstring

```lean
/-- [IV.D91] Parallel transport along a path γ in T²:
    the solution to D_γ ψ = 0. For U(1), this is a phase rotation. -/
```

## Source Excerpt

```lean
structure ParallelTransport where
  /-- Whether the path is closed (loop). -/
  is_loop : Bool
  /-- Phase accumulated (as scaled integer, in units of 2π/N). -/
  phase_numer : Int
  phase_denom : Nat
  denom_pos : phase_denom > 0
  deriving Repr
```
