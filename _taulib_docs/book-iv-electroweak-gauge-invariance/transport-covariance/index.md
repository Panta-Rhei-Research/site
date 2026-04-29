---
{
  "projection_kind": "taulib_declaration",
  "title": "TransportCovariance",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/transport-covariance/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance::TransportCovariance",
  "declaration_slug": "transport-covariance",
  "kind": "structure",
  "name": "TransportCovariance",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/",
  "source_line_start": 315,
  "source_line_end": 320,
  "registry_ids": [
    "IV.P38"
  ],
  "related_registry_items": [
    {
      "id": "IV.P38",
      "title": "Parallel Transport is Gauge-Covariant",
      "url": "/registry/object/IV.P38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L315-L320",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L315-L320",
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
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L315-L320)
- Source range: L315-L320
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P38` — Parallel Transport is Gauge-Covariant

## Immediate Comment / Docstring

```lean
/-- [IV.P38] Parallel transport is gauge-covariant for open paths and
    gauge-invariant for closed paths (loops). The holonomy around a
    loop is a physical observable (the AB phase). -/
```

## Source Excerpt

```lean
structure TransportCovariance where
  /-- Open-path transport is gauge-covariant. -/
  open_covariant : Bool := true
  /-- Closed-path (loop) holonomy is gauge-invariant. -/
  closed_invariant : Bool := true
  deriving Repr
```
