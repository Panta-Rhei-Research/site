---
{
  "projection_kind": "taulib_declaration",
  "title": "CoherenceHorizon",
  "permalink": "/verify/taulib/docs/book-v-temporal-temporal-ignition/coherence-horizon/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.TemporalIgnition`.",
  "declaration_id": "TauLib.BookV.Temporal.TemporalIgnition::CoherenceHorizon",
  "declaration_slug": "coherence-horizon",
  "kind": "structure",
  "name": "CoherenceHorizon",
  "module_name": "TauLib.BookV.Temporal.TemporalIgnition",
  "module_url": "/verify/taulib/docs/book-v-temporal-temporal-ignition/",
  "source_line_start": 207,
  "source_line_end": 214,
  "registry_ids": [
    "V.D23"
  ],
  "related_registry_items": [
    {
      "id": "V.D23",
      "title": "Coherence Horizon",
      "url": "/registry/object/V.D23/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L207-L214",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.TemporalIgnition",
        "url": "/verify/taulib/docs/book-v-temporal-temporal-ignition/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L207-L214",
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

- Module: [TauLib.BookV.Temporal.TemporalIgnition](/verify/taulib/docs/book-v-temporal-temporal-ignition/)
- Source path: [`TauLib/BookV/Temporal/TemporalIgnition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L207-L214)
- Source range: L207-L214
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D23` — Coherence Horizon

## Immediate Comment / Docstring

```lean
/-- [V.D23] Coherence horizon: the depth n_coh beyond which further
    refinement yields no new observable predictions at current
    experimental precision.

    The universe has effectively "converged" — profinite completion
    has reached practical saturation. Deeper levels exist but are
    observationally inaccessible.

    n_coh depends on experimental precision; structurally, we only
    require n_coh > n_ign (past ignition) and n_coh ≤ n_* (present). -/
```

## Source Excerpt

```lean
structure CoherenceHorizon where
  /-- The coherence horizon depth. -/
  n_coh : Nat
  /-- Past ignition. -/
  n_coh_pos : n_coh > 0
  /-- Whether convergence is effective (to current precision). -/
  effectively_converged : Bool
  deriving Repr
```
