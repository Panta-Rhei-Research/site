---
{
  "projection_kind": "taulib_declaration",
  "title": "NoIsolatedChargesThm",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/no-isolated-charges-thm/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.ChargeObstruction`.",
  "declaration_id": "TauLib.BookV.FluidMacro.ChargeObstruction::NoIsolatedChargesThm",
  "declaration_slug": "no-isolated-charges-thm",
  "kind": "structure",
  "name": "NoIsolatedChargesThm",
  "module_name": "TauLib.BookV.FluidMacro.ChargeObstruction",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/",
  "source_line_start": 96,
  "source_line_end": 103,
  "registry_ids": [
    "V.T73"
  ],
  "related_registry_items": [
    {
      "id": "V.T73",
      "title": "No Isolated Charges",
      "url": "/registry/object/V.T73/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L96-L103",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.ChargeObstruction",
        "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L96-L103",
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

- Module: [TauLib.BookV.FluidMacro.ChargeObstruction](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/)
- Source path: [`TauLib/BookV/FluidMacro/ChargeObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L96-L103)
- Source range: L96-L103
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T73` — No Isolated Charges

## Immediate Comment / Docstring

```lean
/-- [V.T73] No Isolated Charges theorem: for any τ-admissible
    configuration on τ³, the total boundary charge vanishes.

    Q_∂^total = ∫_L Hol_{B+C}(d) dσ = 0

    Every electric charge has a compensating partner, and global
    neutrality is a topological necessity. -/
```

## Source Excerpt

```lean
structure NoIsolatedChargesThm where
  /-- Positive charges. -/
  positive_charges : Nat
  /-- Negative charges. -/
  negative_charges : Nat
  /-- They balance. -/
  balance : positive_charges = negative_charges
  deriving Repr
```
