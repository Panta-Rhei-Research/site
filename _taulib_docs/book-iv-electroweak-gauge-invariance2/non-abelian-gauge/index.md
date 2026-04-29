---
{
  "projection_kind": "taulib_declaration",
  "title": "NonAbelianGauge",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/non-abelian-gauge/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance2::NonAbelianGauge",
  "declaration_slug": "non-abelian-gauge",
  "kind": "structure",
  "name": "NonAbelianGauge",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/",
  "source_line_start": 96,
  "source_line_end": 104,
  "registry_ids": [
    "IV.D97"
  ],
  "related_registry_items": [
    {
      "id": "IV.D97",
      "title": "Non-Abelian Gauge Field",
      "url": "/registry/object/IV.D97/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L96-L104",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.GaugeInvariance2",
        "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L96-L104",
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

- Module: [TauLib.BookIV.Electroweak.GaugeInvariance2](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/)
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L96-L104)
- Source range: L96-L104
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D97` — Non-Abelian Gauge Field

## Immediate Comment / Docstring

```lean
/-- [IV.D97] Non-abelian gauge potential: Lie-algebra-valued 1-form
    A_μ = A_μ^a T^a where T^a are generators of the Lie algebra.
    Field strength gains self-interaction: F = dA + A ∧ A. -/
```

## Source Excerpt

```lean
structure NonAbelianGauge where
  /-- Lie algebra dimension (generators count). -/
  algebra_dim : Nat
  /-- Whether the group is abelian (U(1): dim=1, abelian). -/
  is_abelian : Bool
  /-- Self-interaction present iff non-abelian. -/
  has_self_interaction : Bool
  interaction_eq : has_self_interaction = !is_abelian
  deriving Repr
```
