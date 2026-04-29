---
{
  "projection_kind": "taulib_declaration",
  "title": "ABPhaseUniqueness",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/abphase-uniqueness/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance2::ABPhaseUniqueness",
  "declaration_slug": "abphase-uniqueness",
  "kind": "structure",
  "name": "ABPhaseUniqueness",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/",
  "source_line_start": 134,
  "source_line_end": 140,
  "registry_ids": [
    "IV.T39"
  ],
  "related_registry_items": [
    {
      "id": "IV.T39",
      "title": "tau-AB Kernel Theorem",
      "url": "/registry/object/IV.T39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L134-L140",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L134-L140",
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
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L134-L140)
- Source range: L134-L140
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T39` — tau-AB Kernel Theorem

## Immediate Comment / Docstring

```lean
/-- [IV.T39] The Aharonov-Bohm phase is the UNIQUE gauge-invariant
    functional of the connection on a closed loop.
    For abelian U(1): any gauge-invariant loop functional = f(Φ_AB). -/
```

## Source Excerpt

```lean
structure ABPhaseUniqueness where
  /-- Group is abelian. -/
  abelian : Bool
  abelian_true : abelian = true
  /-- Phase uniquely determines observable. -/
  phase_determines : Bool := true
  deriving Repr
```
