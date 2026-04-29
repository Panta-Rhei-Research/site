---
{
  "projection_kind": "taulib_declaration",
  "title": "AharonovBohmPhase",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/aharonov-bohm-phase/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance::AharonovBohmPhase",
  "declaration_slug": "aharonov-bohm-phase",
  "kind": "structure",
  "name": "AharonovBohmPhase",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/",
  "source_line_start": 233,
  "source_line_end": 241,
  "registry_ids": [
    "IV.D93"
  ],
  "related_registry_items": [
    {
      "id": "IV.D93",
      "title": "Aharonov-Bohm Phase",
      "url": "/registry/object/IV.D93/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L233-L241",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L233-L241",
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
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L233-L241)
- Source range: L233-L241
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D93` — Aharonov-Bohm Phase

## Immediate Comment / Docstring

```lean
/-- [IV.D93] Aharonov-Bohm phase: Φ_AB = exp(ie/ℏ ∮ A·dl).
    Observable even when F=0 locally; encodes global topology.
    The phase is the holonomy of the EM connection around a loop. -/
```

## Source Excerpt

```lean
structure AharonovBohmPhase where
  /-- Enclosed magnetic flux (scaled). -/
  flux_numer : Int
  flux_denom : Nat
  denom_pos : flux_denom > 0
  /-- The path is a closed loop. -/
  is_loop : Bool
  loop_true : is_loop = true
  deriving Repr
```
