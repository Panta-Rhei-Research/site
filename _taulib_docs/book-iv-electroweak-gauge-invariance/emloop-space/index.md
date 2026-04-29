---
{
  "projection_kind": "taulib_declaration",
  "title": "EMLoopSpace",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/emloop-space/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance::EMLoopSpace",
  "declaration_slug": "emloop-space",
  "kind": "structure",
  "name": "EMLoopSpace",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/",
  "source_line_start": 250,
  "source_line_end": 256,
  "registry_ids": [
    "IV.D94"
  ],
  "related_registry_items": [
    {
      "id": "IV.D94",
      "title": "EM Loop Space",
      "url": "/registry/object/IV.D94/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L250-L256",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L250-L256",
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
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L250-L256)
- Source range: L250-L256
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D94` — EM Loop Space

## Immediate Comment / Docstring

```lean
/-- [IV.D94] EM loop space: the space of closed loops on T² equipped
    with the holonomy map. Loops compose by concatenation, giving
    a group structure on holonomies. -/
```

## Source Excerpt

```lean
structure EMLoopSpace where
  /-- Base space (T²). -/
  base_dim : Nat
  base_eq : base_dim = 2
  /-- The holonomy is multiplicative under loop composition. -/
  holonomy_multiplicative : Bool := true
  deriving Repr
```
