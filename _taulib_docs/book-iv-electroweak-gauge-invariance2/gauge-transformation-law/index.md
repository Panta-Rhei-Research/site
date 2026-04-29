---
{
  "projection_kind": "taulib_declaration",
  "title": "GaugeTransformationLaw",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/gauge-transformation-law/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance2::GaugeTransformationLaw",
  "declaration_slug": "gauge-transformation-law",
  "kind": "structure",
  "name": "GaugeTransformationLaw",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/",
  "source_line_start": 194,
  "source_line_end": 203,
  "registry_ids": [
    "IV.T121"
  ],
  "related_registry_items": [
    {
      "id": "IV.T121",
      "title": "Gauge covariance of D_mu",
      "url": "/registry/object/IV.T121/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L194-L203",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L194-L203",
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
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L194-L203)
- Source range: L194-L203
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T121` — Gauge covariance of D_mu

## Immediate Comment / Docstring

```lean
/-- [IV.T121] Gauge transformation law: A_μ → A_μ + ∂_μΛ for U(1),
    A_μ → g A_μ g⁻¹ + g ∂_μ g⁻¹ for non-abelian groups.
    The abelian law is a special case with g = e^{iΛ}. -/
```

## Source Excerpt

```lean
structure GaugeTransformationLaw where
  /-- Whether the gauge group is abelian. -/
  abelian : Bool
  /-- Transformation adds gradient for abelian. -/
  adds_gradient : Bool
  grad_eq : adds_gradient = abelian
  /-- Transformation has conjugation term for non-abelian. -/
  has_conjugation : Bool
  conj_eq : has_conjugation = !abelian
  deriving Repr
```
