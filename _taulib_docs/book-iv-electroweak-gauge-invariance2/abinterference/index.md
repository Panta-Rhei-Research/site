---
{
  "projection_kind": "taulib_declaration",
  "title": "ABInterference",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/abinterference/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance2::ABInterference",
  "declaration_slug": "abinterference",
  "kind": "structure",
  "name": "ABInterference",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/",
  "source_line_start": 307,
  "source_line_end": 315,
  "registry_ids": [
    "IV.P173"
  ],
  "related_registry_items": [
    {
      "id": "IV.P173",
      "title": "AB interference shift",
      "url": "/registry/object/IV.P173/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L307-L315",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L307-L315",
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
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L307-L315)
- Source range: L307-L315
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P173` — AB interference shift

## Immediate Comment / Docstring

```lean
/-- [IV.P173] Aharonov-Bohm interference from split paths: a charged
    particle taking two paths around a solenoid acquires a relative
    phase Φ_AB = e/ℏ · ∫ A·dl, producing interference fringes. -/
```

## Source Excerpt

```lean
structure ABInterference where
  /-- Number of paths (two, for standard AB setup). -/
  path_count : Nat
  path_eq : path_count = 2
  /-- Relative phase is the AB phase. -/
  relative_phase_is_ab : Bool := true
  /-- Interference is observable. -/
  observable : Bool := true
  deriving Repr
```
