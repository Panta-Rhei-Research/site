---
{
  "projection_kind": "taulib_declaration",
  "title": "DriftBoundedByRepair",
  "permalink": "/verify/taulib/docs/book-vi-source-epigenetics/drift-bounded-by-repair/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.Epigenetics`.",
  "declaration_id": "TauLib.BookVI.Source.Epigenetics::DriftBoundedByRepair",
  "declaration_slug": "drift-bounded-by-repair",
  "kind": "structure",
  "name": "DriftBoundedByRepair",
  "module_name": "TauLib.BookVI.Source.Epigenetics",
  "module_url": "/verify/taulib/docs/book-vi-source-epigenetics/",
  "source_line_start": 361,
  "source_line_end": 370,
  "registry_ids": [
    "VI.T49"
  ],
  "related_registry_items": [
    {
      "id": "VI.T49",
      "title": "Drift Bounded by Repair",
      "url": "/registry/object/VI.T49/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L361-L370",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Source.Epigenetics",
        "url": "/verify/taulib/docs/book-vi-source-epigenetics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L361-L370",
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

- Module: [TauLib.BookVI.Source.Epigenetics](/verify/taulib/docs/book-vi-source-epigenetics/)
- Source path: [`TauLib/BookVI/Source/Epigenetics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L361-L370)
- Source range: L361-L370
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T49` — Drift Bounded by Repair

## Immediate Comment / Docstring

```lean
/-- [VI.T49] Epigenetic Drift Bounded by Repair Budget.
    DNMT1 (maintenance methyltransferase) and histone mark copying
    consume repair resources (VI.D45, RepairBudget).
    When the repair budget is exhausted (VI.P16, RepairBudgetExhaustion),
    epigenetic maintenance fails and drift becomes uncontrolled.
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure DriftBoundedByRepair where
  /-- Maintenance consumes repair budget (VI.D45). -/
  consumes_repair_budget : Bool := true
  /-- Budget exhaustion → uncontrolled drift (VI.P16). -/
  exhaustion_implies_drift : Bool := true
  /-- Bounded while budget remains. -/
  bounded_while_funded : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
