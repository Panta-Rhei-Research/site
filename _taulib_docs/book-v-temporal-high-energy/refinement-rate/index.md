---
{
  "projection_kind": "taulib_declaration",
  "title": "RefinementRate",
  "permalink": "/verify/taulib/docs/book-v-temporal-high-energy/refinement-rate/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.HighEnergy`.",
  "declaration_id": "TauLib.BookV.Temporal.HighEnergy::RefinementRate",
  "declaration_slug": "refinement-rate",
  "kind": "structure",
  "name": "RefinementRate",
  "module_name": "TauLib.BookV.Temporal.HighEnergy",
  "module_url": "/verify/taulib/docs/book-v-temporal-high-energy/",
  "source_line_start": 180,
  "source_line_end": 191,
  "registry_ids": [
    "V.D26"
  ],
  "related_registry_items": [
    {
      "id": "V.D26",
      "title": "Refinement Progression Rate",
      "url": "/registry/object/V.D26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L180-L191",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.HighEnergy",
        "url": "/verify/taulib/docs/book-v-temporal-high-energy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L180-L191",
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

- Module: [TauLib.BookV.Temporal.HighEnergy](/verify/taulib/docs/book-v-temporal-high-energy/)
- Source path: [`TauLib/BookV/Temporal/HighEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L180-L191)
- Source range: L180-L191
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D26` — Refinement Progression Rate

## Immediate Comment / Docstring

```lean
/-- [V.D26] Refinement progression rate H(n): how fast the tower advances.

    H(n) := 1 / Δt(n) where Δt(n) is the proper-time increment of tick n.
    Since Δt(n) ~ ι_τ^n, H(n) ~ ι_τ^(-n): the progression rate is
    exponentially large at early depths and decays with tower depth.

    This is the τ-native Hubble parameter:
    - Early (opening): H is large → rapid progression → inflation
    - Late (temporal): H is small → slow progression → current epoch

    We store H(n) as a Nat pair (numer, denom). -/
```

## Source Excerpt

```lean
structure RefinementRate where
  /-- Depth at which this rate is evaluated. -/
  depth : Nat
  /-- Depth is positive. -/
  depth_pos : depth > 0
  /-- Rate numerator (proportional to ι_τ^(-n)). -/
  rate_numer : Nat
  /-- Rate denominator. -/
  rate_denom : Nat
  /-- Denominator positive. -/
  denom_pos : rate_denom > 0
  deriving Repr
```
