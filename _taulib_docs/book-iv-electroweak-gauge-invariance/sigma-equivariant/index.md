---
{
  "projection_kind": "taulib_declaration",
  "title": "SigmaEquivariant",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/sigma-equivariant/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance::SigmaEquivariant",
  "declaration_slug": "sigma-equivariant",
  "kind": "structure",
  "name": "SigmaEquivariant",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/",
  "source_line_start": 265,
  "source_line_end": 271,
  "registry_ids": [
    "IV.D95"
  ],
  "related_registry_items": [
    {
      "id": "IV.D95",
      "title": "Sigma-Equivariance",
      "url": "/registry/object/IV.D95/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L265-L271",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L265-L271",
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
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L265-L271)
- Source range: L265-L271
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D95` — Sigma-Equivariance

## Immediate Comment / Docstring

```lean
/-- [IV.D95] A σ-equivariant functional on P_EM: a functional that
    commutes with the U(1) action (σ). Physical observables must
    be σ-equivariant; this is the structural content of gauge invariance. -/
```

## Source Excerpt

```lean
structure SigmaEquivariant where
  /-- The functional commutes with U(1) action. -/
  equivariant : Bool := true
  /-- Observable iff equivariant. -/
  is_observable : Bool
  obs_eq : is_observable = equivariant
  deriving Repr
```
