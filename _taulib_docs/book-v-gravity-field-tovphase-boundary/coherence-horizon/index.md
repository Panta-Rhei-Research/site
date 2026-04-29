---
{
  "projection_kind": "taulib_declaration",
  "title": "CoherenceHorizon",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/coherence-horizon/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TOVPhaseBoundary`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVPhaseBoundary::CoherenceHorizon",
  "declaration_slug": "coherence-horizon",
  "kind": "structure",
  "name": "CoherenceHorizon",
  "module_name": "TauLib.BookV.GravityField.TOVPhaseBoundary",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/",
  "source_line_start": 103,
  "source_line_end": 114,
  "registry_ids": [
    "V.D76"
  ],
  "related_registry_items": [
    {
      "id": "V.D76",
      "title": "Coherence Horizon",
      "url": "/registry/object/V.D76/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L103-L114",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TOVPhaseBoundary",
        "url": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L103-L114",
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

- Module: [TauLib.BookV.GravityField.TOVPhaseBoundary](/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/)
- Source path: [`TauLib/BookV/GravityField/TOVPhaseBoundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L103-L114)
- Source range: L103-L114
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D76` — Coherence Horizon

## Immediate Comment / Docstring

```lean
/-- [V.D76] Coherence horizon M_n*: the critical mass where the
    topology crossing occurs.

    Properties:
    - Well-defined: unique for given equation of state
    - Finite: bounded above by a function of iota_tau
    - Positive: M_n* > 0 (no zero-mass BH)
    - Above Chandrasekhar: M_n* >= M_Ch -/
```

## Source Excerpt

```lean
structure CoherenceHorizon where
  /-- Critical mass numerator. -/
  mass_numer : Nat
  /-- Critical mass denominator. -/
  mass_denom : Nat
  /-- Denominator positive. -/
  denom_pos : mass_denom > 0
  /-- Mass is positive. -/
  mass_positive : mass_numer > 0
  /-- Whether this is above Chandrasekhar. -/
  above_chandrasekhar : Bool := true
  deriving Repr
```
