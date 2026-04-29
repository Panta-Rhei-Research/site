---
{
  "projection_kind": "taulib_declaration",
  "title": "MaximalCouplingCondition",
  "permalink": "/verify/taulib/docs/book-v-temporal-high-energy/maximal-coupling-condition/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.HighEnergy`.",
  "declaration_id": "TauLib.BookV.Temporal.HighEnergy::MaximalCouplingCondition",
  "declaration_slug": "maximal-coupling-condition",
  "kind": "structure",
  "name": "MaximalCouplingCondition",
  "module_name": "TauLib.BookV.Temporal.HighEnergy",
  "module_url": "/verify/taulib/docs/book-v-temporal-high-energy/",
  "source_line_start": 95,
  "source_line_end": 103,
  "registry_ids": [
    "V.D24"
  ],
  "related_registry_items": [
    {
      "id": "V.D24",
      "title": "Maximal Coupling Condition",
      "url": "/registry/object/V.D24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L95-L103",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L95-L103",
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
- Source path: [`TauLib/BookV/Temporal/HighEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L95-L103)
- Source range: L95-L103
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D24` — Maximal Coupling Condition

## Immediate Comment / Docstring

```lean
/-- [V.D24] Maximal coupling condition: at the ignition depth, all
    sectors couple with near-maximal strength.

    As the tower deepens beyond n_ign, couplings differentiate toward
    their asymptotic values κ(S;d). The maximal condition characterizes
    the "unified" state at ignition.

    We record:
    - All 5 sectors are active
    - The coupling budget is fully allocated (temporal complement) -/
```

## Source Excerpt

```lean
structure MaximalCouplingCondition where
  /-- Number of active sectors at ignition. -/
  active_sectors : Nat
  /-- All 5 sectors active. -/
  all_active : active_sectors = 5
  /-- Temporal complement still holds (budget constraint). -/
  temporal_balanced : Bool
  temporal_proof : temporal_balanced = true
  deriving Repr
```
