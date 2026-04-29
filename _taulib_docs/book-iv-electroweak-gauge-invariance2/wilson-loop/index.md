---
{
  "projection_kind": "taulib_declaration",
  "title": "WilsonLoop",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/wilson-loop/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance2::WilsonLoop",
  "declaration_slug": "wilson-loop",
  "kind": "structure",
  "name": "WilsonLoop",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/",
  "source_line_start": 64,
  "source_line_end": 73,
  "registry_ids": [
    "IV.D96"
  ],
  "related_registry_items": [
    {
      "id": "IV.D96",
      "title": "Wilson Loop",
      "url": "/registry/object/IV.D96/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L64-L73",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L64-L73",
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
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L64-L73)
- Source range: L64-L73
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D96` — Wilson Loop

## Immediate Comment / Docstring

```lean
/-- [IV.D96] Wilson loop W(γ) = tr(P exp(i∮_γ A·dl)).
    For U(1): W(γ) = exp(iΦ_AB) (no path-ordering needed).
    W(γ) is gauge-invariant by construction (trace of holonomy). -/
```

## Source Excerpt

```lean
structure WilsonLoop where
  /-- The holonomy phase (scaled: phase/2π as rational). -/
  phase_numer : Int
  phase_denom : Nat
  denom_pos : phase_denom > 0
  /-- Gauge-invariant by construction. -/
  gauge_invariant : Bool := true
  /-- Whether the gauge group is abelian. -/
  abelian : Bool
  deriving Repr
```
