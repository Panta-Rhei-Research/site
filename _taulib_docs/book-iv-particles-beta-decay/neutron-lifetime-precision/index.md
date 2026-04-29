---
{
  "projection_kind": "taulib_declaration",
  "title": "NeutronLifetimePrecision",
  "permalink": "/verify/taulib/docs/book-iv-particles-beta-decay/neutron-lifetime-precision/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.BetaDecay`.",
  "declaration_id": "TauLib.BookIV.Particles.BetaDecay::NeutronLifetimePrecision",
  "declaration_slug": "neutron-lifetime-precision",
  "kind": "structure",
  "name": "NeutronLifetimePrecision",
  "module_name": "TauLib.BookIV.Particles.BetaDecay",
  "module_url": "/verify/taulib/docs/book-iv-particles-beta-decay/",
  "source_line_start": 389,
  "source_line_end": 402,
  "registry_ids": [
    "IV.T203"
  ],
  "related_registry_items": [
    {
      "id": "IV.T203",
      "title": "Neutron Lifetime Precision Prediction",
      "url": "/registry/object/IV.T203/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L389-L402",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.BetaDecay",
        "url": "/verify/taulib/docs/book-iv-particles-beta-decay/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L389-L402",
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

- Module: [TauLib.BookIV.Particles.BetaDecay](/verify/taulib/docs/book-iv-particles-beta-decay/)
- Source path: [`TauLib/BookIV/Particles/BetaDecay.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L389-L402)
- Source range: L389-L402
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T203` — Neutron Lifetime Precision Prediction

## Immediate Comment / Docstring

```lean
/-- [IV.T203] τ_n = K/(|V_ud|²·(1+3g_A²)·f·(1+Δ_r)) ≈ 878.7 s.
    Bottle: 878.4±0.5 s → +340 ppm. Beam: 887.7±1.2 s → excluded at 7.5σ. -/
```

## Source Excerpt

```lean
structure NeutronLifetimePrecision where
  /-- τ_n prediction (s ×10). -/
  tau_n_predicted_x10 : Nat := 8787
  /-- Bottle average (s ×10). -/
  bottle_avg_x10 : Nat := 8784
  /-- Beam average (s ×10). -/
  beam_avg_x10 : Nat := 8877
  /-- Deviation from bottle (ppm). -/
  bottle_deviation_ppm : Nat := 340
  /-- Beam excluded at σ (×10). -/
  beam_excluded_sigma_x10 : Nat := 75
  /-- Selects bottle. -/
  selects_bottle : Bool := true
  deriving Repr
```
