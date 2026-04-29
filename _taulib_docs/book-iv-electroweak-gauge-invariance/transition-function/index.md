---
{
  "projection_kind": "taulib_declaration",
  "title": "TransitionFunction",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/transition-function/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance::TransitionFunction",
  "declaration_slug": "transition-function",
  "kind": "structure",
  "name": "TransitionFunction",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance/",
  "source_line_start": 109,
  "source_line_end": 118,
  "registry_ids": [
    "IV.D87"
  ],
  "related_registry_items": [
    {
      "id": "IV.D87",
      "title": "Transition Function",
      "url": "/registry/object/IV.D87/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L109-L118",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L109-L118",
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
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L109-L118)
- Source range: L109-L118
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D87` — Transition Function

## Immediate Comment / Docstring

```lean
/-- [IV.D87] Transition function g_{UV}: U ∩ V → U(1).
    On overlaps, relates two local trivializations.
    The cocycle condition g_{UV}·g_{VW} = g_{UW} holds. -/
```

## Source Excerpt

```lean
structure TransitionFunction where
  /-- Source patch index. -/
  patch_u : Nat
  /-- Target patch index. -/
  patch_v : Nat
  /-- Winding number of the transition function (integer for T²). -/
  winding : Int
  /-- Satisfies cocycle condition. -/
  cocycle : Bool := true
  deriving Repr
```
