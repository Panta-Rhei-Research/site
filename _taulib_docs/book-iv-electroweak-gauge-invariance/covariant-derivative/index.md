---
{
  "projection_kind": "taulib_declaration",
  "title": "CovariantDerivative",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/covariant-derivative/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance::CovariantDerivative",
  "declaration_slug": "covariant-derivative",
  "kind": "structure",
  "name": "CovariantDerivative",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/",
  "source_line_start": 171,
  "source_line_end": 177,
  "registry_ids": [
    "IV.D90"
  ],
  "related_registry_items": [
    {
      "id": "IV.D90",
      "title": "Covariant Derivative",
      "url": "/registry/object/IV.D90/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L171-L177",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L171-L177",
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
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L171-L177)
- Source range: L171-L177
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D90` — Covariant Derivative

## Immediate Comment / Docstring

```lean
/-- [IV.D90] Covariant derivative D_μ = ∂_μ + ieA_μ on charged fields.
    The minimal coupling prescription of the B-sector connection. -/
```

## Source Excerpt

```lean
structure CovariantDerivative where
  /-- Coupling constant (charge in units of e). -/
  charge_units : Int
  /-- The connection used. -/
  connection_components : Nat
  conn_eq : connection_components = 4
  deriving Repr
```
