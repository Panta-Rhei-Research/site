---
{
  "projection_kind": "taulib_declaration",
  "title": "EMConnection",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/emconnection/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance::EMConnection",
  "declaration_slug": "emconnection",
  "kind": "structure",
  "name": "EMConnection",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/",
  "source_line_start": 152,
  "source_line_end": 158,
  "registry_ids": [
    "IV.D89"
  ],
  "related_registry_items": [
    {
      "id": "IV.D89",
      "title": "Gauge Connection",
      "url": "/registry/object/IV.D89/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L152-L158",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L152-L158",
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
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L152-L158)
- Source range: L152-L158
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D89` — Gauge Connection

## Immediate Comment / Docstring

```lean
/-- [IV.D89] Connection A on P_EM: a Lie-algebra-valued 1-form on T².
    In local coordinates A = A_μ dx^μ where A_μ: T² → ℝ.
    Under gauge transformation: A_μ → A_μ + ∂_μΛ. -/
```

## Source Excerpt

```lean
structure EMConnection where
  /-- Number of spacetime components. -/
  components : Nat
  comp_eq : components = 4
  /-- The connection is smooth. -/
  smooth : Bool := true
  deriving Repr
```
