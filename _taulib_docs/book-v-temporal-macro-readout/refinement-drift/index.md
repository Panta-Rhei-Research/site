---
{
  "projection_kind": "taulib_declaration",
  "title": "RefinementDrift",
  "permalink": "/verify/taulib/docs/book-v-temporal-macro-readout/refinement-drift/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.MacroReadout`.",
  "declaration_id": "TauLib.BookV.Temporal.MacroReadout::RefinementDrift",
  "declaration_slug": "refinement-drift",
  "kind": "structure",
  "name": "RefinementDrift",
  "module_name": "TauLib.BookV.Temporal.MacroReadout",
  "module_url": "/verify/taulib/docs/book-v-temporal-macro-readout/",
  "source_line_start": 135,
  "source_line_end": 142,
  "registry_ids": [
    "V.D29"
  ],
  "related_registry_items": [
    {
      "id": "V.D29",
      "title": "Refinement Drift (Redshift)",
      "url": "/registry/object/V.D29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L135-L142",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.MacroReadout",
        "url": "/verify/taulib/docs/book-v-temporal-macro-readout/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L135-L142",
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

- Module: [TauLib.BookV.Temporal.MacroReadout](/verify/taulib/docs/book-v-temporal-macro-readout/)
- Source path: [`TauLib/BookV/Temporal/MacroReadout.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/MacroReadout.lean#L135-L142)
- Source range: L135-L142
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D29` — Refinement Drift (Redshift)

## Immediate Comment / Docstring

```lean
/-- [V.D29] Refinement drift (cosmological redshift):
    z(n_s, n_r) := Δt(n_s)/Δt(n_r) − 1. Since Δt(n) ~ ι_τ^n
    and ι_τ < 1, source earlier (n_s < n_r) gives z > 0 (redshift).
    The τ-framework predicts redshift WITHOUT metric expansion. -/
```

## Source Excerpt

```lean
structure RefinementDrift where
  n_source : Nat
  n_receiver : Nat
  source_pos : n_source > 0
  receiver_pos : n_receiver > 0
  /-- Source precedes receiver (cosmological redshift). -/
  source_earlier : n_source < n_receiver
  deriving Repr
```
